import logging
import coloredlogs
import os
import asyncio
from sigen import Sigen


async def main():
    # Read username and password from environment variables
    username = os.getenv('SIGEN_USERNAME')
    password = os.getenv('SIGEN_PASSWORD')

    if not username or not password:
        logging.error("Environment variables SIGEN_USERNAME and SIGEN_PASSWORD must be set")
        return

    # Initialize logging
    coloredlogs.install(level='INFO')
    sigen = Sigen(username=username, password=password)

    # Initialize the Sigen instance
    await sigen.async_initialize()

    # Fetch and log station info
    logging.info("Fetching station info...")
    station_info = await sigen.fetch_station_info()
    logging.info("Station Info:")
    logging.info(f"Station ID: {station_info['stationId']}")
    logging.info(f"Has PV: {station_info['hasPv']}")
    logging.info(f"Has EV: {station_info['hasEv']}")
    logging.info(f"On Grid: {station_info['onGrid']}")
    logging.info(f"PV Capacity: {station_info['pvCapacity']} kW")
    logging.info(f"Battery Capacity: {station_info['batteryCapacity']} kWh")

    # Fetch and log energy flow info
    logging.info("\nFetching energy flow info...")
    energy_flow = await sigen.get_energy_flow()
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
    current_mode = await sigen.get_operational_mode()
    logging.info(f"Current Operational Mode: {current_mode}")

    # Change operational mode (example: setting mode to 'Fully Fed to Grid')
    # logging.info("\nSetting operational mode to 'Fully Fed to Grid'...")
    # response = await sigen.set_operational_mode(5)

    # Or set by label
    # response = await sigen.set_operational_mode_sigen_ai_mode()
    # response = await sigen.set_operational_mode_tou()
    # response = await sigen.set_operational_mode_fully_fed_to_grid()
    # response = await sigen.set_operational_mode_maximum_self_powered()
    # logging.info(f"Response: {response}")

    # logging.info("\nFetching current operational mode...")
    # current_mode = await sigen.get_operational_mode()
    # logging.info(f"Current Operational Mode: {current_mode}")


if __name__ == "__main__":
    asyncio.run(main())