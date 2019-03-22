"""Endpoints Related to Authentication"""
from flask import jsonify, request
from api.v1 import apiv1
from api.v1.helpers.user_helpers import UserHelpers

user_helper = UserHelpers()


@apiv1.route('/', methods=['POST', 'GET'])
def home():
    """The default route"""
    return jsonify({
        'message': 'Welcome To EpicMail',
        'status': '200'
        }), 200


@apiv1.route('/signup', methods=['POST'])
def signup():
    """Create User Account"""
    data = request.get_json()
    return user_helper.make_user(data)
