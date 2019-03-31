"""Handles email, password and username validation"""
import re
from flask import jsonify


class Validate:
    """check if user input is correct"""
    def validate_email(self, email):
        """Validates a user email"""
        if re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", email):
            return True
        return jsonify({
            'status': 400,
            'error': 'An email is Invalid'
            }), 400
        
    def validate_password(self, password):
        """Validates a user password"""
        if len(password) < 8:
            return jsonify({
                'status': 400,
                'error': 'Password must be more than 8 characters'
                }), 400
        return True
        

    def validate_names(self, fname, lname):
        """Validates the first and lastnames"""
        is_string = re.compile(r"^[a-zA-Z]+$")
        if is_string.match(fname) and is_string.match(lname):
            return True
        return jsonify({'status': 400,
                        'error': 'Names should be strings'}), 400

    def validate_length(self, user_input):
        """Check for input from user"""
        if 3 > len(user_input) < 3:
            return jsonify({
                'status': 400,
                'error': 'Must enter three fields'
                }), 400
    
        for key, value in user_input.items():
            if value in ("", " "):
                return jsonify({"status": 400,
                                "error": "Missing '{}' in your input".format(key)
                                }), 400
        return False
