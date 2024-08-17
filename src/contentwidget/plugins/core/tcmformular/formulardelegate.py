from typing import cast

from PySide6.QtCore import QObject, QModelIndex, QAbstractItemModel, QEvent, QSize, Qt
from PySide6.QtGui import QPainter, QFontMetrics, QKeyEvent
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QWidget, QStyle

from .formularmodel import DrugObject
from .drugeditor import DrugEditor
from .drugcell import DrugCell



class FormularDelegate(QStyledItemDelegate):
    def __init__(self, parent: QObject | None = None):
        super().__init__(parent)
        self._middlePadding = 50#px
        self._cell = DrugCell()

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        assert index.isValid() is True

        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)

        if opt.state & QStyle.StateFlag.State_HasFocus:
            opt.state ^= QStyle.StateFlag.State_HasFocus

        style: QStyle = opt.widget.style() if opt.widget else qApp.style()
        style.drawControl(QStyle.ControlElement.CE_ItemViewItem, opt, painter, opt.widget)

        drugObj: DrugObject = index.data(Qt.ItemDataRole.DisplayRole)
        self._cell.renderCell(drugObj, painter, opt)

    # def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize:
    #     size = super().sizeHint(option, index)
    #     if not index.isValid():
    #         return size

    #     drugObj: DrugObject = index.model().maxLengthDrug()
    #     fontMetrics = QFontMetrics(option.font)

    #     width = fontMetrics.horizontalAdvance("".join((drugObj.name, str(drugObj.dose), drugObj.unit))) + self._middlePadding
    #     size.setWidth(max(size.width(), width))
    #     return size

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        editor = DrugEditor(parent)
        return editor

    def setEditorData(self, editor: QWidget, index):
        editor = cast(DrugEditor, editor)
        drugObj: DrugObject = index.data(Qt.ItemDataRole.EditRole)
        editor.setDrug(drugObj)

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: QModelIndex):
        if not index.isValid():
            return super().setModelData(editor, model, index)
        editor = cast(DrugEditor, editor)
        drugObj = editor.submit()
        if drugObj is None:
            return
        else:
            model.setData(index, drugObj, Qt.ItemDataRole.EditRole)

    def updateEditorGeometry(self, editor: QWidget | None, option: QStyleOptionViewItem, index: QModelIndex):
        if editor is None: 
            return
        assert index.isValid() is True
        editor = cast(DrugEditor, editor)
        editor.setGeometry(option.rect)
