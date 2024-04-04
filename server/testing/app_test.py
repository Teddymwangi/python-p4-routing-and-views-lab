import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert b'<h1>Python Operations with Flask Routing and Views</h1>' in response.data

def test_print_string(client):
    response = client.get('/print/test_string')
    assert response.data == b'test_string'

def test_count(client):
    response = client.get('/count/5')
    assert b'0\n1\n2\n3\n4' in response.data

def test_math_addition(client):
    response = client.get('/math/3/+/2')
    assert b'5' in response.data

def test_math_subtraction(client):
    response = client.get('/math/5/-/3')
    assert b'2' in response.data

def test_math_multiplication(client):
    response = client.get('/math/4/*/3')
    assert b'12' in response.data

def test_math_division(client):
    response = client.get('/math/10/div/2')
    assert b'5.0' in response.data

def test_math_modulus(client):
    response = client.get('/math/10/%/3')
    assert b'1' in response.data

def test_math_invalid_operation(client):
    response = client.get('/math/10/invalid/3')
    assert b'Invalid operation' in response.data
