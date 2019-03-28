"""Creates, returns and deletes groups and its members"""
from flask import jsonify
from api.v1.validators.input_validator import Validate
from api.v1.models.database import Database
from flask_jwt_extended import get_jwt_identity

validation = Validate()
storage = Database()


class GroupHelpers:
    """
    Methods for creating, deleting, adding
    users and deleting users from a group
    """
    def get_groups(self):
        """Returns all groups"""
        uid = get_jwt_identity()
        all_groups = storage.get_all_from_table('groups', uid)
        colnames = ['created_on', 'group_id', 'group_name', 'role', 'user_id']
        groups = []
        for value in all_groups:
            groups.append(dict(zip(colnames, value)))

        if all_groups == []:
            return jsonify({
                'status': 200,
                'message': 'You dont have any groups'
            })
        return jsonify({
            'status': 200,
            'data': groups
        })
        dict

    def make_group(self, name):
        """Creates a new group"""
        uid = get_jwt_identity()
        newgrp = storage.save_group(name['name'], uid)
        return jsonify({'status': 201, 'data': [newgrp]})