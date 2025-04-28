from enum import Enum

from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget

from core.widget.bank_viewer_screen.bank_viewer_screen import BankViewerScreen


class MainWindowUI(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setGeometry(0, 0, 1280, 720)
        self.setMinimumSize(400, 300)

        self.bank_viewer_screen: BankViewerScreen = BankViewerScreen(self)

        self.setCentralWidget(self.bank_viewer_screen.ui)
