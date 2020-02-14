import logging

import azure.functions as func

from .monkey_generator import generate_text


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python monkey text generator.')

    gen_size = req.params.get('gen_size')
    if not gen_size:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            gen_size = req_body.get('gen_size')

    if gen_size:
        return func.HttpResponse(generate_text(int(gen_size)))
    else:
        return func.HttpResponse(
            "Please pass a gen_size on the query string or in the request body",
            status_code=400
        )
