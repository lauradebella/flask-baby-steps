from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.runner import Manager

flask = Flask(__name__)
flask.config.from_object('config')

db = SQLAlchemy(flask)
manager = Manager(flask)

