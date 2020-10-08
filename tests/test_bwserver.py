"""Test /bwserver endpoint."""
from fastapi.testclient import TestClient

from main import app

bitrate = 64
bitrate_float = 64.8
nblisteners = 250

client = TestClient(app)


def test_1():
    """With int."""
    response = client.post(url='/bwserver',
                           json={'nblisteners': nblisteners,
                                 'bitrate': bitrate}
                           )
    assert response.status_code == 200
    assert response.json() == {'result': 15625}


def test_2():
    """With float."""
    response = client.post(url='/bwserver',
                           json={'nblisteners': nblisteners,
                                 'bitrate': bitrate_float}
                           )
    assert response.status_code == 200
    assert response.json() == {'result': 15820.3125}
