from flask import jsonify, request, Blueprint


mobile = Blueprint('app', __name__, url_prefix='/app')

@mobile.route('/auth/begin')
def auth_begin():
    return "Auth begin"

@mobile.route('/auth/callback')
def auth_callback():
    return "Auth callback"