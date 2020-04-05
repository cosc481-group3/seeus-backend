from flask import jsonify, request, Blueprint


mobile = Blueprint('app', __name__, url_prefix='/app')

@mobile.route('/')
def hello():
    return "Hello World!"


@mobile.route('/requests/scheduled')
def test(name):
    out = {
        "message": "Hello, " + name,
        "query_params": request.args,
        "name": name
    }
    return jsonify(out)
