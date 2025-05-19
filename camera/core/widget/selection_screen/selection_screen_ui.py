from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from core.widget.selection_screen.clickable_label import ClickableLabel

from core.style import qss


class SelectionScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # title

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Выбор изображения')
        self.title_label.setStyleSheet(qss.title)

        # images

        self.image_1_label: ClickableLabel = ClickableLabel(self)
        self.image_2_label: ClickableLabel = ClickableLabel(self)
        self.image_3_label: ClickableLabel = ClickableLabel(self)

        image_layout = QHBoxLayout()
        image_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_layout.addWidget(
            self.image_1_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        image_layout.addWidget(
            self.image_2_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        image_layout.addWidget(
            self.image_3_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )

        # buttons

        self.cancel_refueling_button: QPushButton = QPushButton(self)
        self.cancel_refueling_button.setText('Отменить заправку')
        self.cancel_refueling_button.setFixedSize(250, 60)
        self.cancel_refueling_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.cancel_refueling_button.setStyleSheet(qss.button)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(
            self.cancel_refueling_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        button_layout.addStretch()

        # main

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addWidget(
            self.title_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addStretch()
        main_layout.addLayout(image_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
