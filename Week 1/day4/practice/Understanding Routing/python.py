from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld(): 
    return 'Hello!'

@app.route('/Dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    return f"hi {name}!!!"

@app.rout('/repeat/<int:number>/<string:word>')
def repeat_word(number, word):
    return ' '.join([word] * number)

@app.routerrorhandler(404)
def not_found(xXx):
    return "sorry bro the pagelooking for not be found", 404

if __name__ == '__main__':
    app.run(debug=True , port=8080)
