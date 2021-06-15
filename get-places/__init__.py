import logging

import azure.functions as func

from .sql_controller import get_places


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(format(get_places()), mimetype='application/json')
