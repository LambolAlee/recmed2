from PySide6.QtWidgets import QWidget, QSizePolicy, QSpacerItem, QGridLayout

from ._ui import Ui_DocumentWidget
from .documentcontent import DocumentContent


class DocumentWidget(QWidget, Ui_DocumentWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setupUi(self)

        self.initUi()

        self.test_view()

    def initUi(self):
        self.scrollArea.setMinimumWidth(650)

    def test_view(self):
        self.doccontent = DocumentContent(self.scrollArea)
        self.scrollArea.setWidget(self.doccontent)
