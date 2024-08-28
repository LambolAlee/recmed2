from math import sqrt, sin, cos, asin, copysign
from typing import Tuple

from PySide6.QtCore import Qt, QSize, QRect, QPoint, Signal
from PySide6.QtGui import QColor, QConicalGradient, QMouseEvent, QPen, QBrush, QPainter, QPaintEvent, QLinearGradient, QPainterPath
from PySide6.QtWidgets import QWidget



class DPoint(QPoint):
    def __abs__(self):
        return self.x() **2 + self.y() **2



class ColorWheel(QWidget):
    colorSelectionChanged = Signal(QColor)

    def __init__(self, centerX: int, centerY: int, meanRadius: int, wheelWidth: int, parent: QWidget | None=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.Popup)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.center = QPoint(centerX, centerY)
        self.meanRadius = meanRadius
        self.wheelWidth = wheelWidth

        marginBetweenSquareAndWheel = 2.0
        squareLength = sqrt(2) * (self.meanRadius - self.wheelWidth / 2) - marginBetweenSquareAndWheel
        self._square = QRect(centerX - squareLength / 2, centerY - squareLength / 2, squareLength, squareLength)
        self._inWheel = False
        self._inSquare = False
        self._wheelCursor = QPoint(self.meanRadius + centerX, centerY)
        self._squareCursor = self._square.topRight()

        self._currentWheelColor = QColor("blue")
        self._currentSquareColor = QColor("blue")

        outerR = self.meanRadius + self.wheelWidth / 2
        self._outerR2 = outerR **2
        self._innerR2 = (self.meanRadius - self.wheelWidth / 2) **2

        self.setFixedSize(centerX*2, centerY*2)

    def color(self) -> QColor:
        return self._currentSquareColor

    @classmethod
    def popup(cls, pos: QPoint):
        w = cls(100, 100, 80, 22)
        w.move(pos)
        return w

    def _makeWheelBrush(self) -> QBrush:
        gradient = QConicalGradient(self.center, 60)
        gradient.setColorAt(0.0, Qt.GlobalColor.yellow)
        gradient.setColorAt(1.0/6.0 * 1, Qt.GlobalColor.red)
        gradient.setColorAt(1.0/6.0 * 2, Qt.GlobalColor.magenta)
        gradient.setColorAt(1.0/6.0 * 3, Qt.GlobalColor.cyan)
        gradient.setColorAt(1.0/6.0 * 4, Qt.GlobalColor.green)
        gradient.setColorAt(1.0/6.0 * 5, Qt.GlobalColor.blue)
        gradient.setColorAt(1.0, Qt.GlobalColor.yellow)

        return QBrush(gradient)

    def _drawGradWheel(self, painter: QPainter):
        painter.save()
        pen = QPen(self._makeWheelBrush(), self.wheelWidth, Qt.PenStyle.SolidLine, Qt.PenCapStyle.SquareCap)
        painter.setPen(pen)
        painter.drawEllipse(self.center, self.meanRadius, self.meanRadius)
        painter.restore()

    def _drawCursorFor(self, cursor: QPoint, painter: QPainter):
        painter.save()
        innerR = self.wheelWidth / 8
        outerR = innerR + self.wheelWidth / 10

        innerPath = QPainterPath()
        innerPath.addEllipse(cursor, innerR, innerR)

        outerPath = QPainterPath()
        outerPath.addEllipse(cursor, outerR, outerR)

        ringPath = outerPath - innerPath

        pen = QPen(Qt.GlobalColor.black)
        painter.setPen(pen)
        painter.setBrush(Qt.GlobalColor.white)
        painter.drawPath(ringPath)
        painter.restore()

    def _makeSquareBrush(self) -> Tuple[QBrush, QBrush]:
        gradWhite = QLinearGradient(self._square.topLeft(), self._square.topRight())
        gradWhite.setColorAt(0.0, Qt.GlobalColor.white)
        gradWhite.setColorAt(0.1, Qt.GlobalColor.white)
        gradWhite.setColorAt(1.0, self._currentWheelColor)

        gradBlack = QLinearGradient(self._square.topLeft(), self._square.bottomLeft())
        gradBlack.setColorAt(0.0, Qt.GlobalColor.transparent)
        gradBlack.setColorAt(0.1, Qt.GlobalColor.transparent)
        gradBlack.setColorAt(1.0, Qt.GlobalColor.black)

        return QBrush(gradWhite), QBrush(gradBlack)

    def _drawGradSquare(self, painter: QPainter):
        painter.save()
        painter.setPen(Qt.PenStyle.NoPen)
        gradWhite, gradBlack = self._makeSquareBrush()

        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Source)
        painter.setBrush(gradWhite)
        painter.drawRect(self._square)

        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        painter.setBrush(gradBlack)
        painter.drawRect(self._square)
        painter.restore()

    def _calculateWheelCursor(self, center2MouseVector: DPoint) -> QPoint:
        distance = sqrt(abs(center2MouseVector))
        radian = asin(center2MouseVector.y() / distance)
        sign = copysign(1, center2MouseVector.x())

        return self.center + QPoint(sign*self.meanRadius*cos(radian), self.meanRadius*sin(radian))

    def _calculateSquareCursor(self, mousePos: QPoint) -> QPoint:
        calculatedX = min(max(self._square.topLeft().x(), mousePos.x()), self._square.topRight().x())
        calculatedY = min(max(self._square.topLeft().y(), mousePos.y()), self._square.bottomLeft().y())
        return QPoint(calculatedX, calculatedY)

    def _pickWheelColor(self) -> QColor:
        self._currentWheelColor = QColor.fromRgb(self.grab(QRect(self._wheelCursor, QSize(1, 1))).toImage().pixel(0, 0))

    def _pickSquareColor(self) -> QColor:
        self._currentSquareColor = QColor.fromRgb(self.grab(QRect(self._squareCursor, QSize(1, 1))).toImage().pixel(0, 0))

    def paintEvent(self, _: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        self._drawGradWheel(painter)
        self._drawCursorFor(self._wheelCursor, painter)
        self._drawGradSquare(painter)
        self._drawCursorFor(self._squareCursor, painter)

    def _locateMouseAndUpdate(self, mousePos: QPoint, zone: str, criteria: callable, *args):
        def emptyF(*_):
            return

        def _handleSquare():
            self._inSquare = True
            self._squareCursor = self._calculateSquareCursor(mousePos)
            self._pickSquareColor()

        def _handleWheel():
            self._inWheel = True
            self._wheelCursor = self._calculateWheelCursor(*args)
            self._pickWheelColor()
            self._pickSquareColor()

        d = {"square": _handleSquare, "wheel": _handleWheel}
        if criteria(*args):
            d[zone]()
            self.update()
            return emptyF
        else:
            return lambda zone, criteria, *args: self._locateMouseAndUpdate(mousePos, zone, criteria, *args)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        mousePos = event.position().toPoint()

        self._locateMouseAndUpdate(
            mousePos, "square", 
            lambda *_: self._square.contains(mousePos)
        )(
            "wheel",
            lambda center2MouseVector: self._innerR2 < abs(center2MouseVector) < self._outerR2,
            DPoint(mousePos - self.center)
        )

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        mousePos = event.position().toPoint()

        self._locateMouseAndUpdate(
            mousePos, "square",
            lambda *_: self._inSquare,
        )(
            "wheel",
            lambda *_: self._inWheel,
            DPoint(mousePos - self.center)
        )

    def mouseReleaseEvent(self, _: QMouseEvent) -> None:
        self._inWheel = False
        self._inSquare = False
        self.colorSelectionChanged.emit(self._currentSquareColor)
