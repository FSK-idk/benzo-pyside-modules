import random

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, QTimer, Signal

from core.widget.refueling_screen.refueling_screen_ui import RefuelingScreenUI


class RefuelingScreen(QObject):
    refuelingFinished: Signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: RefuelingScreenUI = RefuelingScreenUI(parent)

        self.timer: QTimer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.onTime)

        self.ui.show()

    def start(self) -> None:
        self.timer.start()

    def clearInput(self) -> None:
        self.ui.progress_bar.setValue(0)

    def onTime(self) -> None:
        value = self.ui.progress_bar.value()
        max_value = self.ui.progress_bar.maximum()

        self.ui.progress_bar.setValue(min(value + random.randint(1, 5), max_value))

        if (self.ui.progress_bar.value() == max_value):
            self.timer.stop()
            self.refuelingFinished.emit()
