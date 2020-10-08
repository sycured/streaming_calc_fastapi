from fastapi.testclient import TestClient
from main import app

bitrate = 64
bitrate_float = 64.8
nbdays = 1
nbhours = 24
nblisteners = 250

client = TestClient(app)


def test_1():
    response = client.post(url='/serverusagebw',
                           json={'bitrate': bitrate,
                                 'nbdays': nbdays,
                                 'nbhours': nbhours,
                                 'nblisteners': nblisteners
                                 }
                           )
    assert response.status_code == 200
    assert response.json() == {"result": 164794.921875}


def test_2():
    response = client.post(url='/serverusagebw',
                           json={'bitrate': bitrate_float,
                                 'nbdays': nbdays,
                                 'nbhours': nbhours,
                                 'nblisteners': nblisteners
                                 }
                           )
    assert response.status_code == 200
    assert response.json() == {'result': 166854.8583984375}
