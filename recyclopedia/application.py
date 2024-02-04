from flask import Flask

from .containers import Container
from . import views


def create_app() -> Flask:
    container = Container()

    app = Flask(__name__)
    app.container = container
    app.add_url_rule("/", "index", views.index)
    app.add_url_rule("/get-data-from-gpt", "getDataFromGPT", views.getDataFromGPT,  methods=['GET'])

    return app