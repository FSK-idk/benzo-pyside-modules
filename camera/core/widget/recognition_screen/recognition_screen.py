from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

from core.widget.recognition_screen.recognition_screen_ui import RecognitionScreenUI

from core.model.car_number import CarNumber


class RecognitionScreen(QObject):
    confirmClicked: Signal = Signal(CarNumber)
    changeClicked: Signal = Signal(CarNumber)
    cancelRefuelingClicked: Signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: RecognitionScreenUI = RecognitionScreenUI(parent)

        self.ui.confirm_button.clicked.connect(self.onConfirmClicked)
        self.ui.change_button.clicked.connect(self.onChangeClicked)
        self.ui.cancel_refueling_button.clicked.connect(self.cancelRefuelingClicked.emit)

        self.ui.show()

    def setCarNumber(self, car_number: CarNumber):
        self.ui.car_number_label.setText(car_number.text)

    def clearInput(self) -> None:
        self.ui.car_number_label.setText('')

    def onConfirmClicked(self) -> None:
        car_number: CarNumber = CarNumber(text=self.ui.car_number_label.text())
        self.confirmClicked.emit(car_number)

    def onChangeClicked(self) -> None:
        car_number: CarNumber = CarNumber(text=self.ui.car_number_label.text())
        self.changeClicked.emit(car_number)
