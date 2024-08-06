from PySide6.QtWidgets import QMdiSubWindow, QWidget
from .documentwidget import DocumentWidget


class Document(QMdiSubWindow):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setWindowTitle("test doc")

        self.initPage()

    def initPage(self) -> None:
        self.test_view()

    def test_view(self):
        self.docwidget = DocumentWidget(self)
        self.setWidget(self.docwidget)
