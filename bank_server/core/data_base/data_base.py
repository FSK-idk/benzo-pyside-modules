import os
import json
import sqlite3

from core.model.deposit_card import DepositCard
from core.model.payment_log import PaymentLog
from core.model.deposit_cards_request import DepositCardsRequest
from core.model.deposit_card_table_column import DepositCardTableColumn
from core.model.sort_order import SortOrder
from core.model.pay_request import PayRequest

from core.data_base.query import Query


class DataBase():
    def init(self) -> None:
        if not os.path.isdir('data/'):
            os.mkdir('data/')

        self._data_base: sqlite3.Connection = sqlite3.connect('data/data_base.sqlite', check_same_thread=False)

        self._data_base.execute(Query.createDepositCardTable())
        self._data_base.commit()

        json_filename: str = 'data/deposit_card.json'
        with open(json_filename) as json_file:
            json_dict = json.load(json_file)
            for card_json_dict in json_dict['DepositCard']:
                card: DepositCard = DepositCard(
                    id=0,
                    issuer=card_json_dict['issuer'],
                    number=card_json_dict['number'],
                    expiration_date=card_json_dict['expiration_date'],
                    holder_name=card_json_dict['holder_name'],
                    balance=card_json_dict['balance'],
                )
                self.insertDepositCard(card)

        self._data_base.execute(Query.createPaymentLogTable())
        self._data_base.commit()

        json_filename: str = 'data/payment_log.json'
        with open(json_filename) as json_file:
            json_dict = json.load(json_file)
            for log_json_dict in json_dict['PaymentLog']:
                deposit_card_id = self.selectDepositCardIdByNumber(log_json_dict['deposit_card_number'],)
                if deposit_card_id is not None:
                    log: PaymentLog = PaymentLog(
                        id=0,
                        deposit_card_id=deposit_card_id,
                        payment_amount=log_json_dict['payment_amount'],
                        organization_name=log_json_dict['organization_name'],
                        payment_key=log_json_dict['payment_key'],
                    )
                    self.insertPaymentLog(log)

    def __del__(self) -> None:
        self._data_base.close()

    def insertDepositCard(self, card: DepositCard) -> None:
        issuer = card.issuer
        number = card.number
        expiration_date = card.expiration_date
        holder_name = card.holder_name
        balance = card.balance

        self._data_base.execute(Query.insertDepositCard(),
                                (issuer, number, expiration_date, holder_name, balance,))
        self._data_base.commit()

    def insertPaymentLog(self, card: PaymentLog) -> None:
        deposit_card_id = card.deposit_card_id
        payment_amount = card.payment_amount
        organization_name = card.organization_name
        payment_key = card.payment_key

        self._data_base.execute(Query.insertPaymentLog(),
                                (deposit_card_id, payment_amount, organization_name, payment_key,))
        self._data_base.commit()

    def selectDepositCards(self, request: DepositCardsRequest) -> list[DepositCard]:
        deposit_card_issuer = '%' if request.deposit_card_issuer is None else request.deposit_card_issuer
        deposit_card_number_starts_with = '%' if request.deposit_card_number_starts_with is None else request.deposit_card_number_starts_with + '%'
        deposit_card_holder_name_starts_with = '%' if request.deposit_card_holder_name_starts_with is None else request.deposit_card_holder_name_starts_with + '%'
        sort_by = DepositCardTableColumn.ID if request.sort_by is None else request.sort_by
        sort_order = SortOrder.ASC if request.sort_order is None else request.sort_order

        cur = self._data_base.execute(Query.selectDepositCards(sort_by, sort_order),
                                      (deposit_card_issuer, deposit_card_number_starts_with, deposit_card_holder_name_starts_with,))
        self._data_base.commit()

        return [DepositCard.from_list(data) for data in cur.fetchall()]

    def selectDepositCard(self, request: PayRequest) -> DepositCard | None:
        card_number = request.deposit_card_number
        expiration_date = request.deposit_card_expiration_date
        holder_name = request.deposit_card_holder_name

        cur = self._data_base.execute(Query.selectDepositCard(),
                                      (card_number, expiration_date, holder_name,))
        self._data_base.commit()

        data = cur.fetchone()

        return None if data is None else DepositCard.from_list(data)

    def selectDepositCardIdByNumber(self, number: str) -> int | None:
        cur = self._data_base.execute(Query.selectDepositCardIdByNumber(),
                                      (number,))
        self._data_base.commit()

        data = cur.fetchone()

        return data[0]

    def updateDepositCard(self, card: DepositCard) -> None:
        id = card.id
        balance = card.balance

        self._data_base.execute(Query.updateDepositCard(),
                                (balance, id,))
        self._data_base.commit()


data_base: DataBase = DataBase()
