from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class FinishScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Заправка завершена')
        self.title_label.setFont(QFont('Noto Sans', 30))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.confirm_button: QPushButton = QPushButton(self)
        self.confirm_button.setFixedSize(360, 80)
        self.confirm_button.setText('Подтвердить')
        self.confirm_button.setFont(QFont('Noto Sans', 24))
        self.confirm_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        main_layout: QVBoxLayout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.addStretch()
        main_layout.addWidget(
            self.title_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addStretch()
        main_layout.addWidget(
            self.confirm_button,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )

        self.setLayout(main_layout)
