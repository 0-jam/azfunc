import logging

import azure.functions as func

from .sql_controller import show_sql


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(format('\n'.join(show_sql())))
