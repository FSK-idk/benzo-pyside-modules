import json
from dataclasses import dataclass
from typing import Self


@dataclass
class DepositCard:
    id: int
    issuer: str
    number: str
    expiration_date: str
    holder_name: str
    balance: int

    @classmethod
    def from_list(cls, data_list: list) -> Self:
        return cls(
            id=data_list[0],
            issuer=data_list[1],
            number=data_list[2],
            expiration_date=data_list[3],
            holder_name=data_list[4],
            balance=data_list[5],
        )

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        return cls(
            id=data_dict['id'],
            issuer=data_dict['issuer'],
            number=data_dict['number'],
            expiration_date=data_dict['expiration_date'],
            holder_name=data_dict['holder_name'],
            balance=data_dict['balance'],
        )

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        data: dict = {
            "id": self.id,
            "issuer": self.issuer,
            "number": self.number,
            "expiration_date": self.expiration_date,
            "holder_name": self.holder_name,
            "balance": self.balance
        }
        return data

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
