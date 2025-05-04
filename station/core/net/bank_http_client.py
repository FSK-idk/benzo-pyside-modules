from PySide6.QtCore import QObject, QUrl, Signal
from PySide6.QtNetwork import QNetworkRequest, QNetworkReply, QNetworkAccessManager

from core.model.bank_http_api import *

from core.util import get_bank_host, get_bank_port


class BankHttpClient(QObject):
    payResponse: Signal = Signal(PayResponse)
    payError: Signal = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        self._pay_url: QUrl = QUrl()
        self._pay_url.setScheme('http')
        self._pay_url.setHost(get_bank_host())
        self._pay_url.setPort(get_bank_port())
        self._pay_url.setPath('/api/pay')

        self._nam: QNetworkAccessManager = QNetworkAccessManager(self)
        self._nam.finished.connect(self.handleResponse)

    def sendPayRequest(self, pay_request: PayRequest) -> None:
        request = QNetworkRequest(self._pay_url)
        request.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
        self._nam.post(request, pay_request.to_json().encode())

    def handleResponse(self, reply: QNetworkReply) -> None:
        error = reply.error()

        if error == QNetworkReply.NetworkError.NoError:
            deposit_cards_response = PayResponse.from_json(reply.readAll().toStdString())
            self.payResponse.emit(deposit_cards_response)
        else:
            self.payError.emit()
