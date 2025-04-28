from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

from core.widget.start_screen.start_screen_ui import StartScreenUI


class StartScreen(QObject):
    startClicked = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: StartScreenUI = StartScreenUI(parent)

        self.ui.start_button.clicked.connect(self.startClicked.emit)

        self.ui.show()
