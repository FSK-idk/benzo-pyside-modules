from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal, Qt

from core.model.deposit_cards_request import DepositCardsRequest
from core.model.deposit_card_table_column import DepositCardTableColumn
from core.model.sort_order import SortOrder

from core.model.deposit_card import DepositCard

from core.widget.bank_viewer_screen.bank_viewer_screen_ui import BankViewerScreenUI


class BankViewerScreen(QObject):
    depositCardRequest: Signal = Signal(DepositCardsRequest)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: BankViewerScreenUI = BankViewerScreenUI(parent)

        self.ui.deposit_card_table.sortRequest.connect(self.onSortRequest)
        self.ui.update_button.clicked.connect(self.onUpdateClicked)
        self.ui.clear_button.clicked.connect(self.onClearClicked)

        self.ui.issuer_combo_box.addItem('Все')
        self.ui.issuer_combo_box.addItem('Visa')
        self.ui.issuer_combo_box.addItem('MasterCard')
        self.ui.issuer_combo_box.addItem('Mir')

        self._request: DepositCardsRequest = DepositCardsRequest()

        self.ui.show()

    def onClearClicked(self) -> None:
        self._request = DepositCardsRequest()
        self.ui.issuer_combo_box.setCurrentIndex(0)
        self.ui.number_line_edit.setText('')
        self.ui.holder_name_line_edit.setText('')

        self.ui.deposit_card_table.sort(0, Qt.SortOrder.AscendingOrder)

    def setCardTableData(self, cards: list[DepositCard]) -> None:
        self.ui.deposit_card_table.setTableData(cards)

    def onSortRequest(self, index: int, order: Qt.SortOrder) -> None:
        columns = [DepositCardTableColumn.ID, DepositCardTableColumn.ISSUER, DepositCardTableColumn.NUMBER,
                   DepositCardTableColumn.EXPIRATION_DATE, DepositCardTableColumn.HOLDER_NAME, DepositCardTableColumn.BALANCE]

        self._request.sort_by = columns[index]
        self._request.sort_order = SortOrder.ASC if order == Qt.SortOrder.AscendingOrder else SortOrder.DESC
        self.depositCardRequest.emit(self._request)

    def onUpdateClicked(self) -> None:
        self._request.deposit_card_number_starts_with = self.ui.number_line_edit.text()
        self._request.deposit_card_holder_name_starts_with = self.ui.holder_name_line_edit.text()
        self._request.deposit_card_issuer = None if self.ui.issuer_combo_box.currentText(
        ) == 'Все' else self.ui.issuer_combo_box.currentText()

        self.depositCardRequest.emit(self._request)
