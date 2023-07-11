import pytest
from app import app


def test_read():
    client = app.test_client()
    response = client.get('/weather/New York')
    assert response.status_code == 200



def test_post():
    client = app.test_client()
    response = client.post("/weather",json = {"city":"Delhi","temperature":"13454646464645","weather":"dry"})
    assert response.status_code == 308


def test_put():
    client = app.test_client()
    response = client.put("/weather/New York",json = {"city":"Delhi","temperature":"13454646464645","weather":"dry"})
    assert response.status_code == 200


def test_delete():
    client = app.test_client()
    response = client.delete('/weather/New York')
    assert response.status_code == 200