from flask import jsonify, request, Blueprint
from random import random
from database import conn

mobile = Blueprint('app', __name__, url_prefix='/app')


@mobile.route('/')
def hello():
    conn.cursor().execute("insert into seeus_config (name, value) "
                          "values (%(name)s, %(value)s)", {
                              'name': f'name{round(random() * 1000)}',
                              'value': 'some value'
                          })
    conn.commit()
    cursor = conn.cursor()
    cursor.execute("select * from seeus_config")
    return jsonify(cursor.fetchall())


@mobile.route('/requests', methods=['POST'])
def requests():
    data = request.get_json(force=True)
    conn.cursor().execute("insert into requests (user_id, start_location, end_location, start_latitude, "
                          "start_longitude, notes) "
                          "values (%(user_id)s, %(start_location)s, %(end_location)s, %(start_latitude)s, "
                          "%(start_longitude)s, %(notes)s)", {
                              'user_id': 1,
                              'start_location': data["start_location"],
                              'end_location': data["end_location"],
                              'start_latitude': data["start_latitude"],
                              'start_longitude': data["start_longitude"],
                              'notes': data["notes"],
                          })
    conn.commit()
    return data


@mobile.route('/requests/scheduled')
def test(name):
    out = {
        "message": "Hello, " + name,
        "query_params": request.args,
        "name": name
    }
    return jsonify(out)
