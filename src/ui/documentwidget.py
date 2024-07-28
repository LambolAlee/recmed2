from PySide6.QtWidgets import QWidget, QSizePolicy

from ._ui import Ui_DocumentWidget


class DocumentWidget(QWidget, Ui_DocumentWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setupUi(self)

        self.scrollArea.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        self.scrollArea.setMaximumWidth(900)
        self.scrollArea.setMinimumWidth(300)
