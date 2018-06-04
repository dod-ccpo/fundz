import pytest

from fundz.make_app import make_app


@pytest.fixture
def app():
    return make_app({
        'SQLALCHEMY_DATABASE_URI': 'postgres://postgres:postgres@localhost/fundz',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'ENVIRONMENT': 'test',
        'DEBUG': False
    })
