from PySide6.QtWidgets import QHBoxLayout, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class RecognitionScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Номер распознан')
        self.title_label.setFont(QFont('Noto Sans', 30))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.car_number_label: QLabel = QLabel(self)
        self.car_number_label.setText('')
        self.car_number_label.setFont(QFont('Noto Sans', 30))
        self.car_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.confirm_button: QPushButton = QPushButton(self)
        self.confirm_button.setFixedSize(360, 80)
        self.confirm_button.setText('Подтвердить')
        self.confirm_button.setFont(QFont('Noto Sans', 24))
        self.confirm_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.change_button: QPushButton = QPushButton(self)
        self.change_button.setFixedSize(360, 80)
        self.change_button.setText('Изменить')
        self.change_button.setFont(QFont('Noto Sans', 24))
        self.change_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

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
        button_layout.addWidget(
            self.change_button,
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
            self.car_number_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
