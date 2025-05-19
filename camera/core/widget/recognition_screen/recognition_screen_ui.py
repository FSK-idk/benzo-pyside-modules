from PySide6.QtWidgets import QHBoxLayout, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

from core.style import qss


class RecognitionScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # title

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Номер распознан')
        self.title_label.setStyleSheet(qss.title)

        # car number

        self.car_number_label: QLabel = QLabel(self)
        self.car_number_label.setText('')
        self.car_number_label.setStyleSheet(qss.title)

        # buttons

        self.cancel_refueling_button: QPushButton = QPushButton(self)
        self.cancel_refueling_button.setText('Отменить заправку')
        self.cancel_refueling_button.setFixedSize(250, 60)
        self.cancel_refueling_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.cancel_refueling_button.setStyleSheet(qss.button)

        self.change_button: QPushButton = QPushButton(self)
        self.change_button.setText('Изменить')
        self.change_button.setFixedSize(250, 60)
        self.change_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.change_button.setStyleSheet(qss.button)

        self.confirm_button: QPushButton = QPushButton(self)
        self.confirm_button.setText('Подтвердить')
        self.confirm_button.setFixedSize(250, 60)
        self.confirm_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.confirm_button.setStyleSheet(qss.colored_button)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(
            self.cancel_refueling_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        button_layout.addStretch()
        button_layout.addWidget(
            self.change_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        button_layout.addWidget(
            self.confirm_button,
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
        main_layout.addWidget(
            self.car_number_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
