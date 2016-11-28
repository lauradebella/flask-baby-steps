from app import flask
from flask import Blueprint

blueprint = Blueprint('home_controller', __name__, url_prefix='/')

@flask.route("/")
def hello():
    return "Hello World!"
