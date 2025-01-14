from flask import Flask, session, render_template, redirect, request # type: ignore

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/increment_by_2')
def increment_by_2():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return redirect('/')
    
@app.route('/increment', methods=['POST'])
def increment():
    increment_value = int(request.form.get('increment', 1))
    session['counter'] = session.get('counter', 0) + increment_value
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
