from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject

from core.widget.mobile_app_use_screen.mobile_app_use_screen_ui import MobileAppUseScreenUI


class MobileAppUseScreen(QObject):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: MobileAppUseScreenUI = MobileAppUseScreenUI(parent)

        self.ui.show()
