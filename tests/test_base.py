import json
import unittest
from api import create_app
from .mock_data import signup_data
from flask_jwt_extended import JWTManager
from api.v2.models.database import Database
from .mock_data import signup_data, login_data, receiver

class BaseTest(unittest.TestCase):
    def setUp(self):
        app = create_app('testing')
        JWTManager(app)
        self.db = Database()
        self.app = app.test_client()
        self.app.post('/api/v2/auth/signup',
                                 data=json.dumps(signup_data),
                                 content_type='application/json')
        self.app.post('/api/v2/auth/signup',
                                 data=json.dumps(receiver),
                                 content_type='application/json')
        response = self.app.post('/api/v2/auth/login',
                                 data=json.dumps(login_data),
                                 content_type='application/json')
        self.token = response.get_json()["data"][0]["token"]        

    def tearDown(self):

        self.db.drop_all()
        