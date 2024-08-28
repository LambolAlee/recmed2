from typing import Optional

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QLayout

from tag import Tag
from recmedtyping import RMIconType, getIcon
from utils import FlowLayout



class PillTagWidget(QWidget):
    deleteButtonClicked = Signal()

    def __init__(self, tag: Optional[Tag]=None, parent: QWidget | None=None):
        super().__init__(parent)
        self.setupUi()

        self._iconOnly = False
        if tag is not None:
            self.tag = tag

    @property
    def tag(self) -> Tag:
        return self._tag

    @tag.setter
    def tag(self, tag: Tag):
        self._tag = tag
        self.updateUi()

    @property
    def iconOnly(self) -> bool:
        return self._iconOnly

    @iconOnly.setter
    def iconOnly(self, iconOnly: bool):
        self._iconOnly = iconOnly
        self.updateUi()

    def setupUi(self):
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setFixedHeight(30)
        layout = QHBoxLayout()
        layout.setContentsMargins(9,4,9,4)
        layout.setSpacing(0)
        layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        self.label = QLabel(parent=self)
        self.label.setFixedHeight(16)
        layout.addWidget(self.label)

        self.deleteButton = QLabel(parent=self)
        self.deleteButton.setPixmap(getIcon(RMIconType.xmark).pixmap(16, 16))
        self.deleteButton.setVisible(False)
        layout.addWidget(self.deleteButton)

        self.setLayout(layout)

    def setEditMode(self, editMode: bool):
        self.deleteButton.setVisible(editMode)

    def updateUi(self):
        if self._tag.hasIcon():
            if self._iconOnly or self._tag.isTextIconTag():
                self.label.setText(f'<font style="font-family:recmed-fa6; margin-right: 5px">{self._tag.icon.value}</font>')
            else:
                self.label.setText(f'<font style="font-family:recmed-fa6; margin-right: 5px">{self._tag.icon.value}</font> {self._tag.name}')
        else:
            self.label.setText(self._tag.name)


        self.label.setStyleSheet(f"color: {self._tag.fg.name()};")
        self.setStyleSheet(f"background: {self._tag.bg.name()}; border-radius: 10px;")

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            p = event.position()
            if self.label.geometry().contains(p.toPoint()):
                print("label clicked")
                self.setEditMode(True)
                return True
            elif self.deleteButton.isVisible() and self.deleteButton.geometry().contains(p.toPoint()):
                self.deleteButtonClicked.emit()
                return True
        return super().mouseReleaseEvent(event)



class TagContainer(QWidget):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)

        self.taglayout = FlowLayout()
        self.taglayout.setSpacing(4)
        self.setLayout(self.taglayout)

        self._tagwidgets = []
        self._edit = False

    def addTag(self, *tags: Tag):
        for tag in tags:
            pill = PillTagWidget(tag, self)
            pill.deleteButtonClicked.connect(lambda pill=pill: self.removeTag(pill))
            self.taglayout.addWidget(pill)
            self._tagwidgets.append(pill)

    def removeTag(self, pill: PillTagWidget):
        self._tagwidgets.remove(pill)
        self.taglayout.removeWidget(pill)
        pill.deleteButtonClicked.disconnect()
        pill.deleteLater()

    def clear(self) -> None:
        for pill in self._tagwidgets:
            self.removeTag(pill)

    def setEditMode(self, editMode: bool):
        self._edit = editMode
        for pill in self._tagwidgets:
            pill.setEditMode(editMode)

    def isInEdit(self) -> bool:
        return self._edit
