from flask_app import app
from flask import render_template,redirect,request # type: ignore
from flask_app.models.user_model import User 


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
@app.route('/users/<int:id>')
def user_details(id):
    data = {
        'id': id,
    }
    user = User.get_by_id(data)
    return render_template('showuser.html', user=user)

@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        'id': id
    }
    user = User.get_by_id(data)
    return render_template('edituser.html', user=user)


@app.route('/update_user/<int:id>', methods=['POST'])
def update_user(id):
    new_data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update(new_data)
    return redirect('/')


@app.route('/users/<int:id>/delete',)
def delete_user(id):
    User.delete(id)
    return redirect('/')



