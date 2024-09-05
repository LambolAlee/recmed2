from PySide6.QtCore import Qt, Signal, QPoint
from PySide6.QtGui import QColor, QKeyEvent, QMouseEvent
from PySide6.QtWidgets import QWidget, QDialogButtonBox, QVBoxLayout

from .colorwheel import ColorWheel



class ColorWheelPopup(QWidget):
    colorSelectionChanged = Signal(QColor)
    colorDecided = Signal(QColor)
    cancelled = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.Popup)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        layout = QVBoxLayout()
        self.colorWheel = ColorWheel(100, 100, 80, 22, self)
        self.colorWheel.colorSelectionChanged.connect(self.colorSelectionChanged)
        layout.addWidget(self.colorWheel)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.accepted.connect(self.onButtonBoxAccepted)
        self.buttonBox.rejected.connect(self.onButtonBoxRejected)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

    @classmethod
    def popup(cls, pos: QPoint):
        w = cls()
        w.move(pos)
        return w

    def onButtonBoxAccepted(self) -> None:
        self.colorDecided.emit(self.colorWheel.color())
        self.close()

    def onButtonBoxRejected(self) -> None:
        self.cancelled.emit()
        self.close()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if not self.rect().contains(event.position().toPoint()):
            self.cancelled.emit()
        return super().mousePressEvent(event)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        match event.key():
            case Qt.Key.Key_Return:
                self.colorDecided.emit(self.colorWheel.color())
                self.close()
            case Qt.Key.Key_Escape:
                self.cancelled.emit()
                self.close()
            case _:
                return super().keyReleaseEvent(event)
