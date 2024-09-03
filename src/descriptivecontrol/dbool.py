from typing import Self

from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox
from .descriptor import DescriptiveAttr, DescriptiveWidget



class DBoolWidget(DescriptiveWidget):
    def __init__(self, obj: "DBool", parent: QWidget | None=None):
        super().__init__(parent)
        self.attr = obj

    def build(self) -> Self:
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.checkBox = QCheckBox(self)
        layout.addWidget(self.checkBox)
        self.setLayout(layout)
        return self
    
    def setData(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if key == self.attr.public_name:
                self.checkBox.setChecked(value)

    def data(self) -> dict:
        return {self.attr.public_name: self.checkBox.isChecked()}


class DBool(DescriptiveAttr):
    def __init__(self, text: str, default: bool) -> None:
        super().__init__()
        self.text = text
        self._default = default

    def widget(self, parent: QWidget | None = None) -> DescriptiveWidget:
        _widget = DBoolWidget(self, parent).build()
        return _widget
    
    def displayName(self) -> str:
        return self.text
    
    def __get__(self, obj, cls):
        return getattr(obj, self.private_name, self._default)
    
    def __set__(self, obj, value: bool):
        setattr(obj, self.private_name, value)
