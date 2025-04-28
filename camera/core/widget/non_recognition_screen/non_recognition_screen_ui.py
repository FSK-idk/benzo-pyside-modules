from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QSizePolicy, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class NonRecognitionScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Номер не распознан')
        self.title_label.setFont(QFont('Noto Sans', 30))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.enter_label: QLabel = QLabel(self)
        self.enter_label.setText('Введите номер:')
        self.enter_label.setFont(QFont('Noto Sans', 24))
        self.enter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.car_number_line_edit: QLineEdit = QLineEdit(self)
        self.car_number_line_edit.setFixedSize(480, 80)
        self.car_number_line_edit.setFont(QFont('Noto Sans', 30))
        self.car_number_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.car_number_error_label: QLabel = QLabel(self)
        self.car_number_error_label.setText('Неподдерживаемый формат')
        self.car_number_error_label.setFont(QFont('Noto Sans', 14))
        self.car_number_error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        size_policy: QSizePolicy = self.car_number_error_label.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.car_number_error_label.setSizePolicy(size_policy)
        self.car_number_error_label.setHidden(True)

        self.confirm_button: QPushButton = QPushButton(self)
        self.confirm_button.setFixedSize(360, 80)
        self.confirm_button.setText('Подтвердить')
        self.confirm_button.setFont(QFont('Noto Sans', 24))
        self.confirm_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.cancel_refueling_button: QPushButton = QPushButton(self)
        self.cancel_refueling_button.setFixedSize(360, 80)
        self.cancel_refueling_button.setText('Отменить заправку')
        self.cancel_refueling_button.setFont(QFont('Noto Sans', 24))
        self.cancel_refueling_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        button_layout: QHBoxLayout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(
            self.confirm_button,
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
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addStretch()
        main_layout.addWidget(
            self.enter_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addWidget(
            self.car_number_line_edit,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addWidget(
            self.car_number_error_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
