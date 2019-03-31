import os
from flask import Flask
from config import configuration
from api.v2 import apiv2
from flasgger import Swagger
from flask_jwt_extended import JWTManager


def create_app(config_name):
    """create flask app"""
    app = Flask(__name__)
    app.config.from_object(configuration[config_name])
    app.register_blueprint(apiv2, url_prefix="/api/v2")
    app.config['JWT_SECRET_KEY'] = os.environ['SECRET-KEY']
    jwt = JWTManager(app)
    Swagger(app)
    return app
