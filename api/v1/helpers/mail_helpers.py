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
      
        if validation.validate_email(email_input['from']) == False or \
           validation.validate_email(email_input['to']) == False:
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

    def get_message(self, status):
        retrieve = message.fetch_mail(status)
        if not retrieve:
            return jsonify({
                'status': 200,
                'message': 'You don\'t have any {} messages'.format(status)
            }), 200
        return jsonify({
                'status': 200,
                'data': retrieve
            }), 200
    
    def get_or_delete_email(self, mail_id, method):
        if method == 'delete':
            delete = message.delete_email(mail_id)
            if delete:
                return jsonify({'status': 200, 'message': 'Email has been deleted'})

        if method == 'get':
            select = message.fetch_one_mail(mail_id)
            if select : 
                return jsonify({'status':200, 'data' : select})
            
        return jsonify({'status':200, 'error':'this message doesn\'t exist'})

