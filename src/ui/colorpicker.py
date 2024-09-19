from PySide6.QtCore import Qt, QRect, QPoint, QSize, Signal
from PySide6.QtGui import QMouseEvent, QPaintEvent, QPainter, QPainterPath, QColor, QLinearGradient, QBrush, QPixmap
from PySide6.QtWidgets import QWidget



DEFAULT_COLOR = QColor(Qt.GlobalColor.white)



class ColorPreview(QWidget):
    def __init__(self, color: QColor=DEFAULT_COLOR, parent: QWidget | None=None):
        super().__init__(parent)
        self.setFixedSize(40, 256)

        self._previewColor: QColor = color

    def paintEvent(self, _: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.fillRect(self.rect(), QBrush(self._previewColor))

    def preview(self, color: QColor):
        self._previewColor = color
        self.update()



class ColorSquareWithCircleCursor(QWidget):
    """
    The abstract class for drawing a color square with a circle cursor / slider
    """
    def __init__(self, parent: QWidget | None=None):
        super().__init__(parent)

        self._cursorInnerR = 5.0
        self._cursorOuterR = 8.0
        self._background: QPixmap = None
        self._moveCursorInRect = False

        # need to override the attribute in subclass
        self._cursorPos = None

    # override
    def calcUnderCursor(self) -> None:
        raise NotImplementedError

    # override
    def constraint(self, mousePos: QPoint) -> QPoint:
        raise NotImplementedError

    # override
    def drawBackgroundGradient(self, painter: QPainter) -> None:
        raise NotImplementedError

    # override
    def drawCursor(self, painter: QPainter) -> None:
        raise NotImplementedError

    def _clearBackground(self) -> None:
        self._background = None
        self.update()

    def _aboutToMoveCursor(self) -> None:
        self._moveCursorInRect = True

    def _stopMovingCursor(self) -> None:
        self._moveCursorInRect = False

    def _inRect(self) -> bool:
        return self._moveCursorInRect
    
    def paintEvent(self, _: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.drawBackgroundGradient(painter)
        self.drawCursor(painter)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        pos = event.position().toPoint()
        if self.rect().contains(pos):
            self._aboutToMoveCursor()
            self._cursorPos = pos
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        pos = event.position().toPoint()
        if self._inRect():
            self._cursorPos = self.constraint(pos)
            self.update()
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if self._inRect():
            self._stopMovingCursor()
            self.calcUnderCursor()
        return super().mouseReleaseEvent(event)



class ColorHSSelector(ColorSquareWithCircleCursor):
    colorChanged = Signal(QColor)

    def __init__(self, parent: QWidget | None=None):
        super().__init__(parent)
        self.setFixedSize(256, 256)

        self._selectedColor: QColor = DEFAULT_COLOR
        self._cursorPos = self.rect().bottomLeft()

    def color(self) -> QColor:
        return self._selectedColor

    def calcUnderCursor(self) -> None:
        x, y = self._cursorPos.x(), self._cursorPos.y()
        self._selectedColor = QColor.fromHsv(x * 360.0 / self.width(), 255 - y * 255.0 / self.height(), 255)
        self.colorChanged.emit(self._selectedColor)
        self.update()

    def drawBackgroundGradient(self, painter: QPainter) -> None:
        if self._background is None:
            self._background = QPixmap(self.rect().size())
            bgPainter = QPainter(self._background)

            gradH = QLinearGradient(self.rect().topLeft(), self.rect().topRight())
            gradH.setColorAt(0.0 / 360.0, Qt.GlobalColor.red)
            gradH.setColorAt(60.0 / 360.0, Qt.GlobalColor.yellow)
            gradH.setColorAt(120.0 / 360.0, Qt.GlobalColor.green)
            gradH.setColorAt(180.0 / 360.0, Qt.GlobalColor.cyan)
            gradH.setColorAt(240.0 / 360.0, Qt.GlobalColor.blue)
            gradH.setColorAt(300.0 / 360.0, Qt.GlobalColor.magenta)
            gradH.setColorAt(360.0 / 360.0, Qt.GlobalColor.red)

            bgPainter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Source)
            bgPainter.fillRect(self._background.rect(), QBrush(gradH))

            gradV = QLinearGradient(self.rect().topLeft(), self.rect().bottomLeft())
            gradV.setColorAt(0.0, Qt.GlobalColor.transparent)
            gradV.setColorAt(1.0, QColor.fromHsv(0, 0, 255))

            bgPainter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
            bgPainter.fillRect(self._background.rect(), QBrush(gradV))
            bgPainter.end()

        painter.drawPixmap(0,0, self._background)

    def drawCursor(self, painter: QPainter) -> None:
        innerPath = QPainterPath()
        innerPath.addEllipse(self._cursorPos, self._cursorInnerR, self._cursorInnerR)
        outerPath = QPainterPath()
        outerPath.addEllipse(self._cursorPos, self._cursorOuterR, self._cursorOuterR)
        ringPath = outerPath - innerPath

        painter.save()
        painter.fillPath(ringPath, QBrush(Qt.GlobalColor.black))
        painter.restore()

    def constraint(self, mousePos: QPoint) -> QPoint:
        calculatedX = min(max(self.rect().topLeft().x(), mousePos.x()), self.rect().topRight().x())
        calculatedY = min(max(self.rect().topLeft().y(), mousePos.y()), self.rect().bottomLeft().y())
        return QPoint(calculatedX, calculatedY)



class ColorValueSelector(ColorSquareWithCircleCursor):
    valueChanged = Signal(float)

    def __init__(self, width: int=100, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setFixedHeight(12)

        self.setWidth(width)

        self._basicColor = DEFAULT_COLOR
        # self._basicColor = QColor("#FFCBE4")

    def setBasicColor(self, color: QColor):
        if self._basicColor == color:
            return

        self._basicColor = color
        self._clearBackground()

    def setWidth(self, width: int):
        self.setFixedWidth(width)
        tr = self.rect().topRight()
        self._cursorPos = QPoint(tr.x() - self._cursorOuterR, tr.y() + self.rect().height() / 2)
        self._effectiveLength = self.rect().width() - 2 * self._cursorOuterR
        self.update()

    def calcUnderCursor(self) -> None:
        self.valueChanged.emit(255 - (self._cursorPos.x() - self._cursorOuterR) / self._effectiveLength * 255)
        self.update()

    def constraint(self, mousePos: QPoint) -> QPoint:
        calculatedX = min(max(self.rect().topLeft().x() + self._cursorOuterR, mousePos.x()), self.rect().topRight().x() - self._cursorOuterR)
        calculatedY = self.rect().height() / 2
        return QPoint(calculatedX, calculatedY)

    def drawBackgroundGradient(self, painter: QPainter):
        if self._background is None:
            self._background = QPixmap(self.rect().size())
            self._background.fill(Qt.GlobalColor.transparent)
            bgPainter = QPainter(self._background)
            path = QPainterPath()
            path.addRoundedRect(self._background.rect(), 6, 6)

            grad = QLinearGradient(self.rect().topLeft(), self.rect().topRight())
            grad.setColorAt(0.0, Qt.GlobalColor.black)
            grad.setColorAt(1.0, Qt.GlobalColor.transparent)

            bgPainter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Source)
            bgPainter.fillPath(path, QBrush(self._basicColor))
            bgPainter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
            bgPainter.fillPath(path, QBrush(grad))
            bgPainter.end()

        painter.drawPixmap(0,0, self._background)

    def drawCursor(self, painter: QPainter) -> None:
        innerPath = QPainterPath()
        innerPath.addEllipse(self._cursorPos, self._cursorInnerR, self._cursorInnerR)
        outerPath = QPainterPath()
        outerPath.addEllipse(self._cursorPos, self._cursorOuterR, self._cursorOuterR)

        painter.save()
        painter.fillPath(outerPath, QBrush(Qt.GlobalColor.white))
        painter.fillPath(innerPath, QBrush(Qt.GlobalColor.black))
        painter.restore()



class ColorPicker(QWidget):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
