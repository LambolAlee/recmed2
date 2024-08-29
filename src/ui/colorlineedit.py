from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QLineEdit

from utils.colorutils import colorLumaF, string2QColor


class ColorLineEdit(QLineEdit):
    def __init__(self, color: QColor | None= None, parent: QWidget | None=None):
        super().__init__(parent)
        if color is None:
            color = QColor("#79abc9")
        self.setColor(color, True)

        self.textEdited.connect(self.onTextEdited)
        self.editingFinished.connect(self.onEditingFinished)

    def onTextEdited(self, text: str):
        color = string2QColor(text, False)
        if color.isValid():
            self.setColor(color)

    def onEditingFinished(self):
        color = string2QColor(self.text(), False)
        if color.isValid():
            self.setColor(color)
        else:
            self.setColor(self.color)

    def setColor(self, color: QColor, save: bool=False):
        if save:
            self.color = color
        self.setText(color.name())
        self.fontColor = Qt.GlobalColor.black if colorLumaF(color) > 0.5 else Qt.GlobalColor.white
        self.setStyleSheet(f'background: {color.name()}; color: {self.fontColor.name};')

    def restore(self):
        self.setColor(self.color)
