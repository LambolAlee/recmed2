from typing import cast

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy

from ... import IViewport
from ._ui.viewport_ui import Ui_TCMFormularViewport
from ..auxiliarywidget import CardTitle


class TCMFormularViewport(IViewport, Ui_TCMFormularViewport):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setupUi(self)

        self.initUi()

    def initUi(self):
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.cardTitle = CardTitle("TCM Formular", self.editPage)
        layout = cast(QVBoxLayout, self.editPage.layout())
        layout.insertWidget(0, self.cardTitle)

    def setData(self, data):
        pass

    def getDataSpec(self):
        pass

    def save(self):
        pass

    def switchTo(self, preview: bool=False):
        self.viewportSwitcher.setCurrentIndex(1 if preview else 0)
