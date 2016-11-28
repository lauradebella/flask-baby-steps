from flask import jsonify, Blueprint
from app import flask
from app.models.post import Post

blueprint = Blueprint('post_controller', __name__, url_prefix='/posts')

@blueprint.route("/")
def list():
    posts = [dict(d) for d in Post.query.all()]
    return jsonify(posts=posts), 200