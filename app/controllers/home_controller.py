from flask import Blueprint, render_template

blueprint = Blueprint('home_controller', __name__, url_prefix='/')

@blueprint.route("/")
def hello():
    return render_template('home/index.html')
