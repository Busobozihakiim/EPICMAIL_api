import json
import unittest
from api import create_app
from .mock_data import signup_data

class BaseTest(unittest.TestCase):
    def setUp(self):
        app = create_app('testing')
        #JWTManager(app)
        self.app = app.test_client()

    def tearDown(self):
        pass