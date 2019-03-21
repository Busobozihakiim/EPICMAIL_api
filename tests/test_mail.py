import json
from .test_base import BaseTest

class TestMail(BaseTest):
    def test_get_messages(self):
        """Test get all messages"""
        response = self.app.get('api/v1/messages')
        self.assertEquals(response.status_code,  200)
        
    def test_get_messages_null(self):
        """Test get all messages when there are zero in the inbox"""
        response = self.app.get('api/v1/messages')
        self.assertTrue(response.status_code,  200)
        self.assertIn(response.get_json()['message'], 'You dont have messages currently')
