from flask import Blueprint

from App.models import Home

blue = Blueprint("first_blue",__name__)

def init_first_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def hello():
    return "Welcom to use Flask!"

