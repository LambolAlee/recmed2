from typing import Self, Dict, Any

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QHBoxLayout, QToolButton

from .descriptor import DescriptiveAttr, DescriptiveWidget
from ui.colorlineedit import ColorLineEdit
from ui.colorwheel import ColorWheel
from recmedtyping import getIcon, RMIconType



class DColorWidget(DescriptiveWidget):
    def __init__(self, obj: "DColor", parent: QWidget | None=None):
        super().__init__(parent)
        self.attr = obj

    def build(self) -> Self:
        layout = QHBoxLayout()
        layout.setSpacing(0)
        self.lineEdit = ColorLineEdit(parent=self)
        self.lineEdit.setMinimumWidth(120)
        layout.addWidget(self.lineEdit)
        self.colorButton = QToolButton(parent=self)
        self.colorButton.setIcon(getIcon(RMIconType.palette))
        self.colorButton.setToolTip("Choose a color and press enter to select it")
        layout.addWidget(self.colorButton)
        self.setLayout(layout)

        self.colorButton.clicked.connect(self.onColorButtonClicked)
        return self

    def setData(self, **kwargs) -> Self:
        """
        color: QColor
        """
        for key, value in kwargs.items():
            if key == self.attr.public_name:
                self.lineEdit.setColor(value, True)
        return self

    def data(self) -> dict:
        return {self.attr.public_name: self.lineEdit.color}

    def onColorButtonClicked(self) -> None:
        self._popup = ColorWheel.popup(self.colorButton.mapToGlobal(self.colorButton.rect().bottomLeft()))
        self._popup.colorDecided.connect(lambda color: self.lineEdit.setColor(color, save=True))
        self._popup.colorSelectionChanged.connect(self.lineEdit.setColor)
        self._popup.cancelled.connect(self.lineEdit.restore)
        self._popup.show()


class DColor(DescriptiveAttr):
    def __init__(self, text: str, default: str) -> None:
        super().__init__()
        self._default = QColor(default)
        self.text = text

    def widget(self, parent: QWidget | None=None) -> DColorWidget:
        _widget = DColorWidget(self, parent=parent).build()
        return _widget

    def __get__(self, obj, cls) -> QColor:
        if hasattr(obj, self.private_name):
            return getattr(obj, self.private_name)
        else:
            return self._default

    def __set__(self, obj, value):
        if value is None:
            value = self._default
        setattr(obj, self.private_name, QColor(value))