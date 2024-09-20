from PySide6.QtCore import Qt, Signal, QPoint
from PySide6.QtGui import QColor, QKeyEvent, QMouseEvent
from PySide6.QtWidgets import QWidget, QDialogButtonBox, QVBoxLayout

from .colorpicker import ColorPicker



class ColorPickerPopup(QWidget):
    colorSelectionChanged = Signal(QColor)
    colorDecided = Signal(QColor)
    cancelled = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.Popup)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        layout = QVBoxLayout()
        self.colorPicker = ColorPicker(parent=self)
        self.colorPicker.colorChanged.connect(self.colorSelectionChanged)
        layout.addWidget(self.colorPicker)

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
    
    def setCurrentColor(self, color: QColor):
        self.colorPicker.setColor(color)

    def onButtonBoxAccepted(self) -> None:
        self.colorDecided.emit(self.colorPicker.color)
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
                self.colorDecided.emit(self.colorPicker.color)
                self.close()
            case Qt.Key.Key_Escape:
                self.cancelled.emit()
                self.close()
            case _:
                return super().keyReleaseEvent(event)
