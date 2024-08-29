from PySide6.QtWidgets import QWidget, QHBoxLayout, QToolButton

from .descriptor import DescriptiveAttr
from ui.colorlineedit import ColorLineEdit
from ui.colorwheel import ColorWheel
from recmedtyping import getIcon, RMIconType



class DColor(QWidget, DescriptiveAttr):
    def __init__(self) -> None:
        super().__init__()

        layout = QHBoxLayout()
        layout.setSpacing(0)
        self.lineEdit = ColorLineEdit(parent=self)
        layout.addWidget(self.lineEdit)
        self.colorButton = QToolButton(parent=self)
        self.colorButton.setIcon(getIcon(RMIconType.palette))
        self.colorButton.setToolTip("Choose a color and press enter to select it")
        layout.addWidget(self.colorButton)
        self.setLayout(layout)

        self.colorButton.clicked.connect(self.onColorButtonClicked)

    def onColorButtonClicked(self) -> None:
        self._popup = ColorWheel.popup(self.colorButton.mapToGlobal(self.colorButton.rect().bottomLeft()))
        self._popup.colorDecided.connect(lambda color: self.lineEdit.setColor(color, save=True))
        self._popup.colorSelectionChanged.connect(self.lineEdit.setColor)
        self._popup.cancelled.connect(self.lineEdit.restore)
        self._popup.show()
