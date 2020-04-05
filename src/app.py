from flask import Flask, jsonify, request
import psycopg2

app = Flask('SEEUS')


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/hello/<name>')
def test(name):
    out = {
        "message": "Hello, " + name,
        "query_params": request.args,
        "name": name
    }
    return jsonify(out)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
