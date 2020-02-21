import os

import pyodbc
import json

ENV = os.environ
DB_ENDPOINT = ENV.get('SQL_DB_ENDPOINT')
DB_NAME = ENV.get('SQL_DB_NAME')
DB_USERNAME = ENV.get('SQL_DB_USERNAME')
DB_PASSWORD = ENV.get('SQL_DB_PASSWORD')
SQL_DRIVER = '{ODBC Driver 17 for SQL Server}'


def establish_connection():
    return pyodbc.connect('DRIVER=' + SQL_DRIVER + ';SERVER=' + DB_ENDPOINT + ';PORT=1433;DATABASE=' + DB_NAME + ';UID=' + DB_USERNAME + ';PWD=' + DB_PASSWORD)


def rows2json(rows):
    return json.dumps([tuple(row) for row in rows], ensure_ascii=False)


def exec_sql(query):
    connection = establish_connection()
    cursor = connection.cursor()

    cursor.execute(query)

    try:
        rows = cursor.fetchall()
        result_json = rows2json(rows)
    except pyodbc.ProgrammingError:
        rows = cursor.rowcount
        result_json = json.dumps("affected {} rows".format(cursor.rowcount))

    cursor.close()
    connection.close()

    return result_json
