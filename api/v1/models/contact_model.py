"""CONTACT ENTITY"""
from flask import jsonify
from api.v1.validators.input_validator import Validate

validation = Validate()


class Contacts:
    all_contacts = []

    def add_contact(self, args):
        """save contact"""
        if validation.validate_email(args['email']) is not True:
            return validation.validate_email(args['email'])

        if not validation.validate_names(args['firstname'], args['lastname']):
            return jsonify({'status': 400,
                            'error': 'Names should be strings'}), 400

        contact = {
            'id': len(Contacts.all_contacts) + 1,
            'email': args['email'],
            'firstName': args['firstname'],
            'lastName': args['lastname']
        }
        Contacts.all_contacts.append(contact)
        return jsonify({'status': 201, 'data': contact}), 201

    def get_contacts(self):
        """returns all contacts"""
        if Contacts.all_contacts == []:
            return jsonify({'status': 200, 'error': 'You have no contacts'})
        return jsonify({'status': 200, 'data': Contacts.all_contacts})

    def check_contact(self, email):
        """Does a contact exist"""
        if not Contacts.all_contacts:
            return jsonify({'status': 200,
                            'error': 'You have no contacts'})
        contact = [contact for contact in Contacts.all_contacts if contact['email'] == email]
        print(contact)
        if len(contact) != 0:
            return True
        return jsonify({'status': 200,
                        'error': 'The email your sending to is not in your contacts'})

    def remove_contact(self, the_id):
        """deletes a contact"""
        for contact in Contacts.all_contacts:
            if contact['id'] == the_id:
                del Contacts.all_contacts[0]
                return jsonify({'status': 200, 'error': 'Contact removed'})
        return jsonify({'status': 200, 'error': 'Contact doesn\'t exist'})
