from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

from core.widget.reconnection_screen.reconnection_screen_ui import ReconnectionScreenUI


class ReconnectionScreen(QObject):
    reconnectClicked: Signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: ReconnectionScreenUI = ReconnectionScreenUI(parent)

        self.ui.retry_button.clicked.connect(self.reconnectClicked)

        self.ui.show()
