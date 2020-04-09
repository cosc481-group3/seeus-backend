from flask import Flask, jsonify

from blueprints.dispatcher import dispatcher
from blueprints.mobile import mobile
from config import config
from database import db

app = Flask('SEEUS')
app.secret_key = config.secret_key
app.register_blueprint(mobile)
app.register_blueprint(dispatcher)


@app.route('/locations')
def locations():
    result = db.query_all("select * from locations")
    return jsonify(result)


@app.route('/hours')
def hours():
    result = db.query_one("select value from seeus_config where name='hours'")
    return jsonify(result['value'] if result else None)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
