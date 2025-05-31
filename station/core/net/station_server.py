import json
from mailbox import Message
from bidict import bidict
from typing import cast

from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtWebSockets import QWebSocket, QWebSocketServer
from PySide6.QtNetwork import QHostAddress

from core.model.station_api import *

from core.util import get_station_host, get_station_port


class StationServer(QObject):
    serviceReady: Signal = Signal()
    serviceNotReady: Signal = Signal()
    serviceStarted: Signal = Signal()
    refuelingCanceled: Signal = Signal()
    useStationT1: Signal = Signal(UseStationT1Message)
    stationUsedT2: Signal = Signal()
    mobileAppUsedT2: Signal = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        self._server: QWebSocketServer = QWebSocketServer('', QWebSocketServer.SslMode.NonSecureMode, self)

        self._clients: list[QWebSocket] = list()
        self._station_client: bidict[QWebSocket, SenderType] = bidict()

        self._server.newConnection.connect(self.onNewConnection)

        self._server.closed.connect(self.onStopped)

    def __del__(self) -> None:
        self._server.close()

    def start(self) -> None:
        if (self._server.isListening()):
            print('STATION SERVER | warning: server already started')
            return

        port = get_station_port()
        host = get_station_host()

        result = self._server.listen(QHostAddress(host), port)

        if (result):
            print('STATION SERVER | server started')
        else:
            print('STATION SERVER | error: server cannont start')

    def stop(self) -> None:
        for k in self._clients.copy():
            print(f'STATION SERVER | will disconnect {k.peerAddress().toString()}:{k.peerPort()}')
            k.close()

        self._server.close()

    def sendServiceReady(self) -> None:
        message = ServiceReadyMessage()
        self.sendToAll(message.to_json())

    def sendServiceStarted(self) -> None:
        message = ServiceStartedMessage()
        self.sendToAll(message.to_json())

    def sendServiceEnded(self) -> None:
        message = ServiceEndedMessage()
        self.sendToAll(message.to_json())

    def sendRefuelingCanceled(self) -> None:
        message = RefuelingCanceledMessage()
        self.sendToAll(message.to_json())

    def sendStationUsedT1(self) -> None:
        message = StationUsedT1Message()
        self.sendToAll(message.to_json())

    def sendStationUsedT2(self) -> None:
        message = StationUsedT2Message()
        self.sendToAll(message.to_json())

    def sendGasNozzleUsedT1(self) -> None:
        message = GasNozzleUsedT1Message()
        self.sendToAll(message.to_json())

    def sendGasNozzleUsedT2(self) -> None:
        message = GasNozzleUsedT2Message()
        self.sendToAll(message.to_json())

    def sendMobileAppUsedT1(self) -> None:
        message = MobileAppUsedT1Message()
        self.sendToAll(message.to_json())

    def sendMobileAppUsedT2(self) -> None:
        message = MobileAppUsedT2Message()
        self.sendToAll(message.to_json())

    def sendToAll(self, json_str: str) -> None:
        camera = self._station_client.inv.get(SenderType.CAMERA)
        gas_nozzle = self._station_client.inv.get(SenderType.GAS_NOZZLE)

        if (camera is not None):
            camera.sendTextMessage(json_str)
        if (gas_nozzle is not None):
            gas_nozzle.sendTextMessage(json_str)

    @Slot()
    def onNewConnection(self) -> None:
        client = self._server.nextPendingConnection()
        print(f'STATION SERVER | client {client.peerAddress().toString()}:{client.peerPort()} connected')
        client.textMessageReceived.connect(self.onTextMessageReceived)
        client.disconnected.connect(self.onClientDisconnected)
        self._clients.append(client)

    @Slot()
    def onTextMessageReceived(self, json_str: str) -> None:
        print(f'STATION SERVER | message received: {json_str}')

        client = cast(QWebSocket, self.sender())
        message_type = MessageType(json.loads(json_str)['message_type'])

        match (message_type):
            case MessageType.CONNECT:
                message = ConnectMessage.from_json(json_str)

                if (self._station_client.inv.get(message.sender_type) is None):
                    self._station_client[client] = message.sender_type
                    match message.sender_type:
                        case SenderType.CAMERA:
                            new_message = ConnectedMessage()
                            client.sendTextMessage(message.to_json())
                        case SenderType.GAS_NOZZLE:
                            new_message = ConnectedMessage()
                            client.sendTextMessage(new_message.to_json())

                    if (None not in [self._station_client.inv.get(SenderType.CAMERA), self._station_client.inv.get(SenderType.GAS_NOZZLE)]):
                        self.sendServiceReady()
                        self.serviceReady.emit()
                else:
                    print(f'STATION SERVER | warning: one more {message.sender_type.value} wants connect')

            case MessageType.START_SERVICE:
                self.sendServiceStarted()
                self.serviceStarted.emit()

            case MessageType.USE_STATION_T1:
                message = UseStationT1Message.from_json(json_str)
                self.useStationT1.emit(message)

            case MessageType.USE_STATION_T2:
                self.sendStationUsedT2()
                self.stationUsedT2.emit()

            case MessageType.CANCEL_REFUELING:
                self.sendRefuelingCanceled()
                self.refuelingCanceled.emit()

            case MessageType.USE_MOBILE_APP_T2:
                self.sendMobileAppUsedT2()
                self.mobileAppUsedT2.emit()

    @Slot()
    def onClientDisconnected(self) -> None:
        client = cast(QWebSocket, self.sender())
        sender_type = self._station_client[client]

        match(sender_type):
            case SenderType.CAMERA:
                message = ServiceNotReadyMessage()
                gas_nozzle = self._station_client.inv.get(SenderType.GAS_NOZZLE)
                if (gas_nozzle is not None):
                    gas_nozzle.sendTextMessage(message.to_json())
                self.serviceNotReady.emit()

            case SenderType.GAS_NOZZLE:
                message = ServiceNotReadyMessage()
                camera = self._station_client.inv.get(SenderType.CAMERA)
                if (camera is not None):
                    camera.sendTextMessage(message.to_json())
                self.serviceNotReady.emit()

        if (sender_type is not None):
            del self._station_client[client]

        print(f'STATION SERVER | client {client.peerAddress().toString()}:{client.peerPort()} disconnected')
        self._clients.remove(client)

    @Slot()
    def onStopped(self) -> None:
        print('STATION SERVER | server stopped')
