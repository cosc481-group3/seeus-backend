import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = psycopg2.connect(f"dbname='{os.getenv('POSTGRES_DB')}' user='{os.getenv('POSTGRES_USER')}' host='{os.getenv('POSTGRES_USER')}' password='{os.getenv('POSTGRES_PASSWORD')}'")
except psycopg2.Error:
    print("Unable to connect to the database")
