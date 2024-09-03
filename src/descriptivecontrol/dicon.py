from typing import Self

from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QCheckBox

from .descriptor import DescriptiveAttr, DescriptiveWidget
from recmedtyping import RMIconType


# TODO: wraite a icon selector widget
class DIconWidget(DescriptiveWidget):
    def __init__(self, obj: "DIcon", parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.attr = obj

    def build(self) -> Self:
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.comboBox = QComboBox(self)
        self.comboBox.addItems([icon.value for icon in RMIconType])
        layout.addWidget(self.comboBox)
        self.setLayout(layout)
        return self

    def setData(self, **kwargs) -> None:
        """
        icon: None is allowed
        """
        for key, icon in kwargs.items():
            if key == self.attr.public_name:
                if icon is None:
                    return
                self.comboBox.setCurrentText(icon.value)

    def data(self) -> dict:
        return {self.attr.public_name: RMIconType[self.comboBox.currentText()]}


class DIcon(DescriptiveAttr):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text

    def widget(self, parent: QWidget | None = None) -> DescriptiveWidget:
        _widget = DIconWidget(self, parent=parent).build()
        return _widget

    def displayName(self) -> str:
        return self.text
