from flask import Flask, send_from_directory
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__, static_url_path="/static")

environment = Environment(loader=FileSystemLoader("templates/"))


@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('static/css', path)


@app.route("/figs/<path:path>")
def send_figs(path):
    return send_from_directory('static/figs', path)


@app.route("/")
def index():
    template = environment.get_template("index.html")
    return template.render()


@app.route("/contact")
def contact_info():
    template = environment.get_template("contact.html")
    return template.render()


@app.route("/about")
def about():
    template = environment.get_template("about.html")
    return template.render()


@app.route("/research")
def research():
    template = environment.get_template("research.html")
    return template.render()


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
