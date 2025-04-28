from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class StationUseScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Используйте экран заправочной колонки')
        self.title_label.setFont(QFont('Noto Sans', 30))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout: QVBoxLayout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.addWidget(
            self.title_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )

        self.setLayout(main_layout)
