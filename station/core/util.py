import os


def get_port() -> int:
    port: str | None = os.getenv('PORT')
    if (port is None):
        port = '5000'
        print('WARNING: PORT not found. Will be 5000')

    return int(port)
