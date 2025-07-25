import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_create_user(client):
    response = client.post('/users', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'test123'
    })
    assert response.status_code == 201

def test_login(client):
    client.post('/users', json={
        'name': 'Login User',
        'email': 'login@example.com',
        'password': 'secret123'
    })
    response = client.post('/login', json={
        'email': 'login@example.com',
        'password': 'secret123'
    })
    assert response.json['status'] == 'success'
