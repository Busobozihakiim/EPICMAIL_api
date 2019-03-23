"""MESSAGES ENTITY"""
from flask import jsonify
from datetime import datetime

class Messages:
    MESSAGES = []

    def __init__(self):
        self.messages = Messages.MESSAGES
        
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
    
    def fetch_mail(self, status):
        folder = []
        for mail in self.messages:
            if mail['status'] == '{}'.format(status):
                folder.append(mail)
        if folder:
            return folder
        return False

    def fetch_one_mail(self, this_id):
        email = []
        for this_email in self.messages:
            if this_email['id'] == this_id:
                this_email['status'] = 'read'
                email.append(this_email)
        if not email:
            return False
        return email        

    def delete_email(self, the_id):
        for email in self.messages:
            if email['id'] == the_id:
                del self.messages[0]
                return True
        return False
