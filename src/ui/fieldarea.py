from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QWidget

from ._ui.fieldarea_ui import Ui_FieldArea
from modelview.fieldlinedelegate import FieldLineDelegate
from modelview.fieldmodel import FieldModel



class FieldArea(QWidget, Ui_FieldArea):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._editMode = False
        self._model = FieldModel(self)
        self._delegate = FieldLineDelegate(self)

        self.fieldContainerView.horizontalHeader().setStretchLastSection(True)
        self.fieldContainerView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fieldContainerView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fieldContainerView.setModel(self._model)
        self.fieldContainerView.setItemDelegate(self._delegate)

        self.keyLineEdit.setPlaceholderText("Key content")
        self.valueLineEdit.setPlaceholderText("Value content")

        self.addButton.clicked.connect(self.addField)
        self.keyLineEdit.returnPressed.connect(self.addField)
        self.valueLineEdit.returnPressed.connect(self.addField)
        self._delegate.deleteFieldSignal.connect(self.deleteField)

        self.resizeToContents()
        self.setVisible(False)

    def addField(self):
        if self.keyLineEdit.text() == "":
            return

        key = QStandardItem(self.keyLineEdit.text() + ":")
        value = QStandardItem(self.valueLineEdit.text())
        self._model.appendRow([key, value])
        self.fieldContainerView.openPersistentEditor(self._model.indexFromItem(key))

        self.resizeToContents()
        self.keyLineEdit.clear()
        self.valueLineEdit.clear()
        self.keyLineEdit.setFocus()

    def deleteField(self, item: QStandardItem):
        self._model.removeRow(item.row())
        self.resizeToContents()

    def resizeToContents(self) -> None:
        self.fieldContainerView.resizeColumnToContents(0)

        height = sum(self.fieldContainerView.rowHeight(i) for i in range(self._model.rowCount()))
        self.fieldContainerView.setFixedHeight(height + 1)      # add 1 can display a slim solid line when there is no user-defined field
