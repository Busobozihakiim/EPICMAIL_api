"""Endpoints Related to groups"""
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from api.v1 import apiv1
from api.v1.helpers.group_helpers import GroupHelpers

user_grps = GroupHelpers()

@apiv1.route('/groups', methods=['POST', 'GET'])
@jwt_required
def groups():
    """Create or retrieve all groups"""
    if request.method == 'POST':
        data = request.get_json()
        return user_grps.make_group(data)
    return user_grps.get_groups()

@apiv1.route('/groups/<group_id>', methods=['DELETE'])
@jwt_required
def delete_group(group_id):
    """removes a group"""
    return user_grps.remove_group(group_id)

@apiv1.route('/groups/<group_id>/users', methods=['POST'])
@jwt_required
def add_user(group_id):
    """saves a user to a group"""
    return user_grps.new_grp_user(group_id)

@apiv1.route('/groups/<int:group_id>/users/<int:uid>', methods=['DELETE'])
@jwt_required
def delete_user(group_id, uid):
    """removes a user"""
    return user_grps.delete_user(group_id, uid)

@apiv1.route('/groups/<group_id>/name', methods=['PATCH'])
@jwt_required
def edit_name(group_id):
    """updates the name of the group"""
    data = request.get_json()
    return user_grps.change_name(group_id, data)
