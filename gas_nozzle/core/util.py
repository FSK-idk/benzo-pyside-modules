import os
import sys

from PySide6.QtCore import QUrl


def get_url() -> QUrl:
    host: str | None = os.getenv('HOST')
    if (host is None):
        host = '127.0.0.1'
        print('WARNING: HOST not found. Will be 127.0.0.1')

    port: str | None = os.getenv('PORT')
    if (port is None):
        port = '5000'
        print('WARNING: PORT not found. Will be 5000')

    url: QUrl = QUrl()
    url.setScheme('ws')
    url.setHost(host)
    url.setPort(int(port))

    return url


def resource_path(relative_path):
    try:
        return sys._MEIPASS + relative_path[1::]
    except Exception:
        return relative_path
