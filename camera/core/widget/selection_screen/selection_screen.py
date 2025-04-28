import os
from functools import partial

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QObject, Slot, Signal

from core.widget.selection_screen.selection_screen_ui import SelectionScreenUI

from core.model.camera_load import CameraLoad

from core.data_base.data_base import data_base

from core.util import get_random_image_filenames


class SelectionScreen(QObject):
    imageSelected: Signal = Signal(CameraLoad)
    cancelRefuelingClicked: Signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__()

        self.ui: SelectionScreenUI = SelectionScreenUI(parent)

        self.ui.image_1_label.clicked.connect(partial(self.onImageClicked, 0))
        self.ui.image_2_label.clicked.connect(partial(self.onImageClicked, 1))
        self.ui.image_3_label.clicked.connect(partial(self.onImageClicked, 2))

        self.ui.cancel_refueling_button.clicked.connect(self.cancelRefuelingClicked.emit)

        self.image_filenames: list[str]
        self.resetImages()

        self.ui.show()

    def resetImages(self) -> None:
        self.image_filenames = get_random_image_filenames()

        height: int = 300

        pixmap_1: QPixmap = QPixmap(self.image_filenames[0]).scaledToHeight(height)
        pixmap_2: QPixmap = QPixmap(self.image_filenames[1]).scaledToHeight(height)
        pixmap_3: QPixmap = QPixmap(self.image_filenames[2]).scaledToHeight(height)

        self.ui.image_1_label.setPixmap(pixmap_1)
        self.ui.image_2_label.setPixmap(pixmap_2)
        self.ui.image_3_label.setPixmap(pixmap_3)

    @Slot()
    def onImageClicked(self, index: int) -> None:
        image_file: str = os.path.basename(self.image_filenames[index])
        self.imageSelected.emit(data_base.selectCameraLoadByImageFilename(image_file))
