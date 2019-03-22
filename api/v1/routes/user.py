"""Endpoints Related to Authentication"""
from flask import jsonify, request
from api.v1 import apiv1
from api.v1.helpers.user_helpers import UserHelpers
#from flask_jwt_extended import jwt_required, get_jwt_identity

user_helper = UserHelpers()


@apiv1.route('/', methods=['POST', 'GET'])
def home():
    """The default route"""
    return jsonify({
        'message': 'Welcome To EpicMail',
        'status': '200'
        }), 200


@apiv1.route('/auth/signup', methods=['POST'])
def signup():
    """Create User Account"""
    data = request.get_json()
    return user_helper.make_user(data)


@apiv1.route('/auth/login', methods=['POST'])
def login():
    """login using account details"""
    data = request.get_json()
    return user_helper.login_user(data)
