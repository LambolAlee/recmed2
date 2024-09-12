from PySide6.QtWidgets import QWidget

from ._ui.docmetadatawidget_ui import Ui_DocMetadataWidget
from recmedtyping import getIcon, RMIconType
from .tagarea import TagArea


class DocMetadataWidget(QWidget, Ui_DocMetadataWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setupUi(self)
        self.title.setFixedHeight(30)

        self.tagArea = TagArea(self)
        self.docmetadataLayout.addWidget(self.tagArea)
        self.editToolButton.setCheckable(True)
        self.editToolButton.toggled.connect(self.setEditMode)

        self.editToolButton.setIcon(getIcon(RMIconType.pencil))
        self.saveToolButton.setIcon(getIcon(RMIconType.circleCheck))
        self.discardToolButton.setIcon(getIcon(RMIconType.circleXmark))

    def setTitle(self, title: str):
        self.titleLabel.setText(title)
        self.titleEdit.setText(title)

    def setEditMode(self, editMode: bool):
        self.editToolButton.setDisabled(editMode)
        self.tagArea.setEditMode(editMode)
