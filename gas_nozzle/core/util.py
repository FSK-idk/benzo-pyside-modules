import os
import sys

from PySide6.QtCore import QUrl


def get_station_host() -> str:
    host = os.getenv('STATION_HOST')
    if (host is None):
        host = '127.0.0.1'
        print('WARNING: STATION_HOST not found. Will be 127.0.0.1')
    return host


def get_station_port() -> int:
    port = os.getenv('STATION_PORT')
    if (port is None):
        port = '5000'
        print('WARNING: STATION_PORT not found. Will be 5000')
    return int(port)
