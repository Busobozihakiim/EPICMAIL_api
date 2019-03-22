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
