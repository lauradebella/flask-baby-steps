from os import getenv, getcwd, path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask.ext.runner import Manager

flask = Flask(__name__, template_folder=path.join(getcwd(), __name__, 'views'))
flask.config.from_object('config.'+ getenv('ENV', 'Development'))

db = SQLAlchemy(flask)
migrate = Migrate(flask, db)
manager = Manager(flask)