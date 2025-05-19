from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QDoubleSpinBox, QVBoxLayout, QLabel, QComboBox, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

from core.style import qss


class FuelSelectionScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # title

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Выбор топлива')
        self.title_label.setStyleSheet(qss.title)

        # fuel type

        self.fuel_type_label: QLabel = QLabel(self)
        self.fuel_type_label.setText('Тип')
        self.fuel_type_label.setStyleSheet(qss.heading2)

        self.fuel_type_combo_box: QComboBox = QComboBox(self)
        self.fuel_type_combo_box.setFixedSize(400, 50)
        self.fuel_type_combo_box.setStyleSheet(qss.combo_box2)

        # fuel amount

        self.fuel_amount_label: QLabel = QLabel(self)
        self.fuel_amount_label.setText('Количество')
        self.fuel_amount_label.setStyleSheet(qss.heading2)

        self.fuel_amount_spin_box: QDoubleSpinBox = QDoubleSpinBox(self)
        self.fuel_amount_spin_box.setFixedSize(400, 50)
        self.fuel_amount_spin_box.setSuffix(' л.')
        self.fuel_amount_spin_box.setStyleSheet(qss.double_spin_box2)
        self.fuel_amount_spin_box.editingFinished.connect(self.fuel_amount_spin_box.clearFocus)

        self.fuel_amount_error_label: QLabel = QLabel(self)
        self.fuel_amount_error_label.setText('Не должно быть нулём')
        size_policy = self.fuel_amount_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.fuel_amount_error_label.setSizePolicy(size_policy)
        self.fuel_amount_error_label.setHidden(True)
        self.fuel_amount_error_label.setStyleSheet(qss.script)

        # payment amount

        self.payment_amount_label: QLabel = QLabel(self)
        self.payment_amount_label.setText('Сумма')
        self.payment_amount_label.setStyleSheet(qss.heading2)

        self.payment_amount_spin_box: QDoubleSpinBox = QDoubleSpinBox(self)
        self.payment_amount_spin_box.setFixedSize(400, 50)
        self.payment_amount_spin_box.setSuffix(' руб.')
        self.payment_amount_spin_box.setStyleSheet(qss.double_spin_box2)
        self.payment_amount_spin_box.editingFinished.connect(self.payment_amount_spin_box.clearFocus)

        self.payment_amount_error_label: QLabel = QLabel(self)
        self.payment_amount_error_label.setText('Не должно быть нулём')
        size_policy = self.payment_amount_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.payment_amount_error_label.setSizePolicy(size_policy)
        self.payment_amount_error_label.setHidden(True)
        self.payment_amount_error_label.setStyleSheet(qss.script)

        # price

        self.price_label: QLabel = QLabel(self)
        self.price_label.setText('Цена: 0.00 руб.')
        self.price_label.setStyleSheet(qss.heading2)

        # form

        form_layout = QGridLayout()
        form_layout.setColumnMinimumWidth(0, 300)
        form_layout.setRowMinimumHeight(1, 30)
        form_layout.setRowMinimumHeight(3, 30)
        form_layout.setRowMinimumHeight(5, 30)
        form_layout.setSpacing(0)
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        form_layout.addWidget(
            self.fuel_type_label, 0, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addWidget(
            self.fuel_type_combo_box, 0, 1,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )

        form_layout.addWidget(
            self.fuel_amount_label, 2, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addWidget(
            self.fuel_amount_spin_box, 2, 1,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addWidget(
            self.fuel_amount_error_label, 3, 1,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
        )

        form_layout.addWidget(
            self.payment_amount_label, 4, 0,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addWidget(
            self.payment_amount_spin_box, 4, 1,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addWidget(
            self.payment_amount_error_label, 5, 1,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
        )

        form_layout.addWidget(
            self.price_label, 6, 1,
            alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
        )

        # buttons

        self.cancel_refueling_button: QPushButton = QPushButton(self)
        self.cancel_refueling_button.setText('Отменить заправку')
        self.cancel_refueling_button.setFixedSize(250, 60)
        self.cancel_refueling_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.cancel_refueling_button.setStyleSheet(qss.button)

        self.continue_payment_button: QPushButton = QPushButton(self)
        self.continue_payment_button.setText('Перейти к оплате')
        self.continue_payment_button.setFixedSize(250, 60)
        self.continue_payment_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.continue_payment_button.setStyleSheet(qss.colored_button)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(
            self.cancel_refueling_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        button_layout.addStretch()
        button_layout.addWidget(
            self.continue_payment_button,
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
        main_layout.addLayout(form_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
