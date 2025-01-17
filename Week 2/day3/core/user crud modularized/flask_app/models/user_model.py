from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        result = connectToMySQL(DB).query_db(query)
        users = []
        for user in result:
            users.append(cls(user))
        return users
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def delete(cls,id):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL(DB).query_db(query,{'id': id})
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        user = User(result[0])
        return user
    

    


    