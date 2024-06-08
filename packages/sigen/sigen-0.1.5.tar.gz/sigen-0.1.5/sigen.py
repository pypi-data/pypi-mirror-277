import requests
import logging
import coloredlogs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import time

class Sigen:
    BASE_URL = "https://api-eu.sigencloud.com/"

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = encrypt_password(password)
        self.token_info = self.get_access_token()
        self.access_token = self.token_info['access_token']
        self.refresh_token = self.token_info['refresh_token']
        self.token_expiry = time.time() + self.token_info['expires_in']
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        self.station_id = None
        self.operational_modes = None
        self.fetch_station_info()
        create_dynamic_methods(self)
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
            if response_data is None or 'access_token' not in response_data or 'refresh_token' not in response_data or 'expires_in' not in response_data:
                raise Exception(
                    f"\n\nPOST {url}\n\nFailed to get access token for user '{self.username}'\nResponse text: '{response.text}'")
            return response_data
        else:
            raise Exception(
                f"\n\nPOST {url}\n\nFailed to get access token for user '{self.username}'\nResponse code: {response.status_code} \nResponse text: '{response.text}'")

    def refresh_access_token(self):
        url = f"{self.BASE_URL}auth/oauth/token"
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token
        }
        response = requests.post(url, data=data, auth=('sigen', 'sigen'))

        if response.status_code == 200:
            response_json = response.json()
            response_data = response_json['data']
            if response_data and 'access_token' in response_data and 'refresh_token' in response_data and 'expires_in' in response_data:
                self.access_token = response_data['access_token']
                self.refresh_token = response_data['refresh_token']
                self.token_expiry = time.time() + response_data['expires_in']
                self.headers['Authorization'] = f'Bearer {self.access_token}'
            else:
                raise Exception(
                    f"\n\nPOST {url}\n\nFailed to refresh access token\nResponse text: '{response.text}'")
        else:
            raise Exception(
                f"\n\nPOST {url}\n\nFailed to refresh access token\nResponse code: {response.status_code} \nResponse text: '{response.text}'")

    def ensure_valid_token(self):
        if time.time() >= self.token_expiry:
            self.refresh_access_token()

    def fetch_station_info(self):
        self.ensure_valid_token()
        url = f"{self.BASE_URL}device/owner/station/home"
        response = requests.get(url, headers=self.headers)
        data = response.json()['data']
        self.station_id = data['stationId']

        logging.debug(f"Station ID: {self.station_id}")
        logging.debug(f"Has PV: {data['hasPv']}")
        logging.debug(f"Has EV: {data['hasEv']}")
        logging.debug(f"On Grid: {data['onGrid']}")
        logging.debug(f"PV Capacity: {data['pvCapacity']} kW")
        logging.debug(f"Battery Capacity: {data['batteryCapacity']} kWh")

        return data

    def get_energy_flow(self):
        self.ensure_valid_token()
        url = f"{self.BASE_URL}device/sigen/station/energyflow?id={self.station_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()['data']

    def get_operational_mode(self):
        self.ensure_valid_token()
        url = f"{self.BASE_URL}device/setting/operational/mode/{self.station_id}"
        response = requests.get(url, headers=self.headers)
        current_mode = response.json()['data']

        if self.operational_modes is None:
            self.fetch_operational_modes()

        for mode in self.operational_modes:
            if mode['value'] == str(current_mode):
                return mode['label']

        return "Unknown mode"

    def fetch_operational_modes(self):
        self.ensure_valid_token()
        url = f"{self.BASE_URL}device/sigen/station/operational/mode/v/{self.station_id}"
        response = requests.get(url, headers=self.headers)
        self.operational_modes = response.json()['data']

    def set_operational_mode(self, mode: int):
        self.ensure_valid_token()
        url = f"{self.BASE_URL}device/setting/operational/mode/"
        payload = {
            'stationId': self.station_id,
            'operationMode': mode
        }
        response = requests.put(url, headers=self.headers, json=payload)
        return response.json()

    def get_operational_modes(self):
        if not self.operational_modes:
            self.get_operational_mode()
        return self.operational_modes


def create_dynamic_methods(sigen: Sigen):
    operational_modes = sigen.get_operational_modes()

    for mode in operational_modes:
        method_name = f"set_operational_mode_{mode['label'].lower().replace(' ', '_').replace('-', '_')}"
        mode_value = int(mode['value'])

        def method(self, value=mode_value):
            return self.set_operational_mode(value)

        method.__name__ = method_name
        setattr(Sigen, method_name, method)


def encrypt_password(password):
    key = "sigensigensigenp"
    iv = "sigensigensigenp"

    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('latin1'))
    encrypted = cipher.encrypt(pad(password.encode('utf-8'), AES.block_size))
    return base64.b64encode(encrypted).decode('utf-8')

# Example usage:
# sigen = Sigen(username="your_username", password="your_password")
# print(sigen.fetch_station_info())
# print(sigen.get_energy_flow())
# print(sigen.get_operational_mode())
# print(sigen.set_operational_mode_sigen_ai_mode())
# print(sigen.set_operational_mode_maximum_self_powered())
# print(sigen.set_operational_mode_tou())
# print(sigen.set_operational_fully_fed_to_grid())