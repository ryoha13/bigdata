import os
from flask import Flask
from configs import configs


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    from .main import main
    app.register_blueprint(main)
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    from .api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
