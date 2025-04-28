from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

from core.widget.payment_selection_screen.payment_selection_screen_ui import PaymentSelectionScreenUI

from core.model.payment_selection_data import PaymentSelectionData


class PaymentSelectionScreen(QObject):
    payClicked: Signal = Signal(PaymentSelectionData)
    backFuelSelectionClicked: Signal = Signal()
    cancelRefuelingClicked: Signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: PaymentSelectionScreenUI = PaymentSelectionScreenUI(parent)

        self.ui.using_bonuses_spin_box.valueChanged.connect(self.onBonusesUsedChanged)

        self.ui.pay_button.clicked.connect(self.onPayClicked)
        self.ui.cancel_refueling_button.clicked.connect(self.cancelRefuelingClicked.emit)
        self.ui.back_fuel_selection_button.clicked.connect(self.backFuelSelectionClicked.emit)

        self._bonuses: int = 0
        self._payment_amount: int = 0

        self.setCurrentBonuses(0)
        self.setCurrentPaymentAmount(0)

        self.ui.show()

    def setLoyaltyCardHolderName(self, name: str) -> None:
        self.ui.loyalty_card_label.setText(f'Карта лояльности ({name})')

    def setCurrentBonuses(self, bonuses: int) -> None:
        self._bonuses = bonuses
        self.ui.bonuses_label.setText(f'Бонусы: {self._fromat_money(self._bonuses)} руб.')

    def setCurrentPaymentAmount(self, payment_amount: int) -> None:
        self._payment_amount = payment_amount
        self.ui.payment_amount_label.setText(f'К оплате: {self._fromat_money(self._payment_amount)} руб.')
        self.ui.using_bonuses_spin_box.setMaximum(self._fromat_money(min(self._bonuses, self._payment_amount)))

    def showLoyaltyCardForm(self) -> None:
        self.ui.loyalty_card_widget.setHidden(False)

    def hideLoyaltyCardForm(self) -> None:
        self.ui.loyalty_card_widget.setHidden(True)

    def clearInput(self) -> None:
        self.setLoyaltyCardHolderName('')
        self.setCurrentBonuses(0)
        self.setCurrentPaymentAmount(0)
        self.ui.using_bonuses_spin_box.setValue(0)
        self.ui.bank_card_number_line_edit.setText('')
        self.ui.expiration_month_line_edit.setText('')
        self.ui.expiration_year_line_edit.setText('')
        self.ui.holder_name_line_edit.setText('')
        self.ui.bank_card_number_error_label.setHidden(True)
        self.ui.expiration_date_error_label.setHidden(True)
        self.ui.holder_name_error_label.setHidden(True)
        self.hideLoyaltyCardForm()

    def onBonusesUsedChanged(self) -> None:
        bonuses_used = self._unfromat_money(self.ui.using_bonuses_spin_box.value())
        self.ui.payment_amount_label.setText(
            f'К оплате: {self._fromat_money(self._payment_amount - bonuses_used)} руб.')

    def onPayClicked(self) -> None:
        is_valid: bool = True

        if (not self.ui.bank_card_number_line_edit.hasAcceptableInput()):
            self.ui.bank_card_number_error_label.setHidden(False)
            is_valid = False
        else:
            self.ui.bank_card_number_error_label.setHidden(True)

        if (not self.ui.expiration_month_line_edit.hasAcceptableInput() or not self.ui.expiration_year_line_edit.hasAcceptableInput()):
            self.ui.expiration_date_error_label.setHidden(False)
            is_valid = False
        else:
            self.ui.expiration_date_error_label.setHidden(True)

        if (self.ui.holder_name_line_edit.text() == ''):
            self.ui.holder_name_error_label.setHidden(False)
            is_valid = False
        else:
            self.ui.holder_name_error_label.setHidden(True)

        if (is_valid):
            data = PaymentSelectionData(
                used_bonuses=self._unfromat_money(self.ui.using_bonuses_spin_box.value()),
                payment_amount=self._payment_amount - self._unfromat_money(self.ui.using_bonuses_spin_box.value()),
                card_number=self.ui.bank_card_number_line_edit.text().replace(' ', ''),
                expiration_date=self.ui.expiration_month_line_edit.text() + '/' + self.ui.expiration_year_line_edit.text(),
                holder_name=self.ui.holder_name_line_edit.text()
            )
            self.payClicked.emit(data)

    @staticmethod
    def _fromat_money(price: int) -> float:
        return price / 100

    @staticmethod
    def _unfromat_money(price: float) -> int:
        return int(price * 100)
