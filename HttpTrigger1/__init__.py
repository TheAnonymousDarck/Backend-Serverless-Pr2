import logging
from cryptography.fernet import Fernet

import azure.functions as func
    
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    key = Fernet.generate_key()
    f = Fernet(key)

    mensaje = req.params.get('mensaje')
    if not mensaje:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            mensaje = req_body.get('mensaje')
    
    if mensaje:
        temp = mensaje.encode()
        encriptado = f.encrypt(temp)
        
        return func.HttpResponse(f"Key: {key} \n original: {mensaje} \n encriptado: {encriptado}")
    else:
        return func.HttpResponse(            
             f"This HTTP triggered function executed successfully. Pass a mensaje in the query string or in the request body for a personalized response. \n",
             status_code=200
        )

    # objeto = {
    #     'mensaje': mensaje,
    #     'key': n,
    #     'encrypt': encriptado
    # }