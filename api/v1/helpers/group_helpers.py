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
        colnames = ['group_id', 'group_name', 'role', 'created_on', 'user_id']
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
    
    def remove_group(self, Gid):
        """deletes a group"""
        uid = get_jwt_identity()
        delete = storage.delete_from_table('groups', 'group', Gid, uid)
        if delete:
            return jsonify({'status': 200,
                            'message': 'Group has been deleted'})
    
    def new_grp_user(self, Gid):
        """Saves a user """
        saved_user = storage.grp_user(Gid)
        print(saved_user)
        if saved_user:
            return jsonify({'status': 201, 'data': [saved_user]})
        return jsonify({'status': 200, 'error': 'Group doesn\'t exist'})

    def delete_user(self, Gid, uid):
        """Removes a group member"""
        delete = storage.delete_user(Gid, uid)
        if delete:
            return jsonify({'status': 200,
                            'message': 'user removed from group'})

    def change_name(self, Gid, name):
        """Update the name of the group"""
        uid = get_jwt_identity()
        update = storage.update(name['name'], Gid, uid)
        if not update:
            return jsonify({'status': 200,
                            'error': 'Can\'t change name of unavialable group'})
        return jsonify({'status': 200,
                        'data': update})
