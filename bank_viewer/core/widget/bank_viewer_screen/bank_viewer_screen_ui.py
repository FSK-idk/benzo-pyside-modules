from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QComboBox
from PySide6.QtCore import Qt

from core.widget.deposit_card_table_widget.deposit_card_table_widget import DepositCardTableWidget

from core.style import qss


class BankViewerScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # title

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Банковские карты')
        self.title_label.setStyleSheet(qss.title)

        # issuer

        self.issuer_label: QLabel = QLabel(self)
        self.issuer_label.setText('Платёжная система')
        self.issuer_label.setStyleSheet(qss.heading2)

        self.issuer_combo_box: QComboBox = QComboBox(self)
        self.issuer_combo_box.setFixedSize(200, 50)
        self.issuer_combo_box.setStyleSheet(qss.combo_box2)

        # number

        self.number_label: QLabel = QLabel(self)
        self.number_label.setText('Номер')
        self.number_label.setStyleSheet(qss.heading2)

        self.number_line_edit: QLineEdit = QLineEdit(self)
        self.number_line_edit.setFixedSize(200, 50)
        self.number_line_edit.setStyleSheet(qss.line_edit2)

        # holder name

        self.holder_name_label: QLabel = QLabel(self)
        self.holder_name_label.setText('Держатель')
        self.holder_name_label.setStyleSheet(qss.heading2)

        self.holder_name_line_edit: QLineEdit = QLineEdit(self)
        self.holder_name_line_edit.setFixedSize(200, 50)
        self.holder_name_line_edit.setStyleSheet(qss.line_edit2)

        # form

        form_layout = QHBoxLayout()
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(
            self.issuer_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addSpacing(5)
        form_layout.addWidget(
            self.issuer_combo_box,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addSpacing(15)
        form_layout.addWidget(
            self.number_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addSpacing(5)
        form_layout.addWidget(
            self.number_line_edit,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addSpacing(15)
        form_layout.addWidget(
            self.holder_name_label,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        form_layout.addSpacing(5)
        form_layout.addWidget(
            self.holder_name_line_edit,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        form_layout.addStretch()

        # table

        self.deposit_card_table: DepositCardTableWidget = DepositCardTableWidget(self)
        self.deposit_card_table.setStyleSheet(qss.table)

        # buttons

        self.clear_button: QPushButton = QPushButton(self)
        self.clear_button.setText('Сбросить')
        self.clear_button.setFixedSize(250, 60)
        self.clear_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.clear_button.setStyleSheet(qss.button)

        self.update_button: QPushButton = QPushButton(self)
        self.update_button.setFixedSize(250, 60)
        self.update_button.setText('Обновить')
        self.update_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.update_button.setStyleSheet(qss.colored_button)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(
            self.clear_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        button_layout.addStretch()
        button_layout.addWidget(
            self.update_button,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )

        # main

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addWidget(
            self.title_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addSpacing(20)
        main_layout.addLayout(form_layout)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.deposit_card_table)
        main_layout.addSpacing(20)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
