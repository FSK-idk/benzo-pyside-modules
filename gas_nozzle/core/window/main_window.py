from PySide6.QtCore import QObject, Slot

from core.window.main_window_ui import MainWindowUI, ViewName

from core.net.station_ws_client import StationWsClient


class MainWindow(QObject):
    def __init__(self) -> None:
        super().__init__()

        self.ui: MainWindowUI = MainWindowUI()

        self.ui.start_screen.startClicked.connect(self.onStartClicked)
        self.ui.refueling_screen.refuelingFinished.connect(self.onRefuelingFinished)
        self.ui.finish_screen.confirmClicked.connect(self.onConfirmClicked)
        self.ui.reconnection_screen.reconnectClicked.connect(self.onReconnectClicked)

        self.station_ws_client: StationWsClient = StationWsClient(self)

        self.station_ws_client.connected.connect(self.onStationConnected)
        self.station_ws_client.disconnected.connect(self.onStationDisconnected)
        self.station_ws_client.cameraDisconnected.connect(self.onCameraDisconnected)
        self.station_ws_client.resetService.connect(self.onResetService)
        self.station_ws_client.startStation.connect(self.onStartStation)
        self.station_ws_client.cancelRefueling.connect(self.onCancelRefueling)
        self.station_ws_client.startGasNozzle.connect(self.onStartGasNozzle)
        self.station_ws_client.finishGasNozzle.connect(self.onFinishGasNozzle)

        self.ui.setCurrentView(ViewName.WAITING)
        self.station_ws_client.start()

        self.ui.show()

    @Slot()
    def clearInput(self) -> None:
        self.ui.refueling_screen.clearInput()

    # ui

    @Slot()
    def onReconnectClicked(self) -> None:
        self.station_ws_client.start()

    @Slot()
    def onStartClicked(self) -> None:
        self.ui.setCurrentView(ViewName.REFUELING)
        self.ui.refueling_screen.start()

    @Slot()
    def onRefuelingFinished(self) -> None:
        self.ui.setCurrentView(ViewName.FINISH)

    @Slot()
    def onConfirmClicked(self) -> None:
        self.clearInput()
        self.station_ws_client.sendFinishGasNozzleRequest()

    # station ws client

    @Slot()
    def onStationConnected(self) -> None:
        self.ui.setCurrentView(ViewName.WAITING)

    @Slot()
    def onStationDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.RECONNECTION)

    @Slot()
    def onCameraDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.WAITING)

    @Slot()
    def onResetService(self) -> None:
        self.clearInput()
        self.ui.setCurrentView(ViewName.CAMERA_USE)

    @Slot()
    def onCancelRefueling(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)

    @Slot()
    def onStartStation(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)

    @Slot()
    def onStartGasNozzle(self) -> None:
        self.ui.setCurrentView(ViewName.START)

    @Slot()
    def onFinishGasNozzle(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)
