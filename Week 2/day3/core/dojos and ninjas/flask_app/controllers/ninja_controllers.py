from flask import render_template, redirect, request # type: ignore
from flask_app import app
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/ninjas')
def add_ninja():
    return render_template("add_ninja.html", dojos=Dojo.get_all())

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/dojos')
