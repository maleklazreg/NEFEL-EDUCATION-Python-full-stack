from flask import Flask, session, render_template, redirect, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Root route to display the counter
@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

# Route to destroy the session
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

# NINJA BONUS: Route to increment by 2
@app.route('/increment_by_2')
def increment_by_2():
    if 'counter' in session:
        session['counter'] += 2
    else:
        session['counter'] = 2
    return redirect('/')

# SENSEI BONUS: Route to increment by a user-defined value
@app.route('/increment', methods=['POST'])
def increment():
    increment_value = int(request.form.get('increment', 1))
    session['counter'] = session.get('counter', 0) + increment_value
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
