from flask import render_template, request, redirect, flash # type: ignore
from flask_app import app
from flask_app.models.email_model import Email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/email', methods=['POST'])
def submit_email():
    if Email.validate_email(request.form):
        data = {
            "email": request.form['email']
        }
        Email.create(data)
        flash("Email address added successfully!", "success")
        return redirect('/submit')
    return redirect('/')

@app.route('/submit')
def submit():
    emails = Email.get_all()
    return render_template("submit.html", emails=emails)