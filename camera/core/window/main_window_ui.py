from enum import Enum

from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget

from core.widget.station_server_reconnection_screen.station_server_reconnection_screen import StationServerReconnectionScreen
from core.widget.component_connection_screen.component_connection_screen import ComponentConnectionScreen
from core.widget.start_screen.start_screen import StartScreen
from core.widget.selection_screen.selection_screen import SelectionScreen
from core.widget.recognition_screen.recognition_screen import RecognitionScreen
from core.widget.non_recognition_screen.non_recognition_screen import NonRecognitionScreen
from core.widget.station_use_screen.station_use_screen import StationUseScreen
from core.widget.gas_nozzle_use_screen.gas_nozzle_use_screen import GasNozzleUseScreen
from core.widget.mobile_app_use_screen.mobile_app_use_screen import MobileAppUseScreen


class ViewName(Enum):
    STATION_SERVER_RECONNECTION = 'station_server_reconnection_screen'
    COMPONENT_CONNECTION = 'component_connection_screen'
    START = 'start_screen'
    SELECTION = 'selection_screen'
    RECOGNITION = 'recognition_screen'
    NON_RECOGNITION = 'non_recognition_screen'
    STATION_USE = 'station_use_screen'
    GAS_NOZZLE_USE = 'gas_nozzle_use_screen'
    MOBILE_APP_USE = 'mobile_app_use_screen'


class MainWindowUI(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setGeometry(0, 0, 1280, 720)
        self.setMinimumSize(400, 300)

        self.station_server_reconnection_screen: StationServerReconnectionScreen = StationServerReconnectionScreen(self)
        self.component_connection_screen: ComponentConnectionScreen = ComponentConnectionScreen(self)
        self.start_screen: StartScreen = StartScreen(self)
        self.selection_screen: SelectionScreen = SelectionScreen(self)
        self.recognition_screen: RecognitionScreen = RecognitionScreen(self)
        self.non_recognition_screen: NonRecognitionScreen = NonRecognitionScreen(self)
        self.station_use_screen: StationUseScreen = StationUseScreen(self)
        self.gas_nozzle_use_screen: GasNozzleUseScreen = GasNozzleUseScreen(self)
        self.mobile_app_use_screen: MobileAppUseScreen = MobileAppUseScreen(self)

        self.stack: QStackedWidget = QStackedWidget(self)

        self.stack_indices: dict = {
            ViewName.STATION_SERVER_RECONNECTION: self.stack.addWidget(self.station_server_reconnection_screen.ui),
            ViewName.COMPONENT_CONNECTION: self.stack.addWidget(self.component_connection_screen.ui),
            ViewName.START: self.stack.addWidget(self.start_screen.ui),
            ViewName.SELECTION: self.stack.addWidget(self.selection_screen.ui),
            ViewName.RECOGNITION: self.stack.addWidget(self.recognition_screen.ui),
            ViewName.NON_RECOGNITION: self.stack.addWidget(self.non_recognition_screen.ui),
            ViewName.STATION_USE: self.stack.addWidget(self.station_use_screen.ui),
            ViewName.GAS_NOZZLE_USE: self.stack.addWidget(self.gas_nozzle_use_screen.ui),
            ViewName.MOBILE_APP_USE: self.stack.addWidget(self.mobile_app_use_screen.ui),
        }

        self.setCentralWidget(self.stack)

    def setCurrentView(self, view_name: ViewName) -> None:
        self.stack.setCurrentIndex(self.stack_indices[view_name])
