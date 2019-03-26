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
    "email": "qw@epictester.com",
    "password": "ferdertf"
}
bad_creds = {
    "email": "testing@ngalabi.com",
    "password": "ferdertf"
}
email = {
    "subject" : "d",
	"message" : "String" ,
	"from" : "Me@epctester.com" ,
	"to" : "John@epictester.com"
}
message_urself = {
    "subject" : "d",
	"message" : "String" ,
	"from" : "me@tester.com" ,
	"to" : "me@tester.com"
}
email_invalid = {
    "subject" : "d",
	"message" : "String" ,
	"from" : "qwepictester.com" ,
	"to" : "qw@epictester.com"
}
email_less = {
	"message" : "String" ,
	"from" : "qw@epctester.com" ,
	"to" : "qw@epictester.com"
}
empty_input = {
    "subject" : "",
	"message" : "String" ,
	"from" : "qw@epctester.com" ,
	"to" : "qw@epictester.com"
}
contact = {
    "firstname" : "John",
	"lastname" : "Smith" ,
	"email" : "John@epictester.com"    
}
contact_bad_email = {
    "firstname" : "John",
	"lastname" : "Smith" ,
	"email" : "Johntester.com"    
}
contact_bad_name = {
    "firstname" : "5",
	"lastname" : "Smith" ,
	"email" : "John@epictester.com"    
}
email_to_delete = {
    "subject" : "d",
	"message" : "String" ,
	"from" : "Me@epctester.com" ,
	"to" : "John@epictester.com"
}
email_bad_contact = {
    "subject" : "d",
	"message" : "String" ,
	"from" : "Me@epctester.com" ,
	"to" : "Johnepictester.com"
}
email_none = {
    "subject" : "d",
	"message" : "String" ,
	"from" : "Me@epctester.com" ,
	"to" : "Joh@epictester.com"
}