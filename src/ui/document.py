from PySide6.QtWidgets import QMdiSubWindow, QWidget, QVBoxLayout
from .documentwidget import DocumentWidget
from .docmetadatawidget import DocMetadataWidget


class Document(QMdiSubWindow):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setWindowTitle("test doc")

        self.initPage()

    def initPage(self) -> None:
        self.test_view()

    def test_view(self):
        self.wrapper = QWidget(self)
        layout = QVBoxLayout()
        self.docwidget = DocumentWidget(self)
        self.metadatawidget = DocMetadataWidget(self)
        layout.addWidget(self.metadatawidget, stretch=0)
        layout.addWidget(self.docwidget, stretch=1)
        self.wrapper.setLayout(layout)
        self.setWidget(self.wrapper)
