from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://sa:131313@localhost:1433/Flask?driver=SQL+Server+Native+Client+11.0"

db = SQLAlchemy(app)
#models
class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    def __iter__(self):
        yield 'id', self.id
        yield 'title', self.title
        yield 'content', self.content



@app.route("/")
def hello():
    return "Hello World!"


@app.route("/posts")
def Posts():
    posts = [dict(d) for d in Post.query.all()]
    return jsonify(posts=posts), 200

app.run()

