from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject

from core.widget.waiting_screen.waiting_screen_ui import WaitingScreenUI


class WaitingScreen(QObject):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: WaitingScreenUI = WaitingScreenUI(parent)

        self.ui.show()
