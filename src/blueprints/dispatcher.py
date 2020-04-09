from flask import Blueprint

dispatcher = Blueprint('dispatcher', __name__, url_prefix='/dispatcher')

@dispatcher.route('/requests')
def hello():
    return ""
