import psycopg2

from config import config

try:
    conn = psycopg2.connect(f"dbname='{config.database.name}' user='{config.database.user}' "
                            f"host='{config.database.host}' password='{config.database.password}'")
except psycopg2.Error:
    print("Unable to connect to the database")
