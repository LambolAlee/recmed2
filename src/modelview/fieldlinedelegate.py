from typing import Union, cast

from PySide6.QtCore import QObject, QSize, Qt, QModelIndex, QPersistentModelIndex, QAbstractItemModel, Signal, QLocale
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFontMetrics, QPainter
from PySide6.QtWidgets import QStyledItemDelegate, QWidget, QStyleOptionViewItem, QLineEdit, QStyle

from ui.fieldkey import FieldKey



class FieldLineDelegate(QStyledItemDelegate):
    deleteFieldSignal = Signal(QStandardItem)

    def __init__(self, parent: QObject | None=None) -> None:
        super().__init__(parent)

        self._maxWidth = 0
        self._fontMetrics = None

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex | QPersistentModelIndex) -> None:
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)

        if opt.state & QStyle.StateFlag.State_HasFocus:
            opt.state &= ~QStyle.StateFlag.State_HasFocus

        super().paint(painter, opt, index)

    def displayText(self, value: str, locale: Union[QLocale, QLocale.Language]) -> str:
        return self._fontMetrics.elidedText(value, Qt.TextElideMode.ElideRight, 0.5 * self._maxWidth)    

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex | QPersistentModelIndex) -> QSize:
        if index.column() != 0:
            return super().sizeHint(option, index)

        text = index.data()
        self._maxWidth = option.widget.rect().width()
        self._fontMetrics = QFontMetrics(option.font)
        textWidth = self._fontMetrics.horizontalAdvance(text)

        padding = 60
        w = min(textWidth + padding, 0.7 * self._maxWidth)   
        return QSize(w, super().sizeHint(option, index).height())

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]) -> QWidget:
        if index.column() == 0:
            editor = FieldKey(parent)
            model: QStandardItemModel = index.model()
            item: QStandardItem = model.itemFromIndex(index)
            editor.deleteFieldSignal.connect(lambda item=item: self.deleteFieldSignal.emit(item))
            return editor
        return super().createEditor(parent, option, index)

    def setEditorData(self, editor: QWidget, index: QModelIndex | QPersistentModelIndex) -> None:
        if index.column() == 0:
            data = index.data(Qt.ItemDataRole.DisplayRole)
            editor = cast(FieldKey, editor)
            editor.setValue(data)
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: Union[QModelIndex, QPersistentModelIndex]) -> None:
        if index.column() == 0:
            editor = cast(FieldKey, editor)
            data = editor.value()
            model.setData(index, data, Qt.ItemDataRole.DisplayRole)
        else:
            super().setModelData(editor, model, index)

    def updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]) -> None:
        editor.setGeometry(option.rect)
