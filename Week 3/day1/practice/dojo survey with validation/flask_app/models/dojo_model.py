from flask_app.config.connectomysql import connectToMySQL
from flask_app import DB
from flask import flash # type: ignore

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """insert into dojos (name , location , language , comment )
        values (%(name)s , %(location)s , %(language)s , %(comment)s);"""
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if not results:  # Check if results are empty
            return None
        return cls(results[0])

    @staticmethod
    def validate_dojo(data):
        is_valid = True
        if len(data['name']) < 3:
            flash('Name must be at least 3 characters.')
            is_valid = False
        if len(data['location']) < 3:
            flash('Location must be at least 3 characters.')
            is_valid = False
        if len(data['language']) < 3:
            flash('Language must be at least 3 characters.')
            is_valid = False
        return is_valid
