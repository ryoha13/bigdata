import os
from flask import Flask
from configs import configs
from .extensions import db, bootstrap


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    register_plugins(app)
    register_app_blueprint(app)

    return app


def register_plugins(app):
    db.init_app(app)
    bootstrap.init_app(app)


def register_app_blueprint(app):
    from .main import main
    app.register_blueprint(main)
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    from .api import api
    app.register_blueprint(api, url_prefix='/api')
