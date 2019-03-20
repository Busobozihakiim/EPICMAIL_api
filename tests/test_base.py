import unittest
from api import create_app
from flask_jwt_extended import JWTManager

class BaseTest(unittest.TestCase):
    def setUp(self):
        app = create_app('testing')
        JWTManager(app)
        self.app = app.test_client()

    def tearDown(self):
        pass