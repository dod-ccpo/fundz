import pytest


@pytest.fixture
def app():
    from fundz.app import app
    return app
