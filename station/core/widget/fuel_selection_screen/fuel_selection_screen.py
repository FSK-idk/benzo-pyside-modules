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

        self.ui.fuel_type_combo_box.addItem(FuelType.FT_92.value)
        self.ui.fuel_type_combo_box.addItem(FuelType.FT_95.value)
        self.ui.fuel_type_combo_box.addItem(FuelType.FT_98.value)
        self.ui.fuel_type_combo_box.addItem(FuelType.FT_DT.value)

        self.ui.fuel_amount_spin_box.setMaximum(MAX_FUEL_AMOUNT)

        self.ui.fuel_type_combo_box.currentIndexChanged.connect(self.onFuelTypeChanged)
        self.ui.fuel_amount_spin_box.valueChanged.connect(self.onFuelAmountChanged)
        self.ui.payment_amount_spin_box.valueChanged.connect(self.onPaymentAmountChanged)

        self.ui.continue_payment_button.clicked.connect(self.onContinueClicked)
        self.ui.cancel_refueling_button.clicked.connect(self.cancelRefuelingClicked.emit)

        self._price: int = 0
        self._fuel_price_data: FuelPriceData = FuelPriceData(
            price={
                FuelType.FT_92: 5962,
                FuelType.FT_95: 6153,
                FuelType.FT_98: 7680,
                FuelType.FT_DT: 7628,
            }
        )

        self.onFuelTypeChanged()

        self.ui.show()

    def setFuelPriceData(self, fuel_price_data: FuelPriceData) -> None:
        self._fuel_price_data = fuel_price_data

    def clearInput(self) -> None:
        self.ui.fuel_type_combo_box.setCurrentIndex(0)
        self.ui.fuel_amount_spin_box.setValue(0)
        self.ui.payment_amount_spin_box.setValue(0)

    def setCurrentPrice(self, price: int) -> None:
        self._price = price
        self.ui.price_label.setText(f'Цена: {self._fromat_money(self._price)} руб.')
        self.ui.payment_amount_spin_box.setMaximum(self._fromat_money(self._price) * MAX_FUEL_AMOUNT)
        self.onFuelAmountChanged()

    def onFuelTypeChanged(self) -> None:
        match FuelType(self.ui.fuel_type_combo_box.currentText()):
            case FuelType.FT_92:
                self.setCurrentPrice(self._fuel_price_data.price[FuelType.FT_92])
            case FuelType.FT_95:
                self.setCurrentPrice(self._fuel_price_data.price[FuelType.FT_95])
            case FuelType.FT_98:
                self.setCurrentPrice(self._fuel_price_data.price[FuelType.FT_98])
            case FuelType.FT_DT:
                self.setCurrentPrice(self._fuel_price_data.price[FuelType.FT_DT])

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
