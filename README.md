[![Build Status](https://travis-ci.com/Busobozihakiim/EPICMAIL_api.svg?branch=develop)](https://travis-ci.com/Busobozihakiim/EPICMAIL_api)
[![Coverage Status](https://coveralls.io/repos/github/Busobozihakiim/EPICMAIL_api/badge.svg?branch=develop)](https://coveralls.io/github/Busobozihakiim/EPICMAIL_api?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/0ff59272bb422a064fa1/maintainability)](https://codeclimate.com/github/Busobozihakiim/EPICMAIL_api/maintainability)
# Epic Mail
A web app that helps people exchange messages/information over the internet.

## Features
- `Create a user account.` User should be sign up for an account
- `Sign in a user.` User should be able to log in  using their account details
- `Get all received emails for a user.` User should be able to fetch all her emails
- `Get all unread emails for a user.` Users should be able to fetch all their unread messages
- `Get all emails sent by a user .`  Users should be able to view all the emails they sent
- `Get a specific user’s email.` User should be able to fetch and view a single message
- `Send email to individuals .` User should be able to send a message
- `Delete an email in a user’s inbox.` A user should be able to delete a message by its id

## Installing
First clone this repository

```
git clone -b develop https://github.com/Busobozihakiim/EPICMAIL_api.git 
cd EPICMAIL_api
```

Then create a virtual environment
```
virtualenv epicmail
```
and start it
```
On Windows
epicmail/Scripts/activate
On linux
source epicmail/bin/activate
```

Then install all the necessary dependencies
```
pip install -r requirements.txt
```

## Running
At the terminal type in
```
python run.py
```

To run tests run this command at the console/terminal
```
pytest
```

Use the api endpoints with an app like [Postman](https://www.getpostman.com/apps) 

## Hosted on Heroku
The online api can be found [here](https://epicmail007.herokuapp.com/api/v1/)

And documentation is [here](https://epicmail007.herokuapp.com/apidocs/)

Acceptable post format When:
- Signing up for an account
```
{
    'email' : String,
    'firstName' : String,
    'lastName' : String,
    'password' : String,
}
```
- logging in
```
{
    'email':string,
    'password':string,

}
```
- Sending an Email
```
{
    'to' : string,
    'from' : string,
    'subject' : String ,
    'message' : String ,
}
```

## Available API Endpoints
|  EndPoint  |  Functionality  |
| ------------- | ------------- |
| POST /auth/signup | Create a user account. |
| POST /auth/login | Login a user. |
| POST /messages | Create or send an email. |
| GET /messages | Fetch all received emails. |
| GET /messages/unread | Fetch all unread received emails. |
| GET /messages/sent | Fetch all sent emails. |
| GET /messages/\<message-id> | Fetch a specific email record. |
| DELETE /messages/<message-id> | Delete a specific email record. |
