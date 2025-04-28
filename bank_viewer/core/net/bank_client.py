import os

from PySide6.QtCore import QObject, QUrl, Signal
from PySide6.QtNetwork import QNetworkRequest, QNetworkReply, QNetworkAccessManager

from core.model.deposit_cards_request import DepositCardsRequest
from core.model.deposit_cards_response import DepositCardsResponse


class BankClient(QObject):
    depositCardsResponse: Signal = Signal(DepositCardsResponse)

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        host = os.getenv('BANK_HOST')
        port = os.getenv('BANK_PORT')

        self._url: str = f'http://{host}:{port}/api'

        self._nam: QNetworkAccessManager = QNetworkAccessManager(self)
        self._nam.finished.connect(self.handleResponse)

    def sendDepositCardsRequest(self, deposit_cards_request: DepositCardsRequest) -> None:
        request = QNetworkRequest(QUrl(self._url + '/deposit-cards'))
        request.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
        self._nam.get(request, deposit_cards_request.to_json().encode())

    def handleResponse(self, reply: QNetworkReply) -> None:
        error = reply.error()

        if error == QNetworkReply.NetworkError.NoError:
            deposit_cards_response = DepositCardsResponse.from_json(reply.readAll().toStdString())
            self.depositCardsResponse.emit(deposit_cards_response)
