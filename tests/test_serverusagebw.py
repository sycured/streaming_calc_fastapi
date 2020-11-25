"""Test /serverusagebw endpoint."""
from fastapi.testclient import TestClient

from main import app

bitrate = 64
bitrate_float = 64.8
nbdays = 1
nbhours = 24
nblisteners = 250

client = TestClient(app)
svusbw = '/serverusagebw'


def test_post_int():
    """With int."""
    response = client.post(url=svusbw,
                           json={'bitrate': bitrate,
                                 'nbdays': nbdays,
                                 'nbhours': nbhours,
                                 'nblisteners': nblisteners
                                 }
                           )
    assert response.status_code == 200
    assert response.json() == {'result': 164794.921875}


def test_post_float():
    """With float."""
    response = client.post(url=svusbw,
                           json={'bitrate': bitrate_float,
                                 'nbdays': nbdays,
                                 'nbhours': nbhours,
                                 'nblisteners': nblisteners
                                 }
                           )
    assert response.status_code == 200
    assert response.json() == {'result': 166854.8583984375}


def test_get():
    """Test GET request."""
    response = client.get(url=svusbw)
    assert response.status_code == 405


def test_options():
    """Test OPTIONS request."""
    response = client.options(url=svusbw)
    assert response.status_code == 405


def test_delete():
    """Test DELETE request."""
    response = client.delete(url=svusbw)
    assert response.status_code == 405


def test_head():
    """Test HEAD request."""
    response = client.head(url=svusbw)
    assert response.status_code == 405


def test_put():
    """Test PUT request."""
    response = client.put(url=svusbw)
    assert response.status_code == 405


def test_patch():
    """Test PATCH request."""
    response = client.patch(url=svusbw)
    assert response.status_code == 405
