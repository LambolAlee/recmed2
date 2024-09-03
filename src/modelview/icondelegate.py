"""
From Source: https://github.com/Liniyous/ElaWidgetTools/blob/main/example/ModelView/T_IconDelegate.cpp
"""
from PySide6.QtCore import QObject, QModelIndex, Qt, QSize
from PySide6.QtGui import QPainter, QFont
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QStyle

from recmedtyping import RMIconType



class IconDelegate(QStyledItemDelegate):
    def __init__(self, parent: QObject | None=None) -> None:
        super().__init__(parent)

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)

        if option.state & QStyle.StateFlag.State_HasFocus:
            opt.state &= ~QStyle.StateFlag.State_HasFocus
        super().paint(painter, opt, index)

        icon = RMIconType[index.data(Qt.ItemDataRole.UserRole)]
        painter.save()
        painter.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform)
        painter.save()
        iconfont = QFont(qApp.IconFontName)
        iconfont.setPixelSize(22)
        painter.setFont(iconfont)
        painter.drawText(option.rect.x()+option.rect.width()/2-11, option.rect.y()+option.rect.height()/2-11, icon.value)
        painter.restore()

        painter.setPen(Qt.GlobalColor.black)
        titlefont = painter.font()
        titlefont.setPixelSize(13)
        painter.setFont(titlefont)
        rowWidth = option.rect.width() * 0.8
        subTitleRow = min(2, painter.fontMetrics().horizontalAdvance(icon.name) / rowWidth)
        if subTitleRow > 0:
            subTitle = icon.name
            i = 0
            while i < subTitleRow:
                text = painter.fontMetrics().elidedText(subTitle, Qt.TextElideMode.ElideRight, rowWidth)
                if text.endswith('…') and i < subTitleRow-1:
                    text = text.replace('…', subTitle[len(text)-1])
                subTitle = subTitle.replace(text, '')
                painter.drawText(option.rect.x()+option.rect.width()/2-painter.fontMetrics().horizontalAdvance(text)/2, option.rect.y() +option.rect.height()-15*(subTitleRow+1-i), text)
                i += 1
        else:
            painter.drawText(option.rect.x()+option.rect.width()/2-painter.fontMetrics().horizontalAdvance(icon.name)/2, option.rect.y() +option.rect.height()-30, icon.name)
        painter.restore()

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize:
        return QSize(100, 100)
