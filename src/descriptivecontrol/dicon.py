from typing import Self, Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QHBoxLayout, QToolButton

from .descriptor import DescriptiveAttr, DescriptiveWidget
from recmedtyping import RMIconType, getIcon
from ui.iconselector import IconSelector



class DIconWidget(DescriptiveWidget):
    def __init__(self, obj: "DIcon", parent: QWidget | None=None) -> None:
        super().__init__(obj, parent)
        self._icon = None
        self._iconSelector = IconSelector()
        self._iconSelector.iconSelected.connect(self.setIcon)

    def build(self) -> Self:
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        self.selectButton = QToolButton(self)
        self.selectButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.selectButton.setText("Click to select icon...")
        self.selectButton.clicked.connect(self.onSelectButtonClicked)
        layout.addWidget(self.selectButton)

        self.clearButton = QToolButton(self)
        self.clearButton.setIcon(getIcon(RMIconType.circleXmark))
        self.clearButton.clicked.connect(self.onClearButtonClicked)
        layout.addWidget(self.clearButton)

        self.setLayout(layout)
        return self

    def setData(self, **kwargs) -> None:
        """
        icon: None is allowed
        """
        for key, icon in kwargs.items():
            if key == self.attr.public_name:
                self.setIcon(icon)

    def data(self) -> dict:
        return {self.attr.public_name: self._icon}

    def onSelectButtonClicked(self):
        self._iconSelector.move(self.selectButton.mapToGlobal(self.selectButton.rect().bottomLeft()))
        self._iconSelector.show()

    def onClearButtonClicked(self):
        self.setIcon(None)

    def setIcon(self, icon: Optional[RMIconType]):
        self._icon = icon
        if icon is None:
            self.selectButton.setIcon(QIcon())
            self.selectButton.setText("Click to select icon...")
        else:
            self.selectButton.setIcon(getIcon(icon))
            self.selectButton.setText(icon.name)



class DIcon(DescriptiveAttr):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text

    def widget(self, parent: QWidget | None = None) -> DescriptiveWidget:
        _widget = DIconWidget(self, parent=parent).build()
        return _widget

    def displayName(self) -> str:
        return self.text
