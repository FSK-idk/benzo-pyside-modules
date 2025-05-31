from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject

from core.widget.component_connection_screen.component_connection_screen_ui import ComponentConnectionScreenUI


class ComponentConnectionScreen(QObject):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: ComponentConnectionScreenUI = ComponentConnectionScreenUI(parent)

        self.ui.show()
