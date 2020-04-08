from flask import Flask, jsonify

from dispatcher import dispatcher
from mobile import mobile
from database import conn

app = Flask('SEEUS')
app.register_blueprint(mobile)
app.register_blueprint(dispatcher)


@app.route('/locations')
def locations():
    cursor = conn.cursor()
    cursor.execute("select * from locations")
    return jsonify(cursor.fetchall())


@app.route('/hours')
def hours():
    cursor = conn.cursor()
    cursor.execute("select value from seeus_config where name='hours'")
    return jsonify(cursor.fetchone()[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
