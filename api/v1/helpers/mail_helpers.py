"""Return messages after interacting with validators and DataStructures"""
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from api.v1.validators.input_validator import Validate
from api.v1.models.mail_model import Messages
from api.v1.models.contact_model import Contacts

validation = Validate()
message = Messages()
contact = Contacts()


class MessageHelpers:
    """Contains methods for executing enpoint tasks
    which are mostly validation and connecting to models
    for retrival, stroring or querying data
    """
    def get_messages(self):
        """Returns all messages"""
        uid = get_jwt_identity()
        if message.check_storage(uid):
            return jsonify({
                'status': 200,
                'message': 'You dont have messages currently'
            }), 200
        read_all = message.fetch_all_mail(uid)
        return jsonify({
            'status': 200,
            'data': read_all
            }), 200

    def send_message(self, email_input):
        """Sends a message"""
        if validation.validate_length(email_input) is not False:
            return validation.validate_length(email_input)

        if contact.check_contact(email_input['to']) is not True:
            return contact.check_contact(email_input['to'])
        
        uid = get_jwt_identity()
        message.create_email(uid, email_input)
        return jsonify({
            'status': 201,
            'message': 'Message has been created'
            }), 201

    def get_message(self, status):
        """Returns sent or unread messages"""
        uid = get_jwt_identity()
        retrieve = message.fetch_mail(status, uid)
        if retrieve is False:
            return jsonify({
                'status': 200,
                'message': 'You don\'t have any {} messages'.format(status)
            }), 200
        return jsonify({
            'status': 200,
            'data': retrieve
            }), 200

    def get_or_delete_email(self, mail_id, method):
        """deletes or returns an email"""
        uid = get_jwt_identity()

        if method == 'delete'and message.delete_email(mail_id, uid):
            return jsonify({'status': 200,
                            'message': 'Email has been deleted'})

        if method == 'get' and message.fetch_one_mail(uid, mail_id):
            return jsonify({'status': 200,
                            'data': message.fetch_one_mail(uid, mail_id)})

        return jsonify({'status': 200, 'error': 'this message doesn\'t exist'})
