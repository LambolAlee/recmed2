from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from ._ui.fieldline_ui import Ui_FieldLine
from recmedtyping import getIcon, RMIconType



class FieldLine(QWidget, Ui_FieldLine):
    deleteFieldSignal = Signal()

    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.deleteButton.setIcon(getIcon(RMIconType.trashCan))
        self.deleteButton.clicked.connect(self.deleteFieldSignal)

    def value(self) -> str:
        return self.valueLineEdit.text()

    def setValue(self, value: str):
        self.valueLineEdit.setText(value)
