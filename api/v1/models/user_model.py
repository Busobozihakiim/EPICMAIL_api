"""USER ENTITY """
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

class Users:
    USER = []

    def __init__(self):        
        self.users = Users.USER

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

    def check_matching_password(self, email, password):
        """check if password and email exist"""
        for a_user in self.users:
            if a_user['email'] == email and \
               check_password_hash(a_user['password'], password):
                return True
        return False
