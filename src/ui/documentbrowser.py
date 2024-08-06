from PySide6.QtWidgets import QMdiArea, QWidget

from .document import Document


class DocumentBrowser(QMdiArea):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setTabsClosable(True)  # Enable the close button on each tab
        self.setViewMode(QMdiArea.ViewMode.TabbedView)

    def test_view(self):
        self.doc = Document(self)
        self.addSubWindow(self.doc)
        self.doc.show()
