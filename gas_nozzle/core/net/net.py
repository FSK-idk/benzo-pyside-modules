from PySide6.QtCore import QObject, Signal

from core.net.station_server_client import StationServerClient


class Net(QObject):
    componentConnection: Signal = Signal()
    stationServerDisconnected: Signal = Signal()
    reset: Signal = Signal()
    stationUsed: Signal = Signal()
    gasNozzleUsed: Signal = Signal()
    mobileAppUsed: Signal = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        self._station_server_client: StationServerClient = StationServerClient(self)

        self._station_server_client.connected.connect(self.componentConnection.emit)
        self._station_server_client.serviceNotReady.connect(self.componentConnection.emit)

        self._station_server_client.disconnected.connect(self.stationServerDisconnected.emit)

        self._station_server_client.serviceReady.connect(self.reset.emit)
        self._station_server_client.serviceEnded.connect(self.reset.emit)

        self._state = 't1'
        self._station_server_client.gasNozzleUsedT1.connect(self.onGasNozzleUsedT1)
        self._station_server_client.gasNozzleUsedT2.connect(self.onGasNozzleUsedT2)

        self._station_server_client.refuelingCanceled.connect(self.stationUsed.emit)
        self._station_server_client.stationUsedT1.connect(self.stationUsed.emit)
        self._station_server_client.stationUsedT2.connect(self.stationUsed.emit)

        self._station_server_client.mobileAppUsedT1.connect(self.mobileAppUsed.emit)
        self._station_server_client.mobileAppUsedT2.connect(self.mobileAppUsed.emit)

    def connectStationServer(self) -> None:
        self._station_server_client.start()

    def onGasNozzleUsedT1(self) -> None:
        self._state = 't1'
        self.gasNozzleUsed.emit()

    def onGasNozzleUsedT2(self) -> None:
        self._state = 't2'
        self.gasNozzleUsed.emit()

    def finish(self) -> None:
        if (self._state == 't1'):
            self._station_server_client.sendUseStationT2()
        elif (self._state == 't2'):
            self._station_server_client.sendUseMobileAppT2()
