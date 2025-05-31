from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

from core.widget.station_server_reconnection_screen.station_server_reconnection_screen_ui import StationServerReconnectionScreenUI


class StationServerReconnectionScreen(QObject):
    reconnectClicked: Signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: StationServerReconnectionScreenUI = StationServerReconnectionScreenUI(parent)

        self.ui.retry_button.clicked.connect(self.reconnectClicked)

        self.ui.show()
