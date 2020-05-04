from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config:
    class DatabaseConfig:
        host = getenv('POSTGRES_HOST')
        user = getenv('POSTGRES_USER')
        password = getenv('POSTGRES_PASSWORD')
        name = getenv('POSTGRES_DB')

    class OauthConfig:
        client_id = getenv('OAUTH_CLIENT_ID')
        client_secret = getenv('OAUTH_CLIENT_SECRET')

    app_base_url = getenv('BASE_URL')
    secret_key = getenv('SECRET_KEY')
    flask_env = getenv('FLASK_ENV')
    is_dev = flask_env == 'development'

    database = DatabaseConfig()
    oauth = OauthConfig()


config = Config()
