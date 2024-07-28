from ._ui.metadatawidget_ui import Ui_MetadataWidget

from PySide6.QtWidgets import QWidget


class MetadataWidget(QWidget, Ui_MetadataWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setFixedHeight(30)   # FIXME change the name of the stackedwidget to a more reliable one

        self.pushButton.clicked.connect(self.togglePanel)

    def togglePanel(self):
        self.plainTextEdit.setVisible(not self.plainTextEdit.isVisible())
        self.layout().invalidate()
        self.layout().update()
