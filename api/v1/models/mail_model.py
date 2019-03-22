"""MESSAGES ENTITY"""
from datetime import datetime
MESSAGES = []

class Messages:
    def __init__(self):
        self.messages = MESSAGES
    
    def create_email(self, args):
        """Method to send an email"""
        one_email = {
            'id' : len(self.messages) + 1, 
            'createdOn': datetime.now(),
            'subject': args['subject'],
            'message': args['message'],
            'senderId': args['from'],
            'receiverId':args['to'],
            'status' : 'sent'
        }
        self.messages.append(one_email)
        return one_email

    def check_storage(self):
        if self.messages == []:
            return True
        return False

    def fetch_all_mail(self):
        return self.messages