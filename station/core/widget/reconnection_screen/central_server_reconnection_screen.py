from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

from core.widget.reconnection_screen.central_server_reconnection_screen_ui import CentralServerReconnectionScreenUI


class CentralServerReconnectionScreen(QObject):
    reconnectClicked: Signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: CentralServerReconnectionScreenUI = CentralServerReconnectionScreenUI(parent)

        self.ui.retry_button.clicked.connect(self.reconnectClicked)

        self.ui.show()
