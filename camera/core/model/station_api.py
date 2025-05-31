import json
from enum import Enum
from dataclasses import dataclass
from typing import Self, ClassVar

from core.model.car_number import CarNumber


class MessageType(Enum):
    CONNECT = 'connect'
    CONNECTED = 'connected'
    SERVICE_READY = 'service_ready'
    SERVICE_NOT_READY = 'service_not_ready'
    START_SERVICE = 'start_service'
    SERVICE_STARTED = 'service_started'
    END_SERVICE = 'end_service'
    SERVICE_ENDED = 'service_ended'
    CANCEL_REFUELING = 'cancel_refueling'
    REFUELING_CANCELED = 'refueling_canceled'
    USE_STATION_T1 = 'use_station_t1'
    STATION_USED_T1 = 'station_used_t1'
    USE_STATION_T2 = 'use_station_t2'
    STATION_USED_T2 = 'station_used_t2'
    USE_GAS_NOZZLE_T1 = 'use_gas_nozzle_t1'
    GAS_NOZZLE_USED_T1 = 'gas_nozzle_used_t1'
    USE_GAS_NOZZLE_T2 = 'use_gas_nozzle_t2'
    GAS_NOZZLE_USED_T2 = 'gas_nozzle_used_t2'
    USE_MOBILE_APP_T1 = 'use_mobile_app_t1'
    MOBILE_APP_USED_T1 = 'mobile_app_used_t1'
    USE_MOBILE_APP_T2 = 'use_mobile_app_t2'
    MOBILE_APP_USED_T2 = 'mobile_app_used_t2'


class SenderType(Enum):
    CAMERA = 'camera'
    GAS_NOZZLE = 'gas_nozzle'


@dataclass
class ConnectMessage:
    message_type: ClassVar[MessageType] = MessageType.CONNECT
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
class ConnectedMessage:
    message_type: ClassVar[MessageType] = MessageType.CONNECTED

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
class ServiceReadyMessage:
    message_type: ClassVar[MessageType] = MessageType.SERVICE_READY

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
class ServiceNotReadyMessage:
    message_type: ClassVar[MessageType] = MessageType.SERVICE_NOT_READY

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
class ServiceStartedMessage:
    message_type: ClassVar[MessageType] = MessageType.SERVICE_STARTED

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
class EndServiceMessage:
    message_type: ClassVar[MessageType] = MessageType.END_SERVICE

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
class ServiceEndedMessage:
    message_type: ClassVar[MessageType] = MessageType.SERVICE_ENDED

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
class CancelRefuelingMessage:
    message_type: ClassVar[MessageType] = MessageType.CANCEL_REFUELING

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
class RefuelingCanceledMessage:
    message_type: ClassVar[MessageType] = MessageType.REFUELING_CANCELED

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
class UseStationT1Message:
    message_type: ClassVar[MessageType] = MessageType.USE_STATION_T1
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
class StationUsedT1Message:
    message_type: ClassVar[MessageType] = MessageType.STATION_USED_T1

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
class UseStationT2Message:
    message_type: ClassVar[MessageType] = MessageType.USE_STATION_T2

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
class StationUsedT2Message:
    message_type: ClassVar[MessageType] = MessageType.STATION_USED_T2

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
class UseGasNozzleT1Message:
    message_type: ClassVar[MessageType] = MessageType.USE_GAS_NOZZLE_T1

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
class GasNozzleUsedT1Message:
    message_type: ClassVar[MessageType] = MessageType.GAS_NOZZLE_USED_T1

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
class UseGasNozzleT2Message:
    message_type: ClassVar[MessageType] = MessageType.USE_GAS_NOZZLE_T2

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
class GasNozzleUsedT2Message:
    message_type: ClassVar[MessageType] = MessageType.GAS_NOZZLE_USED_T2

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
class UseMobileAppT1Message:
    message_type: ClassVar[MessageType] = MessageType.USE_MOBILE_APP_T1

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
class MobileAppUsedT1Message:
    message_type: ClassVar[MessageType] = MessageType.MOBILE_APP_USED_T1

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
class UseMobileAppT2Message:
    message_type: ClassVar[MessageType] = MessageType.USE_MOBILE_APP_T2

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
class MobileAppUsedT2Message:
    message_type: ClassVar[MessageType] = MessageType.MOBILE_APP_USED_T2

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
