from typing import List

from PySide6.QtWidgets import QWidget, QSizePolicy

from tag import Tag
from utils import FlowLayout
from .pilltagwidget import PillTagWidget
from .tageditor import TagEditor



class TagContainer(QWidget):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        self.taglayout = FlowLayout()
        self.taglayout.setSpacing(4)
        self.setLayout(self.taglayout)
        self._editor = TagEditor()
        self._editor.editingFinished.connect(self.saveChanges)
        self._editor.tagRemoveRequest.connect(self.removeTag)

        self._pills = []
        self._inEditMode = False

    def addTag(self, *tags: Tag) -> List[PillTagWidget]:
        result = []
        for tag in tags:
            pill = PillTagWidget(tag, self)
            pill.deleteButtonClicked.connect(lambda pill=pill: self.removeTag(pill))
            pill.editing.connect(self.edit)
            self.taglayout.addWidget(pill)
            self._pills.append(pill)
            
            result.append(pill)
        return result

    def removeTag(self, pill: PillTagWidget):
        self._pills.remove(pill)
        self.taglayout.removeWidget(pill)
        pill.disconnect(None, None, None)
        pill.deleteLater()

    def edit(self, pill: PillTagWidget):
        self._editor.build(pill) \
                    .move(pill.mapToGlobal(pill.rect().bottomLeft())) \
                    .show()

    def saveChanges(self, pill: PillTagWidget, data: dict) -> None:
        for name, value in data.items():
           pill.tag[name] = value
        pill.updateUi()

    def clear(self) -> None:
        for pill in self._pills:
            self.removeTag(pill)

    def setEditMode(self, editMode: bool):
        self._inEditMode = editMode
        for pill in self._pills:
            pill.setEditMode(editMode)

    def isInEdit(self) -> bool:
        return self._inEditMode
