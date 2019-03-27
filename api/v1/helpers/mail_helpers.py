"""Return messages after interacting with validators and DataStructures"""
from flask import jsonify
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
        if message.check_storage():
            return jsonify({
                'status': 200,
                'message': 'You dont have messages currently'
            }), 200
        read_all = message.fetch_all_mail()
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

        message.create_email(email_input)
        return jsonify({
            'status': 201,
            'message': 'Message has been created'
            }), 201

    def get_message(self, status):
        """Returns sent or unread messages"""
        retrieve = message.fetch_mail(status)
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
        if method == 'delete'and message.delete_email(mail_id, 1):
            return jsonify({'status': 200,
                            'message': 'Email has been deleted'})

        if method == 'get' and message.fetch_one_mail(mail_id, 1):
            return jsonify({'status': 200,
                            'data': message.fetch_one_mail(mail_id, 1)})

        return jsonify({'status': 200, 'error': 'this message doesn\'t exist'})
