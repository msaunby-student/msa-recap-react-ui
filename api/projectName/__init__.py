import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

        return func.HttpResponse('FEE1504',
             status_code=200
        )