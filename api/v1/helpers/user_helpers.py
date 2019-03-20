"""Creates User And Returns token"""
from flask import jsonify
from api.v1.validators.input_validator import Validate
from api.v1.models.user_model import Users

validation = Validate()
signup = Users()


class UserHelpers:
    def make_user(self, signup_data):
        """Checks if data is valid gives a user an access token"""
        if len(signup_data) < 4:
            return jsonify({
                'status': 400,
                'message': 'Your missing a field'
                }), 400

        if not validation.validate_email(signup_data['email']):
            return jsonify({
                'status': 400,
                'error': 'Invalid Email'
                }), 400

        if not validation.validate_password(signup_data['password']):
            return jsonify({
                'status': 400,
                'error': 'Password must be more than 8 characters'
                }), 400

        if not validation.validate_names(
                signup_data['firstName'], signup_data['firstName']):
            return jsonify({
                'status': 400,
                'error': 'Names must be strings'
                }), 400

        signup.create_user(signup_data)
        
        return jsonify({
            'status': 201,
            'data': [{
                'token': '45erkjherht45495783'
                }]
            }), 201
