from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout



class ContentWidgetContainer(QWidget):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)

        self.contentLayout = QGridLayout(self)
        self.contentLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.contentLayout.setContentsMargins(4,0,4,0)
        self.test_view()

    def test_view(self):
        from contentwidget import CWLoader
        self.loader = CWLoader()
        self.loader.loadContentPlugins()
        plugin = self.loader.getPlugin("patientinfo", "core")
        self.contentLayout.addWidget(plugin.viewport(self))
        plugin = self.loader.getPlugin("tcmformular", "core")
        self.contentLayout.addWidget(plugin.viewport(self))
