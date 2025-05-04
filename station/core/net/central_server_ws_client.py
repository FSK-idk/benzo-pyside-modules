from email import message
import json

from PySide6.QtCore import QObject, QUrl, Slot, Signal
from PySide6.QtWebSockets import QWebSocket

from core.model.central_server_ws_api import *

from core.util import get_central_server_host, get_central_server_port, get_station_id


class CentralServerWsClient(QObject):
    connected: Signal = Signal()
    disconnected: Signal = Signal()

    stationNotTaken: Signal = Signal()
    stationTakenOffline: Signal = Signal()
    fuelPriceDataSent: Signal = Signal(FuelPriceDataSentMessage)
    loyaltyCardSent: Signal = Signal(LoyaltyCardSentMessage)
    paymentReceived: Signal = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        self._url: QUrl = QUrl()
        self._url.setScheme('ws')
        self._url.setHost(get_central_server_host())
        self._url.setPort(get_central_server_port())
        self._url.setPath(f'/api/ws/station/{get_station_id()}')

        self._client: QWebSocket = QWebSocket(self._url.toString(), parent=self)

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
        message = ConnectRequestMessage()
        self._client.sendTextMessage(message.to_json())

    def sendStationNotTakenRequest(self) -> None:
        message = StationNotTakenRequestMessage()
        self._client.sendTextMessage(message.to_json())

    def sendStationTakenOfflineRequest(self) -> None:
        message = StationTakenOfflineRequestMessage()
        self._client.sendTextMessage(message.to_json())

    def sendFuelPriceDataAsk(self) -> None:
        message = FuelPriceDataAskMessage()
        self._client.sendTextMessage(message.to_json())

    def sendLoyaltyCardAsk(self, message: LoyaltyCardAskMessage) -> None:
        self._client.sendTextMessage(message.to_json())

    def sendPaymentSent(self, message: PaymentSentMessage) -> None:
        self._client.sendTextMessage(message.to_json())

    @Slot()
    def onTextMessageReceived(self, json_str: str) -> None:
        print(f'CENTRAL SERVER CLIENT | message received: {json_str}')

        message_type = MessageType(json.loads(json_str)['message_type'])

        match (message_type):
            case MessageType.CONNECTED:
                self.connected.emit()
            case MessageType.STATION_NOT_TAKEN:
                self.stationNotTaken.emit()
            case MessageType.STATION_TAKEN_OFFLINE:
                self.stationTakenOffline.emit()
            case MessageType.FUEL_PRICE_DATA_SENT:
                message = FuelPriceDataSentMessage.from_json(json_str)
                self.fuelPriceDataSent.emit(message)
            case MessageType.LOYALTY_CARD_SENT:
                message = LoyaltyCardSentMessage.from_json(json_str)
                self.loyaltyCardSent.emit(message)
            case MessageType.PAYMENT_RECEIVED:
                self.paymentReceived.emit()

    @Slot()
    def onConnected(self) -> None:
        print(
            f'CENTRAL SERVER CLIENT | connected on {self._client.localAddress().toString()}:{self._client.localPort()}')
        self._sendConnectRequest()

    @Slot()
    def onDisconnected(self) -> None:
        print(f'CENTRAL SERVER CLIENT | disconnected')
        self.disconnected.emit()
