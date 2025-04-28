from flask import Flask

from core.net import routes


def create_app() -> Flask:
    app = Flask(__name__)

    routes.init_app(app)

    return app
