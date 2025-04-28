from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject

from core.widget.gas_nozzle_use_screen.gas_nozzle_use_screen_ui import GasNozzleUseScreenUI


class GasNozzleUseScreen(QObject):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: GasNozzleUseScreenUI = GasNozzleUseScreenUI(parent)

        self.ui.show()
