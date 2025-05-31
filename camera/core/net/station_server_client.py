import json

from PySide6.QtCore import QObject, QUrl, Slot, Signal
from PySide6.QtWebSockets import QWebSocket

from core.model.station_api import *

from core.util import get_station_host, get_station_port


class StationServerClient(QObject):
    connected: Signal = Signal()
    disconnected: Signal = Signal()
    serviceReady: Signal = Signal()
    serviceNotReady: Signal = Signal()
    serviceStarted: Signal = Signal()
    serviceEnded: Signal = Signal()
    refuelingCanceled: Signal = Signal()
    stationUsedT1: Signal = Signal()
    stationUsedT2: Signal = Signal()
    gasNozzleUsedT1: Signal = Signal()
    gasNozzleUsedT2: Signal = Signal()
    mobileAppUsedT1: Signal = Signal()
    mobileAppUsedT2: Signal = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        self._client: QWebSocket = QWebSocket('', parent=self)

        self._url: QUrl = QUrl()
        self._url.setScheme('ws')
        self._url.setHost(get_station_host())
        self._url.setPort(get_station_port())

        self._client.textMessageReceived.connect(self.onTextMessageReceived)

        self._client.connected.connect(self.onConnected)
        self._client.disconnected.connect(self.onDisconnected)

    def __del__(self) -> None:
        self.stop()

    def start(self) -> None:
        self._client.open(self._url)

    def stop(self) -> None:
        self._client.close()

    def _sendConnect(self) -> None:
        message = ConnectMessage(sender_type=SenderType.CAMERA)
        self._client.sendTextMessage(message.to_json())

    def sendStartService(self) -> None:
        message = StartServiceMessage()
        self._client.sendTextMessage(message.to_json())

    def sendCancelRefueling(self) -> None:
        message = CancelRefuelingMessage()
        self._client.sendTextMessage(message.to_json())

    def sendUseStationT1(self, car_number: CarNumber) -> None:
        message = UseStationT1Message(car_number=car_number)
        self._client.sendTextMessage(message.to_json())

#

    @Slot()
    def onTextMessageReceived(self, json_str: str) -> None:
        print(f'STATION CLIENT | message received: {json_str}')

        message_type = MessageType(json.loads(json_str)['message_type'])

        match (message_type):
            case MessageType.CONNECTED:
                self.connected.emit()
            case MessageType.SERVICE_READY:
                self.serviceReady.emit()
            case MessageType.SERVICE_NOT_READY:
                self.serviceNotReady.emit()
            case MessageType.SERVICE_STARTED:
                self.serviceStarted.emit()
            case MessageType.SERVICE_ENDED:
                self.serviceEnded.emit()
            case MessageType.REFUELING_CANCELED:
                self.refuelingCanceled.emit()
            case MessageType.STATION_USED_T1:
                self.stationUsedT1.emit()
            case MessageType.STATION_USED_T2:
                self.stationUsedT2.emit()
            case MessageType.GAS_NOZZLE_USED_T1:
                self.gasNozzleUsedT1.emit()
            case MessageType.GAS_NOZZLE_USED_T2:
                self.gasNozzleUsedT2.emit()
            case MessageType.MOBILE_APP_USED_T1:
                self.mobileAppUsedT1.emit()
            case MessageType.MOBILE_APP_USED_T2:
                self.mobileAppUsedT2.emit()

    @Slot()
    def onConnected(self) -> None:
        print(f'STATION CLIENT | connected on {self._client.localAddress().toString()}:{self._client.localPort()}')
        self._sendConnect()

    @Slot()
    def onDisconnected(self) -> None:
        print(f'STATION CLIENT | disconnected')
        self.disconnected.emit()
