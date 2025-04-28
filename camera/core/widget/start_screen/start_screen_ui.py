from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class StartScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.start_button: QPushButton = QPushButton(self)
        self.start_button.setFixedSize(480, 120)
        self.start_button.setText('Начать')
        self.start_button.setFont(QFont('Noto Sans', 30))
        self.start_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        main_layout: QVBoxLayout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.addWidget(
            self.start_button,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )

        self.setLayout(main_layout)
