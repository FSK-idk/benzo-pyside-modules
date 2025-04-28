from ctypes import alignment
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QDoubleSpinBox, QVBoxLayout, QLabel, QComboBox, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class FuelSelectionScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Выбор топлива')
        self.title_label.setFont(QFont('Noto Sans', 30))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fuel_type_label: QLabel = QLabel(self)
        self.fuel_type_label.setText('Тип')
        self.fuel_type_label.setFont(QFont('Noto Sans', 22))
        self.fuel_type_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.fuel_type_combo_box: QComboBox = QComboBox(self)
        self.fuel_type_combo_box.setFixedSize(360, 60)
        self.fuel_type_combo_box.setFont(QFont('Noto Sans', 22))
        self.fuel_type_combo_box.setStyleSheet('''
            QComboBox { padding: 0 0 0 30px; }
        ''')

        fuel_type_layout = QHBoxLayout()
        fuel_type_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fuel_type_layout.addWidget(
            self.fuel_type_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        fuel_type_layout.addStretch()
        fuel_type_layout.addWidget(
            self.fuel_type_combo_box,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )

        self.fuel_amount_label: QLabel = QLabel(self)
        self.fuel_amount_label.setText('Количество')
        self.fuel_amount_label.setFont(QFont('Noto Sans', 22))
        self.fuel_amount_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.fuel_amount_spin_box: QDoubleSpinBox = QDoubleSpinBox(self)
        self.fuel_amount_spin_box.setFixedSize(360, 60)
        self.fuel_amount_spin_box.setFont(QFont('Noto Sans', 22))
        self.fuel_amount_spin_box.setSuffix(' л.')
        self.fuel_amount_spin_box.setStyleSheet('''
            QDoubleSpinBox { padding: 0 0 0 30px; }
            QDoubleSpinBox::down-button { width: 30 }
            QDoubleSpinBox::up-button { width: 30 }
        ''')
        self.fuel_amount_spin_box.editingFinished.connect(self.fuel_amount_spin_box.clearFocus)

        self.fuel_amount_error_label: QLabel = QLabel(self)
        self.fuel_amount_error_label.setText('Не должно быть нулём')
        self.fuel_amount_error_label.setFont(QFont('Noto Sans', 14))
        self.fuel_amount_error_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.fuel_amount_error_label.hide()
        size_policy: QSizePolicy = self.fuel_amount_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.fuel_amount_error_label.setSizePolicy(size_policy)
        self.fuel_amount_error_label.setHidden(True)

        fuel_amount_layout = QHBoxLayout()
        fuel_amount_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fuel_amount_layout.addWidget(
            self.fuel_amount_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        fuel_amount_layout.addStretch()
        fuel_amount_layout.addWidget(
            self.fuel_amount_spin_box,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )

        self.payment_amount_label: QLabel = QLabel(self)
        self.payment_amount_label.setText('Сумма')
        self.payment_amount_label.setFont(QFont('Noto Sans', 22))
        self.payment_amount_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.payment_amount_spin_box: QDoubleSpinBox = QDoubleSpinBox(self)
        self.payment_amount_spin_box.setFixedSize(360, 60)
        self.payment_amount_spin_box.setFont(QFont('Noto Sans', 22))
        self.payment_amount_spin_box.setSuffix(' руб.')
        self.payment_amount_spin_box.setStyleSheet('''
            QDoubleSpinBox { padding: 0 0 0 30; }
            QDoubleSpinBox::down-button { width: 30 }
            QDoubleSpinBox::up-button { width: 30 }
        ''')
        self.payment_amount_spin_box.editingFinished.connect(self.payment_amount_spin_box.clearFocus)

        self.payment_amount_error_label: QLabel = QLabel(self)
        self.payment_amount_error_label.setText('Не должно быть нулём')
        self.payment_amount_error_label.setFont(QFont('Noto Sans', 14))
        self.payment_amount_error_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.payment_amount_error_label.hide()
        size_policy: QSizePolicy = self.payment_amount_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.payment_amount_error_label.setSizePolicy(size_policy)
        self.payment_amount_error_label.setHidden(True)

        payment_amount_layout = QHBoxLayout()
        payment_amount_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        payment_amount_layout.addWidget(
            self.payment_amount_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        payment_amount_layout.addStretch()
        payment_amount_layout.addWidget(
            self.payment_amount_spin_box,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )

        self.price_label: QLabel = QLabel(self)
        self.price_label.setText('Цена: 0.00 руб.')
        self.price_label.setFont(QFont('Noto Sans', 22))
        self.price_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        form_layout = QGridLayout()
        form_layout.setColumnStretch(0, 5)
        form_layout.setColumnStretch(1, 3)
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addLayout(fuel_type_layout, 0, 0)
        form_layout.addLayout(fuel_amount_layout, 1, 0)
        form_layout.addLayout(payment_amount_layout, 2, 0)
        form_layout.addWidget(
            self.price_label, 0, 1,
            alignment=Qt.AlignmentFlag.AlignRight,
        )
        form_layout.addWidget(
            self.fuel_amount_error_label, 1, 1,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addWidget(
            self.payment_amount_error_label, 2, 1,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )

        self.continue_payment_button: QPushButton = QPushButton(self)
        self.continue_payment_button.setFixedSize(360, 80)
        self.continue_payment_button.setText('Перейти к оплате')
        self.continue_payment_button.setFont(QFont('Noto Sans', 24))
        self.continue_payment_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.cancel_refueling_button: QPushButton = QPushButton(self)
        self.cancel_refueling_button.setFixedSize(360, 80)
        self.cancel_refueling_button.setText('Отменить заправку')
        self.cancel_refueling_button.setFont(QFont('Noto Sans', 24))
        self.cancel_refueling_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(
            self.continue_payment_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        button_layout.addStretch()
        button_layout.addWidget(
            self.cancel_refueling_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.addWidget(
            self.title_label,
            alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addStretch()
        main_layout.addLayout(form_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
