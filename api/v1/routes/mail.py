"""Contains Endpoints that work on messages features"""
from flask import request
from flasgger.utils import swag_from
from api.v1 import apiv1
from api.v1.helpers.mail_helpers import MessageHelpers

messages = MessageHelpers()


@apiv1.route('/messages', methods=['GET', 'POST'])
@swag_from('../docs/send_messages.yml', methods=['POST'])
@swag_from('../docs/get_messages.yml', methods=['GET'])
def get_or_send_emails():
    """Endpoint to return or send emails"""
    if request.method == 'GET':
        return messages.get_messages()
    data = request.get_json()
    return messages.send_message(data)


@apiv1.route('/messages/<string:status>', methods=['GET'])
@swag_from('../docs/view_message_by_status.yml', methods=['GET'])
def view_sent_or_unread_emails(status):
    """Endpoint to return sent or unread emails"""
    return messages.get_message(status)


@apiv1.route('/messages/<int:mail_id>', methods=['GET', 'DELETE'])
@swag_from('../docs/get_email_by_id.yml', methods=['GET'])
@swag_from('../docs/delete_email_by_id.yml', methods=['DELETE'])
def view_or_delete_emails(mail_id):
    """Endpoint to view or delete emails """
    if request.method == 'GET':
        return messages.get_or_delete_email(mail_id, 'get')
    return messages.get_or_delete_email(mail_id, 'delete')
