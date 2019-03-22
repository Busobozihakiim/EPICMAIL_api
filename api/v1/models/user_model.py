"""USER ENTITY """
import uuid
from werkzeug.security import generate_password_hash


class Users:
    def __init__(self):
        USER = []
        self.users = USER

    def create_user(self, args):
        """ Creates a user"""
        one_user = {
            'id': len(self.users) + 1,
            'email': args['email'],
            'firstName': args['firstName'],
            'lastName': args['lastName'],
            'password': generate_password_hash(args['password'], 'pbkdf2:sha256', 9),
        }
        self.users.append(one_user)
        return one_user

    def check_email_exists(self, email):
        """checks if an email is already used"""
        for a_user in self.users:
            if a_user['email'] == email:
                return True
        return False