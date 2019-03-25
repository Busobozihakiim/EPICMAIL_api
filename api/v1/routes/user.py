"""Endpoints Related to Authentication"""
from flask import jsonify, request
from api.v1 import apiv1
from api.v1.helpers.user_helpers import UserHelpers
from api.v1.models.contact_model import Contacts

user_helper = UserHelpers()
contacts = Contacts()

@apiv1.route('/', methods=['POST', 'GET'])
def home():
    """The default route"""
    return jsonify({
        'message': 'Welcome To EpicMail',
        'status': '200'
        }), 200


@apiv1.route('/auth/<string:route>', methods=['POST'])
def signup(route):
    """Creates User Account or lgos in a user"""
    if route == 'signup':
        data = request.get_json()
        return user_helper.make_user(data)
    if route == 'login':
        data = request.get_json()
        return user_helper.login_user(data)

@apiv1.route('/contact', methods=['POST', 'GET'])
def contact():
    """Creates or views a contact"""
    if request.method == 'POST':
        data = request.get_json()
        return contacts.add_contact(data)
    return contacts.get_contacts()

@apiv1.route('/contact/<int:contactid>', methods=['DELETE'])
def delete_contact(contactid):
    """Remove a contact"""
    return contacts.remove_contact(contactid)
