# explore flask and create basic web server usaing flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h3>Hello, World!</h3>"

@app.route("/about")
def about():
    return "<h3>Hello, Harsh this side how do you do!</h3>"

@app.route("/contact")
def contact():
    return "<h3>Hello, This is a contact page!</h3>"

app.run()