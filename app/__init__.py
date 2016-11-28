from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask = Flask(__name__)

flask.config['DEBUG'] = True
flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
flask.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://sa:131313@localhost:1433/Flask?driver=SQL+Server+Native+Client+11.0"

db = SQLAlchemy(flask)

