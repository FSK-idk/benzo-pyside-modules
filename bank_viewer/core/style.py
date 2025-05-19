import sass


class Qss:
    def __init__(self) -> None:
        self.primary1_color = '#e74c3c'
        self.primary2_color = '#d53b2b'
        self.primary3_color = '#c43b2b'
        self.light1_color = '#ffffff'
        self.light2_color = '#f8f9fa'
        self.light3_color = '#edeff2'
        self.text_light_color = '#ffffff'
        self.text_dark_color = '#333333'
        self.bg_color = '#ffffff'
        self.border_color = '#e0e0e0'
        self.font_family = 'Segoe UI'
        self.border_color = '#e0e0e0'

        self.variables: str = """
            $primary1-color: #e74c3c;
            $primary2-color: #d53b2b;
            $primary3-color: #c43b2b;
            $light1-color: #ffffff;
            $light2-color: #f8f9fa;
            $light3-color: #edeff2;
            $text-light-color: #ffffff;
            $text-dark-color: #333333;
            $bg-color: #ffffff;
            $border-color: #e0e0e0;
            $font-family: 'Segoe UI';
            $border-color: #e0e0e0;
        """

        # button

        self.button: str = self._compile("""
            QPushButton {
                padding: 10px 10px;
                border: 1px solid $border-color;
                border-radius: 10px;
                font-family: $font-family;
                font-size: 16pt;
                font-weight: 600;
                text-align: center;
                background: $light1-color;
                color: $text-dark-color;
            }

            QPushButton:hover {
                background: $light2-color;
            }

            QPushButton:pressed {
                background: $light3-color;
            }
        """)

        self.colored_button: str = self._compile("""
            QPushButton {
                padding: 10px 10px;
                border-radius: 10px;
                font-family: $font-family;
                font-size: 16pt;
                font-weight: 600;
                text-align: center;
                background: $primary1-color;
                color: $text-light-color;
            }

            QPushButton:hover {
                background: $primary2-color;
            }

            QPushButton:pressed {
                background: $primary3-color;
            }
        """)

        # progress bar

        self.progress_bar: str = self._compile("""
            QProgressBar {
                border: 1px solid $border-color;
                border-radius: 10px;
                font-family: $font-family;
                font-size: 16pt;
                font-weight: 600;
                text-align: center;
                background-color: $light1-color;
                color: $text-dark-color;
                selection-background-color: $primary1-color;
                selection-color: $text-light-color;
            }

            QProgressBar::chunk {
                border-radius: 10px;
                background: $primary1-color;
            }
        """)

        # line edit

        self.line_edit1: str = self._compile("""
            QLineEdit {
                padding: 12px 12px;
                border: 1px solid $border-color;
                border-radius: 10px;
                font-family: $font-family;
                font-size: 18pt;
                font-weight: 500;
                text-align: center;
                background: $light1-color;
                color: $text-dark-color;
                qproperty-alignment: AlignCenter;
            }

            QLineEdit:focus {
                border-color: $primary1-color;
            }
        """)

        self.line_edit2: str = self._compile("""
            QLineEdit {
                padding: 10px 10px;
                border: 1px solid $border-color;
                border-radius: 10px;
                font-family: $font-family;
                font-size: 16pt;
                font-weight: 500;
                text-align: center;
                background: $light1-color;
                color: $text-dark-color;
            }

            QLineEdit:focus {
                border-color: $primary1-color;
            }
        """)

        self.line_edit2_consolas: str = self._compile("""
            QLineEdit {
                padding: 10px 10px;
                border: 1px solid $border-color;
                border-radius: 10px;
                font-family: 'consolas';
                font-size: 16pt;
                font-weight: 500;
                text-align: center;
                background: $light1-color;
                color: $text-dark-color;
                qproperty-alignment: AlignCenter;
            }

            QLineEdit:focus {
                border-color: $primary1-color;
            }
        """)

        # combo box

        self.combo_box2: str = self._compile("""
            QComboBox {
                padding: 10px 10px;
                border: 1px solid $border-color;
                border-radius: 10px;
                font-family: $font-family;
                font-size: 16pt;
                font-weight: 500;
                text-align: center;
                background: $light1-color;
                color: $text-dark-color;
                combobox-popup: 0;
            }

            QComboBox:focus {
                border-color: $primary1-color;
            }

            QComboBox::drop-down {
                width: 20px;
                border-left: 1px solid $border-color;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
                subcontrol-origin: padding;
                subcontrol-position: right;
                image: url(assets/arrow_drop_down.svg);
            }

            QAbstractItemView {
                border: 1px solid $border-color;
                border-radius: 10px;
                background: $light1-color;
                color: $text-dark-color;
                outline: none;
            }

            QAbstractItemView::item {
                padding: 10px 10px;
                border-radius: 10px;
                font-family: $font-family;
                font-size: 16pt;
                font-weight: 500;
                text-align: center;
                background: $light1-color;
                color: $text-dark-color;
            }

            QAbstractItemView::item:selected {
                background: $primary1-color;
                color: $text-light-color;
            }

        """)

        # spin box

        self.double_spin_box2: str = self._compile("""
            QDoubleSpinBox {
                padding: 10px 10px;
                border: 1px solid $border-color;
                border-radius: 10px;
                font-family: $font-family;
                font-size: 16pt;
                font-weight: 500;
                text-align: center;
                background: $light1-color;
                color: $text-dark-color;
            }

            QDoubleSpinBox:focus {
                border-color: $primary1-color;
            }

            QDoubleSpinBox::up-button {
                width: 20px;
                border-left: 1px solid $border-color;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
                subcontrol-origin: padding;
                subcontrol-position: right top;
                image: url(assets/arrow_drop_up.svg);
            }

            QDoubleSpinBox::down-button {
                width: 20px;
                border-left: 1px solid $border-color;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
                subcontrol-origin: padding;
                subcontrol-position: right bottom;
                image: url(assets/arrow_drop_down.svg);
                background: $light1-color;
            }

            QDoubleSpinBox::down-button:hover, QDoubleSpinBox::up-button:hover {
                background: $light2-color;
            }

            QDoubleSpinBox::down-button:pressed, QDoubleSpinBox::up-button:pressed {
                background: $light3-color;
            }
        """)

        # table

        self.table: str = self._compile("""
            QTableView {
                border: none;
                font-family: $font-family;
                font-size: 14pt;
                font-weight: 500;
                background: $light1-color;
                color: $text-dark-color;
                selection-background-color: $light2-color;
                selection-color: $text-dark-color;
                gridline-color: $light1-color;
            }

            QHeaderView::section {
                padding: 5px;
                border: none;
                font-size: 10pt;
                font-weight: 600;
                letter-spacing: 1px;
                text-transform: uppercase;
                text-align: left;
                background-color: $light3-color;
            }

            QHeaderView::down-arrow {
                width: 15px;
                subcontrol-origin: padding;
                subcontrol-position: right;
                image: url(assets/arrow_drop_down.svg);
                background: $light3-color;
            }

            QHeaderView::up-arrow {
                width: 15px;
                subcontrol-origin: padding;
                subcontrol-position: right;
                image: url(assets/arrow_drop_up.svg);
                background: $light3-color;
            }
                                        
            QHeaderView::section:first {
                border-top-left-radius: 10px
            }

            QHeaderView::section:last {
                border-top-right-radius: 10px
            }

            QScrollBar:vertical {
                border: 0 solid red;
                border-radius: 5px;
                background:$light3-color;
                width:15px;
                margin: 0px 0px 0px 5px;
            }

            QScrollBar::handle:vertical {
                border-radius: 3px;
                background: $primary1-color;
                min-height: 50px;
                margin: 2px;
            }

            QScrollBar::add-line:vertical {
                background: blue;
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:vertical {
                background: green;
                height: 0 px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }

        """)

        # text

        self.title: str = self._compile("""
            QLabel {
                font-family: $font-family;
                font-size: 26pt;
                font-weight: 600;
                text-align: center;
                color: $text-dark-color;
                qproperty-alignment: AlignCenter;
            }
        """)

        self.colored_title: str = self._compile("""
            QLabel {
                padding-top: 12px;
                border-top: 3px solid $primary1-color;
                font-family: $font-family;
                font-size: 26pt;
                font-weight: 600;
                text-align: center;
                color: $text-dark-color;
                qproperty-alignment: AlignCenter;
            }
        """)

        self.heading1: str = self._compile("""
            QLabel {
                font-family: $font-family;
                font-size: 18pt;
                font-weight: 500;
                text-align: center;
                color: $text-dark-color;
                qproperty-alignment: AlignCenter;
            }
        """)

        self.heading2: str = self._compile("""
            QLabel {
                font-family: $font-family;
                font-size: 16pt;
                font-weight: 500;
                text-align: center;
                color: $text-dark-color;
                qproperty-alignment: AlignCenter;
            }
        """)

        self.script: str = self._compile("""
            QLabel {
                font-family: $font-family;
                font-size: 10pt;
                font-weight: 500;
                text-align: center;
                color: $text-dark-color;
                qproperty-alignment: AlignCenter;
            }
        """)

    def _compile(self, style) -> str:
        return sass.compile(string=self.variables + style)


qss: Qss = Qss()
