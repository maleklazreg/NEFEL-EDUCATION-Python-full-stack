from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create(cls, data):
        query = """INSERT INTO users 
        (first_name, last_name,email, password) 
        VALUES 
        (%(first_name)s, %(last_name)s,%(email)s,%(password)s);"""
        return connectToMySQL(DB).query_db(query, data)
    

    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM users WHERE id=%(id)s;"""
        result = connectToMySQL(DB).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data):
        query = """SELECT * FROM users WHERE email=%(email)s;"""
        result = connectToMySQL(DB).query_db(query, data)
        if result :
            return cls(result[0])
        return False
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name'])<2:
            is_valid =False
            flash("First Name not valid", "first_name")
        if len(data['last_name'])<2:
            is_valid =False
            flash("Last Name not valid", "last_name")
        if not EMAIL_REGEX.match(data['email']): 
            is_valid = False
            flash("Email not valid", "email")
        # if data email exist in the the database 
        elif User.get_by_email({'email': data['email']}):
            is_valid = False
            flash("email already taken ", "email")
        if len(data["password"])<7:
            is_valid = False
            flash("Password too short", "password")
        elif data["password"]!= data["confirm_password"]:
            is_valid = False
            flash("Password and confirm password must match", "password")
        return is_valid