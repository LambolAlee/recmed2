from typing import cast

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QToolBar, QCheckBox
from PySide6.QtWidgets import QSizePolicy

from ... import IViewport
from ._ui.viewport_ui import Ui_TCMFormularViewport
from ..auxiliarywidget import CardTitle
from .formulartoolbar import FormularToolBar
from .formularmodel import FormularTableModel
from .formulardelegate import FormularDelegate
from .formulartableview import FormularTableView



class TCMFormularViewport(IViewport, Ui_TCMFormularViewport):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.addActions([self.actionAdd, self.actionNewRow, self.actionRemove, self.actionTidy])

        layout = cast(QVBoxLayout, self.editPage.layout())
        self.toolbar = FormularToolBar(self)
        self.toolbar.addActions(self.actions())
        layout.addWidget(self.toolbar)

        self.tableView = FormularTableView(self)
        self.model = FormularTableModel(self)
        self.model.drugCountChanged.connect(self.toolbar.setDrugCount)
        self.model.setFormularData([
            {"name": "熟大黄", "dose": 45, "decoction": "先煎"},
            {"name": "土鳖虫", "dose": 45},
            {"name": "水蛭", "dose": 45, "decoction": "后下"},
            {"name": "虻虫", "dose": 45},
            {"name": "蛴螬", "dose": 45},
            {"name": "干漆", "dose": 45},
            {"name": "桃仁", "dose": 45},
            {"name": "苦杏仁", "dose": 45},
            {"name": "白花蛇舌草", "dose": 45},
            {"name": "地黄", "dose": 45},
        ])
        self.delegate = FormularDelegate(self.tableView)
        self.tableView.setModel(self.model)
        self.tableView.setItemDelegate(self.delegate)
        self.toolbar.selectAllSignal.connect(
            lambda: self.tableView.selectAll() \
                if not self.tableView.selectionModel().hasSelection() \
                else self.tableView.selectionModel().clearSelection()
        )
        layout.addWidget(self.tableView)

    def initActionIcons(self):
        self.actionAdd.setIcon(self._helper.getIcon(self._helper.RMIconType.grid2Plus))
        self.actionRemove.setIcon(self._helper.getIcon(self._helper.RMIconType.trashCanXmark))
        self.actionTidy.setIcon(self._helper.getIcon(self._helper.RMIconType.brush))
        self.actionNewRow.setIcon(self._helper.getIcon(self._helper.RMIconType.tableRows))

        self.actionRemove.triggered.connect(lambda: self.model.removeDrugs(self.tableView.selectionModel()))
        self.actionTidy.triggered.connect(self.model.tidy)
        self.actionAdd.triggered.connect(lambda: self.tableView.edit(self.model.add()))
        self.actionNewRow.triggered.connect(self.model.appendEmptyRow)

    def setData(self, data):
        pass

    def getDataSpec(self):
        pass

    def save(self):
        pass

    def switchTo(self, preview: bool=False):
        self.viewportSwitcher.setCurrentIndex(1 if preview else 0)

    def setPluginHelper(self, pluginHelper):
        self._helper = pluginHelper


def main():
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    vp = TCMFormularViewport()
    vp.show()
    app.exec()

if __name__ == '__main__':
    main()
