from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ._ui.fieldarea_ui import Ui_FieldArea



class FieldArea(QWidget, Ui_FieldArea):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

    def setEditMode(self, editMode: bool):
        self.stackedWidget.setCurrentWidget(self.editPage if editMode else self.previewPage)

