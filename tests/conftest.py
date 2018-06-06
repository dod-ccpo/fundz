import pytest

from fundz.make_app import make_app, make_config


@pytest.fixture
def app():
    return make_app(make_config())
