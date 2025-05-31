from PySide6.QtCore import QObject, Signal

from core.model.car_number import CarNumber

from core.net.station_server_client import StationServerClient


class Net(QObject):
    componentConnection: Signal = Signal()
    stationServerDisconnected: Signal = Signal()
    serviceStarted: Signal = Signal()
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

        self._station_server_client.serviceStarted.connect(self.serviceStarted.emit)

        self._station_server_client.refuelingCanceled.connect(self.stationUsed.emit)
        self._station_server_client.stationUsedT1.connect(self.stationUsed.emit)
        self._station_server_client.stationUsedT2.connect(self.stationUsed.emit)

        self._station_server_client.gasNozzleUsedT1.connect(self.gasNozzleUsed.emit)
        self._station_server_client.gasNozzleUsedT2.connect(self.gasNozzleUsed.emit)

        self._station_server_client.mobileAppUsedT1.connect(self.mobileAppUsed.emit)
        self._station_server_client.mobileAppUsedT2.connect(self.mobileAppUsed.emit)

    def connectStationServer(self) -> None:
        self._station_server_client.start()

    def startService(self) -> None:
        self._station_server_client.sendStartService()

    def cancelRefueling(self) -> None:
        self._station_server_client.sendCancelRefueling()

    def useStation(self, car_number: CarNumber) -> None:
        self._station_server_client.sendUseStationT1(car_number)
