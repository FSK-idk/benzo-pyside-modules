from enum import Enum

from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget

from core.widget.fuel_selection_screen.fuel_selection_screen import FuelSelectionScreen
from core.widget.payment_selection_screen.payment_selection_screen import PaymentSelectionScreen
from core.widget.payment_processing_screen.payment_processing_screen import PaymentProcessingScreen
from core.widget.payment_error_screen.payment_error_screen import PaymentErrorScreen
from core.widget.finish_screen.finish_screen import FinishScreen
from core.widget.camera_use_screen.camera_use_screen import CameraUseScreen
from core.widget.gas_nozzle_use_screen.gas_nozzle_use_screen import GasNozzleUseScreen
from core.widget.waiting_screen.waiting_screen import WaitingScreen


class ViewName(Enum):
    FUEL_SELECTION = 'fuel_selection_screen'
    PAYMENT_SELECTION = 'payment_selection_screen'
    PAYMENT_PROCESSING = 'payment_processing_screen'
    PAYMENT_ERROR = 'payment_error_screen'
    FINISH = 'finish_screen'

    CAMERA_USE = 'camera_use_screen'
    GAS_NOZZLE_USE = 'gas_nozzle_use_screen'

    WAITING = 'waiting_screen'


class MainWindowUI(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setGeometry(0, 0, 1280, 720)
        self.setMinimumSize(400, 300)

        self.fuel_selection_screen: FuelSelectionScreen = FuelSelectionScreen(self)
        self.payment_selection_screen: PaymentSelectionScreen = PaymentSelectionScreen(self)
        self.payment_processing_screen: PaymentProcessingScreen = PaymentProcessingScreen(self)
        self.payment_error_screen: PaymentErrorScreen = PaymentErrorScreen(self)
        self.finish_screen: FinishScreen = FinishScreen(self)
        self.camera_use_screen: CameraUseScreen = CameraUseScreen(self)
        self.gas_nozzle_use_screen: GasNozzleUseScreen = GasNozzleUseScreen(self)
        self.waiting_screen: WaitingScreen = WaitingScreen(self)

        self.stack: QStackedWidget = QStackedWidget()

        self.stack_indices: dict = {
            ViewName.FUEL_SELECTION: self.stack.addWidget(self.fuel_selection_screen.ui),
            ViewName.PAYMENT_SELECTION: self.stack.addWidget(self.payment_selection_screen.ui),
            ViewName.PAYMENT_PROCESSING: self.stack.addWidget(self.payment_processing_screen.ui),
            ViewName.PAYMENT_ERROR: self.stack.addWidget(self.payment_error_screen.ui),
            ViewName.FINISH: self.stack.addWidget(self.finish_screen.ui),
            ViewName.CAMERA_USE: self.stack.addWidget(self.camera_use_screen.ui),
            ViewName.GAS_NOZZLE_USE: self.stack.addWidget(self.gas_nozzle_use_screen.ui),
            ViewName.WAITING: self.stack.addWidget(self.waiting_screen.ui),
        }

        self.setCentralWidget(self.stack)

    def setCurrentView(self, view_name: ViewName) -> None:
        self.stack.setCurrentIndex(self.stack_indices[view_name])
