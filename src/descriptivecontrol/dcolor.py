from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QBrush, QPixmap
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout

from .descriptor import DescriptiveAttr



class DColor(QWidget, DescriptiveAttr):
    def __init__(self) -> None:
        super(QWidget, self).__init__()
        super(DescriptiveAttr, self).__init__()

        self.background = QBrush()
        self.background.setTexture(QPixmap(":/colorwidget/alphaback"))

        self.textEdited.connect(self.onTextEdited)
        self.editingFinished.connect(self.onEditingFinished)

    def onTextEdited(self, text: str) -> None:
        self.setStyleSheet(f"background-color: {text}")

    def onEditingFinished(self) -> None:
        self.setStyleSheet("")
        self.setText(self.text())

