from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask_app import DB
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = ""

    @classmethod
    def save(cls,data):
        query = """insert into recipes (name, description, instruction, date_cooked,
        under_30, user_id) values (%(name)s,%(description)s,%(instruction)s,
        %(date_cooked)s,%(under_30)s,%(user_id)s)"""
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id;
                """
        results = connectToMySQL(DB).query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe.posted_by= f'{row["first_name"]}{row["last_name"]}'
            recipes.append(recipe)
        return recipes
    
    
    @classmethod
    def get_by_id(cls,data):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id
                WHERE recipes.id = %(id)s
                """
        result = connectToMySQL(DB).query_db(query,data)
        recipe = cls(result[0])
        recipe.posted_by = f'{result[0]["first_name"]}{result[0]["last_name"]}'
        return recipe
    
    @classmethod
    def update(cls, data):
        query = """
        UPDATE recipes 
        SET name=%(name)s, 
        description=%(description)s, 
        instruction=%(instruction)s, 
        date_cooked=%(date_cooked)s, 
        under_30=%(under_30)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DB).query_db(query, data)

    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Recipe name must be at least 3 characters.","recipe_name")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters.","description")
            is_valid = False
        if len(data['instruction']) < 3:
            flash("instruction must be at least 3 characters.","instruction")
            is_valid = False
        if not data['date_cooked']:
            flash("Please select a date.")
            is_valid = False
        if 'under_30' not in data:
            flash("Please specify if the recipe takes less than 30 minutes.","date")
            is_valid = False
        return is_valid
    



    
    

    
    
# save
# """
#         Saves a new recipe to the database.
#         - Accepts a dictionary `data` with the recipe details (name, description, instruction, date_cooked, under_30, user_id).
#         - Inserts a new record into the 'recipes' table using the provided data.
#         - Returns the ID of the newly created recipe.
#         """

#get_all
#  Retrieves all recipes from the database along with their associated user information.
#         - Joins the 'recipes' table with the 'users' table to include the recipe owner's details.
#         - Creates `Recipe` objects for each result and adds them to a list.
#         - Sets the `posted_by` attribute for each recipe to display the owner's full name.
#         - Returns a list of all `Recipe` objects.

#get_by_id
#  Retrieves a single recipe by its ID from the database.
#         - Accepts a dictionary `data` containing the recipe ID (`data['id']`).
#         - Joins the 'recipes' table with the 'users' table to include the recipe owner's details.
#         - Creates and returns a `Recipe` object for the retrieved record.
#         - Sets the `posted_by` attribute to display the owner's full name.