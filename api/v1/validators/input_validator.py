"""Handles email, password and username validation"""
import re
from flask import jsonify

class Validate:
    def validate_email(self, email):
        """Validates a user email"""
        if re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", email):
            return True
        return False
        
    def validate_password(self, password):
        """Validates a user password"""
        if len(password) < 8:
            return False
        return True
    
    def validate_names(self, fname, lname):
        """Validates the first and lastnames"""
        if not re.match(r"^[a-zA-Z]+$", fname) and \
           not re.match(r"^[a-zA-Z]+$", lname):
           return False
        return True
