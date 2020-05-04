import os
import sys
from typing import Tuple

from requests_oauthlib import OAuth2Session

from .config import config
from .models import User, GoogleUserInfo
from .query import find_or_create_user

google_auth_base_url = 'https://accounts.google.com/o/oauth2/v2/auth'
google_token_url = 'https://www.googleapis.com/oauth2/v4/token'
google_user_info_url = 'https://www.googleapis.com/oauth2/v1/userinfo'

oauth_scope = ['openid', 'email', 'profile']
callback_uri = f'{config.app_base_url}/app/oauth/callback'
client_id = config.oauth.client_id + '.apps.googleusercontent.com'
client_secret = config.oauth.client_secret

# oauthlib thinks the token scope is changing, even though it's not
# so we disable the warning with this environmental variable
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

# disable oauthlib SSL requirement in dev environment
if config.is_dev:
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


def begin_oauth(username: str):
    """
    Begin the oauth process.
    :param username: the username of the user (without @emich.edu)
    :return: authorization_url, state
    """
    oauth_session = _construct_oauth_session()
    login_hint = f'{username}@emich.edu'
    authorization_url, state = oauth_session.authorization_url(
        google_auth_base_url,
        access_type='offline',
        login_hint=login_hint,
        hd='emich.edu'
    )

    return authorization_url, state


def complete_oauth(response_url, state) -> Tuple[User, str]:
    """
    Finish off the oauth process. Create JWT token for user to authenticate with.
    :param response_url: full request callback url that google redirected to
    :param state: state generated in begin_oauth call
    :return: User, jwt
    """
    oauth_session = _construct_oauth_session(state=state)
    token = oauth_session.fetch_token(
        google_token_url,
        client_secret=client_secret,
        authorization_response=response_url
    )
    print(f'token dict = {token}', file=sys.stdout)

    google_user_info = _fetch_google_user_info(oauth_session)
    print(f'google user info = {google_user_info}', file=sys.stdout)

    user = find_or_create_user(google_user_info)

    # todo: return JWT token for client side to store
    jwt = ''
    return user, jwt


def _fetch_google_user_info(oauth_session) -> GoogleUserInfo:
    """
    Fetches google's user info.
    :param oauth_session: the oauthlib session object
    :return: GoogleUserInfo
    """
    json = oauth_session.get(google_user_info_url).json()

    if json.get('hd') != 'emich.edu' or '@emich.edu' not in json.get('email', ''):
        raise RuntimeError('Invalid domain name')

    print(f'google user info json = {json}')

    return GoogleUserInfo(
        id=json.get('id'),
        email=json.get('email'),
        first_name=json.get('given_name'),
        last_name=json.get('family_name'),
        picture_url=json.get('picture'),
    )


def _construct_oauth_session(**kwargs):
    return OAuth2Session(client_id, scope=oauth_scope, redirect_uri=callback_uri, **kwargs)
