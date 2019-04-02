import json
from .test_base import BaseTest

class TestGroups(BaseTest):

    def test_get_groups(self):
        """Test get all groups when none are available"""
        response = self.app.get('api/v2/groups',
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['message'], 'You dont have any groups')
        
    def test_make_groups(self):
        """Test to make a group"""
        response = self.app.post('api/v2/groups', content_type='application/json',
                                data=json.dumps({"name": "Almighty"}),
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['data']['group_name'], 'Almighty')
    
    def test_get_all_groups(self):
        """Test to get all groups"""
        self.app.post('api/v2/groups', content_type='application/json',
                      data=json.dumps({"name": "Almighty"}),
                      headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.get('api/v2/groups',
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['data'][0]['group_name'], 'Almighty')

    def test_delete_group(self):
        """Test to get all groups"""
        self.app.post('api/v2/groups', content_type='application/json',
                      data=json.dumps({"name": "Almighty"}),
                      headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.delete('api/v2/groups/1',
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['message'], 'Group has been deleted')
    
    def test_delete_null_group(self):
        """Test to get all groups"""
        self.app.post('api/v2/groups', content_type='application/json',
                      data=json.dumps({"name": "Almighty"}),
                      headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.delete('api/v2/groups/55',
                                headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['error'], 'Group Doesnt exist')
    
    def test_add_group_user(self):
        """Test to add a group member"""
        self.app.post('api/v2/groups', content_type='application/json',
                      data=json.dumps({"name": "Almighty"}),
                      headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.post('api/v2/groups/1/users', headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['data'][0]['role'], 'member')
    
    def test_adds_group_user(self):
        """Test to add a group member when group doesnt exist"""
        self.app.post('api/v2/groups', content_type='application/json',
                      data=json.dumps({"name": "Almighty"}),
                      headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.post('api/v2/groups/5/users', headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['error'], 'Group doesn\'t exist')
        
    def test_deletes_group_user(self):
        """Test to remove a group member"""
        self.app.post('api/v2/groups', content_type='application/json',
                      data=json.dumps({"name": "Almighty"}),
                      headers={'Authorization': 'Bearer ' + self.token})
        self.app.post('api/v2/groups/1/users',
                      headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.delete('api/v2/groups/1/users/1', headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['message'], 'user removed from group')
    
    def test_deletes_null_group_user(self):
        """Test to remove a group member that doesnt exist"""
        self.app.post('api/v2/groups', content_type='application/json',
                      data=json.dumps({"name": "Almighty"}),
                      headers={'Authorization': 'Bearer ' + self.token})
        self.app.post('api/v2/groups/1/users',
                      headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.delete('api/v2/groups/1/users/5', headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['error'], 'group or user doesnt exist')
    
    def test_edit_group_name(self):
        """Test to change a group's name"""
        self.app.post('api/v2/groups', content_type='application/json',
                      data=json.dumps({"name": "Almighty"}),
                      headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.patch('api/v2/groups/1/name', content_type='application/json',
                                 data=json.dumps({"name": "The other gods"}),
                                 headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['message'], 'Group name updated')
    
    def test_edit_null_group_name(self):
        """Test to change a group's name when the group doest exist"""
        self.app.post('api/v2/groups', content_type='application/json',
                      data=json.dumps({"name": "Almighty"}),
                      headers={'Authorization': 'Bearer ' + self.token})
        response = self.app.patch('api/v2/groups/5/name', content_type='application/json',
                                 data=json.dumps({"name": "The other gods"}),
                                 headers={'Authorization': 'Bearer ' + self.token})
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.get_json()['error'], 'Can\'t change name of unavialable group')
        