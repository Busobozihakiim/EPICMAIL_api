import os
from urllib import parse
import psycopg2


class Database:
    """Contains methods to create a db connection and create some tables"""

    def __init__(self):
        """Creates a connection to the database"""
        try:
            url = parse.urlparse(os.environ['DATABASE_URL'])
            db_url = "dbname={} user={} password={} host={} \
            ".format(url.path[1:], url.username, url.password, url.hostname)
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
            sender_id INT REFERENCES Users(user_id) NOT NULL,
            receiver_id INT NOT NULL,
            status VARCHAR(10) DEFAULT 'sent',
            receiver_status VARCHAR(10) DEFAULT 'unread'
            )''',
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
        drop_groups_table = "DROP TABLE groups cascade"
        drop_mesages_table = "DROP TABLE messages cascade"
        drop_users_table = "DROP TABLE users cascade"
        self.cur.execute(drop_groups_table)
        self.cur.execute(drop_messages_table)
        self.cur.execute(drop_users_table)

    def save_user(self, firstname, lastname, email, password):
        """Adds a user to a database"""
        query = (''' INSERT INTO users (email, firstName, lastName, password)
                    VALUES ('{}','{}','{}','{}')
                '''.format(email, firstname, lastname, password))
        self.cur.execute(query)
        return True

    def save_message(self, subject, message, receiver, uid):
        """Adds a message to a database"""
        query = ('''INSERT INTO messages (subject, message, receiver_id, sender_id)
                    VALUES('{}','{}','{}','{}')
                 '''.format(subject, message, receiver, uid))
        self.cur.execute(query)
        return True

    def save_group(self, name, uid):
        """Adds a group to storage"""
        query = ('''INSERT INTO groups (group_name, user_id)
                    VALUES('{}','{}') RETURNING *'''.format(name, uid))
        group = self.cur.execute(query)
        colnames = [column[0] for column in self.cur.description]
        group = self.cur.fetchall()
        for value in group:
            return dict(zip(colnames, value))
        

    def grp_user(self, Gid):
        """Adds a user to a group"""
        query = ('''INSERT INTO groupmembers (group_id)
                    VALUES('{}') RETURNING *'''.format(Gid))
        try:
            group = self.cur.execute(query)
            colnames = [column[0] for column in self.cur.description]
            group = self.cur.fetchall()
            for value in group:
                return dict(zip(colnames, value))
        except psycopg2.IntegrityError:
            return False

    def get_all_from_table(self, table, uid):
        """retreive all records of a given table of a given user"""
        query = ('''SELECT * FROM {}
                    WHERE user_id = '{}' '''.format(table, uid))
        self.cur.execute(query)
        records = self.cur.fetchall()
        return records

    def get_from_table(self, record_Id):
        """fetch one message using the message and user id"""
        query = ('''SELECT * FROM messages
                    where message_id = '{}' '''.format(record_Id))
        self.cur.execute(query)
        message = self.cur.fetchall()
        return message

    def delete_group(self, Id, user_id):
        """
        removes a group using it's id, and admins id
        """
        query = ('''DELETE FROM groups where group_id = '{}' AND
                    USER_ID = '{}' '''.format(Id, user_id))
        self.cur.execute(query)
        return True

    def login_user(self, email):
        """Return the password hash of a give email"""
        query = "SELECT PASSWORD FROM users WHERE email='{}'".format(email)
        self.cur.execute(query)
        user = self.cur.fetchone()
        if user is None:
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
        if status == 'sent':
            query = ('''SELECT * FROM messages
                        WHERE status = '{}' AND
                        sender_id='{}' '''.format(status, user_id))
        elif status == 'unread':
            query = ('''SELECT * FROM messages
                        WHERE receiver_status = '{}' AND
                        receiver_id='{}' '''.format(status, user_id))

        self.cur.execute(query)
        records = self.cur.fetchall()
        return records

    def userid(self, email):
        """Return the userid of a given email"""
        query = "SELECT user_id FROM users WHERE email='{}'".format(email)
        self.cur.execute(query)
        user = self.cur.fetchone()
        if user is None:
            return False
        return user[0]

    def delete_user(self, Gid, uid):
        """
        removes group meber from a table using the group id and memeber id
        """
        exits = ('''SELECT exists (SELECT 1 FROM groupmembers
                    WHERE group_id = '{}' and
                    member_id = '{}' LIMIT 1)
                '''.format(Gid, uid))
        self.cur.execute(exits)
        group_member_exists = self.cur.fetchone()
        if True in group_member_exists:
            query = ('''DELETE FROM groupmembers
                        where group_id = '{}' AND
                        member_id = '{}'
                        '''.format(Gid, uid))
            self.cur.execute(query)
            return True
        return False

    def update(self, name, Gid, uid):
        """Change the name of a group"""
        exits = ('''SELECT exists (SELECT 1 FROM groups
                    WHERE group_id = '{}' and
                    user_id = '{}' LIMIT 1)
                '''.format(Gid, uid))
        self.cur.execute(exits)
        does_it = self.cur.fetchone()
        if True in does_it:
            query = ('''UPDATE groups  SET group_name = '{}'
                        WHERE group_id = '{}' and user_id = '{}'
                        RETURNING group_name, group_id, role
                    '''.format(name, Gid, uid))
            self.cur.execute(query)
            return self.cur.fetchall()
        return False

    def fetch_inbox(self, uid):
        """Returns all messages in users inbox"""
        query = ('''SELECT * FROM messages
                    where receiver_id = '{}' OR sender_id = '{}'
                '''.format(uid, uid))
        self.cur.execute(query)
        inbox = self.cur.fetchall()
        return inbox
    
    def group_exists(self, Gid, uid):
        """Returns all messages in users inbox"""
        query = ('''SELECT * FROM groups
                    where group_id = '{}' AND user_id='{}'
                '''.format(Gid, uid))
        self.cur.execute(query)
        grps_available = self.cur.fetchall()
        if grps_available:
            return True
        return False
    
    def delete_message(self, Id):
        """
        removes a message using it's id
        """
        query = ('''DELETE FROM messages where message_id = '{}' '''.format(Id))
        self.cur.execute(query)
        return True
