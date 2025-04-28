import os

from PySide6.QtCore import QObject, QUrl, Signal
from PySide6.QtNetwork import QNetworkRequest, QNetworkReply, QNetworkAccessManager

from core.model.pay_request import PayRequest
from core.model.pay_response import PayResponse


class BankClient(QObject):
    payResponse: Signal = Signal(PayResponse)
    payError: Signal = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        host = os.getenv('BANK_HOST')
        port = os.getenv('BANK_PORT')

        self._url: str = f'http://{host}:{port}/api'

        self._nam: QNetworkAccessManager = QNetworkAccessManager(self)
        self._nam.finished.connect(self.handleResponse)

    def sendPayRequest(self, pay_request: PayRequest) -> None:
        request = QNetworkRequest(QUrl(self._url + '/pay'))
        request.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
        self._nam.post(request, pay_request.to_json().encode())

    def handleResponse(self, reply: QNetworkReply) -> None:
        error = reply.error()

        if error == QNetworkReply.NetworkError.NoError:
            deposit_cards_response = PayResponse.from_json(reply.readAll().toStdString())
            self.payResponse.emit(deposit_cards_response)
        else:
            self.payError.emit()
