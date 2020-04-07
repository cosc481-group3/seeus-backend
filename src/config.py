from dotenv import load_dotenv
from os import getenv

load_dotenv()

config = {
    'mode': getenv('FLASK_ENV'),
    'database': {
        'host': getenv('POSTGRES_HOST'),
        'user': getenv('POSTGRES_USER'),
        'password': getenv('POSTGRES_PASSWORD'),
        'name': getenv('POSTGRES_DB')
    },
    'oauth': {
        'client_id': getenv('OAUTH_CLIENT_ID'),
        'client_secret': getenv('OAUTH_CLIENT_SECRET'),
    }
}
