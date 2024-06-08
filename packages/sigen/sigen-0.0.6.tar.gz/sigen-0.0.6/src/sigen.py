import requests
import logging
import coloredlogs
import auth_tools


class Sigen:
    BASE_URL = "https://api-eu.sigencloud.com/"

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = auth_tools.encrypt_password(password)
        self.token = self.get_access_token()
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        self.station_id = None
        coloredlogs.install(level='INFO')

    def get_access_token(self):
        url = f"{self.BASE_URL}auth/oauth/token"
        data = {
            'username': self.username,
            'password': self.password,
            'grant_type': 'password'
        }
        response = requests.post(url, data=data, auth=('sigen', 'sigen'))

        if response.status_code == 401:
            raise Exception(
                f"\n\nPOST {url}\n\nFailed to get access token for user '{self.username}'\nResponse code: {response.status_code} \nResponse text: '{response.text}'\nCheck basic auth is working.")

        if response.status_code == 200:

            response_json = response.json()
            if 'data' not in response_json:
                raise Exception(
                    f"\n\nPOST {url}\n\nFailed to get access token for user '{self.username}'\nResponse text: '{response.text}'")
            response_data = response_json['data']
            if response_data is None or 'access_token' not in response_data:
                raise Exception(
                    f"\n\nPOST {url}\n\nFailed to get access token for user '{self.username}'\nResponse text: '{response.text}'")
            return response_data['access_token']
        else:
            raise Exception(
                f"\n\nPOST {url}\n\nFailed to get access token for user '{self.username}'\nResponse code: {response.status_code} \nResponse text: '{response.text}'")

    def get_station_info(self):
        url = f"{self.BASE_URL}device/owner/station/home"
        response = requests.get(url, headers=self.headers)
        data = response.json()['data']
        self.station_id = data['stationId']

        logging.info(f"Station ID: {self.station_id}")
        logging.info(f"Has PV: {data['hasPv']}")
        logging.info(f"Has EV: {data['hasEv']}")
        logging.info(f"On Grid: {data['onGrid']}")
        logging.info(f"PV Capacity: {data['pvCapacity']} kW")
        logging.info(f"Battery Capacity: {data['batteryCapacity']} kWh")

        return data

    def get_energy_flow(self):
        if not self.station_id:
            self.get_station_info()

        url = f"{self.BASE_URL}device/sigen/station/energyflow?id={self.station_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()['data']

    def get_operational_mode(self):
        if not self.station_id:
            self.get_station_info()

        url = f"{self.BASE_URL}device/setting/operational/mode/{self.station_id}"
        response = requests.get(url, headers=self.headers)
        current_mode = response.json()['data']

        url = f"{self.BASE_URL}device/sigen/station/operational/mode/v/{self.station_id}"
        response = requests.get(url, headers=self.headers)
        modes = response.json()['data']

        for mode in modes:
            if mode['value'] == str(current_mode):
                return mode['label']

        return "Unknown mode"

    def set_operational_mode(self, mode: int):
        if not self.station_id:
            self.get_station_info()

        url = f"{self.BASE_URL}device/setting/operational/mode/"
        payload = {
            'stationId': self.station_id,
            'operationMode': mode
        }
        response = requests.put(url, headers=self.headers, json=payload)
        return response.json()

# Example usage:
# sigen = Sigen(username="your_username", password="your_password")
# print(sigen.get_station_info())
# print(sigen.get_energy_flow())
# print(sigen.get_operational_mode())
# print(sigen.set_operational_mode(5))
