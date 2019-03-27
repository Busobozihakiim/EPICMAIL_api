"""CONTACT ENTITY"""
from flask import jsonify
from api.v1.validators.input_validator import Validate
from api.v1.models.database import Database

validation = Validate()


class Contacts():
    storage = Database()

    def __init__(self):
        pass

    def add_contact(self, args):
        """save contact"""
        if validation.validate_email(args['email']) is not True:
            return validation.validate_email(args['email'])

        if validation.validate_names(args['firstname'], args['lastname']) is not True:
            return validation.validate_names(args['firstname'], args['lastname'])

        self.storage.save_contact(args['firstname'], args['lastname'],
                                  args['email'], 1)
        return jsonify({'status': 201,
                        'message': 'contact has been saved'}), 201

    def get_contacts(self):
        """returns all contacts"""
        saved_contacts = self.storage.get_all_from_table('Contacts')
        if not saved_contacts:
            return jsonify({'status': 200, 'error': 'You have no contacts'})
        return jsonify({'status': 200, 'data': saved_contacts})

    def check_contact(self, email, userid=None):
        """Does a contact exist"""
        saved_contacts = self.storage.get_all_from_table('Contacts')
        if not saved_contacts:
            return jsonify({'status': 200,
                            'error': 'You have no contacts'})
        contact = self.storage.contact_exist(email, 1)
        if contact:
            return True
        return jsonify({'status': 200,
                        'error': 'The email your sending to \
                                  is not in your contacts'})

    def remove_contact(self, the_id, user_id):
        """deletes a contact"""
        delete = self.storage.delete_from_table('contacts', 'contact', the_id, user_id)
        if delete:
            return jsonify({'status': 200, 'error': 'Contact removed'})
        return jsonify({'status': 200, 'error': 'Contact doesn\'t exist'})
