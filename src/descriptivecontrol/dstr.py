from typing import Self

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit

from .descriptor import DescriptiveAttr, DescriptiveWidget



class DStrWidget(DescriptiveWidget):
    def build(self) -> Self:
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.lineEdit = QLineEdit(self)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)
        return self

    def setData(self, **kwargs) -> Self:
        for key, value in kwargs.items():
            if key == self.attr.public_name:
                self.lineEdit.setText(value)

    def data(self) -> dict:
        return {self.attr.public_name: self.lineEdit.text()}



class DStr(DescriptiveAttr):
    def __init__(self, displayText: str, default: str='', sendEvent: bool=False) -> None:
        super().__init__(sendEvent)
        self.displayText = displayText
        self.defaultText = default

    def widget(self, parent: QWidget | None=None) -> DStrWidget:
        _widget = DStrWidget(self, parent=parent).build()
        return _widget

    def displayName(self) -> str:
        return self.displayText
    
    def default(self):
        return self.defaultText
