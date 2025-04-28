import os
import sys

from dotenv import load_dotenv

from core.window.main_window import MainWindow
from PySide6.QtWidgets import QApplication


def main() -> None:
    os.chdir(os.path.dirname(sys.argv[0]))
    load_dotenv('.env')

    app = QApplication()
    app.setApplicationDisplayName('proj-camera')

    window: MainWindow = MainWindow()

    app.exec()


if __name__ == '__main__':
    main()
