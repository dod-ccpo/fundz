import pytest
import tornado.web
from fundz.app import make_app

@pytest.fixture
def app():
    return make_app()

@pytest.mark.gen_test
def test_routes(http_client, base_url):
    for path in (
            '/',
            ):
        response = yield http_client.fetch(base_url + path)
    assert response.code == 200
