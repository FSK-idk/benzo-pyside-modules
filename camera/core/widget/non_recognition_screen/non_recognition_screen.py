from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal, QRegularExpression

from core.widget.non_recognition_screen.non_recognition_screen_ui import NonRecognitionScreenUI

from core.model.car_number import CarNumber


CAR_NUMBER_REGEX: str = r'^(([АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{1,2})(\d{2,3})|(\d{4}(?<!0000)[АВЕКМНОРСТУХ]{2})(\d{2})|(\d{3}(?<!000)(C?D|[ТНМВКЕ])\d{3}(?<!000))(\d{2}(?<!00))|([ТСК][АВЕКМНОРСТУХ]{2}\d{3}(?<!000))(\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}(?<!000)[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]\d{4}(?<!0000))(\d{2})|(\d{3}(?<!000)[АВЕКМНОРСТУХ])(\d{2})|(\d{4}(?<!0000)[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]{2}\d{4}(?<!0000))(\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}(?<!000))(\d{2,3})|(^Т[АВЕКМНОРСТУХ]{2}\d{3}(?<!000)\d{2,3}))$'


class NonRecognitionScreen(QObject):
    confirmClicked: Signal = Signal(CarNumber)
    cancelRefuelingClicked: Signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: NonRecognitionScreenUI = NonRecognitionScreenUI(parent)

        self.ui.confirm_button.clicked.connect(self.onConfirmClicked)
        self.ui.cancel_refueling_button.clicked.connect(self.cancelRefuelingClicked.emit)

        self.regex = QRegularExpression(CAR_NUMBER_REGEX)

        self.ui.show()

    def setCarNumber(self, car_number: CarNumber):
        self.ui.car_number_line_edit.setText(car_number.text)

    def clearInput(self) -> None:
        self.ui.car_number_line_edit.setText('')

    def onConfirmClicked(self) -> None:
        car_number: CarNumber = CarNumber(text=self.ui.car_number_line_edit.text())

        match = self.regex.match(car_number.text)
        if (match.hasMatch()):
            self.ui.car_number_error_label.setHidden(True)
            self.confirmClicked.emit(car_number)
        else:
            self.ui.car_number_error_label.setHidden(False)
