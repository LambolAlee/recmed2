from typing import Optional

from PySide6.QtCore import Qt, QPoint, Signal
from PySide6.QtGui import QMouseEvent, QPaintEvent, QPainter, QPainterPath, QColor, QLinearGradient, QBrush, QPixmap, QResizeEvent
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy



DEFAULT_COLOR = QColor(Qt.GlobalColor.white)



class ColorPreview(QWidget):
    def __init__(self, color: QColor=DEFAULT_COLOR, parent: QWidget | None=None):
        super().__init__(parent)
        self.setFixedSize(40, 256)

        self._previewColor = color

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

    # override
    def locate(self, color: QColor):
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
            self._cursorPos = self.constraint(pos)
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

        self.color: QColor = DEFAULT_COLOR
        self._cursorPos = self.rect().bottomLeft()

    def calcUnderCursor(self) -> None:
        x, y = self._cursorPos.x(), self._cursorPos.y()
        self.color = QColor.fromHsv(x * 360.0 / self.width(), 255 - y * 255.0 / self.height(), 255)
        self.colorChanged.emit(self.color)
        self.update()

    def locate(self, color: QColor):
        self.color = color
        self._cursorPos = QPoint(color.hsvHue() / 360.0 * self.width(), 255 - color.hsvSaturation() / 255.0 * self.height())
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
    valueChanged = Signal(int)

    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setFixedHeight(12)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.value = 255
        self._basicColor = DEFAULT_COLOR

    def setBasicColor(self, color: QColor):
        if self._basicColor == color:
            return

        self._basicColor = color
        self._clearBackground()

    def locate(self, color: QColor):
        basicColor = QColor.fromHsv(color.hsvHue(), color.hsvSaturation(), 255)
        self.value = color.value()
        if self.isVisible():
            self._cursorPos = QPoint(color.value() / 255 * self._effectiveLength + self._cursorOuterR, self.rect().height() / 2)
        self.setBasicColor(basicColor)

    def resizeEvent(self, event: QResizeEvent):
        tr = self.rect().topRight()
        self._effectiveLength = self.rect().width() - 2 * self._cursorOuterR
        if self.value == 255:
            self._cursorPos = QPoint(tr.x() - self._cursorOuterR, tr.y() + self.rect().height() / 2)
        else:
            self._cursorPos = QPoint(self.value / 255 * self._effectiveLength + self._cursorOuterR, self.rect().height() / 2)
        return super().resizeEvent(event)

    def calcUnderCursor(self) -> None:
        self.value = int((self._cursorPos.x() - self._cursorOuterR) / self._effectiveLength * 255)
        self.valueChanged.emit(self.value)
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
    colorChanged = Signal(QColor)

    def __init__(self, color: QColor | None=None, parent: QWidget | None=None) -> None:
        super().__init__(parent)

        hlayout = QHBoxLayout()
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(16)
        self.hsSelector = ColorHSSelector(self)
        self.colorPreview = ColorPreview(parent=self)
        hlayout.addWidget(self.hsSelector)
        hlayout.addWidget(self.colorPreview)

        vlayout = QVBoxLayout()
        vlayout.setSpacing(16)
        self.valueSelector = ColorValueSelector(self)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.valueSelector)

        self.setLayout(vlayout)

        self.setColor(color)

        self.hsSelector.colorChanged.connect(self.valueSelector.setBasicColor)
        self.hsSelector.colorChanged.connect(self.previewWithColorChanged)
        self.valueSelector.valueChanged.connect(self.previewWithValueChanged)

    def setColor(self, color: Optional[QColor]):
        if color is None:
            self.color = DEFAULT_COLOR
        else:
            self.color = color
            self.hsSelector.locate(color)
            self.valueSelector.locate(color)
            self.colorPreview.preview(color)

    def previewWithColorChanged(self, color: QColor):
        value = self.valueSelector.value
        self.color = QColor.fromHsv(color.hsvHue(), color.hsvSaturation(), value)
        self.colorPreview.preview(self.color)
        self.colorChanged.emit(self.color)

    def previewWithValueChanged(self, value: int):
        color = self.hsSelector.color
        self.color = QColor.fromHsv(color.hsvHue(), color.hsvSaturation(), value)
        self.colorPreview.preview(self.color)
        self.colorChanged.emit(self.color)
