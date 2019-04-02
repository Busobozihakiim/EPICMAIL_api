"""Endpoints Related to Authentication"""
from flask import jsonify, request
from flasgger.utils import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.v2 import apiv2
from api.v2.helpers.user_helpers import UserHelpers

user_helper = UserHelpers()


@apiv2.route('/', methods=['POST', 'GET'])
def home():
    """The default route"""
    return jsonify({
        'message': 'Welcome To EpicMail',
        'status': '200'
        }), 200


@apiv2.route('/auth/signup', endpoint='signup', methods=['POST'])
@swag_from('../docs/signup.yml', methods=['POST'])
def signup():
    """Creates a User Account """
    data = request.get_json()
    return user_helper.make_user(data)


@apiv2.route('/auth/login', endpoint='login', methods=['POST'])
@swag_from('../docs/login.yml', methods=['POST'])
def login_user():
    """logs in a user"""
    data = request.get_json()
    return user_helper.login_user(data)

@apiv2.route('/auth/reset', endpoint='reset', methods=['POST'])
def login_user():
    """resets a password"""
    data = request.get_json()
    return user_helper.reset_link(data)
