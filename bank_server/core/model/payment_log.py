import json
from dataclasses import dataclass
from typing import Self


@dataclass
class PaymentLog:
    id: int
    deposit_card_id: int
    payment_amount: int
    organization_name: str
    payment_key: str

    @classmethod
    def from_list(cls, data_list: list) -> Self:
        return cls(
            id=data_list[0],
            deposit_card_id=data_list[1],
            payment_amount=data_list[2],
            organization_name=data_list[3],
            payment_key=data_list[4],
        )

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        return cls(
            id=data_dict['id'],
            deposit_card_id=data_dict['deposit_card_id'],
            payment_amount=data_dict['payment_amount'],
            organization_name=data_dict['organization_name'],
            payment_key=data_dict['payment_key'],
        )

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        data: dict = {
            "id": self.id,
            "deposit_card_id": self.deposit_card_id,
            "payment_amount": self.payment_amount,
            "organization_name": self.organization_name,
            "payment_key": self.payment_key,
        }
        return data

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
