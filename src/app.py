from flask import Flask
from mobile import mobile
from dispatcher import dispatcher

app = Flask('SEEUS')
app.register_blueprint(mobile)
app.register_blueprint(dispatcher)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
