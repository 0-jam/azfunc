import logging
import os

import azure.functions as func

import pyodbc


def show_sql():
    server = str(os.environ.get('SQL_DB_ENDPOINT'))
    database = str(os.environ.get('SQL_DB_NAME'))
    username = str(os.environ.get('SQL_DB_USERNAME'))
    password = str(os.environ.get('SQL_DB_PASSWORD'))
    driver = '{ODBC Driver 17 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
    row = cursor.fetchone()

    rows = []

    while row:
        rows.append(str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()

    return rows


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(format('\n'.join(show_sql())))
