from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject

from core.widget.camera_use_screen.camera_use_screen_ui import CameraUseScreenUI


class CameraUseScreen(QObject):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: CameraUseScreenUI = CameraUseScreenUI(parent)

        self.ui.show()
