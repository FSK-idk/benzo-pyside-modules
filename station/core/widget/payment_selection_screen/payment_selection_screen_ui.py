from PySide6.QtWidgets import QWidget, QPushButton, QSizePolicy, QGridLayout, QDoubleSpinBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QSpacerItem
from PySide6.QtGui import QFont, QRegularExpressionValidator
from PySide6.QtCore import Qt, QRegularExpression

from core.style import qss

from core.widget.payment_selection_screen.holder_name_validator import HolderNameValidator


class PaymentSelectionScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # title

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Оплата')
        self.title_label.setStyleSheet(qss.title)

        # loyalty card

        self.loyalty_card_label: QLabel = QLabel(self)
        self.loyalty_card_label.setText('Карта лояльности (Name Name)')
        self.loyalty_card_label.setStyleSheet(qss.heading1)

        # using bonuses

        self.using_bonuses_label: QLabel = QLabel(self)
        self.using_bonuses_label.setText('Использовать бонусы')
        self.using_bonuses_label.setStyleSheet(qss.heading2)

        self.using_bonuses_spin_box: QDoubleSpinBox = QDoubleSpinBox(self)
        self.using_bonuses_spin_box.setFixedSize(400, 50)
        self.using_bonuses_spin_box.setSuffix(' руб.')
        self.using_bonuses_spin_box.setStyleSheet(qss.double_spin_box2)
        self.using_bonuses_spin_box.editingFinished.connect(self.using_bonuses_spin_box.clearFocus)

        self.bonuses_label: QLabel = QLabel(self)
        self.bonuses_label.setText('Бонусы: 0.00 руб.')
        self.bonuses_label.setStyleSheet(qss.heading2)

        # bonuses form

        bonuses_form_layout = QGridLayout()
        bonuses_form_layout.setColumnMinimumWidth(0, 300)
        bonuses_form_layout.setRowMinimumHeight(1, 30)
        bonuses_form_layout.setRowMinimumHeight(3, 30)
        bonuses_form_layout.setSpacing(0)
        bonuses_form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        bonuses_form_layout.addWidget(
            self.loyalty_card_label, 0, 0, 1, 2,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )

        bonuses_form_layout.addWidget(
            self.using_bonuses_label, 2, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        bonuses_form_layout.addWidget(
            self.using_bonuses_spin_box, 2, 1,
            alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter,
        )

        bonuses_form_layout.addWidget(
            self.bonuses_label, 4, 1,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )

        self.loyalty_card_widget: QWidget = QWidget(self)
        self.loyalty_card_widget.setLayout(bonuses_form_layout)
        self.loyalty_card_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # bank card

        self.bank_card_label: QLabel = QLabel(self)
        self.bank_card_label.setText('Банковкая карта')
        self.bank_card_label.setStyleSheet(qss.heading1)

        # card number

        self.bank_card_number_label: QLabel = QLabel(self)
        self.bank_card_number_label.setText('Номер карты')
        self.bank_card_number_label.setStyleSheet(qss.heading2)

        self.bank_card_number_line_edit: QLineEdit = QLineEdit(self)
        self.bank_card_number_line_edit.setFixedSize(400, 50)
        self.bank_card_number_line_edit.setInputMask('9999 9999 9999 9999')
        self.bank_card_number_line_edit.setStyleSheet(qss.line_edit2_consolas)

        self.bank_card_number_error_label: QLabel = QLabel(self)
        self.bank_card_number_error_label.setText('Необходимо заполнить')
        size_policy: QSizePolicy = self.bank_card_number_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.bank_card_number_error_label.setSizePolicy(size_policy)
        self.bank_card_number_error_label.setHidden(True)
        self.bank_card_number_error_label.setStyleSheet(qss.script)

        # expiration date

        self.expiration_date_label: QLabel = QLabel(self)
        self.expiration_date_label.setText('Срок действия')
        self.expiration_date_label.setStyleSheet(qss.heading2)

        self.expiration_month_line_edit: QLineEdit = QLineEdit(self)
        self.expiration_month_line_edit.setFixedSize(130, 50)
        regex_expiration_month = QRegularExpression("(0[1-9]|[1][0-2])")
        expiration_month_validator = QRegularExpressionValidator(regex_expiration_month, self)
        self.expiration_month_line_edit.setValidator(expiration_month_validator)
        self.expiration_month_line_edit.setStyleSheet(qss.line_edit2_consolas)

        self.expiration_slash_label: QLabel = QLabel(self)
        self.expiration_slash_label.setText('/')
        self.expiration_slash_label.setFixedSize(140, 50)
        self.expiration_slash_label.setStyleSheet(qss.heading2)

        self.expiration_year_line_edit: QLineEdit = QLineEdit(self)
        self.expiration_year_line_edit.setFixedSize(130, 50)
        regex_expiration_year = QRegularExpression("([0-9][0-9])")
        expiration_year_validator = QRegularExpressionValidator(regex_expiration_year, self)
        self.expiration_year_line_edit.setValidator(expiration_year_validator)
        self.expiration_year_line_edit.setStyleSheet(qss.line_edit2_consolas)

        expiration_date_layout = QHBoxLayout()
        expiration_date_layout.setContentsMargins(0, 0, 0, 0)
        expiration_date_layout.setSpacing(0)
        expiration_date_layout.addWidget(
            self.expiration_month_line_edit,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        expiration_date_layout.addWidget(
            self.expiration_slash_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        expiration_date_layout.addWidget(
            self.expiration_year_line_edit,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )

        self.expiration_date_widget: QWidget = QWidget(self)
        self.expiration_date_widget.setLayout(expiration_date_layout)

        self.expiration_date_error_label: QLabel = QLabel(self)
        self.expiration_date_error_label.setText('Необходимо заполнить')
        size_policy = self.expiration_date_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.expiration_date_error_label.setSizePolicy(size_policy)
        self.expiration_date_error_label.setHidden(True)
        self.expiration_date_error_label.setStyleSheet(qss.script)

        # holder name

        self.holder_name_label: QLabel = QLabel(self)
        self.holder_name_label.setText('Имя держателя')
        self.holder_name_label.setStyleSheet(qss.heading2)

        self.holder_name_line_edit: QLineEdit = QLineEdit(self)
        self.holder_name_line_edit.setFixedSize(400, 50)
        self.holder_name_line_edit.setValidator(HolderNameValidator(self))
        self.holder_name_line_edit.setStyleSheet(qss.line_edit2_consolas)

        self.holder_name_error_label: QLabel = QLabel(self)
        self.holder_name_error_label.setText('Необходимо заполнить')
        size_policy = self.holder_name_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.holder_name_error_label.setSizePolicy(size_policy)
        self.holder_name_error_label.setHidden(True)
        self.holder_name_error_label.setStyleSheet(qss.script)

        # payment amount

        self.payment_amount_label: QLabel = QLabel(self)
        self.payment_amount_label.setText('К оплате: 0.00 руб.')
        self.payment_amount_label.setStyleSheet(qss.heading2)

        # bank form

        bank_form_layout = QGridLayout()
        bank_form_layout.setColumnMinimumWidth(0, 300)
        bank_form_layout.setRowMinimumHeight(1, 30)
        bank_form_layout.setRowMinimumHeight(3, 30)
        bank_form_layout.setRowMinimumHeight(5, 30)
        bank_form_layout.setRowMinimumHeight(7, 30)
        bank_form_layout.setSpacing(0)
        bank_form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        bank_form_layout.addWidget(
            self.bank_card_label, 0, 0, 1, 2,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )

        bank_form_layout.addWidget(
            self.bank_card_number_label, 2, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.bank_card_number_line_edit, 2, 1,
            alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.bank_card_number_error_label, 3, 1,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
        )

        bank_form_layout.addWidget(
            self.expiration_date_label, 4, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.expiration_date_widget, 4, 1,
            alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.expiration_date_error_label, 5, 1,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
        )

        bank_form_layout.addWidget(
            self.holder_name_label, 6, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.holder_name_line_edit, 6, 1,
            alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.holder_name_error_label, 7, 1,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
        )

        bank_form_layout.addWidget(
            self.payment_amount_label, 8, 1,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )

        # bank widget

        self.bank_card_widget: QWidget = QWidget(self)
        self.bank_card_widget.setLayout(bank_form_layout)
        self.bank_card_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # buttons

        self.cancel_refueling_button: QPushButton = QPushButton(self)
        self.cancel_refueling_button.setText('Отменить заправку')
        self.cancel_refueling_button.setFixedSize(250, 60)
        self.cancel_refueling_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.cancel_refueling_button.setStyleSheet(qss.button)

        self.back_fuel_selection_button: QPushButton = QPushButton(self)
        self.back_fuel_selection_button.setText('Назад')
        self.back_fuel_selection_button.setFixedSize(250, 60)
        self.back_fuel_selection_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.back_fuel_selection_button.setStyleSheet(qss.button)

        self.pay_button: QPushButton = QPushButton(self)
        self.pay_button.setText('Оплатить')
        self.pay_button.setFixedSize(250, 60)
        self.pay_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pay_button.setStyleSheet(qss.colored_button)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(
            self.cancel_refueling_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        button_layout.addStretch()
        button_layout.addWidget(
            self.back_fuel_selection_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        button_layout.addWidget(
            self.pay_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )

        # main

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addWidget(
            self.title_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addStretch()
        main_layout.addWidget(self.loyalty_card_widget)
        main_layout.addWidget(self.bank_card_widget)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
