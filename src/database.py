import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = psycopg2.connect(f"dbname='postgres' user='{os.getenv('POSTGRES_USER')}' host='database' password='{os.getenv('POSTGRES_PASSWORD')}'")
except psycopg2.Error:
    print("Unable to connect to the database")
