"""USER ENTITY """
from werkzeug.security import generate_password_hash, check_password_hash
from api.v1.models.database import Database


class Users():
    """Maps to the user entity"""
    storage = Database()

    def __init__(self):
        pass

    def create_user(self, args):
        """ Creates a user"""
        email = args['email']
        firstname = args['firstName']
        lastname = args['lastName']
        password = generate_password_hash(args['password'], 'pbkdf2:sha256', 9)
        savedUser = self.storage.save_user(firstname, lastname, email, password)
        return True

    def check_email_exists(self, email):
        """checks if an email is already used"""
        if self.storage.check_email(email):
            return True
        return False

    def check_matching_password(self, email, login_pass):
        """check if password and email exist"""
        password = self.storage.login_user(email)
        if check_password_hash(password, login_pass):
            return True
        return False
