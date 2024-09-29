from PySide6.QtWidgets import QMdiSubWindow, QWidget, QScrollArea
from .documentwidget import DocumentWidget



class Document(QMdiSubWindow):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setWindowTitle("test doc")

        self.initPage()

    def initPage(self) -> None:
        self.test_view()

    def test_view(self):
        self._scrollArea = QScrollArea(self)
        self._scrollArea.horizontalScrollBar().hide()
        self.docWidget = DocumentWidget(self._scrollArea)
        self._scrollArea.setWidget(self.docWidget)
        self.setWidget(self._scrollArea)
