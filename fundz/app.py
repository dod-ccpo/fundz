import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile(
    os.path.join(os.path.dirname(__file__), 'config.py'))
db = SQLAlchemy(app)

# Import our models so Alembic can autogenerate migrations.
from fundz.models import *
