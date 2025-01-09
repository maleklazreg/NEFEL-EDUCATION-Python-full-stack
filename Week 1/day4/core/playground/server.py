from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def grounds():
    return render_template('ground.html', length=3, color="blue")

@app.route('/play')
def play():
    return render_template('ground.html', length=3, color="blue")

@app.route('/play/<int:o>')
def play_length(o):
    return render_template('ground.html', length=o, color="blue")

@app.route('/play/<int:o>/<color>')
def play_color(o, color):
    return render_template('ground.html', length=o, color=color)

if __name__ == '__main__':
    app.run(debug=True)
