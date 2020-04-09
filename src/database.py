from typing import Union, Sequence, Dict, Optional

import psycopg2
import psycopg2.extras

from config import config

QueryParams = Union[Sequence, Dict]


class Database:
    def __init__(self, connection):
        """
        Creates a database instance.
        :param connection: The psycopg2 connection object
        """
        self._connection = connection

    def query(self, sql, params: Optional[QueryParams] = None):
        cursor = self._create_dict_cursor()
        cursor.execute(sql, params)
        return cursor

    def query_commit(self, sql, params: Optional[QueryParams] = None):
        self.query(sql, params)
        self.commit()

    def query_all(self, sql, params: Optional[QueryParams] = None):
        cursor = self.query(sql, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def query_one(self, sql, params: Optional[QueryParams] = None):
        cursor = self.query(sql, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def commit(self):
        self._connection.commit()

    def _create_dict_cursor(self):
        # create a dict cursor so we can reference columns by name
        return self._connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


try:
    conn = psycopg2.connect(f"dbname='{config.database.name}' user='{config.database.user}' "
                            f"host='{config.database.host}' password='{config.database.password}'")
    db = Database(conn)
except psycopg2.Error:
    print("Unable to connect to the database")
