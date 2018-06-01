import os

FLASK_ENV = os.getenv('ENVIRONMENT', 'development')
DEBUG = bool(os.getenv('DEBUG', True))

SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URI',
    'postgres://postgres:postgres@localhost/fundz'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
