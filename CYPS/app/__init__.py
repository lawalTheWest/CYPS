# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        # Imports parts of the application
        from . import routes

        # Registers Blueprints / APIs
        # from .api import api_bp
        # app.register_blueprint(api_bp, url_prefix='/api')

        return app
