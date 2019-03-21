"""Mock data to be used in the tests"""

signup_data = {
    "email": "qw@epictester.com",
    "firstName": "String",
    "lastName": "String",
    "password": "ferdertf"
    }

missing_required_data = {
    "email": "testing@ngalabi.com",
    "lastName": "String",
    "password": "ferdertf"
}

bad_email = {
    "email": "testing.ngalabi.com",
    "firstName": "String",
    "lastName": "String",
    "password": "ferdertf"
}

short_password = {
    "email": "testing@ngalabi.com",
    "firstName": "String",
    "lastName": "String",
    "password": "rdertf"
}

bad_names = {
    "email": "testing@ngalabi.com",
    "firstName": "6",
    "lastName": "String",
    "password": "ferdertf"
}

missing_login_field = {
    "email": "testing@ngalabi.com"
}

login_data = {
    "email": "testing@ngalabi.com",
    "password": "ferdertf"
}

bad_creds = {
    "email": "testing@ngalabi.com",
    "password": "ferdertf"
}