from PySide6.QtCore import QObject, Slot

from core.window.main_window_ui import MainWindowUI, ViewName

from core.net.net import Net


class MainWindow(QObject):
    def __init__(self) -> None:
        super().__init__()

        self.ui: MainWindowUI = MainWindowUI()

        self.ui.start_screen.startClicked.connect(self.onStartClicked)
        self.ui.refueling_screen.refuelingFinished.connect(self.onRefuelingFinished)
        self.ui.finish_screen.confirmClicked.connect(self.onConfirmClicked)
        self.ui.station_server_reconnection_screen.reconnectClicked.connect(self.onReconnectClicked)

        self._net: Net = Net(self)

        self._net.stationServerDisconnected.connect(self.onStationServerDisconnected)
        self._net.reset.connect(self.onReset)
        self._net.gasNozzleUsed.connect(self.onGasNozzleUsed)
        self._net.componentConnection.connect(self.onComponentConnection)
        self._net.stationUsed.connect(self.onStationUsed)
        self._net.mobileAppUsed.connect(self.onMobileAppUsed)

        self.ui.setCurrentView(ViewName.STATION_SERVER_RECONNECTION)
        self._net.connectStationServer()

        self.ui.show()

    @Slot()
    def clearInput(self) -> None:
        self.ui.refueling_screen.clearInput()

    @Slot()
    def onReconnectClicked(self) -> None:
        self._net.connectStationServer()

    @Slot()
    def onStationServerDisconnected(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_SERVER_RECONNECTION)

    @Slot()
    def onReset(self) -> None:
        self.clearInput()
        self.ui.setCurrentView(ViewName.CAMERA_USE)

    @Slot()
    def onGasNozzleUsed(self) -> None:
        self.ui.setCurrentView(ViewName.START)

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
        self._net.finish()

    @Slot()
    def onComponentConnection(self) -> None:
        self.ui.setCurrentView(ViewName.COMPONENT_CONNECTION)

    @Slot()
    def onStationUsed(self) -> None:
        self.ui.setCurrentView(ViewName.STATION_USE)

    @Slot()
    def onMobileAppUsed(self) -> None:
        self.ui.setCurrentView(ViewName.MOBILE_APP_USE)
