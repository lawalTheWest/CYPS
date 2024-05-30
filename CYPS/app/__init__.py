# app/__init__.py
import os
from flask import Flask, render_template

template_dir = os.path.abspath('path/to/custom_templates')

def create_app():
    app = Flask(__name__)

    with app.app_context():
        # Imports parts of the application
        from . import routes

        # Registers Blueprints / APIs
        # from .api import api_bp
        # app.register_blueprint(api_bp, url_prefix='/api')

        return app
