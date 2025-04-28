from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from core.widget.selection_screen.clickable_label import ClickableLabel


class SelectionScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Выбор изображения')
        self.title_label.setFont(QFont('Noto Sans', 30))

        self.image_1_label: ClickableLabel = ClickableLabel(self)
        self.image_2_label: ClickableLabel = ClickableLabel(self)
        self.image_3_label: ClickableLabel = ClickableLabel(self)

        image_layout: QHBoxLayout = QHBoxLayout()
        image_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_layout.addWidget(
            self.image_1_label,
            alignment=Qt.AlignmentFlag.AlignVCenter)
        image_layout.addWidget(
            self.image_2_label,
            alignment=Qt.AlignmentFlag.AlignVCenter)
        image_layout.addWidget(
            self.image_3_label,
            alignment=Qt.AlignmentFlag.AlignVCenter)

        self.cancel_refueling_button: QPushButton = QPushButton(self)
        self.cancel_refueling_button.setFixedSize(360, 80)
        self.cancel_refueling_button.setText('Отменить заправку')
        self.cancel_refueling_button.setFont(QFont('Noto Sans', 24))
        self.cancel_refueling_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        button_layout: QHBoxLayout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        main_layout.addLayout(image_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
