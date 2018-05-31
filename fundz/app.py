import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from fundz.api import api

app = Flask(__name__)
app.config.from_object('fundz.config')
app.register_blueprint(api)

db = SQLAlchemy(app)

# Import our models so Alembic can autogenerate migrations.
from fundz.models import *
