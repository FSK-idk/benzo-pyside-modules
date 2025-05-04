from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

from core.widget.fuel_selection_screen.fuel_selection_screen_ui import FuelSelectionScreenUI

from core.model.fuel_type import FuelType
from core.model.fuel_price_data import FuelPriceData
from core.model.fuel_request import FuelSelectionData


MAX_FUEL_AMOUNT = 99


class FuelSelectionScreen(QObject):
    continuePaymentClicked: Signal = Signal(FuelSelectionData)
    cancelRefuelingClicked: Signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: FuelSelectionScreenUI = FuelSelectionScreenUI(parent)

        self.ui.fuel_amount_spin_box.setMaximum(MAX_FUEL_AMOUNT)

        self.ui.fuel_type_combo_box.currentIndexChanged.connect(self.onFuelTypeChanged)
        self.ui.fuel_amount_spin_box.valueChanged.connect(self.onFuelAmountChanged)
        self.ui.payment_amount_spin_box.valueChanged.connect(self.onPaymentAmountChanged)

        self.ui.continue_payment_button.clicked.connect(self.onContinueClicked)
        self.ui.cancel_refueling_button.clicked.connect(self.cancelRefuelingClicked.emit)

        self._price: int = 0
        self._fuel_price_data: FuelPriceData = FuelPriceData(price={})

        self.ui.show()

    def setFuelPriceData(self, fuel_price_data: FuelPriceData) -> None:
        self._fuel_price_data = fuel_price_data

        self.ui.fuel_type_combo_box.clear()
        self.ui.fuel_type_combo_box.setCurrentText('')
        for k, v in self._fuel_price_data.price.items():
            self.ui.fuel_type_combo_box.addItem(k.value)

        self.onFuelTypeChanged()

    def clearInput(self) -> None:
        self.setFuelPriceData(FuelPriceData(price={}))
        self.ui.fuel_amount_spin_box.setValue(0)
        self.ui.payment_amount_spin_box.setValue(0)

    def setCurrentPrice(self, price: int) -> None:
        self._price = price
        self.ui.price_label.setText(f'Цена: {self._fromat_money(self._price)} руб.')
        self.ui.payment_amount_spin_box.setMaximum(self._fromat_money(self._price) * MAX_FUEL_AMOUNT)
        self.onFuelAmountChanged()

    def onFuelTypeChanged(self) -> None:
        if (self.ui.fuel_type_combo_box.currentText() != ''):
            fuel_type = FuelType(self.ui.fuel_type_combo_box.currentText())
            self.setCurrentPrice(self._fuel_price_data.price[fuel_type])

    def onFuelAmountChanged(self) -> None:
        fuel_amount = self.ui.fuel_amount_spin_box.value()
        self.ui.payment_amount_spin_box.blockSignals(True)
        self.ui.payment_amount_spin_box.setValue(fuel_amount * self._fromat_money(self._price))
        self.ui.payment_amount_spin_box.blockSignals(False)

    def onPaymentAmountChanged(self) -> None:
        payment_amount = self.ui.payment_amount_spin_box.value()
        self.ui.fuel_amount_spin_box.blockSignals(True)
        self.ui.fuel_amount_spin_box.setValue(payment_amount / self._fromat_money(self._price))
        self.ui.fuel_amount_spin_box.blockSignals(False)

    def onContinueClicked(self) -> None:
        is_valid = True

        if (self.ui.fuel_amount_spin_box.value() == 0):
            self.ui.fuel_amount_error_label.setHidden(False)
            is_valid = False
        else:
            self.ui.fuel_amount_error_label.setHidden(True)

        if (self.ui.payment_amount_spin_box.value() == 0):
            self.ui.payment_amount_error_label.setHidden(False)
            is_valid = False
        else:
            self.ui.payment_amount_error_label.setHidden(True)

        if (is_valid):
            data = FuelSelectionData(
                fuel_type=FuelType(self.ui.fuel_type_combo_box.currentText()),
                fuel_amount=self._unfromat_money(self.ui.fuel_amount_spin_box.value()),
                payment_amount=self._unfromat_money(self.ui.payment_amount_spin_box.value()),
            )
            self.continuePaymentClicked.emit(data)

    @staticmethod
    def _fromat_money(price: int) -> float:
        return price / 100

    @staticmethod
    def _unfromat_money(price: float) -> int:
        return int(price * 100)
