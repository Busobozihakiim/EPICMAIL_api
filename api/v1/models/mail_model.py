"""MESSAGES ENTITY"""
from datetime import datetime


class Messages:
    """Maps to the Messages entity"""
    USERMESSAGES = []

    def __init__(self):
        self.message = Messages.USERMESSAGES

    def create_email(self, args):
        """Method to send an email"""
        one_email = {
            'id': len(self.message) + 1,
            'createdOn': datetime.now(),
            'subject': args['subject'],
            'message': args['message'],
            'senderId': args['from'],
            'receiverId': args['to'],
            'status': 'sent'
        }
        self.message.append(one_email)
        return one_email

    def check_storage(self):
        """Are messages available"""
        if self.message == []:
            return True
        return False

    def fetch_all_mail(self):
        """Return all"""
        return self.message

    def fetch_mail(self, status):
        """Return based on status"""
        folder = []
        for mail in self.message:
            if mail['status'] == '{}'.format(status):
                folder.append(mail)
        if folder:
            return folder
        return False

    def fetch_one_mail(self, this_id):
        """Return one message"""
        email = []
        print(self.message)
        print(email)
        for this_email in self.message:
            if this_email['id'] == this_id:
                this_email['status'] = 'read'
                email.append(this_email)
        if not email:
            return False
        return email

    def delete_email(self, the_id):
        """Removes mail"""
        for email in self.message:
            if email['id'] == the_id:
                del self.message[0]
                return True
        return False
