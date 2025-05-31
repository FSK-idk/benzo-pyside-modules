from PySide6.QtCore import QObject, Slot

from core.window.main_window_ui import MainWindowUI, ViewName

from core.model.camera_load import CameraLoad
from core.model.car_number import CarNumber

from core.net.net import Net

from core.data_base.data_base import data_base


class MainWindow(QObject):
    def __init__(self) -> None:
        super().__init__()

        data_base.init()

        self.ui: MainWindowUI = MainWindowUI()

        self.ui.station_server_reconnection_screen.reconnectClicked.connect(self.onReconnectClicked)

        self.ui.start_screen.startClicked.connect(self.onStartClicked)
        self.ui.selection_screen.imageSelected.connect(self.onImageSelected)
        self.ui.selection_screen.cancelRefuelingClicked.connect(self.onCancelRefuelingClicked)
        self.ui.recognition_screen.changeClicked.connect(self.onChangeClicked)
        self.ui.recognition_screen.confirmClicked.connect(self.onConfirmClicked)
        self.ui.recognition_screen.cancelRefuelingClicked.connect(self.onCancelRefuelingClicked)
        self.ui.non_recognition_screen.confirmClicked.connect(self.onConfirmClicked)
        self.ui.non_recognition_screen.cancelRefuelingClicked.connect(self.onCancelRefuelingClicked)

        self._net: Net = Net(self)

        self._net.stationServerDisconnected.connect(self.onStationServerDisconnected)
        self._net.reset.connect(self.onReset)
        self._net.serviceStarted.connect(self.onServiceStarted)
        self._net.componentConnection.connect(self.onComponentConnection)
        self._net.stationUsed.connect(self.onStationUsed)
        self._net.gasNozzleUsed.connect(self.onGasNozzleUsed)
        self._net.mobileAppUsed.connect(self.onMobileAppUsed)

        self.ui.setCurrentView(ViewName.STATION_SERVER_RECONNECTION)
        self._net.connectStationServer()

        self.ui.show()

    @Slot()
    def clearInput(self) -> None:
        self.ui.selection_screen.resetImages()
        self.ui.recognition_screen.clearInput()
        self.ui.non_recognition_screen.clearInput()

    @Slot()
    def onReconnectClicked(self) -> None:
        self._net.connectStationServer()

    @Slot()
    def onStationServerDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_SERVER_RECONNECTION)

    @Slot()
    def onReset(self) -> None:
        self.clearInput()
        self.ui.setCurrentView(ViewName.START)

    @Slot()
    def onStartClicked(self) -> None:
        self._net.startService()

    @Slot()
    def onServiceStarted(self) -> None:
        self.ui.setCurrentView(ViewName.SELECTION)

    @Slot()
    def onCancelRefuelingClicked(self) -> None:
        self._net.cancelRefueling()

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
        self._net.useStation(car_number)

    @Slot()
    def onComponentConnection(self) -> None:
        self.ui.setCurrentView(ViewName.COMPONENT_CONNECTION)

    @Slot()
    def onStationUsed(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)

    @Slot()
    def onGasNozzleUsed(self) -> None:
        self.ui.setCurrentView(ViewName.GAS_NOZZLE_USE)

    @Slot()
    def onMobileAppUsed(self) -> None:
        self.ui.setCurrentView(ViewName.MOBILE_APP_USE)
