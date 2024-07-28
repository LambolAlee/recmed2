from PySide6.QtCore import Qt
from ._ui import Ui_ContentTemplateEditor

from PySide6.QtWidgets import QWidget


class ContentTemplateEditor(QWidget, Ui_ContentTemplateEditor):
    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
        # TODO the editor needs a toolbar and a beautiful theme of highlight xml code
