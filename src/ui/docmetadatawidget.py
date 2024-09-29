from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout

from .titlearea import TitleArea
from .toolarea import ToolArea
from .tagarea import TagArea



class DocMetadataWidget(QWidget):
    showFieldSignal = Signal(bool)

    def __init__(self, parent: QWidget | None=None):
        super().__init__(parent)

        vlayout = QVBoxLayout()
        vlayout.setContentsMargins(0,0,0,4)
        vlayout.setSpacing(0)
        self._titleArea = TitleArea(parent=self)
        self._toolArea = ToolArea(self)
        vlayout.addWidget(self._toolArea)
        vlayout.addWidget(self._titleArea)

        layout = QVBoxLayout()
        layout.setContentsMargins(2, 4, 2, 4)
        layout.setSpacing(2)
        self._tagArea = TagArea(parent=self)
        layout.addLayout(vlayout, stretch=0)
        layout.addWidget(self._tagArea, stretch=0)

        self.setLayout(layout)

        self._toolArea.editTitleSignal.connect(self._titleArea.setEditMode)
        self._toolArea.newTagSignal.connect(self._tagArea.newTag)
        self._toolArea.editTagSignal.connect(self._tagArea.setEditMode)
        self._toolArea.showFieldSignal.connect(self.showFieldSignal)
