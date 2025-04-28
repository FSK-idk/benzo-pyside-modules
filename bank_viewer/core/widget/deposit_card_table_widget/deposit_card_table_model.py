from typing import Any

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QPersistentModelIndex

from core.model.deposit_card import DepositCard


class DepositCardTableModel(QAbstractTableModel):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._data: list[list] = list()
        self._horizontal_headers: list[str] = [
            "ID", "Платёжная система", "Номер", "Срок действия", "Держатель", "Баланс"]

    def setTableData(self, cards: list[DepositCard]) -> None:
        self._data = [
            [card.id, card.issuer, card.number, self._format_expiration_date(card.expiration_date), card.holder_name, self._format_balance(card.balance)] for card in cards]
        self.layoutChanged.emit()

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        return len(self._data)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        return len(self._horizontal_headers)

    def data(self, index: QModelIndex | QPersistentModelIndex, /, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self._horizontal_headers[section]

    @staticmethod
    def _format_expiration_date(expiration_date: str) -> str:
        # yyyy-MM-01 -> MM/yy
        return expiration_date[5:7] + '/' + expiration_date[2:4]

    @staticmethod
    def _format_balance(balance: int) -> float:
        return balance / 100
