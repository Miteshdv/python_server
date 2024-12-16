import requests
from flask import current_app as app
@app.route('/test')
def hello_world():
    """
    A simple endpoint that returns a 'Hello, World!' message.

    Returns:
        str: A 'Hello, World!' message.
    """
    return 'Hello, World!'

@app.route('/load_data')
def loadData():
    """
    An endpoint that fetches data from an external API and returns it.

    Returns:
        Response: The response from the external API.
    """
    url = 'https://trxivq9lv1.execute-api.us-west-2.amazonaws.com/dev/eks-gateway-resource'
    response = requests.get(url)
    return response.json()
