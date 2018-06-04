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
    CONFIG_FILENAME = os.path.join(
        os.path.dirname(__file__),
        '..',
        os.getenv('CONFIG_FILENAME', 'config.ini')
    )
    config = ConfigParser()
    config.read(CONFIG_FILENAME)
    return map_config(config)
