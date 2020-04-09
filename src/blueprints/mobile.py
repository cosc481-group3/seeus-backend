from http import HTTPStatus

from flask import jsonify, request, Blueprint, session, redirect

from auth import begin_oauth, complete_oauth

mobile = Blueprint('app', __name__, url_prefix='/app')


@mobile.route('/oauth/start')
def auth_start():
    username = request.args.get('username', '').split('@')[0]

    if not username:
        return 'Error: username is required', 400

    auth_url, state = begin_oauth(username)
    session['oauth_state'] = state
    return redirect(auth_url)


@mobile.route('/oauth/callback')
def auth_callback():
    state = session.get('oauth_state', '')
    if not state:
        return 'Invalid request', HTTPStatus.BAD_REQUEST

    session['oauth_state'] = None

    user, jwt = complete_oauth(request.url, state)
    auth_data = {
        'user': user,
        'jwt': jwt
    }
    json = jsonify(auth_data).get_data(as_text=True)

    # This javascript snippet will render in the oauth webview within the app
    # It sends the auth info to the app via the webview message interface
    return (
        f"""
        <script>
            window.ReactNativeWebView.postMessage(JSON.stringify({json}))
        </script>
        """
    )
