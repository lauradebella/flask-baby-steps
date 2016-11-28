from flask import jsonify
from app import flask
from app.models.post import Post


@flask.route("/")
def hello():
    return "Hello World!"


@flask.route("/posts")
def Posts():
    posts = [dict(d) for d in Post.query.all()]
    return jsonify(posts=posts), 200


flask.run()
