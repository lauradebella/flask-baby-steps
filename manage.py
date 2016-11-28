from app import flask
from app.controllers.home_controller import blueprint as home
from app.controllers.post_controller import blueprint as post

flask.register_blueprint(home)
flask.register_blueprint(post)

flask.run()
