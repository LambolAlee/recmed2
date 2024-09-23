from typing import List

from PySide6.QtWidgets import QWidget, QSizePolicy

from tag import Tag
from utils import FlowLayout
from .pilltagwidget import PillTagWidget
from .tageditor import TagEditor



class TagArea(QWidget):
    def __init__(self, *tags: List[Tag], parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.hide()

        self.taglayout = FlowLayout()
        self.taglayout.setSpacing(4)
        self.setLayout(self.taglayout)
        self._editor = TagEditor()
        self._editor.editingFinished.connect(self.saveChanges)
        self._editor.tagRemoveRequest.connect(self.removeTag)

        self._pills = []
        self._inEditMode = False

        self.addTag(*tags)

    def _updateVisible(self):
        if len(self._pills) == 0:
            if self.isVisible():
                self.hide()
        else:
            if not self.isVisible():
                self.show()

    def newTag(self) -> PillTagWidget:
        pillTag: PillTagWidget = self.addTag(Tag('Input your tag name...'))[0]
        self.edit(pillTag)
        return pillTag

    def addTag(self, *tags: Tag) -> List[PillTagWidget]:
        result = []
        for tag in tags:
            pill = PillTagWidget(tag, self)
            pill.deleteButtonClicked.connect(lambda pill=pill: self.removeTag(pill))
            pill.editing.connect(self.edit)
            self.taglayout.addWidget(pill)
            self._pills.append(pill)
            
            result.append(pill)
        self._updateVisible()
        return result

    def removeTag(self, pill: PillTagWidget):
        self._pills.remove(pill)
        self.taglayout.removeWidget(pill)
        pill.disconnect(None, None, None)
        pill.deleteLater()
        self._updateVisible()

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
        self._updateVisible()

    def setEditMode(self, editMode: bool):
        self._inEditMode = editMode
        for pill in self._pills:
            pill.setEditMode(editMode)

    def isInEdit(self) -> bool:
        return self._inEditMode
    
    def __len__(self) -> int:
        return len(self._pills)
