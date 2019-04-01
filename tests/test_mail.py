import json
from .test_base import BaseTest
from .mock_data import (email, email_invalid, email_less, empty_input,
                        message_urself, email_to_delete,email_none)


class TestMailEmpty(BaseTest):
    def test_a_get_messages(self):
        """Test get all messages when there are none in the inbox"""
        response = self.app.get('api/v2/messages',
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['message'],
                      'You dont have messages currently')

    def test_view_sent_messages(self):
        """Test viewing sent messages"""
        response = self.app.get('api/v2/messages/sent',
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['message'],
                      'You don\'t have any sent messages')
    
    def test_deleting(self):
        """Test deleting emails when non are available"""
        response = self.app.delete('api/v2/messages/5',
                                    headers={'Authorization': 'Bearer ' + self.token})
        print(response.data)
        self.assertIn(response.get_json()['error'], 'this message doesn\'t exist')

class TestMailFilled(BaseTest):
    def test_send_email(self):
        response = self.app.post('api/v2/messages',
                                 data=json.dumps(email),
                                 content_type='application/json',
                                 headers={'Authorization': 'Bearer ' + self.token})
        print(response.data)
        self.assertTrue(response.status_code,  400)
        self.assertEqual(response.get_json()['message'], 'Message has been created')
    
    def test_get_messages(self):
        """Test get all messages"""
        self.app.post('api/v2/messages',
                                 data=json.dumps(email),
                                 content_type='application/json',
                                 headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.get('api/v2/messages',
                                headers={'Authorization': 'Bearer ' + self.token})
        print(response.data)
        self.assertEqual(response.status_code,  200)
        self.assertIn(response.get_json()['data'][0]['sender_status'], 'sent')        

    def test_send_mail_with_invalid_receiver(self):
        """Test send an email when a receiver doesnt exist"""
        response = self.app.post('api/v2/messages',
                                 data=json.dumps(email_invalid),
                                 content_type='application/json',
                                 headers={'Authorization': 'Bearer ' + self.token})
        print(response.data)
        self.assertTrue(response.status_code,  400)
        self.assertIn(response.get_json()['error'],
                      'receiver doesnt exist')

    def test_send_mail_less_input(self):
        """Test sending with missing input data eg subject,receiver addr"""
        response = self.app.post('api/v2/messages',
                                 data=json.dumps(email_less),
                                 content_type='application/json',
                                 headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code,  400)
        self.assertIn(response.get_json()['error'],
                      'Must enter three fields')

    def test_sending_no_field(self):
        """Test sending email with empty subject or message"""
        response = self.app.post('api/v2/messages',
                                 data=json.dumps(empty_input),
                                 content_type='application/json',
                                 headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code,  400)
        self.assertIn(response.get_json()['error'],
                      'Missing \'subject\' in your input')

    def test_viewing_of_sent_message(self):
        """Test viewing sent email """
        self.app.post('api/v2/messages',
                                 data=json.dumps(email),
                                 content_type='application/json',
                                 headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.get('api/v2/messages/sent',
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        print(response.data)
        self.assertIn(response.get_json()['data'][0]['sender_status'], 'sent')

    def test_viewing_email_null(self):
        """Test viewing one email with an id that doesn't exist"""
        response = self.app.get('api/v2/messages/5',
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['error'],
                      'this message doesn\'t exist')

    def test_viewing_email_exist(self):
        """Test viewing one email with an id that exists"""
        self.app.post('api/v2/messages',
                                 data=json.dumps(email),
                                 content_type='application/json',
                                 headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.get('api/v2/messages/1',
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        print(response.data)
        self.assertIn(response.get_json()['data'][0]['sender_status'], 'sent')

    def test_viewing_unread_mesages(self):
        """Test viewing unread emails"""
        response = self.app.get('api/v2/messages/unread',
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertIn(response.get_json()['message'],
                         'You don\'t have any unread messages')
    
    def test_zdeleting(self):
        """Test deleting emails"""
        self.app.post('api/v2/messages',
                                 data=json.dumps(email),
                                 content_type='application/json',
                                 headers={'Authorization': 'Bearer ' + self.token})
        response1 = self.app.delete('api/v2/messages/1',
                                    headers={'Authorization': 'Bearer ' + self.token})
        print(response1.data)
        self.assertIn(response1.get_json()['message'], 'Email has been deleted')                     
                             
