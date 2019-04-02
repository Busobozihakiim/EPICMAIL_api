import json
from .mock_data import (signup_data, missing_login_field, message_urself,
                        message_urself, missing_required_data, bad_creds,
                        bad_email, bad_names, short_password, login_data,
                        signup_data2)
from .test_base import BaseTest

class TestUserRoutes(BaseTest):
    def test_home_route(self):
        """ checks if home endpoint exists"""
        response = self.app.get('/api/v2/')
        self.assertEqual(response.status_code, 200)
    
    def test_signup(self):
        """test to create an account"""
        response = self.app.post('/api/v2/auth/signup',
                                 data=json.dumps(signup_data2),
                                 content_type='application/json')
        print(response.data)
        self.assertIn(response.get_json()["message"], "Signed up successfully")
        self.assertTrue(response.status_code, 201)
    
    def test_signup_missing_field(self):
        """test if user hasn't input the firstname, 
        lastname, password, and email"""
        response = self.app.post('/api/v2/auth/signup',
                                 data=json.dumps(missing_required_data),
                                 content_type='application/json')
        self.assertIn(response.get_json()["error"], "Must enter four fields")
        self.assertEqual(response.status_code, 400)
    
    def test_signup_invalid_email(self):
        """test signup with invalid email"""
        response = self.app.post('/api/v2/auth/signup',
                                 data=json.dumps(bad_email),
                                 content_type='application/json')
        print(response.data)
        self.assertIn(response.get_json()["error"], "An email is Invalid")                        
        self.assertEqual(response.status_code, 400)
    
    def test_signup_short_password(self):
        """test password that is less than 8 chracters"""
        response = self.app.post('/api/v2/auth/signup',
                                 data=json.dumps(short_password),
                                 content_type='application/json')
        print(response.data)
        self.assertIn(response.get_json()["error"], "Password must be more than 8 characters")
        self.assertEqual(response.status_code, 400)
    
    def test_if_signup_name_string(self):
        """test if firstname and lastname are not strings"""
        response = self.app.post('/api/v2/auth/signup',
                                 data=json.dumps(bad_names),
                                 content_type='application/json')
        self.assertIn(response.get_json()["error"], "Names should be strings")
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        """test login"""
        response = self.app.post('/api/v2/auth/signup',
                                 data=json.dumps(signup_data),
                                 content_type='application/json')
        self.assertTrue(response.status_code, 201)
        response = self.app.post('/api/v2/auth/login',
                                 data=json.dumps(login_data),
                                 content_type='application/json')
        self.assertIn(response.get_json()["message"], "logged in successfully")
        self.assertEqual(response.status_code, 200)

    def test_login_missing_fields(self):
        """test if input is less"""
        response = self.app.post('/api/v2/auth/login',
                                 data=json.dumps(missing_login_field),
                                 content_type='application/json')
        self.assertIn(response.get_json()["error"], "Your missing an email or password")
        self.assertEqual(response.status_code, 400)

    def test_bad_credentials(self):
        """test credentials are wrong"""
        response = self.app.post('/api/v2/auth/login',
                                 data=json.dumps(bad_creds),
                                 content_type='application/json')
        self.assertIn(response.get_json()["error"], "Incorrect credentials")
        self.assertEqual(response.status_code, 400)
    
    def test_reset_link(self):
        """test sending a reset link"""
        self.app.post('/api/v2/auth/signup',
                                 data=json.dumps(signup_data),
                                 content_type='application/json')
        response = self.app.post('/api/v2/auth/reset',
                      data=json.dumps({"email":"qw@epictester.com"}),
                      content_type='application/json')
        print(response.data)
        self.assertIn(response.get_json()["data"][0]["message"], "Check your email for password reset link")
        self.assertEqual(response.status_code, 200)
    
    def test_reset_link_2(self):
        """test sending a reset link when the email doesnt exist"""
        response = self.app.post('/api/v2/auth/signup',
                                 data=json.dumps(signup_data),
                                 content_type='application/json')
        response = self.app.post('/api/v2/auth/reset',
                                 data=json.dumps({"email":"we@epictester.com"}),
                                 content_type='application/json')
        print(response.data)
        self.assertIn(response.get_json()["message"], "Invalid email")
        self.assertEqual(response.status_code, 400)
        