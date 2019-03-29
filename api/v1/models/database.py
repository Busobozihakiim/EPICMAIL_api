import os
from urllib import parse
import psycopg2

class Database:
    """Contains methods to create a db connection and create some tables"""

    def __init__(self):
        """Creates a connection to the database"""
        try:
            url = parse.urlparse(os.environ['DATABASE_URL'])
            db_url = "dbname={} user={} password={} host={} ".format(url.path[1:], url.username, url.password, url.hostname)
            self.conn = psycopg2.connect(db_url)
            self.cur = self.conn.cursor()
            self.conn.autocommit = True
            self.create_table()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error connecting to the database", error)

    def create_table(self):
        """Creates the users and messages tables"""
        queries = (
            '''
            CREATE TABLE IF NOT EXISTS Users(
            user_id serial PRIMARY KEY NOT NULL,
            email VARCHAR(20) NOT NULL,
            firstName VARCHAR(20) NOT NULL,
            lastName VARCHAR(20) NOT NULL,
            password VARCHAR(150) NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS Messages(
            message_id serial PRIMARY KEY NOT NULL,
            created_on timestamp default current_timestamp,
            subject VARCHAR(100) NOT NULL,
            message VARCHAR(500) NOT NULL,
            sender_id VARCHAR(100) NOT NULL,
            receiver_id VARCHAR(100),
            status VARCHAR(100) DEFAULT 'sent',
            user_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
            )''',
            '''
            CREATE TABLE IF NOT EXISTS Contacts(
            contact_id serial PRIMARY KEY NOT NULL,
            email VARCHAR(20) NOT NULL,
            firstname VARCHAR(20) NOT NULL,
            lastname VARCHAR(20) NOT NULL,
            user_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            ''',
            """
            CREATE TABLE IF NOT EXISTS Groups(
            group_id serial PRIMARY KEY NOT NULL,
            group_name VARCHAR(50) NOT NULL,
            role VARCHAR(100) DEFAULT 'Admin' NOT NULL,
            created_on timestamp default current_timestamp,
            user_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
            )""",
            """
            CREATE TABLE IF NOT EXISTS groupmembers(
            member_id serial primary key,
            group_id INT REFERENCES groups(group_id),
            created_on timestamp default current_timestamp,
            role VARCHAR(100) DEFAULT 'member' NOT NULL
            )"""
        )
        for sql in queries:
            self.cur.execute(sql)
        print("Tables created")

    def drop_all(self):
        drop_contacts_table = "DROP TABLE contacts cascade"
        drop_mesages_table = "DROP TABLE messages cascade"
        drop_users_table = "DROP TABLE users cascade"
        self.cur.execute(drop_contacts_table)
        self.cur.execute(drop_messages_table)
        self.cur.execute(drop_users_table)

    def save_user(self, firstname, lastname, email, password):
        """Adds a user to a database"""
        query = (''' INSERT INTO users (email, firstName, lastName, password) VALUES ('{}','{}','{}','{}')
                '''.format(email, firstname, lastname, password))
        self.cur.execute(query)
        return True
    
    def save_contact(self, firstname, lastname, email, uid):
        """Adds a contact to a database"""
        query = ('''INSERT INTO contacts (firstName, lastname, email, user_id) VALUES( '{}','{}','{}','{}')
                 '''.format(firstname, lastname, email, uid))
        self.cur.execute(query)
        return True

    def save_message(self, subject, message, receiver, sender, uid):
        """Adds a message to a database"""
        query = ('''INSERT INTO messages (subject, message, receiver_id, sender_id, user_id) VALUES('{}','{}','{}','{}','{}')
                 '''.format(subject, message, receiver, sender, uid))
        self.cur.execute(query)
        return True

    def save_group(self, name, uid):
        """Adds a group to storage"""
        query = ('''INSERT INTO groups (group_name, user_id) VALUES('{}','{}') RETURNING *'''.format(name, uid))
        self.cur.execute(query)
        colnames = [column[0] for column in self.cur.description]
        group = self.cur.fetchall()
        for value in group:
            return dict(zip(colnames, value))
    
    def grp_user(self, Gid):
        """Adds a user to a group"""
        query = ('''INSERT INTO groupmembers (group_id) VALUES('{}') RETURNING *'''.format(Gid))
        try:
            self.cur.execute(query)
            colnames = [column[0] for column in self.cur.description]
            group = self.cur.fetchall()
            for value in group:
                return dict(zip(colnames, value))
        except psycopg2.IntegrityError:
            return False

    def get_all_from_table(self, table, uid):
        """retreive all records of a given table of a given user"""
        query = ('''SELECT * FROM {} where user_id = '{}' '''.format(table, uid))
        self.cur.execute(query)
        records = self.cur.fetchall()
        return records

    def get_from_table(self, table, user_id, record_Id):
        """fetch one record from a table using a records id, a table name and users id"""
        query = ('''SELECT * FROM {} where user_id = '{}' AND message_id = '{}' '''.format(table, user_id, record_Id))
        self.cur.execute(query)
        colnames = [column[0] for column in self.cur.description]
        parcel = self.cur.fetchall()
        for this_parcel in parcel:
            return dict(zip(colnames, this_parcel))

    def contact_exist(self, email, userid):
        """fetch one contact from a table using a users id and an email"""
        query = ('''SELECT * FROM contacts WHERE email = '{}' AND user_id = '{}' '''.format(email, userid))
        self.cur.execute(query)
        exists = self.cur.fetchone()
        if exists:
            return True

    def delete_from_table(self, table, column, Id, user_id):
        """removes a record from a table using it's id, a table name and users id"""
        query = ('''DELETE FROM {} where {}_id = '{}' AND USER_ID = '{}' '''.format(table, column, Id, user_id))
        self.cur.execute(query)
        return True

    def login_user(self, email):
        """Return the password hash of a give email"""
        query = "SELECT PASSWORD FROM users WHERE email='{}'".format(email)
        self.cur.execute(query)
        user = self.cur.fetchone()
        if user is None :
            return 'False'
        return user[0]

    def check_email(self, email):
        """Return the password hash of a give email"""
        query = "SELECT * FROM users WHERE email='{}'".format(email)
        self.cur.execute(query)
        user = self.cur.fetchone()
        return user

    def get_by_status(self, status, user_id):
        """retreive all records of a given table"""
        query = ('''SELECT * FROM messages WHERE status = '{}' AND user_id='{}' '''.format(status, user_id))
        self.cur.execute(query)
        records = self.cur.fetchall()
        return records
    
    def userid(self, email):
        """Return the userid of a given email"""
        query = "SELECT user_id FROM users WHERE email='{}'".format(email)
        self.cur.execute(query)
        user = self.cur.fetchone()
        if user is None:
            return 'user[0]'
        return user[0]
    
    def delete_user(self, Gid, uid):
        """removes group meber from a table using the group id and memeber id"""
        query = ('''DELETE FROM groupmembers where group_id = '{}' AND member_id = '{}' '''.format(Gid, uid))
        self.cur.execute(query)
        return True
