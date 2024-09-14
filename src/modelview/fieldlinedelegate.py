from typing import Union, cast

from PySide6.QtCore import Qt, QModelIndex, QPersistentModelIndex, QAbstractItemModel, Signal
from PySide6.QtGui import QPainter, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QStyledItemDelegate, QWidget, QStyleOptionViewItem, QStyle

from ui.fieldline import FieldLine



class FieldLineDelegate(QStyledItemDelegate):
    deleteFieldSignal = Signal(QStandardItem)

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]):
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)

        if opt.state & QStyle.StateFlag.State_HasFocus:
            opt.state &= ~QStyle.StateFlag.State_HasFocus

        style = option.widget.style() if option.widget else qApp.style()
        style.drawControl(QStyle.ControlElement.CE_ItemViewItem, opt, painter, option.widget)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]) -> QWidget:
        editor = FieldLine(parent)
        model: QStandardItemModel = index.model()
        item: QStandardItem = model.itemFromIndex(index)
        editor.deleteFieldSignal.connect(lambda item=item: self.deleteFieldSignal.emit(item))
        return editor

    def setEditorData(self, editor: QWidget, index: Union[QModelIndex, QPersistentModelIndex]) -> None:
        editor = cast(FieldLine, editor)
        editor.setValue(index.data(Qt.ItemDataRole.DisplayRole))

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: Union[QModelIndex, QPersistentModelIndex]) -> None:
        editor = cast(FieldLine, editor)
        model.setData(index, editor.value(), Qt.ItemDataRole.DisplayRole)

    def updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]) -> None:
        editor.setGeometry(option.rect)
