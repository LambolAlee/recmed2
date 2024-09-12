from typing import Union, cast

from PySide6.QtCore import QObject, Qt, QModelIndex, QRect, QEvent, QPersistentModelIndex, QAbstractItemModel, QSize
from PySide6.QtGui import QPainter, QMouseEvent
from PySide6.QtWidgets import QStyledItemDelegate, QStyle, QStyleOptionButton, QStyleOptionViewItem

from recmedtyping import getIcon, RMIconType



class FieldLineDelegate(QStyledItemDelegate):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self._buttonSize = 32
        self._iconSize = 16

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)

        if opt.state & QStyle.StateFlag.State_HasFocus:
            opt.state &= ~QStyle.StateFlag.State_HasFocus

        style: QStyle = option.widget.style() if option.widget else qApp.style()
        style.drawControl(QStyle.ControlElement.CE_ItemViewItem, opt, painter, opt.widget)

        buttonOption = QStyleOptionButton()
        buttonOption.rect = self.getToolButtonRect(option)
        buttonOption.icon = getIcon(RMIconType.trashCan)
        buttonOption.iconSize = QSize(self._iconSize, self._iconSize)
        style.drawControl(QStyle.ControlElement.CE_PushButton, buttonOption, painter, option.widget)

    def getToolButtonRect(self, option: QStyleOptionViewItem) -> QRect:
        return QRect(option.rect.right() - self._buttonSize, option.rect.top(), self._buttonSize, option.rect.height())

    def editorEvent(self, event: QEvent, model: QAbstractItemModel, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]) -> bool:
        if event.type() == QEvent.Type.MouseButtonRelease:
            event = cast(QMouseEvent, event)
            p = event.position().toPoint()
            if self.getToolButtonRect(option).contains(p):
                model.removeRow(index.row())

        return super().editorEvent(event, model, option, index)
