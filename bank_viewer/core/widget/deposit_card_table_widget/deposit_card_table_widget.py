from PySide6.QtWidgets import QWidget, QTableView, QAbstractItemView, QHeaderView
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

from core.widget.deposit_card_table_widget.deposit_card_table_model import DepositCardTableModel

from core.model.deposit_card import DepositCard


class DepositCardTableWidget(QTableView):
    sortRequest: Signal = Signal(int, Qt.SortOrder)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._table_model: DepositCardTableModel = DepositCardTableModel(self)

        self.setModel(self._table_model)

        self.horizontalHeader().setFont(QFont("Noto Sans", 12))
        self.setFont(QFont("Noto Sans", 14))

        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.verticalHeader().hide()
        self.horizontalHeader().setMinimumSectionSize(40)

        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.setSortingEnabled(True)
        self.horizontalHeader().sortIndicatorChanged.connect(self.sort)
        self.horizontalHeader().setSortIndicator(0, Qt.SortOrder.AscendingOrder)

    def setTableData(self, cards: list[DepositCard]) -> None:
        self._table_model.setTableData(cards)

    def sort(self, index: int, order: Qt.SortOrder) -> None:
        self.sortRequest.emit(index, order)
