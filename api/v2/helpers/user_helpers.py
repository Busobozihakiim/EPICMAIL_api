"""Creates User And Returns token"""
from flask import jsonify
from api.v2.validators.input_validator import Validate
from api.v2.models.user_model import Users
from api.v2.models.database import Database
from flask_jwt_extended import create_access_token
import datetime

validation = Validate()
signup = Users()


class UserHelpers:
    user = Database()

    def make_user(self, signup_data):
        """Checks if data is valid gives a user an access token"""
        if len(signup_data) < 4:
            return jsonify({'status':400,
                            'error':'Must enter four fields'}), 400

        if validation.validate_email(signup_data['email']) is not True:
            return validation.validate_email(signup_data['email'])

        if validation.validate_password(signup_data['password']) is not True:
            return validation.validate_password(signup_data['password'])

        if validation.validate_names(signup_data['firstName'],
                                     signup_data['lastName']) is not True:
            return validation.validate_names(signup_data['firstName'],
                                             signup_data['lastName'])

        if signup.check_email_exists(signup_data['email']):
            return jsonify({
                'status': 400,
                'error': 'Email already exists'
                }), 400

        signup.create_user(signup_data)
        expires = datetime.timedelta(hours=2)
        uid=self.user.userid(signup_data['email'])
        access_token = create_access_token(identity=uid, expires_delta=expires)
        
        return jsonify({
            'message' : 'Signed up successfully',
            'status': 201,
            'data': [{'token': access_token}]
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

        uid=self.user.userid(login_data['email'])
        expires = datetime.timedelta(hours=2)
        access_token = create_access_token(identity=uid, expires_delta=expires)
        if not access_account:
            return jsonify({
                'status': 400,
                'error': 'Incorrect credentials'
                }), 400
        return jsonify({
            'message' : 'logged in successfully',
            'status': 200,
            'data': [{'token': access_token}]
        }), 200

    def reset_link(self, reset_data):
        if signup.check_email_exists(reset_data['email']):
            return jsonify({
                'status': 200,
                'data': [{
                    'message' : 'Check your email for password reset link',
                    'email': reset_data['email']
                    }]
            })
        return jsonify({
                'status': 400,
                'message' : 'Invalid email'
                }), 400
