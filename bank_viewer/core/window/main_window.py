from PySide6.QtCore import QObject, Slot

from core.window.main_window_ui import MainWindowUI

from core.model.deposit_cards_request import DepositCardsRequest
from core.model.deposit_cards_response import DepositCardsResponse

from core.net.bank_client import BankClient


class MainWindow(QObject):
    def __init__(self) -> None:
        super().__init__()

        self.ui: MainWindowUI = MainWindowUI()

        self.ui.bank_viewer_screen.depositCardRequest.connect(self.onUpdateClicked)

        self.bank_client: BankClient = BankClient(self)

        self.bank_client.depositCardsResponse.connect(self.onDepositCardsResponse)

        self.onUpdateClicked(DepositCardsRequest())

        self.ui.show()

    @Slot()
    def onUpdateClicked(self, deposit_card_request: DepositCardsRequest) -> None:
        self.bank_client.sendDepositCardsRequest(deposit_card_request)

    @Slot()
    def onDepositCardsResponse(self, deposit_card_response: DepositCardsResponse) -> None:
        self.ui.bank_viewer_screen.setCardTableData(deposit_card_response.deposit_cards)
