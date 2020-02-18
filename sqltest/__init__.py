import logging

import azure.functions as func

from .sql_controller import show_sql


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
        return func.HttpResponse(f"Hello {query}!")
    else:
        return func.HttpResponse(format('\n'.join(show_sql())))
