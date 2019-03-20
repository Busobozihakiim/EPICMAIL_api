"""USER ENTITY """
import uuid

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
            'password': args['password'],
        }
        self.users.append(one_user)
        return one_user