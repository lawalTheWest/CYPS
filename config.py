import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    # Add other configuration variables here

class DevelopmentConfig(Config):
    DEBUG = True
    # Add other development-specific configurations here

class ProductionConfig(Config):
    DEBUG = False
    # Add other production-specific configurations here
