"""MESSAGES ENTITY"""
from datetime import datetime
from api.v1.models.database import Database


class Messages():
    """Maps to the Messages entity"""
    storage = Database()

    def create_email(self, uid, args):
        """Method to send an email"""
        one_email = self.storage.save_message(args['subject'], args['message'],
                                              args['from'], args['to'], uid)
        return one_email

    def check_storage(self, uid):
        """Are messages available"""
        if self.storage.get_all_from_table('messages', uid):
            return False
        return True

    def fetch_all_mail(self, uid):
        """Return all"""
        return self.storage.get_all_from_table('messages', uid)

    def fetch_mail(self, status, uid):
        """Return based on status"""
        if self.storage.get_by_status(status, uid):
            return self.storage.get_by_status(status, uid)
        return False

    def fetch_one_mail(self, uid, mail_id):
        """Return one message"""
        return self.storage.get_from_table('messages', uid, mail_id)

    def delete_email(self, Id, uid):
        """Removes mail from storage"""
        return self.storage.delete_from_table('messages', 'message', Id, uid)
