"""USER ENTITY """
import uuid
from werkzeug.security import generate_password_hash
USERS = []


class Users:
    def __init__(self):
        self.users = USERS

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