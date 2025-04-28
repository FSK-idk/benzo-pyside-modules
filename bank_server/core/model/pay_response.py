import json
from dataclasses import dataclass
from typing import Self


@dataclass
class PayResponse:
    payment_key: str

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        return cls(payment_key=data_dict['payment_key'])

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {"payment_key": self.payment_key}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
