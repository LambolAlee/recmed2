from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from ._ui.fieldkey_ui import Ui_FieldKey
from recmedtyping import getIcon, RMIconType



class FieldKey(QWidget, Ui_FieldKey):
    deleteFieldSignal = Signal()

    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._text = ""
        self.deleteButton.setIcon(getIcon(RMIconType.trashCan))
        self.deleteButton.clicked.connect(self.deleteFieldSignal)

    def value(self) -> str:
        return self._text

    def setValue(self, value: str):
        self._text = value
