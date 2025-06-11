from PySide6.QtCore import QObject, Signal

from core.model import station_api
from core.model import central_server_api
from core.model import bank_api
from core.net.station_server import StationServer
from core.net.central_server_client import CentralServerClient
from core.net.bank_client import BankClient

from core.model.car_number import CarNumber


class Net(QObject):
    componentConnection: Signal = Signal()
    centralServerDisconnected: Signal = Signal()
    reset: Signal = Signal()
    refuelingCanceled: Signal = Signal()
    stationUsedT1: Signal = Signal()
    stationUsedT2: Signal = Signal()
    gasNozzleUsed: Signal = Signal()
    mobileAppUsed: Signal = Signal()
    paymentError: Signal = Signal()
    paymentSuccess: Signal = Signal(bank_api.PayResponse)

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        self.car_number: CarNumber | None = None
        self.fuelPriceDataSent: central_server_api.FuelPriceDataSentMessage | None = None
        self.loyaltyCardSent: central_server_api.LoyaltyCardSentMessage | None = None

        self._station_server: StationServer = StationServer(self)
        self._central_server_client: CentralServerClient = CentralServerClient(self)
        self._bank_client: BankClient = BankClient(self)

        self._central_server_client.connected.connect(self._station_server.start)
        self._central_server_client.connected.connect(self.componentConnection.emit)

        self._station_server.serviceNotReady.connect(self._central_server_client.sendServiceNotReady)
        self._station_server.serviceNotReady.connect(self.componentConnection.emit)

        self._central_server_client.disconnected.connect(self.onCentralServerDisonnected)

        self._station_server.serviceReady.connect(self._central_server_client.sendServiceReady)
        self._station_server.serviceReady.connect(self.reset.emit)

        self._station_server.serviceStarted.connect(self._central_server_client.sendServiceStarted)

        self._station_server.useStationT1.connect(self.onUseStationT1)

        self._central_server_client.fuelPriceDataSent.connect(self.onFuelPriceDataSent)
        self._central_server_client.loyaltyCardSent.connect(self.onLoyaltyCardSent)

        self._station_server.stationUsedT2.connect(self.stationUsedT2.emit)

        self._station_server.refuelingCanceled.connect(self.refuelingCanceled.emit)

        self._bank_client.payError.connect(self.paymentError.emit)

        self._bank_client.paymentSuccess.connect(self.onPaymentSuccess)

        self._central_server_client.gasNozzleUsedT2.connect(self.gasNozzleUsed.emit)
        self._central_server_client.gasNozzleUsedT2.connect(self._station_server.sendGasNozzleUsedT2)

        self._station_server.mobileAppUsedT2.connect(self.mobileAppUsed.emit)

        self._central_server_client.mobileAppUsedT1.connect(self.useMobileApp)

        self._central_server_client.mobileAppServiceEnded.connect(self.reset)
        self._central_server_client.mobileAppServiceEnded.connect(self._station_server.sendServiceEnded)

    def connectCentralServer(self) -> None:
        self._central_server_client.start()

    def onCentralServerDisonnected(self) -> None:
        self._station_server.stop()
        self.centralServerDisconnected.emit()

    def endService(self) -> None:
        self._station_server.sendServiceEnded()
        self._central_server_client.sendServiceEnded()
        self.reset.emit()

    def onUseStationT1(self, message: station_api.UseStationT1Message) -> None:
        self.car_number = message.car_number
        self._central_server_client.sendFuelPriceDataAsk()
        self._central_server_client.sendLoyaltyCardAsk(self.car_number)

    def onFuelPriceDataSent(self, message: central_server_api.FuelPriceDataSentMessage) -> None:
        self.fuelPriceDataSent = message
        if (self.loyaltyCardSent is not None):
            self._station_server.sendStationUsedT1()
            self.stationUsedT1.emit()

    def onLoyaltyCardSent(self, message: central_server_api.LoyaltyCardSentMessage) -> None:
        self.loyaltyCardSent = message
        if (self.fuelPriceDataSent is not None):
            self._station_server.sendStationUsedT1()
            self.stationUsedT1.emit()

    def cancelRefueling(self) -> None:
        self.refuelingCanceled.emit()
        self._station_server.sendRefuelingCanceled()

    def payRequest(self, message: bank_api.PayRequest) -> None:
        self._bank_client.sendPayRequest(message)

    def onPaymentSuccess(self, message: bank_api.PayResponse) -> None:
        self.paymentSuccess.emit(message)
        self.gasNozzleUsed.emit()
        self._station_server.sendGasNozzleUsedT1()

    def savePayment(self, message: central_server_api.SavePaymentMessage) -> None:
        self._central_server_client.sendSavePayment(message)

    def useMobileApp(self) -> None:
        self.mobileAppUsed.emit()
        self._station_server.sendMobileAppUsedT1()
