"""MESSAGES ENTITY"""
from datetime import datetime
from api.v1.models.database import Database


class Messages():
    """Maps to the Messages entity"""
    storage = Database()

    def create_email(self, args):
        """Method to send an email"""
        one_email = self.storage.save_message(args['subject'], args['message'],
                                              args['from'], args['to'],)
        return one_email

    def check_storage(self):
        """Are messages available"""
        if self.storage.get_all_from_table('messages'):
            return False
        return True

    def fetch_all_mail(self):
        """Return all"""
        return self.storage.get_all_from_table('messages')

    def fetch_mail(self, status):
        """Return based on status"""
        if self.storage.get_by_status(status, 1):
            return self.storage.get_by_status(status, 1)
        return False

    def fetch_one_mail(self, Object_id, Userid):
        """Return one message"""
        return self.storage.get_from_table('messages', 1, Object_id)

    def delete_email(self, Id, Uid):
        """Removes mail from storage"""
        return self.storage.delete_from_table('messages', 'message', Id, 1)
