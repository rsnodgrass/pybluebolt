#!/usr/local/bin/python3

import os
import sys
import pprint
import logging
import json

from pybluebolt import PyBlueBOLT

def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def main():
    host = os.getenv('BLUEBOLT_HOST', None)
    port = os.getenv('BLUEBOLT_PORT', None)

    if (host == None) or (port == None):
        print("ERROR! Must define env variables BLUEBOLT_HOST and BLUEBOLT_PORT")
        raise SystemExit

    pp = pprint.PrettyPrinter(indent = 2)
 
    bluebolt = PyBlueBOLT(host, port)
    print(f"Connected? {bluebolt.is_connected}")

    print(f"\n--Status--\n")
    print(f"Voltage: {bluebolt.voltage}\n")
    print(f"Current: {bluebolt.current}\n")

    print(f"\n--Outlet Status--\n")
    for outlet in bluebolt.outlets:
        pp.pprint(outlet)

    if false:
        bluebolt.power_off()
        bluebolt.power_on()
        bluebolt.toggle_reboot1()
        bluebolt.toggle_reboot2()
        bluebolt.toggle_green()
        bluebolt.outlets[1].turn_off()
        bluebolt.outlets[2].turn_on()
    
if __name__ == "__main__":
    main()
