from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QToolButton, QHBoxLayout

from .tagcontainer import TagContainer
from .pilltagwidget import PillTagWidget
from tag import Tag
from recmedtyping import getIcon, RMIconType



class TagArea(QWidget):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        
        layout = QHBoxLayout()
        self.container = TagContainer(self)
        layout.addWidget(self.container)

        self.addNewTagToolButton = QToolButton(self)
        self.addNewTagToolButton.setArrowType(Qt.ArrowType.LeftArrow)
        self.addNewTagToolButton.setIcon(getIcon(RMIconType.tag))
        self.addNewTagToolButton.setVisible(False)
        self.addNewTagToolButton.clicked.connect(self.addNewTag)      
        layout.addWidget(self.container)

        self.setLayout(layout)

    def addNewTag(self):
        pillTags: PillTagWidget = self.container.addTag(Tag('Input your tag name...'))[0]
        self.container.edit(pillTags)

    def setEditMode(self, editMode: bool):
        self.addNewTagToolButton.setVisible(editMode)
        self.container.setEditMode(editMode)
