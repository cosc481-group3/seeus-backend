from flask import Blueprint, request
from database import db

dispatcher = Blueprint('dispatcher', __name__, url_prefix='/dispatcher')


@dispatcher.route('/config/<name>', methods=['PATCH'])
def toggles(name):
    data = request.get_data(as_text=True)
    db.query_commit("update seeus_config set value = %s where name = %s", [data, name])
    return data
