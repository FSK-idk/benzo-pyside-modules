from PySide6.QtCore import QObject, Slot

from core.window.main_window_ui import MainWindowUI, ViewName

from core.model.camera_load import CameraLoad
from core.model.car_number import CarNumber
from core.model.station_ws_api import CarNumberSentMessage

from core.net.station_ws_client import StationWsClient

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

        self.station_ws_client: StationWsClient = StationWsClient(self)

        self.station_ws_client.connected.connect(self.onStationConnected)
        self.station_ws_client.disconnected.connect(self.onStationDisconnected)
        self.station_ws_client.gasNozzleDisconnected.connect(self.onGasNozzleDisconnected)
        self.station_ws_client.startService.connect(self.onStartService)
        self.station_ws_client.resetService.connect(self.onResetService)
        self.station_ws_client.startStation.connect(self.onStartStation)
        self.station_ws_client.startGasNozzle.connect(self.onStartGasNozzle)
        self.station_ws_client.finishGasNozzle.connect(self.onFinishGasNozzle)

        self.station_ws_client.start()

        self.ui.show()

    @Slot()
    def clearInput(self) -> None:
        self.ui.selection_screen.resetImages()
        self.ui.recognition_screen.clearInput()
        self.ui.non_recognition_screen.clearInput()

    # ui

    @Slot()
    def onReconnectClicked(self) -> None:
        self.station_ws_client.start()

    @Slot()
    def onStartClicked(self) -> None:
        self.station_ws_client.sendStartServiceRequest()

    @Slot()
    def onCancelRefuelingClicked(self) -> None:
        self.station_ws_client.sendResetServiceRequest()

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
        message = CarNumberSentMessage(car_number=car_number)
        self.station_ws_client.sendCarNumberSent(message)

    # station ws client

    @Slot()
    def onStationConnected(self) -> None:
        self.ui.setCurrentView(ViewName.WAITING)

    @Slot()
    def onStationDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.RECONNECTION)

    @Slot()
    def onGasNozzleDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.WAITING)

    @Slot()
    def onStartService(self) -> None:
        self.ui.setCurrentView(ViewName.SELECTION)

    @Slot()
    def onResetService(self) -> None:
        self.clearInput()
        self.ui.setCurrentView(ViewName.START)

    @Slot()
    def onStartStation(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)

    @Slot()
    def onStartGasNozzle(self) -> None:
        self.ui.setCurrentView(ViewName.GAS_NOZZLE_USE)

    @Slot()
    def onFinishGasNozzle(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)
