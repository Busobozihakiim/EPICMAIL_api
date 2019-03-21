import json
from .mock_data import *
from .test_base import BaseTest

class TestUserRoutes(BaseTest):
    def test_home_route(self):
        """ checks if home endpoint exists"""
        response = self.app.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
    
    def test_signup(self):
        """test to create an account"""
        response = self.app.post('/api/v1/auth/signup',
                                 data=json.dumps(signup_data),
                                 content_type='application/json')
        self.assertTrue(response.status_code, 201)
    
    def test_signup_missing_field(self):
        """test if user hasn't input the firstname, 
        lastname, password, and email"""
        response = self.app.post('/api/v1/auth/signup',
                                 data=json.dumps(missing_required_data),
                                 content_type='application/json')
        self.assertIn(response.get_json()["error"], "Your missing a field")
        self.assertEqual(response.status_code, 400)
    
    def test_signup_invalid_email(self):
        """test signup with invalid email"""
        response = self.app.post('/api/v1/auth/signup',
                                 data=json.dumps(bad_email),
                                 content_type='application/json')
        self.assertIn(response.get_json()["error"], "Invalid Email")                         
        self.assertEqual(response.status_code, 400)
    
    def test_signup_short_password(self):
        """test password that is less than 8 chracters"""
        response = self.app.post('/api/v1/auth/signup',
                                 data=json.dumps(short_password),
                                 content_type='application/json')
        self.assertIn(response.get_json()["error"], "Password must be more than 8 characters")
        self.assertEqual(response.status_code, 400)
    
    def test_if_signup_name_string(self):
        """test if firstname and lastname are not strings"""
        response = self.app.post('/api/v1/auth/signup',
                                 data=json.dumps(bad_names),
                                 content_type='application/json')
        self.assertIn(response.get_json()["error"], "Names must be strings")
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        """test login"""
        response = self.app.post('/api/v1/auth/signup',
                                 data=json.dumps(signup_data),
                                 content_type='application/json')
        self.assertTrue(response.status_code, 201)
        response = self.app.post('/api/v1/auth/login',
                                 data=json.dumps(login_data),
                                 content_type='application/json')
        self.assertIn(response.get_json()["message"], "logged in succesfully")
        self.assertEqual(response.status_code, 200)

    def test_login_missing_fields(self):
        """test if input is less"""
        response = self.app.post('/api/v1/auth/login',
                                 data=json.dumps(missing_login_field),
                                 content_type='application/json')
        self.assertIn(response.get_json()["error"], "Your missing an email or password")
        self.assertEqual(response.status_code, 400)

    def test_bad_credentials(self):
        """test credentials are wrong"""
        response = self.app.post('/api/v1/auth/login',
                                 data=json.dumps(bad_creds),
                                 content_type='application/json')
        self.assertIn(response.get_json()["error"], "Incorrect credentials")
        self.assertEqual(response.status_code, 400)

    