from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

from core.widget.finish_screen.finish_screen_ui import FinishScreenUI


class FinishScreen(QObject):
    confirmClicked = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: FinishScreenUI = FinishScreenUI(parent)

        self.ui.confirm_button.clicked.connect(self.confirmClicked.emit)

        self.ui.show()
