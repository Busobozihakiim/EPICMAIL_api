import json
from .test_base import BaseTest
from .mock_data import (email, email_invalid, email_less, contact,
                        empty_input, message_urself, email_to_delete)


class TestMailEmpty(BaseTest):
    def test_a_get_messages(self):
        """Test get all messages when there are none in the inbox"""
        response = self.app.get('api/v1/messages')
        self.assertTrue(response.status_code,  200)
        self.assertIn(response.get_json()['message'],
                      'You dont have messages currently')

    def test_view_sent_messages(self):
        """Test sending email with empty subject or message"""
        response = self.app.get('api/v1/messages/sent')
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['message'],
                      'You don\'t have any sent messages')
    
    def test_deleting(self):
        """Test deleting emails when non are available"""
        response = self.app.delete('api/v1/messages/1')
        self.assertIn(response.get_json()['error'], 'this message doesn\'t exist')

    def test_send_email(self):
        """Test sending mail when you the contact doesn't exist"""
        response = self.app.post('api/v1/messages',
                                 data=json.dumps(email),
                                 content_type='application/json')
        self.assertTrue(response.status_code,  400)
        self.assertEqual(response.get_json()['error'], 'You have no contacts')

class TestMailFilled(BaseTest):
    def test_send_email(self):
        self.app.post('/api/v1/contact',
                      data=json.dumps(contact),
                      content_type='application/json')
        response1 = self.app.post('api/v1/messages',
                                 data=json.dumps(email),
                                 content_type='application/json')
        print(response1.data)
        self.assertTrue(response1.status_code,  400)
        self.assertEqual(response1.get_json()['data']['subject'], 'd')

    def test_get_messages(self):
        """Test get all messages"""
        self.app.post('/api/v1/contact', 
                        data=json.dumps(contact),
                        content_type='application/json')
        self.app.post('api/v1/messages',
                       data=json.dumps(email),
                       content_type='application/json')
        response = self.app.get('api/v1/messages')
        self.assertEqual(response.status_code,  200)
        self.assertEqual(response.get_json()['data'][0]['senderId'],
                         'Me@epctester.com')

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

    def test_viewing_of_sent_message(self):
        """Test viewing sent email with available """
        response = self.app.get('api/v1/messages/sent')
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['data'][0]['status'], 'sent')

    def test_viewing_email_null(self):
        """Test viewing one email with an id that doesn't exist"""
        response = self.app.get('api/v1/messages/5')
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['error'],
                      'this message doesn\'t exist')

    def test_viewing_email_exist(self):
        """Test viewing one email with an id that doesn't exist"""
        response = self.app.get('api/v1/messages/2')
        self.assertTrue(response.status_code, 200)

    def test_viewing_unread_mesages(self):
        """Test viewing unread emails"""
        response = self.app.get('api/v1/messages/unread')
        self.assertIn(response.get_json()['message'],
                         'You don\'t have any unread messages')
    
    def test_deleting(self):
        """Test deleting emails"""
        self.app.post('/api/v1/contact', 
                      data=json.dumps(contact),
                      content_type='application/json')
        self.app.post('api/v1/messages',
                      data=json.dumps(email),
                      content_type='application/json')
        response1 = self.app.delete('api/v1/messages/1')
        print(response1.data)
        self.assertIn(response1.get_json()['message'], 'Email has been deleted')
                           
                             