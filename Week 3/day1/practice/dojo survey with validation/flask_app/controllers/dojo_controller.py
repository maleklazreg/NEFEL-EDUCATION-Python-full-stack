from flask import render_template, request, redirect, session, flash  # type: ignore
from flask_app import app
from flask_app.models.dojo_model import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Validate form data
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    
    # Prepare data for insertion
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
    }
    
    dojo_id = Dojo.save(data)
    return redirect(f'/result?name={data["name"]}&location={data["location"]}&language={data["language"]}&comment={data["comment"]}')


@app.route("/result")
def result():
    # Retrieve dojo using the ID stored in session
    dojo_id = session.get('dojo_id')

    if dojo_id:
        # Get dojo details if dojo_id is present
        dojo = Dojo.get_one({'id': dojo_id})
        if not dojo:
            flash("Dojo not found in the database.")
            return redirect('/')
        return render_template("result.html", dojo=dojo)
    data = request.args.to_dict() 
    if data:
        return render_template("result.html", dojo=data)  
    return redirect('/')
