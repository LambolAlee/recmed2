from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QWidget, QHeaderView

from ._ui.fieldarea_ui import Ui_FieldArea
from modelview.fieldlinedelegate import FieldLineDelegate
from modelview.fieldmodel import FieldModel



class FieldArea(QWidget, Ui_FieldArea):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._editMode = False
        self._model = FieldModel(self)

        self.fieldContainerView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.fieldContainerView.setModel(self._model)
        self.fieldContainerView.setItemDelegateForColumn(1, FieldLineDelegate(self))

        self.keyLineEdit.setPlaceholderText("Key content")
        self.valueLineEdit.setPlaceholderText("Value content")

        self.addButton.clicked.connect(self.addField)

    def addField(self):
        if self.keyLineEdit.text() == "":
            return

        key = QStandardItem(self.keyLineEdit.text() + ":")
        value = QStandardItem(self.valueLineEdit.text())
        self._model.appendRow([key, value])

        self.keyLineEdit.clear()
        self.valueLineEdit.clear()
