import logging

import azure.functions as func

from .sql_controller import exec_sql


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    query = req.params.get('query')
    if not query:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            query = req_body.get('query')

    if query:
        return func.HttpResponse(format(exec_sql(query)))
    else:
        return func.HttpResponse(
            "Please pass a SQL query on the query string or in the request body",
            status_code=400
        )
