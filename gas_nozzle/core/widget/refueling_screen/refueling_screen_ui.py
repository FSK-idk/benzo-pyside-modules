from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class RefuelingScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Идёт заправка')
        self.title_label.setFont(QFont('Noto Sans', 30))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar: QProgressBar = QProgressBar(self)
        self.progress_bar.setFixedSize(720, 80)
        self.progress_bar.setFont(QFont('Noto Sans', 24))
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setValue(0)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.addWidget(
            self.title_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addStretch()
        main_layout.addWidget(
            self.progress_bar,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addStretch()

        self.setLayout(main_layout)
