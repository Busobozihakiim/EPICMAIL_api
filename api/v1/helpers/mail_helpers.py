from flask import jsonify
#from flask_jwt_extended import create_access_token
from api.v1.validators.input_validator import Validate
from api.v1.models.mail_model import Messages

validation = Validate()
message = Messages()

class MessageHelpers:
    def get_messages(self):
        if message.check_storage():
            return jsonify({
                'status':200,
                'message':'You dont have messages currently'
            }), 200
        read_all = message.fetch_all_mail()
        return jsonify({
            'status':200,
            'data': read_all
            }), 200