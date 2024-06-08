## Sigen
_A package to reading and writing data to and from Sigenergy inverters._

### Installation
```bash
pip install sigen
```

### Usage

```python
from sigen import Sigen

# username and password you use in the mySigen app.
sigen = Sigen(username="your_username", password="your_password")

# Read data
print(sigen.fetch_station_info())
print(sigen.get_energy_flow())
print(sigen.get_operational_mode())

# Set modes
print(sigen.set_operational_mode_sigen_ai_mode())
print(sigen.set_operational_mode_maximum_self_powered())
print(sigen.set_operational_mode_tou())
print(sigen.set_operational_fully_fed_to_grid())

```

Full example:
```python
import logging
import coloredlogs
import os
from sigen import Sigen


def main():
    # Read username and password from environment variables
    username = os.getenv('SIGEN_USERNAME')
    password = os.getenv('SIGEN_PASSWORD')

    if not username or not password:
        logging.error("Environment variables SIGEN_USERNAME and SIGEN_PASSWORD must be set")
        return

    # Initialize logging
    coloredlogs.install(level='INFO')
    sigen = Sigen(username=username, password=password)

    # Fetch and log station info
    logging.info("Fetching station info...")
    station_info = sigen.fetch_station_info()
    logging.info("Station Info:")
    logging.info(f"Station ID: {station_info['stationId']}")
    logging.info(f"Has PV: {station_info['hasPv']}")
    logging.info(f"Has EV: {station_info['hasEv']}")
    logging.info(f"On Grid: {station_info['onGrid']}")
    logging.info(f"PV Capacity: {station_info['pvCapacity']} kW")
    logging.info(f"Battery Capacity: {station_info['batteryCapacity']} kWh")

    # Fetch and log energy flow info
    logging.info("\nFetching energy flow info...")
    energy_flow = sigen.get_energy_flow()
    logging.info("Energy Flow Info:")
    logging.info(f"PV Day Energy: {energy_flow['pvDayNrg']} kWh")
    logging.info(f"PV Power: {energy_flow['pvPower']} kW")
    logging.info(f"Buy/Sell Power: {energy_flow['buySellPower']} kW")
    logging.info(f"EV Power: {energy_flow['evPower']} kW")
    logging.info(f"AC Power: {energy_flow['acPower']} kW")
    logging.info(f"Load Power: {energy_flow['loadPower']} kW")
    logging.info(f"Battery Power: {energy_flow['batteryPower']} kW")
    logging.info(f"Battery SOC: {energy_flow['batterySoc']}%")

    # Fetch and log current operational mode
    logging.info("\nFetching current operational mode...")
    current_mode = sigen.get_operational_mode()
    logging.info(f"Current Operational Mode: {current_mode}")

    # Change operational mode (example: setting mode to 'Fully Fed to Grid')
    logging.info("\nSetting operational mode to 'Fully Fed to Grid'...")
    response = sigen.set_operational_mode(5)
    logging.info(f"Response: {response}")

    logging.info("\nFetching current operational mode...")
    current_mode = sigen.get_operational_mode()
    logging.info(f"Current Operational Mode: {current_mode}")


if __name__ == "__main__":
    main()
```

Example output of the above code:
```bash

2024-06-07 06:09:29 INFO Fetching station info...
2024-06-07 06:09:29 INFO Station ID: 20241231231231
2024-06-07 06:09:29 INFO Has PV: True
2024-06-07 06:09:29 INFO Has EV: False
2024-06-07 06:09:29 INFO On Grid: True
2024-06-07 06:09:29 INFO PV Capacity: 10.3 kW
2024-06-07 06:09:29 INFO Battery Capacity: 8.06 kWh

Fetching energy flow info...
2024-06-07 06:09:29 INFO PV Day Energy: 35.25 kWh
2024-06-07 06:09:29 INFO PV Power: 5.232 kW
2024-06-07 06:09:29 INFO Buy/Sell Power: 3.8 kW
2024-06-07 06:09:29 INFO EV Power: 0.0 kW
2024-06-07 06:09:29 INFO AC Power: 0.0 kW
2024-06-07 06:09:29 INFO Load Power: 0.5 kW
2024-06-07 06:09:29 INFO Battery Power: 0.932 kW
2024-06-07 06:09:29 INFO Battery SOC: 48.4%

Fetching current operational mode...
2024-06-07 06:09:29 INFO Current Operational Mode: TOU
```