import os
from flask import Flask
from configparser import ConfigParser

from fundz.config import map_config
from fundz.database import db
from fundz.serializers import marshmallow

def make_app(config):
    app = Flask(__name__)
    app.config.update(config)

    db.init_app(app)
    marshmallow.init_app(app)

    # Imported at the end to avoid circular imports.
    from fundz.api import api
    app.register_blueprint(api)

    return app


def make_config():
    BASE_CONFIG_FILENAME = os.path.join(
        os.path.dirname(__file__),
        '../config/base.ini',
    )
    ENV_CONFIG_FILENAME = os.path.join(
        os.path.dirname(__file__),
        '../config/',
        '{}.ini'.format(os.getenv('FLASK_ENV', 'dev').lower())
    )
    config = ConfigParser()

    # ENV_CONFIG will override values in BASE_CONFIG.
    config.read([BASE_CONFIG_FILENAME, ENV_CONFIG_FILENAME])
    return map_config(config)
