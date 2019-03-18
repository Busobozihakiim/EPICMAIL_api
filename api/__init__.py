from flask import Flask
from config import configuration
from api.v1 import apiv1

def create_app(config_name):
    """create flask app"""
    app = Flask(__name__)
    app.config.from_object(configuration[config_name])
    app.register_blueprint(apiv1, url_prefix="/api/v1")
    return app
