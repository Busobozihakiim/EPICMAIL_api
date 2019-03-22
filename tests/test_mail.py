import json
from .test_base import BaseTest
from .mock_data import *

class TestMail(BaseTest):
    def test_get_messages(self):
        """Test get all messages"""
        response = self.app.get('api/v1/messages')
        self.assertEquals(response.status_code,  200)
        
    def test_get_messages_null(self):
        """Test get all messages when there are zero in the inbox"""
        response = self.app.get('api/v1/messages')
        self.assertTrue(response.status_code,  200)
        self.assertIn(response.get_json()['message'],
                      'You dont have messages currently')
    
    def test_send_mail(self):
        """Test send an email"""
        response = self.app.post('api/v1/messages',
                                 data=json.dumps(email),
                                 content_type='application/json')
        self.assertTrue(response.status_code,  201)
        self.assertEqual(response.get_json()['data']['subject'], 'd')

    def test_send_self_mail(self):
        """Test sending yourself an email"""
        response = self.app.post('api/v1/messages',
                                 data=json.dumps(message_urself),
                                 content_type='application/json')
        self.assertTrue(response.status_code,  400)
        self.assertIn(response.get_json()['error'],
                      'You can\'t send yourself an email')

    def test_send_mail_with_bad_email(self):
        """Test send an email with an invalid email"""
        response = self.app.post('api/v1/messages',
                                 data=json.dumps(email_invalid),
                                 content_type='application/json')
        self.assertTrue(response.status_code,  400)
        self.assertIn(response.get_json()['error'],
                      'An email is Invalid')
    
    def test_send_mail_less_input(self):
        """Test sending with missing input data eg subject,receiver addr"""
        response = self.app.post('api/v1/messages',
                                 data=json.dumps(email_less),
                                 content_type='application/json')
        self.assertTrue(response.status_code,  400)
        self.assertIn(response.get_json()['error'],
                      'Must enter four fields')
    
    def test_sending_no_field(self):
        """Test sending email with empty subject or message"""
        response = self.app.post('api/v1/messages',
                                 data=json.dumps(empty_input),
                                 content_type='application/json')
        self.assertTrue(response.status_code,  400)
        self.assertIn(response.get_json()['error'],
                      'Missing \'subject\' in your input')