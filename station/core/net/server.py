import json
from enum import Enum
from typing import cast

from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtWebSockets import QWebSocket, QWebSocketServer
from PySide6.QtNetwork import QHostAddress

from core.model.car_number import CarNumber

from core.util import get_port


class SenderType(Enum):
    CAMERA = 'camera'
    GAS_NOZZLE = 'gas_nozzle'
    STATION = 'station'


class MessageType(Enum):
    CONNECT = 'connect'

    START_SERVICE = 'start_service'
    RESET_SERVICE = 'reset_service'

    CAR_NUMBER_RECEIVED = 'car_number_received'
    START_GAS_NOZZLE = 'start_gas_nozzle'
    GAS_NOZZLE_FINISHED = 'gas_nozzle_finished'

    CAMERA_CONNECTED = 'camera_connected'
    CAMERA_DISCONNECTED = 'camera_disconnected'
    GAS_NOZZLE_CONNECTED = 'gas_nozzle_connected'
    GAS_NOZZLE_DISCONNECTED = 'gas_nozzle_disconnected'


class Server(QObject):
    startService: Signal = Signal()
    resetService: Signal = Signal()
    carNumberReceived: Signal = Signal(CarNumber)
    gasNozzleFinished: Signal = Signal()

    cameraConnected: Signal = Signal()
    cameraDisconnected: Signal = Signal()
    gasNozzleConnected: Signal = Signal()
    gasNozzleDisconnected: Signal = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        self.port = get_port()

        self.server: QWebSocketServer = QWebSocketServer('', QWebSocketServer.SslMode.NonSecureMode, self)

        self.clients: list[QWebSocket] = list()
        self.named_client: dict[SenderType, QWebSocket] = dict()

        self.server.newConnection.connect(self.onNewConnection)
        self.server.closed.connect(self.onStopped)

    def __del__(self) -> None:
        self.server.close()

    def startServer(self) -> None:
        if (self.server.isListening()):
            print('WARNING. Server already started')
            return

        result = self.server.listen(QHostAddress.SpecialAddress.Any, self.port)

        if (result):
            print('Server started')
        else:
            print('ERROR. Server cannont start')

    def sendStartService(self) -> None:
        json_dict = {
            'sender': SenderType.STATION.value,
            'message_type': MessageType.START_SERVICE.value,
        }
        self.sendToAll(json.dumps(json_dict))

    def sendResetService(self) -> None:
        json_dict = {
            'sender': SenderType.STATION.value,
            'message_type': MessageType.RESET_SERVICE.value,
        }
        self.sendToAll(json.dumps(json_dict))

    def sendCarNumberReceived(self, car_number: CarNumber) -> None:
        json_dict = {
            'sender': SenderType.STATION.value,
            'message_type': MessageType.CAR_NUMBER_RECEIVED.value,
            'car_number': car_number.text,
        }
        self.sendToAll(json.dumps(json_dict))

    def sendStartGasNozzle(self) -> None:
        json_dict = {
            'sender': SenderType.STATION.value,
            'message_type': MessageType.START_GAS_NOZZLE.value,
        }
        self.sendToAll(json.dumps(json_dict))

    def sendGasNozzleFinished(self) -> None:
        json_dict = {
            'sender': SenderType.STATION.value,
            'message_type': MessageType.GAS_NOZZLE_FINISHED.value,
        }
        self.sendToAll(json.dumps(json_dict))

    def sendCameraConnected(self) -> None:
        json_dict = {
            'sender': SenderType.STATION.value,
            'message_type': MessageType.CAMERA_CONNECTED.value,
        }
        self.sendToAll(json.dumps(json_dict))

    def sendGasNozzleConnected(self) -> None:
        json_dict = {
            'sender': SenderType.STATION.value,
            'message_type': MessageType.GAS_NOZZLE_CONNECTED.value,
        }
        self.sendToAll(json.dumps(json_dict))

    def sendToAll(self, json_str: str) -> None:
        camera: QWebSocket | None = self.named_client.get(SenderType.CAMERA)
        gas_nozzle: QWebSocket | None = self.named_client.get(SenderType.GAS_NOZZLE)
        if (camera is not None):
            camera.sendTextMessage(json_str)
        if (gas_nozzle is not None):
            gas_nozzle.sendTextMessage(json_str)

    @Slot()
    def onNewConnection(self) -> None:
        client: QWebSocket = self.server.nextPendingConnection()
        print(f'Client {client.peerAddress().toString()} connected')
        client.textMessageReceived.connect(self.onTextMessageReceived)
        client.disconnected.connect(self.onClientDisconnected)
        self.clients.append(client)

    @Slot()
    def onTextMessageReceived(self, message: str) -> None:
        client: QWebSocket = cast(QWebSocket, self.sender())

        print(f'SERVER: message received: {message}')

        json_dict = json.loads(message)

        if (None in [json_dict.get('message_type'), json_dict.get('sender')]):
            print(f'WARNING. Invalid message: {message}')
            return

        message_type: MessageType = MessageType(json_dict['message_type'])
        sender: SenderType = SenderType(json_dict['sender'])

        match (message_type):
            case MessageType.CONNECT:
                if (self.named_client.get(sender) is None):
                    self.named_client[sender] = client
                    match (sender):
                        case SenderType.CAMERA:
                            self.cameraConnected.emit()
                        case SenderType.GAS_NOZZLE:
                            self.gasNozzleConnected.emit()
                else:
                    print(f'WARNING. One more {json_dict['sender']} wants connect')

            case MessageType.START_SERVICE:
                self.startService.emit()

            case MessageType.RESET_SERVICE:
                self.resetService.emit()

            case MessageType.CAR_NUMBER_RECEIVED:
                car_number: CarNumber = CarNumber(text=json_dict['car_number'])
                self.carNumberReceived.emit(car_number)

            case MessageType.GAS_NOZZLE_FINISHED:
                self.gasNozzleFinished.emit()

    @Slot()
    def onClientDisconnected(self) -> None:
        client: QWebSocket = cast(QWebSocket, self.sender())

        sender: SenderType | None = None

        for sndr, clnt in self.named_client.items():
            if (clnt == client):
                sender = sndr
                break

        match(sender):
            case SenderType.CAMERA:
                json_dict = {
                    'sender': SenderType.STATION.value,
                    'message_type': MessageType.CAMERA_DISCONNECTED.value,
                }
                gas_nozzle: QWebSocket | None = self.named_client.get(SenderType.GAS_NOZZLE)
                if (gas_nozzle is not None):
                    gas_nozzle.sendTextMessage(json.dumps(json_dict))
                self.cameraDisconnected.emit()

            case SenderType.GAS_NOZZLE:
                json_dict = {
                    'sender': SenderType.STATION.value,
                    'message_type': MessageType.GAS_NOZZLE_DISCONNECTED.value,
                }
                camera: QWebSocket | None = self.named_client.get(SenderType.CAMERA)
                if (camera is not None):
                    camera.sendTextMessage(json.dumps(json_dict))
                self.gasNozzleDisconnected.emit()

        if (sender is not None):
            del self.named_client[sender]

        print(f'Client {client.peerAddress().toString()} disconnected')
        self.clients.remove(client)

    def onStopped(self) -> None:
        print('Server stopped')
