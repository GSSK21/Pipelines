import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING']=True
    with app.test_client() as client:
        yield client
def test_app_is_working(client):
    responce=client.get('/')
    assert responce.status_code==200
    assert b"Hello world!" in responce.data