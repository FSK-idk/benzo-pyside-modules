from PySide6.QtCore import QObject, Slot

from core.window.main_window_ui import MainWindowUI, ViewName

from core.model.fuel_type import FuelType
from core.widget.fuel_selection_screen.fuel_selection_screen import FuelSelectionData
from core.model.payment_selection_data import PaymentSelectionData

from core.model import bank_api
from core.model import central_server_api

from core.net.net import Net


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
        self.ui.central_server_reconnection_screen.reconnectClicked.connect(self.onReconnectClicked)

        self._net: Net = Net(self)

        self._net.centralServerDisconnected.connect(self.onCentralServerDisconnected)
        self._net.reset.connect(self.onReset)
        self._net.stationUsedT1.connect(self.onStationUsedT1)
        self._net.paymentError.connect(self.onPaymentError)
        self._net.paymentSuccess.connect(self.onPaymentSuccess)
        self._net.componentConnection.connect(self.onComponentConnection)
        self._net.refuelingCanceled.connect(self.onRefuelingCanceled)
        self._net.stationUsedT2.connect(self.onStationUsedT2)
        self._net.gasNozzleUsed.connect(self.onGasNozzleUsed)
        self._net.mobileAppUsed.connect(self.onMobileAppUsed)

        self._fuel_type: FuelType | None = None
        self._fuel_amount: int | None = None
        self._payment_amount: int | None = None
        self._used_bonuses: int | None = None

        self.ui.setCurrentView(ViewName.CENTRAL_SERVER_RECONNECTION)
        self._net.connectCentralServer()

        self.ui.show()

    def clearInput(self) -> None:
        self._fuel_type = None
        self._fuel_amount = None
        self._payment_amount = None
        self._used_bonuses = None

        self._net.car_number = None
        self._net.fuelPriceDataSent = None
        self._net.loyaltyCardSent = None

        self.ui.fuel_selection_screen.clearInput()
        self.ui.payment_selection_screen.clearInput()

    @Slot()
    def onReconnectClicked(self) -> None:
        self._net.connectCentralServer()

    @Slot()
    def onCentralServerDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.CENTRAL_SERVER_RECONNECTION)

    @Slot()
    def onReset(self) -> None:
        self.clearInput()
        self.ui.setCurrentView(ViewName.CAMERA_USE)

    @Slot()
    def onStationUsedT1(self) -> None:
        fuelPriceDataSent = self._net.fuelPriceDataSent
        if (fuelPriceDataSent is not None):
            self.ui.fuel_selection_screen.setFuelPriceData(fuelPriceDataSent.fuel_price_data)
        else:
            print('STATION | error: no fuel price data sent')

        loyaltyCardSent = self._net.loyaltyCardSent
        if (loyaltyCardSent is not None):
            if (loyaltyCardSent.loyalty_card_available):
                if (loyaltyCardSent.loyalty_card_holder is None):
                    print('STATION | error: loyalty_card_holder not found')
                elif (loyaltyCardSent.loyalty_card_bonuses is None):
                    print('STATION | error: loyalty_card_bonuses not found')
                else:
                    self.ui.payment_selection_screen.setLoyaltyCardHolderName(loyaltyCardSent.loyalty_card_holder)
                    self.ui.payment_selection_screen.setCurrentBonuses(loyaltyCardSent.loyalty_card_bonuses)
                    self.ui.payment_selection_screen.showLoyaltyCardForm()
        else:
            print('STATION | error: no loyalty card sent')

        self.ui.setCurrentView(ViewName.FUEL_SELECTION)

    @Slot()
    def onCancelRefuelingClicked(self) -> None:
        self._net.cancelRefueling()

    @Slot()
    def onContinuePaymentClicked(self, data: FuelSelectionData) -> None:
        self._fuel_type = data.fuel_type
        self._fuel_amount = data.fuel_amount

        self.ui.payment_selection_screen.setCurrentPaymentAmount(data.payment_amount)
        self.ui.setCurrentView(ViewName.PAYMENT_SELECTION)

    @Slot()
    def onBackFuelSelectionClicked(self) -> None:
        self.ui.setCurrentView(ViewName.FUEL_SELECTION)

    @Slot()
    def onPayClicked(self, data: PaymentSelectionData) -> None:
        self._used_bonuses = data.used_bonuses
        self._payment_amount = data.payment_amount

        self.ui.setCurrentView(ViewName.PAYMENT_PROCESSING)
        request = bank_api.PayRequest(
            deposit_card_number=data.card_number,
            deposit_card_expiration_date=self._unformat_expiration_date(data.expiration_date),
            deposit_card_holder_name=data.holder_name,
            payment_amount=data.payment_amount,
        )
        self._net.payRequest(request)

    @Slot()
    def onPaymentError(self) -> None:
        self.ui.setCurrentView(ViewName.PAYMENT_ERROR)

    @Slot()
    def onRetryPaymentClicked(self) -> None:
        self.ui.setCurrentView(ViewName.PAYMENT_SELECTION)

    @Slot()
    def onPaymentSuccess(self, message: bank_api.PayResponse) -> None:
        car_number = self._net.car_number

        if (car_number is None):
            print('STATION | error: car number not found')
        elif (self._fuel_type is None or
              self._fuel_amount is None or
              self._payment_amount is None or
              self._used_bonuses is None):
            print('STATION | error: payment is not full described')
        else:
            new_message = central_server_api.SavePaymentMessage(
                fuel_type=self._fuel_type,
                fuel_amount=self._fuel_amount,
                car_number=car_number,
                payment_amount=self._payment_amount,
                payment_key=message.payment_key,
                used_bonuses=self._used_bonuses
            )
            self._net.savePayment(new_message)

        self.clearInput()

    @Slot()
    def onComponentConnection(self) -> None:
        self.ui.setCurrentView(ViewName.COMPONENT_CONNECTION)

    @Slot()
    def onRefuelingCanceled(self) -> None:
        self.ui.setCurrentView(ViewName.FINISH)

    @Slot()
    def onStationUsedT2(self) -> None:
        self.ui.setCurrentView(ViewName.FINISH)

    @Slot()
    def onConfirmClicked(self) -> None:
        self._net.endService()

    @Slot()
    def onGasNozzleUsed(self) -> None:
        self.ui.setCurrentView(ViewName.GAS_NOZZLE_USE)

    @Slot()
    def onMobileAppUsed(self) -> None:
        self.ui.setCurrentView(ViewName.MOBILE_APP_USE)

    @staticmethod
    def _unformat_expiration_date(expiration_date: str) -> str:
        # MM/yy -> yyyy-MM-01
        return '20' + expiration_date[3:5] + '-' + expiration_date[0:2] + '-01'
