from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLineEdit, QComboBox, QColorDialog

from tag import Tag
from recmedtyping import RMIconType
from ._ui.tageditor_ui import Ui_TagEditor



class TagEditor(QWidget, Ui_TagEditor):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.widgetList = {}
