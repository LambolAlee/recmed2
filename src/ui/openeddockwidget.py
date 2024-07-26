from ._ui import Ui_OpenedDock

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget, QWidget, QMainWindow


class OpenedDockWidget(QWidget, Ui_OpenedDock):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

    def getDockWidget(self, parent: QMainWindow=None) -> QDockWidget:
        dock = QDockWidget("opened", parent)
        self.setParent(dock)
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        dock.setWidget(self)
        return dock
