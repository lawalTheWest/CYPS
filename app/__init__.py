# app/__init__.py

import os
from config import DevelopmentConfig # importing the appropriate config class
from flask import Flask

template_dir = os.path.abspath('path/to/custom_templates')

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__,
                template_folder=config_class.TEMPLATES_DIR,
                static_folder=config_class.STATIC_DIR)
    app.config.from_object(config_class)

    with app.app_context():
        # Imports parts of the application
        from . import routes

        # Registers Blueprints / APIs
        # from .api import api_bp
        # app.register_blueprint(api_bp, url_prefix='/api')

        return app
