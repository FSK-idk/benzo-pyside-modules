from PySide6.QtCore import QObject, Slot

from core.window.main_window_ui import MainWindowUI, ViewName

from core.model.car_number import CarNumber

from core.net.client import Client


class MainWindow(QObject):
    def __init__(self) -> None:
        super().__init__()

        self.ui: MainWindowUI = MainWindowUI()

        self.ui.start_screen.startClicked.connect(self.onStartClicked)
        self.ui.refueling_screen.refuelingFinished.connect(self.onRefuelingFinished)
        self.ui.finish_screen.confirmClicked.connect(self.onConfirmClicked)
        self.ui.reconnection_screen.reconnectClicked.connect(self.onReconnectClicked)

        self.ui.setCurrentView(ViewName.WAITING)

        self.client: Client = Client(self)

        self.client.connected.connect(self.onConnected)
        self.client.disconnected.connect(self.onDisconnected)
        self.client.resetService.connect(self.onResetService)
        self.client.carNumberReceived.connect(self.onCarNumberReceived)
        self.client.startGasNozzle.connect(self.onStartGasNozzle)
        self.client.gasNozzleFinished.connect(self.onGasNozzleFinished)
        self.client.cameraDisconnected.connect(self.onCameraDisconnected)
        self.client.gasNozzleConnected.connect(self.onGasNozzleConnected)

        self.client.startClient()

        self.ui.show()

    @Slot()
    def clearInput(self) -> None:
        self.ui.refueling_screen.clearInput()

    @Slot()
    def onStartClicked(self) -> None:
        self.ui.setCurrentView(ViewName.REFUELING)
        self.ui.refueling_screen.start()

    @Slot()
    def onRefuelingFinished(self) -> None:
        self.ui.setCurrentView(ViewName.FINISH)

    @Slot()
    def onConfirmClicked(self) -> None:
        self.clearInput()
        self.client.sendGasNozzleFinished()

    @Slot()
    def onReconnectClicked(self) -> None:
        self.client.startClient()

    @Slot()
    def onConnected(self) -> None:
        self.client.sendConnect()

    @Slot()
    def onDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.RECONNECTION)

    @Slot()
    def onResetService(self) -> None:
        self.clearInput()
        self.ui.setCurrentView(ViewName.CAMERA_USE)

    @Slot()
    def onCarNumberReceived(self, car_number: CarNumber) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)

    @Slot()
    def onStartGasNozzle(self) -> None:
        self.ui.setCurrentView(ViewName.START)

    @Slot()
    def onGasNozzleFinished(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)

    @Slot()
    def onCameraDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.WAITING)

    @Slot()
    def onGasNozzleConnected(self) -> None:
        self.ui.setCurrentView(ViewName.WAITING)
