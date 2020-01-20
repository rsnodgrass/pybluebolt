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

    #setup_logger()
    pp = pprint.PrettyPrinter(indent = 2)
 
    bluebolt = PyBlueBOLT(host, port)
    print(f"Connected? {bluebolt.is_connected}")
    
if __name__ == "__main__":
    main()
