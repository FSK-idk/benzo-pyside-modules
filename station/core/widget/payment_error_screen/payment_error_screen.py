from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

from core.widget.payment_error_screen.payment_error_screen_ui import PaymentErrorScreenUI


class PaymentErrorScreen(QObject):
    retryPaymentClicked: Signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: PaymentErrorScreenUI = PaymentErrorScreenUI(parent)

        self.ui.retry_payment_button.clicked.connect(self.retryPaymentClicked.emit)

        self.ui.show()
