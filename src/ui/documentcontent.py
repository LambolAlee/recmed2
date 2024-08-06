from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt


class DocumentContent(QWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        # TODO Add MetadataWidget and ContentBox widgets to a vertical layout
        self.initUi()
        self.test_view()

    def initUi(self):
        self.contentlayout = QVBoxLayout(self)
        self.contentlayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.contentlayout)

    def test_view(self):
        from contentwidget import CWLoader
        self.loader = CWLoader()
        self.loader.loadContentPlugins()
        plugin = self.loader.getPlugin("patientinfo", "core")
        self.contentlayout.addWidget(plugin.viewport(self))
