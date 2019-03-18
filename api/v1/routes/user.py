from flask import jsonify
from api.v1 import apiv1

@apiv1.route('/', methods=['POST', 'GET'])
def home():
    """The default route"""
    return jsonify({
            'message': 'Welcome To EpicMail',
            'status': '200'
        }), 200