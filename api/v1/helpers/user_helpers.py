"""Creates User And Returns token"""
from flask import jsonify
#from flask_jwt_extended import create_access_token
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
                'error': 'Your missing a field'
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
                signup_data['firstName'], signup_data['lastName']):
            return jsonify({
                'status': 400,
                'error': 'Names must be strings'
                }), 400

        if signup.check_email_exists(signup_data['email']):
            return jsonify({
                'status': 400,
                'error': 'Email already exists'
                }), 400

        signup.create_user(signup_data)
        return jsonify({
            'status': 201,
            'data': 'account created'
            }), 201

    def login_user(self, login_data):
        """Checks if creds are valid and gives a user an access token"""
        if len(login_data) < 2:
            return jsonify({
                'status': 400,
                'error': 'Your missing an email or password'
                }), 400

        access_account = signup.check_matching_password(
            login_data['email'], login_data['password'])

        if not access_account:
            return jsonify({
                'status': 400,
                'error': 'Incorrect credentials'
                }), 400
        return jsonify({
            'status': 200,
            'message': 'logged in succesfully'
        }), 200
