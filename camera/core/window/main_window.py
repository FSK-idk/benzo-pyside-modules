from PySide6.QtCore import QObject, Slot

from core.window.main_window_ui import MainWindowUI, ViewName

from core.model.camera_load import CameraLoad
from core.model.car_number import CarNumber

from core.net.client import Client

from core.data_base.data_base import data_base


class MainWindow(QObject):
    def __init__(self) -> None:
        super().__init__()

        data_base.init()

        self.ui: MainWindowUI = MainWindowUI()

        self.ui.start_screen.startClicked.connect(self.onStartClicked)
        self.ui.selection_screen.imageSelected.connect(self.onImageSelected)
        self.ui.selection_screen.cancelRefuelingClicked.connect(self.onCancelRefuelingClicked)
        self.ui.recognition_screen.changeClicked.connect(self.onChangeClicked)
        self.ui.recognition_screen.confirmClicked.connect(self.onConfirmClicked)
        self.ui.recognition_screen.cancelRefuelingClicked.connect(self.onCancelRefuelingClicked)
        self.ui.non_recognition_screen.confirmClicked.connect(self.onConfirmClicked)
        self.ui.non_recognition_screen.cancelRefuelingClicked.connect(self.onCancelRefuelingClicked)
        self.ui.reconnection_screen.reconnectClicked.connect(self.onReconnectClicked)

        self.ui.setCurrentView(ViewName.WAITING)

        self.client: Client = Client(self)

        self.client.connected.connect(self.onConnected)
        self.client.disconnected.connect(self.onDisconnected)
        self.client.startService.connect(self.onStartService)
        self.client.resetService.connect(self.onResetService)
        self.client.carNumberReceived.connect(self.onCarNumberReceived)
        self.client.startGasNozzle.connect(self.onStartGasNozzle)
        self.client.gasNozzleFinished.connect(self.onGasNozzleFinished)
        self.client.cameraConnected.connect(self.onCameraConnected)
        self.client.gasNozzleDisconnected.connect(self.onGasNozzleDisconnected)

        self.client.startClient()

        self.ui.show()

    @Slot()
    def clearInput(self) -> None:
        self.ui.selection_screen.resetImages()
        self.ui.recognition_screen.clearInput()
        self.ui.non_recognition_screen.clearInput()

    @Slot()
    def onStartClicked(self):
        self.client.sendStartService()

    @Slot()
    def onCancelRefuelingClicked(self) -> None:
        self.client.sendResetService()

    @Slot()
    def onImageSelected(self, load: CameraLoad | None) -> None:
        if (load is None or load.is_recognized == 'false'):
            self.ui.setCurrentView(ViewName.NON_RECOGNITION)
        else:
            car_number: CarNumber = CarNumber(text=load.car_number)
            self.ui.recognition_screen.setCarNumber(car_number)
            self.ui.setCurrentView(ViewName.RECOGNITION)

    @Slot()
    def onChangeClicked(self, car_number: CarNumber) -> None:
        self.ui.non_recognition_screen.setCarNumber(car_number)
        self.ui.setCurrentView(ViewName.NON_RECOGNITION)

    @Slot()
    def onConfirmClicked(self, car_number: CarNumber) -> None:
        self.clearInput()
        self.client.sendCarNumberReceived(car_number)

    @Slot()
    def onReconnectClicked(self) -> None:
        self.client.startClient()

    @Slot()
    def onConnected(self) -> None:
        self.client.sendConnect()

    @Slot()
    def onDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.RECONNECTION)

    @Slot()
    def onStartService(self) -> None:
        self.ui.setCurrentView(ViewName.SELECTION)

    @Slot()
    def onResetService(self) -> None:
        self.clearInput()
        self.ui.setCurrentView(ViewName.START)

    @Slot()
    def onCarNumberReceived(self, car_number: CarNumber) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)

    @Slot()
    def onStartGasNozzle(self) -> None:
        self.ui.setCurrentView(ViewName.GAS_NOZZLE_USE)

    @Slot()
    def onGasNozzleFinished(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)

    @Slot()
    def onCameraConnected(self) -> None:
        self.ui.setCurrentView(ViewName.WAITING)

    @Slot()
    def onGasNozzleDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.WAITING)
