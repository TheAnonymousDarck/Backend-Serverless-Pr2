import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # headers = {
    #     "Access-Control-Allow-Origin" : "http://localhost:3000",
    #     "Access-Control-Allow-Credentials" : "true",
    #     "Access-Control-Allow-Methods" : "GET, OPTIONS",
    #     "Access-Control-Allow-Headers" : "Origin, Content-Type, Accept"
    # }

    # #handle CORS preflight
    # if req.method == "OPTIONS":
    #     return func.HttpResponse(headers=headers)
    
    return func.HttpResponse(
        'Hola mundo',
        status_code=200
    )
