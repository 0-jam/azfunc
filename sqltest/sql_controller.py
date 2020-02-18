import os

import pyodbc

ENV = os.environ
DB_ENDPOINT = ENV.get('SQL_DB_ENDPOINT')
DB_NAME = ENV.get('SQL_DB_NAME')
DB_USERNAME = ENV.get('SQL_DB_USERNAME')
DB_PASSWORD = ENV.get('SQL_DB_PASSWORD')
SQL_DRIVER = '{ODBC Driver 17 for SQL Server}'


def establish_connection():
    return pyodbc.connect('DRIVER=' + SQL_DRIVER + ';SERVER=' + DB_ENDPOINT + ';PORT=1433;DATABASE=' + DB_NAME + ';UID=' + DB_USERNAME + ';PWD=' + DB_PASSWORD)


# This SQL demo function only works for Azure SQL database's sample data
def show_sql():
    connection = establish_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
    rows = cursor.fetchall()

    return [str(row[0]) + ' ' + str(row[1]) for row in rows]


def exec_sql(query):
    connection = establish_connection()
    cursor = connection.cursor()

    cursor.execute(query)

    connection.commit()
