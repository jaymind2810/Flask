from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
