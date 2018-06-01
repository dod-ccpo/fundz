from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object('fundz.config')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Imported at the end to avoid circular imports.
from fundz.api import api
app.register_blueprint(api)
