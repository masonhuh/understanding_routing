from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    print(name)
    return render_template("say.html",say=say,name=name)

@app.route('/repeat/<int:num>/<string:phrase>')
def repeat(num, phrase):
    return render_template("repeat.html",num=num,phrase=phrase)

if __name__=="__main__":
    app.run(debug=True)

