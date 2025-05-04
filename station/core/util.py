import os


def get_station_host() -> str:
    host = os.getenv('HOST')
    if (host is None):
        host = '127.0.0.1'
        print('WARNING: HOST not found. Will be 127.0.0.1')
    return host


def get_station_port() -> int:
    port = os.getenv('PORT')
    if (port is None):
        port = '5000'
        print('WARNING: PORT not found. Will be 5000')
    return int(port)


def get_bank_host() -> str:
    host = os.getenv('BANK_HOST')
    if (host is None):
        host = '127.0.0.1'
        print('WARNING: BANK_HOST not found. Will be 127.0.0.1')
    return host


def get_bank_port() -> int:
    port = os.getenv('BANK_PORT')
    if (port is None):
        port = '5000'
        print('WARNING: BANK_PORT not found. Will be 5000')
    return int(port)


def get_central_server_host() -> str:
    host = os.getenv('CENTRAL_SERVER_HOST')
    if (host is None):
        host = '127.0.0.1'
        print('WARNING: CENTRAL_SERVER_HOST not found. Will be 127.0.0.1')
    return host


def get_central_server_port() -> int:
    port = os.getenv('CENTRAL_SERVER_PORT')
    if (port is None):
        port = '5000'
        print('WARNING: CENTRAL_SERVER_PORT not found. Will be 5000')
    return int(port)


def get_station_id() -> str:
    station_id = os.getenv('STATION_ID')
    if (station_id is None):
        station_id = '00'
        print('WARNING: STATION_ID not found. Will be 00')
    return station_id
