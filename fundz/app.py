import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('fundz.config')
db = SQLAlchemy(app)

# Import our models so Alembic can autogenerate migrations.
from fundz.models import *
