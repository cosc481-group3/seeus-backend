from flask import Flask
app = Flask(__name__)


@app.route('/requests/ride-request', methods=["GET", "POST"])
def hello_world(eid):
    return 'Hello, World!'