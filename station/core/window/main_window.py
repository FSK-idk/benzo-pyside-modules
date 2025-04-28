from PySide6.QtCore import QObject, Slot

from core.window.main_window_ui import MainWindowUI, ViewName

from core.widget.fuel_selection_screen.fuel_selection_screen import FuelSelectionData

from core.model.car_number import CarNumber
from core.model.pay_request import PayRequest
from core.model.pay_response import PayResponse
from core.model.payment_selection_data import PaymentSelectionData

from core.net.server import Server
from core.net.bank_client import BankClient


class MainWindow(QObject):
    def __init__(self) -> None:
        super().__init__()

        self.ui: MainWindowUI = MainWindowUI()

        self.car_number: CarNumber | None = None

        self.ui.fuel_selection_screen.continuePaymentClicked.connect(self.onContinuePaymentClicked)
        self.ui.fuel_selection_screen.cancelRefuelingClicked.connect(self.onCancelRefuelingClicked)
        self.ui.payment_selection_screen.payClicked.connect(self.onPayClicked)
        self.ui.payment_selection_screen.backFuelSelectionClicked.connect(self.onBackFuelSelectionClicked)
        self.ui.payment_selection_screen.cancelRefuelingClicked.connect(self.onCancelRefuelingClicked)
        self.ui.payment_error_screen.retryPaymentClicked.connect(self.onRetryPaymentClicked)
        self.ui.finish_screen.confirmClicked.connect(self.onConfirmClicked)

        self.ui.setCurrentView(ViewName.WAITING)

        self.server: Server = Server(self)

        self.camera_available: bool = False
        self.gas_nozzle_available: bool = False

        self.server.startService.connect(self.onStartService)
        self.server.resetService.connect(self.onResetService)
        self.server.carNumberReceived.connect(self.onCarNumberReceived)
        self.server.gasNozzleFinished.connect(self.onGasNozzleFinished)
        self.server.cameraConnected.connect(self.onCameraConnected)
        self.server.cameraDisconnected.connect(self.onCameraDisconnected)
        self.server.gasNozzleConnected.connect(self.onGasNozzleConnected)
        self.server.gasNozzleDisconnected.connect(self.onGasNozzleDisconnected)

        self.server.startServer()

        self.bank_client: BankClient = BankClient(self)

        self.bank_client.payResponse.connect(self.onPaymentResponse)
        self.bank_client.payError.connect(self.onPaymentError)

        self.ui.show()

    def clearInput(self) -> None:
        self.car_number = None
        self.ui.fuel_selection_screen.clearInput()
        self.ui.payment_selection_screen.clearInput()

    @Slot()
    def onContinuePaymentClicked(self, request: FuelSelectionData) -> None:
        self.ui.payment_selection_screen.setCurrentPaymentAmount(request.payment_amount)
        self.ui.setCurrentView(ViewName.PAYMENT_SELECTION)

    @Slot()
    def onPayClicked(self, result: PaymentSelectionData) -> None:
        request = PayRequest(
            deposit_card_number=result.card_number,
            deposit_card_expiration_date=self._unformat_expiration_date(result.expiration_date),
            deposit_card_holder_name=result.holder_name,
            payment_amount=result.payment_amount,
        )
        self.bank_client.sendPayRequest(request)
        self.ui.setCurrentView(ViewName.PAYMENT_PROCESSING)

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
        self.onResetService()

    @Slot()
    def onPaymentError(self) -> None:
        self.ui.setCurrentView(ViewName.PAYMENT_ERROR)

    @Slot()
    def onPaymentResponse(self, response: PayResponse) -> None:

        # TODO: decrease used bonuses
        # TODO: save payment on central server

        self.clearInput()
        self.ui.setCurrentView(ViewName.GAS_NOZZLE_USE)

        self.server.sendStartGasNozzle()

    @Slot()
    def onStartService(self) -> None:
        # TODO: set station taken-offline

        self.server.sendStartService()

    @Slot()
    def onResetService(self) -> None:
        self.clearInput()
        self.ui.setCurrentView(ViewName.CAMERA_USE)

        self.server.sendResetService()

    @Slot()
    def onCarNumberReceived(self, car_number: CarNumber) -> None:
        self.car_number = car_number

        # TODO: check if bonuses available
        loyalty_card_avaliable: bool = True
        loyalty_card_holder: str = 'Your Name'
        loyalty_card_bonuses: float = 33265

        if (loyalty_card_avaliable):
            self.ui.payment_selection_screen.setLoyaltyCardHolderName(loyalty_card_holder)
            self.ui.payment_selection_screen.setCurrentBonuses(loyalty_card_bonuses)
            self.ui.payment_selection_screen.showLoyaltyCardForm()

        self.ui.setCurrentView(ViewName.FUEL_SELECTION)

        self.server.sendCarNumberReceived(car_number)

    @Slot()
    def onGasNozzleFinished(self) -> None:
        self.ui.setCurrentView(ViewName.FINISH)
        self.server.sendGasNozzleFinished()

    @Slot()
    def onCameraConnected(self) -> None:
        print('DBG: camera connected')
        self.server.sendCameraConnected()
        self.camera_available = True
        if (self.gas_nozzle_available):
            self.onResetService()

    @Slot()
    def onCameraDisconnected(self) -> None:
        print('DBG: camera disconnected')
        self.camera_available = False
        self.ui.setCurrentView(ViewName.WAITING)

    @Slot()
    def onGasNozzleConnected(self) -> None:
        print('DBG: gas nozzle connected')
        self.server.sendGasNozzleConnected()
        self.gas_nozzle_available = True
        if (self.camera_available):
            self.onResetService()

    @Slot()
    def onGasNozzleDisconnected(self) -> None:
        print('DBG: gas nozzle disconnected')
        self.gas_nozzle_available = False
        self.ui.setCurrentView(ViewName.WAITING)

    @staticmethod
    def _unformat_expiration_date(expiration_date: str) -> str:
        # MM/yy -> yyyy-MM-01
        return '20' + expiration_date[3:5] + '-' + expiration_date[0:2] + '-01'
