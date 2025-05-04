import json
from enum import Enum
from dataclasses import dataclass
from typing import Self, ClassVar

from core.model.car_number import CarNumber


class MessageType(Enum):
    CONNECT_REQUEST = 'connect_request'
    CAMERA_CONNECTED = 'camera_connected'
    CAMERA_DISCONNECTED = 'camera_disconnceted'
    GAS_NOZZLE_CONNECTED = 'gas_nozzle_connected'
    GAS_NOZZLE_DISCONNECTED = 'gas_nozzle_disconnected'

    START_SERVICE_REQUEST = 'start_service_request'
    START_SERVICE = 'start_service'
    RESET_SERVICE_REQUEST = 'reset_service_request'
    RESET_SERVICE = 'reset_service'
    CAR_NUMBER_SENT = 'car_number_sent'
    CAR_NUMBER_RECEIVED = 'car_number_received'
    START_STATION = 'start_station'
    START_GAS_NOZZLE_REQUEST = 'start_gas_nozzle_request'
    START_GAS_NOZZLE = 'start_gas_nozzle'
    FINISH_GAS_NOZZLE_REQUEST = 'finish_gas_nozzle_request'
    FINISH_GAS_NOZZLE = 'finish_gas_nozzle'


class SenderType(Enum):
    CAMERA = 'camera'
    GAS_NOZZLE = 'gas_nozzle'


@dataclass
class ConnectRequestMessage:
    message_type: ClassVar[MessageType] = MessageType.CONNECT_REQUEST
    sender_type: SenderType

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls(
                sender_type=SenderType(data_dict['sender_type']),
            )
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
            'sender_type': self.sender_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class CameraConnectedMessage:
    message_type: ClassVar[MessageType] = MessageType.CAMERA_CONNECTED

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class GasNozzleConnectedMessage:
    message_type: ClassVar[MessageType] = MessageType.GAS_NOZZLE_CONNECTED

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class CameraDisconnectedMessage:
    message_type: ClassVar[MessageType] = MessageType.CAMERA_DISCONNECTED

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class GasNozzleDisconnectedMessage:
    message_type: ClassVar[MessageType] = MessageType.GAS_NOZZLE_DISCONNECTED

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class StartServiceRequestMessage:
    message_type: ClassVar[MessageType] = MessageType.START_SERVICE_REQUEST

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class StartServiceMessage:
    message_type: ClassVar[MessageType] = MessageType.START_SERVICE

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class ResetServiceRequestMessage:
    message_type: ClassVar[MessageType] = MessageType.RESET_SERVICE_REQUEST

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class ResetServiceMessage:
    message_type: ClassVar[MessageType] = MessageType.RESET_SERVICE

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class CarNumberSentMessage:
    message_type: ClassVar[MessageType] = MessageType.CAR_NUMBER_SENT
    car_number: CarNumber

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls(
                car_number=CarNumber(text=data_dict['car_number']),
            )
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
            'car_number': self.car_number.text,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class CarNumberReceivedMessage:
    message_type: ClassVar[MessageType] = MessageType.CAR_NUMBER_RECEIVED
    car_number: CarNumber

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls(
                car_number=CarNumber(text=data_dict['car_number']),
            )
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
            'car_number': self.car_number.text,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class StartStationMessage:
    message_type: ClassVar[MessageType] = MessageType.START_STATION

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class StartGasNozzleRequestMessage:
    message_type: ClassVar[MessageType] = MessageType.START_GAS_NOZZLE_REQUEST

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class StartGasNozzleMessage:
    message_type: ClassVar[MessageType] = MessageType.START_GAS_NOZZLE

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class FinishGasNozzleRequestMessage:
    message_type: ClassVar[MessageType] = MessageType.FINISH_GAS_NOZZLE_REQUEST

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class FinishGasNozzleMessage:
    message_type: ClassVar[MessageType] = MessageType.FINISH_GAS_NOZZLE

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        if data_dict['message_type'] == cls.message_type.value:
            return cls()
        raise ValueError('message_type is invalid')

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            'message_type': self.message_type.value,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
