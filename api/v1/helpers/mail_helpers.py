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

    def send_message(self, email_input):
        if 4 > len(email_input) < 4:
            return jsonify({
                'status': 400,
                'error': 'Must enter four fields'
                }), 400
        
        to = validation.validate_email(email_input['to']) 
        sender = validation.validate_email(email_input['from'])
        
        if to == False or sender == False:
            return jsonify({
                'status': 400,
                'error': 'An email is Invalid'
                }), 400
        
        if email_input['from'] == email_input['to']:
           return jsonify({
                'status': 400,
                'error': 'You can\'t send yourself an email'
                }), 400

        for key, value in email_input.items():
            if value in ("", " "):
                return jsonify({"status":400,
                                "error":"Missing '{}' in your input".format(key)
                                }), 400


        send = message.create_email(email_input)
        return jsonify({
            'status': 201,
            'data': send
        }), 201
