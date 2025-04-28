import json
from dataclasses import dataclass
from typing import Self


@dataclass
class PayRequest:
    deposit_card_number: str
    deposit_card_expiration_date: str
    deposit_card_holder_name: str
    payment_amount: int

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        return cls(
            deposit_card_number=data_dict['deposit_card_number'],
            deposit_card_expiration_date=data_dict['deposit_card_expiration_date'],
            deposit_card_holder_name=data_dict['deposit_card_holder_name'],
            payment_amount=data_dict['payment_amount'],
        )

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        return {
            "deposit_card_number": self.deposit_card_number,
            "deposit_card_expiration_date": self.deposit_card_expiration_date,
            "deposit_card_holder_name": self.deposit_card_holder_name,
            "payment_amount": self.payment_amount,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
