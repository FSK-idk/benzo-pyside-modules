from PySide6.QtCore import QObject, Slot

from core.window.main_window_ui import MainWindowUI, ViewName

from core.model.car_number import CarNumber
from core.model.fuel_type import FuelType
from core.widget.fuel_selection_screen.fuel_selection_screen import FuelSelectionData
from core.model.payment_selection_data import PaymentSelectionData

from core.model.central_server_ws_api import LoyaltyCardAskMessage, LoyaltyCardSentMessage, PaymentSentMessage
from core.model.station_ws_api import CarNumberSentMessage, CarNumberReceivedMessage
from core.model.bank_http_api import PayRequest, PayResponse

from core.net.central_server_ws_client import CentralServerWsClient
from core.net.station_ws_server import StationWsServer
from core.net.bank_http_client import BankHttpClient


class MainWindow(QObject):
    def __init__(self) -> None:
        super().__init__()

        self.ui: MainWindowUI = MainWindowUI()

        self.ui.fuel_selection_screen.continuePaymentClicked.connect(self.onContinuePaymentClicked)
        self.ui.fuel_selection_screen.cancelRefuelingClicked.connect(self.onCancelRefuelingClicked)
        self.ui.payment_selection_screen.payClicked.connect(self.onPayClicked)
        self.ui.payment_selection_screen.backFuelSelectionClicked.connect(self.onBackFuelSelectionClicked)
        self.ui.payment_selection_screen.cancelRefuelingClicked.connect(self.onCancelRefuelingClicked)
        self.ui.payment_error_screen.retryPaymentClicked.connect(self.onRetryPaymentClicked)
        self.ui.finish_screen.confirmClicked.connect(self.onConfirmClicked)
        self.ui.reconnection_screen.reconnectClicked.connect(self.onReconnectClicked)

        self.central_server_ws_client: CentralServerWsClient = CentralServerWsClient(self)

        self.central_server_ws_client.connected.connect(self.onCentralServerConnected)
        self.central_server_ws_client.disconnected.connect(self.onCentralServerDisconnected)
        self.central_server_ws_client.stationNotTaken.connect(self.onStationNotTaken)
        self.central_server_ws_client.stationTakenOffline.connect(self.onStationTakenOffline)
        self.central_server_ws_client.loyaltyCardSent.connect(self.onLoyaltyCardSent)
        self.central_server_ws_client.paymentReceived.connect(self.onPaymentReceived)

        self.station_ws_server: StationWsServer = StationWsServer(self)

        self.station_ws_server.cameraDisconnected.connect(self.onCameraDisconnected)
        self.station_ws_server.gasNozzleDisconnected.connect(self.onGasNozzleDisconnected)
        self.station_ws_server.resetServiceRequest.connect(self.onResetServiceRequest)
        self.station_ws_server.resetService.connect(self.onResetService)
        self.station_ws_server.startServiceRequest.connect(self.onStartServiceRequest)
        self.station_ws_server.carNumberSent.connect(self.onCarNumberSent)
        self.station_ws_server.carNumberReceived.connect(self.onCarNumberReceived)
        self.station_ws_server.startGasNozzleRequest.connect(self.onStartGasNozzleRequest)
        self.station_ws_server.startGasNozzle.connect(self.onStartGasNozzle)
        self.station_ws_server.finishGasNozzleRequest.connect(self.onFinishGasNozzleRequest)
        self.station_ws_server.finishGasNozzle.connect(self.onFinishGasNozzle)

        self.bank_client: BankHttpClient = BankHttpClient(self)

        self.bank_client.payResponse.connect(self.onPaymentSuccess)
        self.bank_client.payError.connect(self.onPaymentError)

        self._fuel_type: FuelType | None = None
        self._fuel_amount: int | None = None
        self._car_number: CarNumber | None = None
        self._payment_amount: int | None = None
        self._payment_key: str | None = None
        self._used_bonuses: int | None = None

        self.ui.setCurrentView(ViewName.WAITING)
        self.central_server_ws_client.start()

        self.ui.show()

    def clearInput(self) -> None:
        self._fuel_type = None
        self._fuel_amount = None
        self._car_number = None
        self._payment_amount = None
        self._payment_key = None
        self._used_bonuses = None

        self.ui.fuel_selection_screen.clearInput()
        self.ui.payment_selection_screen.clearInput()

    # ui

    @Slot()
    def onReconnectClicked(self) -> None:
        self.central_server_ws_client.start()

    @Slot()
    def onContinuePaymentClicked(self, data: FuelSelectionData) -> None:
        self._fuel_type = data.fuel_type
        self._fuel_amount = data.fuel_amount

        self.ui.payment_selection_screen.setCurrentPaymentAmount(data.payment_amount)
        self.ui.setCurrentView(ViewName.PAYMENT_SELECTION)

    @Slot()
    def onPayClicked(self, data: PaymentSelectionData) -> None:
        self._used_bonuses = data.used_bonuses
        self._payment_amount = data.payment_amount

        self.ui.setCurrentView(ViewName.PAYMENT_PROCESSING)
        request = PayRequest(
            deposit_card_number=data.card_number,
            deposit_card_expiration_date=self._unformat_expiration_date(data.expiration_date),
            deposit_card_holder_name=data.holder_name,
            payment_amount=data.payment_amount,
        )
        self.bank_client.sendPayRequest(request)

    @Slot()
    def onBackFuelSelectionClicked(self) -> None:
        self.ui.setCurrentView(ViewName.FUEL_SELECTION)

    @Slot()
    def onCancelRefuelingClicked(self) -> None:
        self.ui.setCurrentView(ViewName.FINISH)

    @Slot()
    def onRetryPaymentClicked(self) -> None:
        self.ui.setCurrentView(ViewName.PAYMENT_SELECTION)

    @Slot()
    def onConfirmClicked(self) -> None:
        self.station_ws_server.sendResetServiceRequest()

    # bank http client

    @Slot()
    def onPaymentError(self) -> None:
        self.ui.setCurrentView(ViewName.PAYMENT_ERROR)

    @Slot()
    def onPaymentSuccess(self, response: PayResponse) -> None:
        self._payment_key = response.payment_key

        if (self._fuel_type is None or
            self._fuel_amount is None or
            self._car_number is None or
            self._payment_amount is None or
            self._payment_key is None or
                self._used_bonuses is None):
            print('STATION | error: payment is not full described')
        else:
            message = PaymentSentMessage(
                fuel_type=self._fuel_type,
                fuel_amount=self._fuel_amount,
                car_number=self._car_number,
                payment_amount=self._payment_amount,
                payment_key=self._payment_key,
                used_bonuses=self._used_bonuses
            )
            self.central_server_ws_client.sendPaymentSent(message)

    # central server ws client

    @Slot()
    def onCentralServerConnected(self) -> None:
        self.station_ws_server.start()
        self.ui.setCurrentView(ViewName.WAITING)

    @Slot()
    def onCentralServerDisconnected(self) -> None:
        self.station_ws_server.stop()
        self.ui.setCurrentView(ViewName.RECONNECTION)

    @Slot()
    def onStationNotTaken(self) -> None:
        self.station_ws_server.sendResetService()

    @Slot()
    def onStationTakenOffline(self) -> None:
        self.station_ws_server.sendStartService()

    @Slot()
    def onLoyaltyCardSent(self, message: LoyaltyCardSentMessage) -> None:
        if (message.loyalty_card_available):
            if (message.loyalty_card_holder is None):
                print('STATION | error: loyalty_card_holder not found')
            elif (message.loyalty_card_bonuses is None):
                print('STATION | error: loyalty_card_bonuses not found')
            else:
                self.ui.payment_selection_screen.setLoyaltyCardHolderName(message.loyalty_card_holder)
                self.ui.payment_selection_screen.setCurrentBonuses(message.loyalty_card_bonuses)
                self.ui.payment_selection_screen.showLoyaltyCardForm()

        self.ui.setCurrentView(ViewName.FUEL_SELECTION)

    @Slot()
    def onPaymentReceived(self) -> None:
        self.clearInput()
        self.station_ws_server.sendStartGasNozzleRequest()

    # station ws server

    @Slot()
    def onCameraDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.WAITING)

    @Slot()
    def onGasNozzleDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.WAITING)

    @Slot()
    def onResetServiceRequest(self) -> None:
        self.central_server_ws_client.sendStationNotTakenRequest()

    @Slot()
    def onResetService(self) -> None:
        self.clearInput()
        self.ui.setCurrentView(ViewName.CAMERA_USE)

    @Slot()
    def onStartServiceRequest(self) -> None:
        self.central_server_ws_client.sendStationTakenOfflineRequest()

    @Slot()
    def onCarNumberSent(self, message: CarNumberSentMessage) -> None:
        new_message = CarNumberReceivedMessage(car_number=message.car_number)
        self.station_ws_server.sendCarNumberReceived(new_message)

    @Slot()
    def onCarNumberReceived(self, message: CarNumberReceivedMessage) -> None:
        self.station_ws_server.sendStartStation()
        self._car_number = message.car_number
        new_message = LoyaltyCardAskMessage(car_number=self._car_number)
        self.central_server_ws_client.sendLoyaltyCardAsk(new_message)

    @Slot()
    def onStartGasNozzleRequest(self) -> None:
        self.station_ws_server.sendStartGasNozzle()

    @Slot()
    def onStartGasNozzle(self) -> None:
        self.ui.setCurrentView(ViewName.GAS_NOZZLE_USE)

    @Slot()
    def onFinishGasNozzleRequest(self) -> None:
        self.station_ws_server.sendFinishGasNozzle()

    @Slot()
    def onFinishGasNozzle(self) -> None:
        self.ui.setCurrentView(ViewName.FINISH)

    # misc

    @staticmethod
    def _unformat_expiration_date(expiration_date: str) -> str:
        # MM/yy -> yyyy-MM-01
        return '20' + expiration_date[3:5] + '-' + expiration_date[0:2] + '-01'
