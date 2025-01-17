from flask import render_template, redirect, request # type: ignore
from flask_app import app
from flask_app.models.dojo_model import Dojo

@app.route('/dojos')
def all_dojos():
    return render_template("all_dojos.html", dojos=Dojo.get_all())

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {"name": request.form['name']}
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {"id": dojo_id}
    return render_template("dojo_show.html", dojo=Dojo.get_dojo_with_ninjas(data))
