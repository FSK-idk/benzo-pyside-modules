from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject

from core.widget.station_use_screen.station_use_screen_ui import StationUseScreenUI


class StationUseScreen(QObject):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: StationUseScreenUI = StationUseScreenUI(parent)

        self.ui.show()
