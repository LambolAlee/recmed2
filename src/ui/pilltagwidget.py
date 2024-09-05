from typing import Optional, Self

from PySide6.QtCore import Qt, Signal, Property
from PySide6.QtGui import QFocusEvent, QKeyEvent, QMouseEvent
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QLayout

from tag import Tag
from recmedtyping import RMIconType, getIcon



class PillTagWidget(QWidget):
    deleteButtonClicked = Signal()
    editing = Signal(object)

    def __init__(self, tag: Tag, parent: QWidget | None=None):
        super().__init__(parent)
        self.setupUi()

        self.tag = tag
        self._inEdit = False

    @property
    def tag(self) -> Tag:
        return self._tag

    @tag.setter
    def tag(self, tag: Tag):
        self._tag = tag
        self.updateUi()

    def setupUi(self):
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setFixedHeight(30)
        layout = QHBoxLayout()
        layout.setContentsMargins(9,4,9,4)
        layout.setSpacing(2)
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
        self._inEdit = editMode
        self.deleteButton.setVisible(editMode)

    def updateUi(self):
        if self._tag.hasIcon():
            if self._tag.iconOnly or (self._tag.hasTextIcon() and self._tag.icon is None):
                self.label.setText(f'<font style="font-family:recmed-fa6; margin-right: 5px">{self._tag.getIcon().value}</font>')
            else:
                self.label.setText(f'<font style="font-family:recmed-fa6; margin-right: 5px">{self._tag.getIcon().value}</font> {self._tag.name}')
        else:
            self.label.setText(self._tag.name)

        self.label.setStyleSheet(f"color: {self._tag.fg.name()};")
        self.setStyleSheet(f"background: {self._tag.bg.name()}; border-radius: 12px;")

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            p = event.position().toPoint()
            if self.deleteButton.isVisible() and self.deleteButton.geometry().contains(p):
                self.deleteButtonClicked.emit()
                return
        return super().mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            p = event.position().toPoint()
            if self.label.geometry().contains(p):
                if self._inEdit:
                    self.editing.emit(self)
                return
        return super().mouseDoubleClickEvent(event)
