from flask import jsonify, request
from api.v1 import apiv1
from api.v1.helpers.mail_helpers import MessageHelpers

messages = MessageHelpers()

@apiv1.route('/messages', methods=['GET'])
def returns_mail():
    return messages.get_messages()

@apiv1.route('/messages', methods=['POST'])
def sends_email():
    data = request.get_json()
    return messages.send_message(data)

@apiv1.route('/messages/sent', methods=['GET'])
def view_sent_emails():
    return messages.get_message('sent')

@apiv1.route('/messages/<int:mail_id>', methods=['GET'])
def view_one_email(mail_id):
    return messages.get_one_message(mail_id)

@apiv1.route('/messages/unread', methods=['GET'])
def view_unread_email():
    return messages.get_message('unread')