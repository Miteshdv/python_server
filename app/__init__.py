"""
This module initializes the Flask application.
"""

from flask import Flask

def create_app():
    """
    Create and configure the Flask application.

    Returns:
        app (Flask): The configured Flask application.
    """
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes
        return app