from tests.factories import PENumberFactory, TaskOrderFactory


def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {'hello': 'world'}


def test_get_task_order_not_found(client):
    response = client.get('/task-order/1')
    assert response.status_code == 404


def test_get_task_order_found(client):
    TaskOrderFactory.create(id=1, number=1)

    response = client.get('/task-order/1')
    json = response.get_json()

    assert response.status_code == 200
    assert json['id'] == 1
    assert json['number'] == '1'


def test_get_pe_number_not_found(client):
    response = client.get('/pe-number/1')
    assert response.status_code == 404


def test_get_pe_number_found(client):
    PENumberFactory.create(number='1', description='Example')

    response = client.get('/pe-number/1')
    json = response.get_json()

    assert response.status_code == 200
    assert json['number'] == '1'
    assert json['description'] == 'Example'
