import json
from dataclasses import dataclass
from typing import Self

from core.model.deposit_card_table_column import DepositCardTableColumn
from core.model.sort_order import SortOrder


@dataclass
class DepositCardsRequest:
    deposit_card_issuer: str | None = None
    deposit_card_number_starts_with: str | None = None
    deposit_card_holder_name_starts_with: str | None = None
    sort_by: DepositCardTableColumn | None = None
    sort_order: SortOrder | None = None

    @classmethod
    def from_dict(cls, data_dict: dict) -> Self:
        sort_by: DepositCardTableColumn | None = None if data_dict.get(
            'sort_by') is None else DepositCardTableColumn(data_dict['sort_by'])
        sort_order: SortOrder | None = None if data_dict.get(
            'sort_order') is None else SortOrder(data_dict['sort_order'])

        return cls(
            deposit_card_issuer=data_dict.get('deposit_card_issuer'),
            deposit_card_number_starts_with=data_dict.get('deposit_card_number_starts_with'),
            deposit_card_holder_name_starts_with=data_dict.get('deposit_card_holder_name_starts_with'),
            sort_by=sort_by,
            sort_order=sort_order,
        )

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict:
        data_dict: dict = dict()
        if self.deposit_card_issuer is not None:
            data_dict['deposit_card_issuer'] = self.deposit_card_issuer
        if self.deposit_card_number_starts_with is not None:
            data_dict['deposit_card_number_starts_with'] = self.deposit_card_number_starts_with
        if self.deposit_card_holder_name_starts_with is not None:
            data_dict['deposit_card_holder_name_starts_with'] = self.deposit_card_holder_name_starts_with
        if self.sort_by is not None:
            data_dict['sort_by'] = self.sort_by.value
        if self.sort_order is not None:
            data_dict['sort_order'] = self.sort_order.value
        return data_dict

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
