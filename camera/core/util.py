import os
import sys
import glob
import random

from PySide6.QtCore import QUrl


DEFAULT_IMAGE_PATH: str = 'data/images/'
SUPPORTED_IMAGE_FORMATS: list[str] = ['*.jpg', '*.png']


def get_random_image_filenames() -> list[str]:
    files = list()
    for format in SUPPORTED_IMAGE_FORMATS:
        files += glob.glob(DEFAULT_IMAGE_PATH + format)
    return random.sample(files, 3)


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
