import logging

import azure.functions as func
# Add more dependencies here as you need to by importing and adding to requirements.txt

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
       HttpTrigger hello world where you insert &name=World to get the url to get you 'Hello World'
    """

    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    # This code below is all error handling in case users do not enter a 'name' string into the url
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    # Modify the code below in order to change the outcome of your function code
    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
