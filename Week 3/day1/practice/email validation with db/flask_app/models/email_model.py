from flask_app.config.connecttomysql import connectToMySQL
from flask import flash
import re #importing the email function
from flask_app import DB
from datetime import datetime

Email_REGEX = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'

class Email:
    def __init__(self,data):
        self.id=data['id']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "select * from emails order by created_at desc;"
        results = connectToMySQL("email_schema").query_db(query)
        return [cls(row) for row in results]
    
    @classmethod
    def create(cls,data):
        query = "insert into emails (email) values (%(email)s);"
        return connectToMySQL("email_schema").query_db(query,data)
    
    @classmethod
    def get_email(cls,data):
        query = "select * from emails where email = %(email)s;"
        result = connectToMySQL(DB).query_db(query,data)
    
    @staticmethod
    def validate_email(email):
        is_valid = True
        email = email.get("email")
        
        if not re.match(Email_REGEX, email):
            flash("Invalid email address!", "error")
            is_valid = False
            
        elif Email.get_email({"email": email}):
            flash("Email already exists!", "error")
            is_valid = False
            
        if is_valid:
            flash("Email successfully","success")
            
        return is_valid
            
        