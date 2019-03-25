from flask import request
"""Contains Endpoints that work on messages features"""
from api.v1 import apiv1
from api.v1.helpers.mail_helpers import MessageHelpers

messages = MessageHelpers()


@apiv1.route('/messages', methods=['GET', 'POST'])
def get_or_send_emails():
    """Endpoint to return or send emails"""
    if request.method == 'GET':
        return messages.get_messages()
    data = request.get_json()
    return messages.send_message(data)

@apiv1.route('/messages/<string:status>', methods=['GET'])
def view_sent_or_unread_emails(status):
    """Endpoint to return sent or unread emails"""
    return messages.get_message(status)

@apiv1.route('/messages/<int:mail_id>', methods=['GET', 'DELETE'])
def view_or_delete_emails(mail_id):
    """Endpoint to view or delete emails """
    if request.method == 'GET':
        return messages.get_or_delete_email(mail_id, 'get')
    if request.method == 'DELETE':
        return messages.get_or_delete_email(mail_id, 'delete')
