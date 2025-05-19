from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtCore import Qt

from core.style import qss


class RefuelingScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Идёт заправка')
        self.title_label.setStyleSheet(qss.colored_title)

        self.progress_bar: QProgressBar = QProgressBar(self)
        self.progress_bar.setFixedSize(700, 60)
        self.progress_bar.setValue(50)
        self.progress_bar.setStyleSheet(qss.progress_bar)

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
            self.progress_bar,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addStretch()

        self.setLayout(main_layout)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
