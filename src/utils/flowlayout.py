"""
Flowlayout python version
translate from https://doc.qt.io/qt-5/qtwidgets-layouts-flowlayout-example.html
"""
from typing import List

from PySide6.QtCore import Qt, QRect, QSize, QMargins, QObject, QPoint
from PySide6.QtWidgets import QLayout,QWidget, QLayoutItem, QStyle, QSizePolicy



class FlowLayout(QLayout):
    def __init__(self, parent: QWidget | None=None, margin: int=-1, hSpacing: int=-1, vSpacing: int=-1) -> None:
        super().__init__(parent)
        self._hSpace = hSpacing
        self._vSpace = vSpacing
        self.itemList: List[QLayoutItem] = []

        self.setContentsMargins(margin, margin, margin, margin)

    def __del__(self):
        self.itemList.clear()

    def addItem(self, item: QLayoutItem):
        self.itemList.append(item)

    def horizontalSpacing(self) -> int:
        if self._hSpace >= 0:
            return self._hSpace
        else:
            return self.smartSpacing(QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self) -> int:
        if self._vSpace >= 0:
            return self._vSpace
        else:
            return self.smartSpacing(QStyle.PM_LayoutVerticalSpacing)

    def expandingDirections(self) -> Qt.Orientation:
        return Qt.Orientation(0)

    def hasHeightForWidth(self) -> bool:
        return True

    def heightForWidth(self, width: int) -> int:
        return self.doLayout(QRect(0, 0, width, 0), True)

    def count(self) -> int:
        return len(self.itemList)

    def itemAt(self, index: int) -> QLayoutItem | None:
        try:
            return self.itemList[index]
        except IndexError:
            return None

    def takeAt(self, index: int) -> QLayoutItem | None:
        try:
            return self.itemList.pop(index)
        except IndexError:
            return None

    def minimumSize(self) -> QSize:
        size = QSize()
        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margins: QMargins = self.contentsMargins()
        size += QSize(margins.left() + margins.right(), margins.top() + margins.bottom())
        return size

    def setGeometry(self, rect: QRect) -> None:
        super().setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self) -> QSize:
        return self.minimumSize()

    def takeAt(self, index: int) -> QLayoutItem | None:
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)
        else:
            return None

    def doLayout(self, rect: QRect, testOnly: bool) -> int:
        left, top, right, bottom = self.getContentsMargins()
        effectiveRect = rect.adjusted(+left, +top, -right, -bottom)
        x = effectiveRect.x()
        y = effectiveRect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.horizontalSpacing()
            if spaceX == -1:
                spaceX = wid.style().layoutSpacing(
                    QSizePolicy.ControlType.PushButton, QSizePolicy.ControlType.PushButton, Qt.Horizontal)
            spaceY = self.verticalSpacing()
            if spaceY == -1:
                spaceY = wid.style().layoutSpacing(
                    QSizePolicy.ControlType.PushButton, QSizePolicy.ControlType.PushButton, Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > effectiveRect.right() and lineHeight > 0:
                x = effectiveRect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y() + bottom

    def smartSpacing(self, pm: QStyle.PixelMetric) -> int:
        parent: QObject= self.parent()
        if not parent:
            return -1
        elif parent.isWidgetType():
            return parent.style().pixelMetric(pm, None, parent)
        else:
            return parent.spacing()
