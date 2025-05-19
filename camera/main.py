import os
import sys

from dotenv import load_dotenv

from PySide6.QtWidgets import QApplication

from core.window.main_window import MainWindow


def main() -> None:
    os.chdir(os.path.dirname(sys.argv[0]))
    load_dotenv('.env')

    app = QApplication()
    app.setApplicationDisplayName('floating')

    app.setStyleSheet("""
        QWidget {
            background: #ffffff;
        }
    """)

    window = MainWindow()

    app.exec()


if __name__ == '__main__':
    main()
