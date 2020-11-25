"""Test /bwserver endpoint."""
from fastapi.testclient import TestClient

from main import app

bitrate = 64
bitrate_float = 64.8
nblisteners = 250

bws = '/bwserver'
client = TestClient(app)


def test_post_int():
    """With int."""
    response = client.post(url=bws,
                           json={'nblisteners': nblisteners,
                                 'bitrate': bitrate}
                           )
    assert response.status_code == 200
    assert response.json() == {'result': 15625}


def test_post_float():
    """With float."""
    response = client.post(url=bws,
                           json={'nblisteners': nblisteners,
                                 'bitrate': bitrate_float}
                           )
    assert response.status_code == 200
    assert response.json() == {'result': 15820.3125}


def test_get():
    """Test GET request."""
    response = client.get(url=bws)
    assert response.status_code == 405


def test_options():
    """Test OPTIONS request."""
    response = client.options(url=bws)
    assert response.status_code == 405


def test_delete():
    """Test DELETE request."""
    response = client.delete(url=bws)
    assert response.status_code == 405


def test_head():
    """Test HEAD request."""
    response = client.head(url=bws)
    assert response.status_code == 405


def test_put():
    """Test PUT request."""
    response = client.put(url=bws)
    assert response.status_code == 405


def test_patch():
    """Test PATCH request."""
    response = client.patch(url=bws)
    assert response.status_code == 405
