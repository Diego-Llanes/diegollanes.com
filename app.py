from flask import Flask
from jinja2 import Environment, FileSystemLoader
import jinja2

app = Flask(__name__)

environment = Environment(loader=FileSystemLoader("templates/"))


@app.route("/")
def index():
    environment = jinja2.Environment()
    template = environment.from_string("Hello, {{ name }}!")
    return template.render(name="World")


@app.route("/fart/<string:name>/<int:loud>")
@app.route("/fart/<string:name>/<float:loud>")
@app.route("/fart/<int:loud>")
@app.route("/fart/<float:loud>")
@app.route("/fart")
def fart(name=None, loud=None):
    if name is None:
        name = "Anon"
    if loud is None:
        loud = -1
    template = environment.get_template("fart.html")
    return template.render(name=name, decibels=loud)
