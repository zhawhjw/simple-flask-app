"""This is a test script to test flask application"""
import pytest
from app.app import app

@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client

def test_main_page_content(client):
    """flask unit testing for content in default page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello CPS3500" in response.data

def test_new_page_content(client):
    """flask unit testing for content in a route page"""
    response = client.get("/new_page")
    assert response.status_code == 200
    assert b"New Page" in response.data


def test_none_user_content(client):
    """flask unit testing for unreachable page if a parameter is missing"""
    response = client.get("/user/")
    assert response.status_code == 404

def test_valid_user_content(client):
    """flask unit testing for content in valid parameter page"""
    response = client.get("/user/jack")
    assert response.status_code == 200
    assert b"jack".upper() in response.data

def test_not_valid_user_content(client):
    """flask unit testing for a not valid parameter page"""
    response = client.get("/user/tom")
    assert response.status_code == 200
    assert b"Anonymous" in response.data
