import json
from dataclasses import dataclass
from typing import Self

from core.model.deposit_card import DepositCard


@dataclass
class DepositCardsResponse:
    deposit_cards: list[DepositCard]

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        return cls(deposit_cards=[DepositCard.from_dict(card_data_dict) for card_data_dict in data_dict['deposit_cards']])

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        data: dict = {'deposit_cards': [card.to_dict() for card in self.deposit_cards]}
        return data

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
