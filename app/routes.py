
from flask import current_app as app
@app.route('/')
def hello_world():
    """
    A simple endpoint that returns a 'Hello, World!' message.

    Returns:
        str: A 'Hello, World!' message.
    """
    return 'Hello, World!'