from flask import Flask, session, render_template, request, redirect  # type: ignore

app = Flask(__name__)
app.secret_key = 'skey'

@app.route('/')
def index():
    return render_template('housess.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)  # Debugging to see form data
    name = request.form.get('user_name')
    location = request.form.get('location')
    language = request.form.get('language')
    comments = request.form.get('comments')

    # Store data in session
    session['user_name'] = name
    session['location'] = location
    session['language'] = language
    session['comments'] = comments
    return redirect('/result')

@app.route('/result')
def result():
    user_name = session.get('user_name')
    location = session.get('location')
    return render_template('results.html', user_name=user_name, location=location)


if __name__ == '__main__':
    app.run(debug=True)
