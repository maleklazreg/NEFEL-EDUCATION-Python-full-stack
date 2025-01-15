from flask_app import app
from flask import render_template,redirect,request,session # type: ignore
from flask_app.models.users_model import User 


@app.route("/")
def index():
    all_users = User.get_all()
    return render_template("allusers.html",all_users=all_users)


@app.route("/users/new")
def display_form():
    return render_template("addnewuser.html")


@app.route('/create_user', methods=['POST'])
def create():
    data = { 'id' : id ,
                'first_name' : request.form['first_name'],
                'last_name' : request.form['last_name'] ,
                'email' : request.form['email'] }
    User.save(data)
    return redirect('/')