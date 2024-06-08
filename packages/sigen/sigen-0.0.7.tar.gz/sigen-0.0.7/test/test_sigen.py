import pytest
import requests_mock
from sigen import Sigen


@pytest.fixture
def sigen_instance():
    with requests_mock.Mocker() as m:
        url = "https://api-eu.sigencloud.com/auth/oauth/token"
        response_data = {
            "data": {
                "access_token": "mock_access_token"
            }
        }
        m.post(url, json=response_data)
        sigen = Sigen(username="mock_user", password="mock_password")
        return sigen


def test_get_access_token(sigen_instance):
    assert sigen_instance.token == "mock_access_token"


def test_get_station_info(requests_mock, sigen_instance):
    url = "https://api-eu.sigencloud.com/device/owner/station/home"
    response_data = {
        "data": {
            "stationId": 2024052311111,
            "hasPv": True,
            "hasEv": False,
            "onGrid": True,
            "pvCapacity": 10.3,
            "batteryCapacity": 8.06
        }
    }
    requests_mock.get(url, json=response_data)

    data = sigen_instance.get_station_info()
    assert data['stationId'] == 2024052311111
    assert data['hasPv'] is True
    assert data['hasEv'] is False
    assert data['onGrid'] is True
    assert data['pvCapacity'] == 10.3
    assert data['batteryCapacity'] == 8.06


def test_get_energy_flow(requests_mock, sigen_instance):
    sigen_instance.station_id = 2024052311111
    url = f"https://api-eu.sigencloud.com/device/sigen/station/energyflow?id={sigen_instance.station_id}"
    response_data = {
        "data": {
            "pvDayNrg": 30.43,
            "pvPower": 5.7,
            "buySellPower": 5.0,
            "evPower": 0.0,
            "acPower": 0.0,
            "loadPower": 0.5,
            "batteryPower": 0.2,
            "batterySoc": 93.8
        }
    }
    requests_mock.get(url, json=response_data)

    data = sigen_instance.get_energy_flow()
    assert data['pvDayNrg'] == 30.43
    assert data['pvPower'] == 5.7
    assert data['buySellPower'] == 5.0
    assert data['evPower'] == 0.0
    assert data['acPower'] == 0.0
    assert data['loadPower'] == 0.5
    assert data['batteryPower'] == 0.2
    assert data['batterySoc'] == 93.8


def test_get_operational_mode(requests_mock, sigen_instance):
    sigen_instance.station_id = 2024052311111

    url_mode = f"https://api-eu.sigencloud.com/device/setting/operational/mode/{sigen_instance.station_id}"
    response_current_mode = {
        "data": 2
    }
    requests_mock.get(url_mode, json=response_current_mode)

    url_modes = f"https://api-eu.sigencloud.com/device/sigen/station/operational/mode/v/{sigen_instance.station_id}"
    response_modes = {
        "data": [
            {"label": "Sigen AI Mode", "value": "1"},
            {"label": "Maximum Self-Powered", "value": "0"},
            {"label": "TOU", "value": "2"},
            {"label": "Fully Fed to Grid", "value": "5"}
        ]
    }
    requests_mock.get(url_modes, json=response_modes)

    mode = sigen_instance.get_operational_mode()
    assert mode == "TOU"


def test_set_operational_mode(requests_mock, sigen_instance):
    sigen_instance.station_id = 2024052311111
    url = "https://api-eu.sigencloud.com/device/setting/operational/mode/"
    response_data = {
        "code": 0,
        "msg": "success"
    }
    requests_mock.put(url, json=response_data)

    response = sigen_instance.set_operational_mode(5)
    assert response['code'] == 0
    assert response['msg'] == "success"
