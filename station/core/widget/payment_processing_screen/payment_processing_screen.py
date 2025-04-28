from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject

from core.widget.payment_processing_screen.payment_processing_screen_ui import PaymentProcessingScreenUI


class PaymentProcessingScreen(QObject):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: PaymentProcessingScreenUI = PaymentProcessingScreenUI(parent)

        self.ui.show()
