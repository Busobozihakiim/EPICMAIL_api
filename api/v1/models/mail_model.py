"""MESSAGES ENTITY"""

class Messages:
    MESSAGES = []

    def __init__(self):
        self.messages = Messages.MESSAGES

    def check_storage(self):
        if self.messages == []:
            return True
        return False

    def fetch_all_mail(self):
        return self.messages