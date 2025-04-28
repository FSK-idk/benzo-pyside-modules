from PySide6.QtGui import QValidator


class HolderNameValidator(QValidator):
    def validate(self, string, pos):
        return QValidator.State.Acceptable, string.upper(), pos
