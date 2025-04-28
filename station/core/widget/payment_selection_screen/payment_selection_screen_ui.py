from PySide6.QtWidgets import QWidget, QPushButton, QSizePolicy, QGridLayout, QDoubleSpinBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QSpacerItem
from PySide6.QtGui import QFont, QRegularExpressionValidator
from PySide6.QtCore import Qt, QRegularExpression


from core.widget.payment_selection_screen.holder_name_validator import HolderNameValidator


class PaymentSelectionScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Оплата')
        self.title_label.setFont(QFont('Noto Sans', 30))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.loyalty_card_label: QLabel = QLabel(self)
        self.loyalty_card_label.setText('Карта лояльности (Name Name)')
        self.loyalty_card_label.setFont(QFont('Noto Sans', 22))

        self.bonuses_label: QLabel = QLabel(self)
        self.bonuses_label.setText('Бонусы: 0.00 руб.')
        self.bonuses_label.setFont(QFont('Noto Sans', 22))

        loyalty_card_title_layout: QHBoxLayout = QHBoxLayout()
        loyalty_card_title_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        loyalty_card_title_layout.addWidget(self.loyalty_card_label)
        loyalty_card_title_layout.addStretch()
        loyalty_card_title_layout.addWidget(self.bonuses_label)

        self.using_bonuses_label: QLabel = QLabel(self)
        self.using_bonuses_label.setText('Использовать бонусы')
        self.using_bonuses_label.setFont(QFont('Noto Sans', 22))

        self.using_bonuses_spin_box: QDoubleSpinBox = QDoubleSpinBox(self)
        self.using_bonuses_spin_box.setFixedSize(360, 60)
        self.using_bonuses_spin_box.setFont(QFont('Noto Sans', 22))
        self.using_bonuses_spin_box.setSuffix(' руб.')
        self.using_bonuses_spin_box.setStyleSheet('''
            QDoubleSpinBox { padding: 0 0 0 30px; }
            QDoubleSpinBox::down-button { width: 30 }
            QDoubleSpinBox::up-button { width: 30 }
        ''')
        self.using_bonuses_spin_box.editingFinished.connect(self.using_bonuses_spin_box.clearFocus)

        bonuses_form_layout: QGridLayout = QGridLayout()
        bonuses_form_layout.setColumnStretch(0, 1)
        bonuses_form_layout.setColumnStretch(1, 1)
        bonuses_form_layout.setColumnStretch(2, 1)
        bonuses_form_layout.addWidget(
            self.using_bonuses_label, 0, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        bonuses_form_layout.addWidget(
            self.using_bonuses_spin_box, 0, 1,
            alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter,
        )

        loyalty_card_layout: QVBoxLayout = QVBoxLayout()
        loyalty_card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        loyalty_card_layout.setContentsMargins(0, 0, 0, 0)
        loyalty_card_layout.addWidget(
            self.title_label,
            alignment=Qt.AlignmentFlag.AlignHCenter)
        loyalty_card_layout.addLayout(loyalty_card_title_layout)
        loyalty_card_layout.addSpacing(10)
        loyalty_card_layout.addLayout(bonuses_form_layout)

        self.loyalty_card_widget: QWidget = QWidget(self)
        self.loyalty_card_widget.setLayout(loyalty_card_layout)
        self.loyalty_card_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.bank_card_label: QLabel = QLabel(self)
        self.bank_card_label.setText('Банковкая карта')
        self.bank_card_label.setFont(QFont('Noto Sans', 22))
        self.bank_card_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.payment_amount_label: QLabel = QLabel(self)
        self.payment_amount_label.setText('К оплате: 0.00 руб.')
        self.payment_amount_label.setFont(QFont('Noto Sans', 22))
        self.payment_amount_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        bank_card_title_layout: QHBoxLayout = QHBoxLayout()
        bank_card_title_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bank_card_title_layout.addWidget(
            self.bank_card_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        bank_card_title_layout.addStretch()
        bank_card_title_layout.addWidget(
            self.payment_amount_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )

        self.bank_card_number_label: QLabel = QLabel(self)
        self.bank_card_number_label.setText('Номер карты')
        self.bank_card_number_label.setFont(QFont('Noto Sans', 22))
        self.bank_card_number_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.bank_card_number_line_edit: QLineEdit = QLineEdit(self)
        self.bank_card_number_line_edit.setFixedSize(360, 60)
        self.bank_card_number_line_edit.setFont(QFont('consolas', 22))
        self.bank_card_number_line_edit.setInputMask('9999 9999 9999 9999')
        self.bank_card_number_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.expiration_date_label: QLabel = QLabel(self)
        self.expiration_date_label.setText('Срок действия')
        self.expiration_date_label.setFont(QFont('Noto Sans', 22))
        self.expiration_date_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.expiration_month_line_edit: QLineEdit = QLineEdit(self)
        self.expiration_month_line_edit.setFixedSize(120, 60)
        self.expiration_month_line_edit.setFont(QFont('consolas', 22))
        self.expiration_month_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        regex_expiration_month = QRegularExpression("(0[1-9]|[1][0-2])")
        expiration_month_validator = QRegularExpressionValidator(regex_expiration_month, self)
        self.expiration_month_line_edit.setValidator(expiration_month_validator)

        self.expiration_slash_label: QLabel = QLabel(self)
        self.expiration_slash_label.setText('/')
        self.expiration_slash_label.setFixedSize(110, 60)
        self.expiration_slash_label.setFont(QFont('Noto Sans', 22))
        self.expiration_slash_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.expiration_year_line_edit: QLineEdit = QLineEdit(self)
        self.expiration_year_line_edit.setFixedSize(120, 60)
        self.expiration_year_line_edit.setFont(QFont('consolas', 22))
        self.expiration_year_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        regex_expiration_year = QRegularExpression("([0-9][0-9])")
        expiration_year_validator = QRegularExpressionValidator(regex_expiration_year, self)
        self.expiration_year_line_edit.setValidator(expiration_year_validator)

        expiration_date_layout: QHBoxLayout = QHBoxLayout()
        expiration_date_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        expiration_date_layout.addWidget(
            self.expiration_month_line_edit,
            alignment=Qt.AlignmentFlag.AlignVCenter)
        expiration_date_layout.addWidget(
            self.expiration_slash_label,
            alignment=Qt.AlignmentFlag.AlignVCenter)
        expiration_date_layout.addWidget(
            self.expiration_year_line_edit,
            alignment=Qt.AlignmentFlag.AlignVCenter)

        self.holder_name_label: QLabel = QLabel(self)
        self.holder_name_label.setText('Имя держателя')
        self.holder_name_label.setFont(QFont('Noto Sans', 22))
        self.holder_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.holder_name_line_edit: QLineEdit = QLineEdit(self)
        self.holder_name_line_edit.setFixedSize(360, 60)
        self.holder_name_line_edit.setFont(QFont('consolas', 22))
        self.holder_name_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.holder_name_line_edit.setValidator(HolderNameValidator(self))

        self.bank_card_number_error_label: QLabel = QLabel(self)
        self.bank_card_number_error_label.setText('Необходимо заполнить')
        self.bank_card_number_error_label.setFont(QFont('Noto Sans', 14))
        self.bank_card_number_error_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.bank_card_number_error_label.hide()
        size_policy: QSizePolicy = self.bank_card_number_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.bank_card_number_error_label.setSizePolicy(size_policy)
        self.bank_card_number_error_label.setHidden(True)

        self.expiration_date_error_label: QLabel = QLabel(self)
        self.expiration_date_error_label.setText('Необходимо заполнить')
        self.expiration_date_error_label.setFont(QFont('Noto Sans', 14))
        self.expiration_date_error_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.expiration_date_error_label.hide()
        size_policy: QSizePolicy = self.expiration_date_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.expiration_date_error_label.setSizePolicy(size_policy)
        self.expiration_date_error_label.setHidden(True)

        self.holder_name_error_label: QLabel = QLabel(self)
        self.holder_name_error_label.setText('Необходимо заполнить')
        self.holder_name_error_label.setFont(QFont('Noto Sans', 14))
        self.holder_name_error_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.holder_name_error_label.hide()
        size_policy: QSizePolicy = self.holder_name_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.holder_name_error_label.setSizePolicy(size_policy)
        self.holder_name_error_label.setHidden(True)

        bank_form_layout: QGridLayout = QGridLayout()
        bank_form_layout.setColumnStretch(0, 1)
        bank_form_layout.setColumnStretch(1, 1)
        bank_form_layout.setColumnStretch(2, 1)
        bank_form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bank_form_layout.addWidget(
            self.bank_card_number_label, 0, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.bank_card_number_line_edit, 0, 1,
            alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.bank_card_number_error_label, 0, 2,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )

        bank_form_layout.addWidget(
            self.expiration_date_label, 1, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addLayout(
            expiration_date_layout, 1, 1,
            alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.expiration_date_error_label, 1, 2,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )

        bank_form_layout.addWidget(
            self.holder_name_label, 2, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.holder_name_line_edit, 2, 1,
            alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter,
        )
        bank_form_layout.addWidget(
            self.holder_name_error_label, 2, 2,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )

        bank_card_layout: QVBoxLayout = QVBoxLayout()
        bank_card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bank_card_layout.setContentsMargins(0, 0, 0, 0)
        bank_card_layout.addLayout(bank_card_title_layout)
        bank_card_layout.addSpacing(10)
        bank_card_layout.addLayout(bank_form_layout)

        self.bank_card_widget: QWidget = QWidget(self)
        self.bank_card_widget.setLayout(bank_card_layout)
        self.bank_card_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.pay_button: QPushButton = QPushButton(self)
        self.pay_button.setFixedSize(360, 80)
        self.pay_button.setText('Оплатить')
        self.pay_button.setFont(QFont('Noto Sans', 24))
        self.pay_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.back_fuel_selection_button: QPushButton = QPushButton(self)
        self.back_fuel_selection_button.setFixedSize(360, 80)
        self.back_fuel_selection_button.setText('Назад')
        self.back_fuel_selection_button.setFont(QFont('Noto Sans', 24))
        self.back_fuel_selection_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.cancel_refueling_button: QPushButton = QPushButton(self)
        self.cancel_refueling_button.setFixedSize(360, 80)
        self.cancel_refueling_button.setText('Отменить заправку')
        self.cancel_refueling_button.setFont(QFont('Noto Sans', 24))
        self.cancel_refueling_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        button_layout: QHBoxLayout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(
            self.pay_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        button_layout.addWidget(
            self.back_fuel_selection_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        button_layout.addStretch()
        button_layout.addWidget(
            self.cancel_refueling_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )

        main_layout: QVBoxLayout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.addWidget(
            self.title_label,
            alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addStretch()
        main_layout.addWidget(self.loyalty_card_widget)
        main_layout.addWidget(self.bank_card_widget)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
