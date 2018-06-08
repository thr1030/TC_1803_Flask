from flask import Flask
from App.ext import init_ext
from App.settings import TEMPLATE_FOLDER, envs
from App.views import init_first_blue


def create_app():
    app = Flask(__name__,template_folder=TEMPLATE_FOLDER)

    init_first_blue(app)

    init_ext(app)

    app.config.from_object(envs.get("develop"))

    return app