from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from core.style import qss


class FinishScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Ждём вас снова')
        self.title_label.setStyleSheet(qss.colored_title)

        self.confirm_button: QPushButton = QPushButton(self)
        self.confirm_button.setText('Подтвердить')
        self.confirm_button.setFixedSize(250, 60)
        self.confirm_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.confirm_button.setStyleSheet(qss.colored_button)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(20, 20, 20, 20)
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
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
