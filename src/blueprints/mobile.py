from flask import jsonify, request, Blueprint
from random import random

from database import conn


mobile = Blueprint('app', __name__, url_prefix='/app')


@mobile.route('/auth/begin', methods=['POST'])
def auth_begin():
    return "Auth begin"

@mobile.route('/auth/callback')
def auth_callback():
    return "Auth callback"

@mobile.route('/')
def hello():
    conn.cursor().execute("insert into seeus_config (name, value) "
                          "values (%(name)s, %(value)s)", {
        'name': f'name{round(random()*1000)}',
        'value': 'some value'
    })
    conn.commit()
    cursor = conn.cursor()
    cursor.execute("select * from seeus_config")
    return jsonify(cursor.fetchall())

@mobile.route('/requests/scheduled')
def test(name):
    out = {
        "message": "Hello, " + name,
        "query_params": request.args,
        "name": name
    }
    return jsonify(out)
