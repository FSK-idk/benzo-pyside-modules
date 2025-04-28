import json
from enum import Enum

from PySide6.QtCore import QObject, QUrl, Slot, Signal
from PySide6.QtWebSockets import QWebSocket

from core.model.car_number import CarNumber

from core.util import get_url


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


class Client(QObject):
    connected: Signal = Signal()
    disconnected: Signal = Signal()

    resetService: Signal = Signal()

    carNumberReceived: Signal = Signal(CarNumber)
    startGasNozzle: Signal = Signal()
    gasNozzleFinished: Signal = Signal()

    cameraDisconnected: Signal = Signal()
    gasNozzleConnected: Signal = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        self.client: QWebSocket = QWebSocket('', parent=self)
        self.url: QUrl = get_url()

        self.client.connected.connect(self.connected.emit)
        self.client.disconnected.connect(self.disconnected.emit)

        self.client.textMessageReceived.connect(self.onTextMessageReceived)

    def __del__(self) -> None:
        self.stopClient()

    def startClient(self) -> None:
        self.client.open(self.url)

    def stopClient(self) -> None:
        self.client.close()

    def sendConnect(self) -> None:
        json_dict = {
            'sender': SenderType.GAS_NOZZLE.value,
            'message_type': MessageType.CONNECT.value,
        }
        self.client.sendTextMessage(json.dumps(json_dict))

    def sendGasNozzleFinished(self) -> None:
        json_dict = {
            'sender': SenderType.GAS_NOZZLE.value,
            'message_type': MessageType.GAS_NOZZLE_FINISHED.value,
        }
        self.client.sendTextMessage(json.dumps(json_dict))

    @Slot()
    def onTextMessageReceived(self, message: str) -> None:
        print(f'CLIENT: message received: {message}')

        json_dict = json.loads(message)

        if (None in [json_dict.get('message_type'), json_dict.get('sender')]):
            print(f'WARNING. Invalid message: {message}')
            return

        message_type: MessageType = MessageType(json_dict['message_type'])
        sender: SenderType = SenderType(json_dict['sender'])

        match (message_type):
            case MessageType.RESET_SERVICE:
                self.resetService.emit()

            case MessageType.CAR_NUMBER_RECEIVED:
                car_number: CarNumber = CarNumber(text=json_dict['car_number'])
                self.carNumberReceived.emit(car_number)

            case MessageType.START_GAS_NOZZLE:
                self.startGasNozzle.emit()

            case MessageType.GAS_NOZZLE_FINISHED:
                self.gasNozzleFinished.emit()

            case MessageType.CAMERA_DISCONNECTED:
                self.cameraDisconnected.emit()

            case MessageType.GAS_NOZZLE_CONNECTED:
                self.gasNozzleConnected.emit()
