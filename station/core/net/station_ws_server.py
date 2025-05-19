import json
from bidict import bidict
from typing import cast

from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtWebSockets import QWebSocket, QWebSocketServer
from PySide6.QtNetwork import QHostAddress

from core.model.station_ws_api import *

from core.util import get_station_host, get_station_port


class StationWsServer(QObject):
    cameraDisconnected: Signal = Signal()
    gasNozzleDisconnected: Signal = Signal()

    startServiceRequest: Signal = Signal()
    resetServiceRequest: Signal = Signal()
    resetService: Signal = Signal()
    cancelRefuelingRequest: Signal = Signal()
    cancelRefueling: Signal = Signal()
    carNumberSent: Signal = Signal(CarNumberSentMessage)
    carNumberReceived: Signal = Signal(CarNumberReceivedMessage)
    startGasNozzleRequest: Signal = Signal()
    startGasNozzle: Signal = Signal()
    finishGasNozzleRequest: Signal = Signal()
    finishGasNozzle: Signal = Signal()

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

    def sendStartService(self) -> None:
        message = StartServiceMessage()
        self.sendToAll(message.to_json())

    def sendResetServiceRequest(self) -> None:
        self.resetServiceRequest.emit()

    def sendResetService(self) -> None:
        self.resetService.emit()
        message = ResetServiceMessage()
        self.sendToAll(message.to_json())

    def sendCancelRefuelingRequest(self) -> None:
        self.cancelRefuelingRequest.emit()

    def sendCancelRefueling(self) -> None:
        self.cancelRefueling.emit()
        message = CancelRefuelingMessage()
        self.sendToAll(message.to_json())

    def sendCarNumberReceived(self, message: CarNumberReceivedMessage) -> None:
        self.carNumberReceived.emit(message)
        self.sendToAll(message.to_json())

    def sendStartStation(self) -> None:
        message = StartStationMessage()
        self.sendToAll(message.to_json())

    def sendStartGasNozzleRequest(self) -> None:
        self.startGasNozzleRequest.emit()

    def sendStartGasNozzle(self) -> None:
        self.startGasNozzle.emit()
        message = StartGasNozzleMessage()
        self.sendToAll(message.to_json())

    def sendFinishGasNozzle(self) -> None:
        self.finishGasNozzle.emit()
        message = FinishGasNozzleMessage()
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
            case MessageType.CONNECT_REQUEST:
                message = ConnectRequestMessage.from_json(json_str)

                if (self._station_client.inv.get(message.sender_type) is None):
                    self._station_client[client] = message.sender_type
                    match message.sender_type:
                        case SenderType.CAMERA:
                            message = CameraConnectedMessage()
                            client.sendTextMessage(message.to_json())
                        case SenderType.GAS_NOZZLE:
                            message = GasNozzleConnectedMessage()
                            client.sendTextMessage(message.to_json())

                    if (None not in [self._station_client.inv.get(SenderType.CAMERA), self._station_client.inv.get(SenderType.GAS_NOZZLE)]):
                        self.sendResetServiceRequest()
                else:
                    print(f'STATION SERVER | warning: one more {message.sender_type.value} wants connect')

            case MessageType.START_SERVICE_REQUEST:
                self.startServiceRequest.emit()
            case MessageType.RESET_SERVICE:
                self.resetService.emit()
            case MessageType.RESET_SERVICE:
                self.resetService.emit()
            case MessageType.CANCEL_REFUELING_REQUEST:
                self.cancelRefuelingRequest.emit()
            case MessageType.CAR_NUMBER_SENT:
                message = CarNumberSentMessage.from_json(json_str)
                self.carNumberSent.emit(message)
            case MessageType.START_GAS_NOZZLE_REQUEST:
                self.startGasNozzleRequest.emit()
            case MessageType.FINISH_GAS_NOZZLE_REQUEST:
                self.finishGasNozzleRequest.emit()

    @Slot()
    def onClientDisconnected(self) -> None:
        client = cast(QWebSocket, self.sender())
        sender_type = self._station_client[client]

        match(sender_type):
            case SenderType.CAMERA:
                message = CameraDisconnectedMessage()
                gas_nozzle = self._station_client.inv.get(SenderType.GAS_NOZZLE)
                if (gas_nozzle is not None):
                    gas_nozzle.sendTextMessage(message.to_json())
                self.cameraDisconnected.emit()

            case SenderType.GAS_NOZZLE:
                message = GasNozzleDisconnectedMessage()
                camera = self._station_client.inv.get(SenderType.CAMERA)
                if (camera is not None):
                    camera.sendTextMessage(message.to_json())
                self.gasNozzleDisconnected.emit()

        if (sender_type is not None):
            del self._station_client[client]

        print(f'STATION SERVER | client {client.peerAddress().toString()}:{client.peerPort()} disconnected')
        self._clients.remove(client)

    def onStopped(self) -> None:
        print('STATION SERVER | server stopped')
