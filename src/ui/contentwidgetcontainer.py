from PySide6.QtWidgets import QWidget, QGridLayout



class ContentWidgetContainer(QWidget):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)

        self.contentLayout = QGridLayout(self)
        self.test_view()

    def test_view(self):
        from contentwidget import CWLoader
        self.loader = CWLoader()
        self.loader.loadContentPlugins()
        plugin = self.loader.getPlugin("patientinfo", "core")
        self.contentLayout.addWidget(plugin.viewport(self))
        plugin = self.loader.getPlugin("tcmformular", "core")
        self.contentLayout.addWidget(plugin.viewport(self))
