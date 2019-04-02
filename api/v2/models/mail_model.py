"""MESSAGES ENTITY"""
from datetime import datetime
from api.v2.models.database import Database


class Messages:
    """Maps to the Messages entity"""
    storage = Database()

    def create_email(self, uid, receiver_id, args):
        """Method to send an email"""
        one_email = self.storage.save_message(args['subject'], args['message'],
                                              receiver_id, uid)
        print(one_email)
        return one_email


    def check_contact(self, email):
        """Does the contact exist"""
        if self.storage.userid(email):
            return self.storage.userid(email)
        return False

    def fetch_all_mail(self, uid):
        """Return all"""
        all_mail = self.storage.fetch_inbox(uid)
        return self.names2values(all_mail)

    def fetch_mail(self, status, uid):
        """Return based on status"""
        all_mail = self.storage.get_by_status(status, uid)
        return self.names2values(all_mail)        

    def fetch_one_mail(self, uid, mail_id):
        """Return one message"""
        all_mail = self.storage.get_from_table(mail_id)
        return self.names2values(all_mail)

    def delete_email(self, Id, uid):
        """Removes mail from storage"""
        print(self.storage.get_from_table(Id))
        if self.storage.get_from_table(Id) == []:
            return False
        return self.storage.delete_message(Id)
        
    
    def names2values(self, all_mail):
        colnames = ['message_id', 'created_on', 'subject', 'message', 'sender_id', 'receiver_id', 'sender_status', 'receiver_status']
        mail = []
        for value in all_mail:
            mail.append(dict(zip(colnames, value)))
        if mail:
            return mail
        return False
