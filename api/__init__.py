import os
from flask import Flask
from config import configuration
from api.v1 import apiv1
from flasgger import Swagger
#from api.v1.models.database import Database
from flask_jwt_extended import JWTManager


def create_app(config_name):
    """create flask app"""
    app = Flask(__name__)
    app.config.from_object(configuration[config_name])
    app.register_blueprint(apiv1, url_prefix="/api/v1")
    app.config['JWT_SECRET_KEY'] = os.environ['SECRET-KEY']
    #db = Database(app.config['DATABASE_URL'])
    #print(app.config['DATABASE_URL'])
    #db.create_table()
    jwt = JWTManager(app)
    Swagger(app)
    return app

def login_user(self, email):
        """Return the password hash of a give email"""
        query = "SELECT PASSWORD FROM users WHERE email='{}'".format(email)
        print(query)
        self.cur.execute(query)
        user = self.cur.fetchone()
        return user[0]
