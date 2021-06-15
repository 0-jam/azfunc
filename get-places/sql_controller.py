import json
import os

import pyodbc

ENV = os.environ
DB_ENDPOINT = ENV.get('SQL_DB_ENDPOINT')
DB_NAME = ENV.get('SQL_DB_NAME')
DB_USERNAME = ENV.get('SQL_DB_USERNAME')
DB_PASSWORD = ENV.get('SQL_DB_PASSWORD')
SQL_DRIVER = '{ODBC Driver 17 for SQL Server}'


def establish_connection() -> pyodbc.Connection:
    return pyodbc.connect('DRIVER=' + SQL_DRIVER + ';SERVER=' + DB_ENDPOINT + ';PORT=1433;DATABASE=' + DB_NAME + ';UID=' + DB_USERNAME + ';PWD=' + DB_PASSWORD)


def exec_sql(query: str) -> list:
    with establish_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            column_names = [desc[0] for desc in cursor.description]

            try:
                rows = cursor.fetchall()
                return [dict(zip(column_names, row)) for row in rows]
            except pyodbc.ProgrammingError:
                return [{'message': 'affected {} rows'.format(cursor.rowcount)}]
            finally:
                connection.commit()


def get_places():
    rows = exec_sql('select * from dbo.places')

    # decimal 型の latitude, longitude を float 型にシリアライズしている
    return json.dumps(rows, ensure_ascii=False, default=float)
