import json

from PySide6.QtCore import QObject, QUrl, Slot, Signal
from PySide6.QtWebSockets import QWebSocket

from core.model.station_ws_api import *

from core.util import get_station_host, get_station_port


class StationWsClient(QObject):
    connected: Signal = Signal()
    disconnected: Signal = Signal()
    gasNozzleDisconnected: Signal = Signal()

    startService: Signal = Signal()
    resetService: Signal = Signal()
    cancelRefueling: Signal = Signal()
    startStation: Signal = Signal()
    startGasNozzle: Signal = Signal()
    finishGasNozzle: Signal = Signal()

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

    def _sendConnectRequest(self) -> None:
        message = ConnectRequestMessage(sender_type=SenderType.CAMERA)
        self._client.sendTextMessage(message.to_json())

    def sendStartServiceRequest(self) -> None:
        message = StartServiceRequestMessage()
        self._client.sendTextMessage(message.to_json())

    def sendCancelRefuelingRequest(self) -> None:
        message = CancelRefuelingRequestMessage()
        self._client.sendTextMessage(message.to_json())

    def sendCarNumberSent(self, message: CarNumberSentMessage) -> None:
        self._client.sendTextMessage(message.to_json())

    @Slot()
    def onTextMessageReceived(self, json_str: str) -> None:
        print(f'STATION CLIENT | message received: {json_str}')

        message_type = MessageType(json.loads(json_str)['message_type'])

        match (message_type):
            case MessageType.CAMERA_CONNECTED:
                self.connected.emit()
            case MessageType.GAS_NOZZLE_DISCONNECTED:
                self.gasNozzleDisconnected.emit()
            case MessageType.START_SERVICE:
                self.startService.emit()
            case MessageType.RESET_SERVICE:
                self.resetService.emit()
            case MessageType.CANCEL_REFUELING:
                self.cancelRefueling.emit()
            case MessageType.START_STATION:
                self.startStation.emit()
            case MessageType.START_GAS_NOZZLE:
                self.startGasNozzle.emit()
            case MessageType.FINISH_GAS_NOZZLE:
                self.finishGasNozzle.emit()

    @Slot()
    def onConnected(self) -> None:
        print(f'STATION CLIENT | connected on {self._client.localAddress().toString()}:{self._client.localPort()}')
        self._sendConnectRequest()

    @Slot()
    def onDisconnected(self) -> None:
        print(f'STATION CLIENT | disconnected')
        self.disconnected.emit()
