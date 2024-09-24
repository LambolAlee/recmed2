from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout

from .titlearea import TitleArea
from .toolarea import ToolArea
from .tagarea import TagArea
from .fieldarea import FieldArea



class DocMetadataWidget(QWidget):
    def __init__(self, parent: QWidget | None=None):
        super().__init__(parent)

        gridLayout = QGridLayout()
        gridLayout.setContentsMargins(0,0,0,0)
        self._titleArea = TitleArea(parent=self)
        self._toolArea = ToolArea(self)
        gridLayout.addWidget(self._titleArea, 0, 0, Qt.AlignmentFlag.AlignLeft)
        gridLayout.addWidget(self._toolArea, 0, 0, Qt.AlignmentFlag.AlignRight)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 4, 0, 4)
        layout.setSpacing(2)
        self._tagArea = TagArea(parent=self)
        self._fieldArea = FieldArea(self)
        layout.addLayout(gridLayout)
        layout.addWidget(self._tagArea)
        layout.addWidget(self._fieldArea)

        self.setLayout(layout)

        self._toolArea.editTitleSignal.connect(self._titleArea.setEditMode)
        self._toolArea.newTagSignal.connect(self._tagArea.newTag)
        self._toolArea.editTagSignal.connect(self._tagArea.setEditMode)
        self._toolArea.showFieldSignal.connect(self._fieldArea.setVisible)
