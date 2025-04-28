from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal


class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, ev):
        self.clicked.emit()
