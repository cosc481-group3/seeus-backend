from http import HTTPStatus

from flask import jsonify, request, Blueprint, session, redirect

from ..auth import begin_oauth, complete_oauth
from ..database import db

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
    msg = json_as_text({
        'action': 'loginSuccess',
        'user': user,
        'jwt': jwt
    })
    loading_msg = json_as_text({'action': 'loading'})

    # This javascript snippet will render in the oauth webview within the app
    # It sends the auth info to the app via the webview message interface
    return (
        f"""
        <script>
            window.ReactNativeWebView.postMessage(JSON.stringify({loading_msg}));
            window.ReactNativeWebView.postMessage(JSON.stringify({msg}));
        </script>
        """
    )


def json_as_text(data: dict) -> str:
    return jsonify(data).get_data(as_text=True)


@mobile.route('/requests', methods=['POST'])
def requests():
    data = request.get_json(force=True)
    db.query_commit("insert into requests (user_id, start_location, end_location, start_latitude, "
                    "start_longitude, notes) "
                    "values (%(user_id)s, %(start_location)s, %(end_location)s, %(start_latitude)s, "
                    "%(start_longitude)s, %(notes)s)", {
                        'user_id': 1,
                        'start_location': data["start_location"],
                        'end_location': data["end_location"],
                        'start_latitude': data["start_latitude"],
                        'start_longitude': data["start_longitude"],
                        'notes': data["notes"]
                    })
    return data
