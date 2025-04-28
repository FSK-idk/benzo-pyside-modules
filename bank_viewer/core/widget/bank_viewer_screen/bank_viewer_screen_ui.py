from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QComboBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from core.widget.deposit_card_table_widget.deposit_card_table_widget import DepositCardTableWidget


class BankViewerScreenUI(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.title_label: QLabel = QLabel(self)
        self.title_label.setText('Банковские карты')
        self.title_label.setFont(QFont('Noto Sans', 30))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.issuer_label: QLabel = QLabel(self)
        self.issuer_label.setText('Платёжная система')
        self.issuer_label.setFont(QFont('Noto Sans', 20))
        self.issuer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.issuer_combo_box: QComboBox = QComboBox(self)
        self.issuer_combo_box.setFixedSize(200, 60)
        self.issuer_combo_box.setFont(QFont('Noto Sans', 20))
        self.issuer_combo_box.setStyleSheet('''
            QComboBox { padding: 0 0 0 10px; }
        ''')

        self.number_label: QLabel = QLabel(self)
        self.number_label.setText('Номер')
        self.number_label.setFont(QFont('Noto Sans', 20))
        self.number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.number_line_edit: QLineEdit = QLineEdit(self)
        self.number_line_edit.setFixedSize(200, 60)
        self.number_line_edit.setFont(QFont('Noto Sans', 20))

        self.holder_name_label: QLabel = QLabel(self)
        self.holder_name_label.setText('Держатель')
        self.holder_name_label.setFont(QFont('Noto Sans', 20))
        self.holder_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.holder_name_line_edit: QLineEdit = QLineEdit(self)
        self.holder_name_line_edit.setFixedSize(200, 60)
        self.holder_name_line_edit.setFont(QFont('Noto Sans', 20))

        form_layout = QHBoxLayout()
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(
            self.issuer_label,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        form_layout.addSpacing(10)
        form_layout.addWidget(
            self.issuer_combo_box,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        form_layout.addSpacing(10)
        form_layout.addWidget(
            self.number_label,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        form_layout.addSpacing(10)
        form_layout.addWidget(
            self.number_line_edit,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        form_layout.addSpacing(10)
        form_layout.addWidget(
            self.holder_name_label,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        form_layout.addSpacing(10)
        form_layout.addWidget(
            self.holder_name_line_edit,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        form_layout.addStretch()

        self.deposit_card_table: DepositCardTableWidget = DepositCardTableWidget(self)

        self.clear_button: QPushButton = QPushButton(self)
        self.clear_button.setFixedSize(360, 80)
        self.clear_button.setText('Сбросить')
        self.clear_button.setFont(QFont('Noto Sans', 24))
        self.clear_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.update_button: QPushButton = QPushButton(self)
        self.update_button.setFixedSize(360, 80)
        self.update_button.setText('Обновить')
        self.update_button.setFont(QFont('Noto Sans', 24))
        self.update_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(
            self.clear_button,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        button_layout.addStretch()
        button_layout.addWidget(
            self.update_button,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)
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
