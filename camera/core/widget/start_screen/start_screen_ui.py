from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

from core.style import qss


class StartScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.start_button: QPushButton = QPushButton(self)
        self.start_button.setText('Начать')
        self.start_button.setFixedSize(250, 60)
        self.start_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.start_button.setStyleSheet(qss.colored_button)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addWidget(
            self.start_button,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )

        self.setLayout(main_layout)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
