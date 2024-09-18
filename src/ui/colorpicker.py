from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QLabel, QFrame

from utils import fillPlaceholderWidget
from .colorwheel import ColorWheel



class ColorPicker(QWidget):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.Popup)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setupUi()
        self.onColorChanged(self.colorWheel.color())

        self.colorWheel.colorSelectionChanged.connect(self.onColorChanged)
        # self.previewLabel.setFixedWidth(80)

    def setupUi(self):
        colorWheelLayout = QVBoxLayout()
        self.previewLabel = QLabel(self)
        self.previewLabel.setFixedHeight(30)
        self.previewLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.previewLabel.setFrameShape(QFrame.Shape.Box)
        self.colorWheel = ColorWheel(100, 100, 80, 22, self)
        colorWheelLayout.addWidget(self.colorWheel)
        colorWheelLayout.addWidget(self.previewLabel)
        colorWheelLayout.setStretch(0, 1)
        self.setLayout(colorWheelLayout)

    def onColorChanged(self, color: QColor):
        self.previewLabel.setText(color.name())
        self.previewLabel.setStyleSheet(f"background-color: {color.name()};")
