from flask_app import app
from flask_app.controllers import dojo_controllers, ninja_controllers

if __name__ == "__main__":
    app.run(debug=True)