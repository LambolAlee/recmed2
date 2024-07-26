from qframelesswindow import FramelessMainWindow
from PySide6.QtCore import Qt

from .recmedtitlebar import RecmedTitleBar
from ._ui import Ui_RecMedWindow
from .openeddockwidget import OpenedDockWidget

from recmedtyping import RMIconType, getIcon, ConfigKeys


class RecMedWindow(FramelessMainWindow, Ui_RecMedWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("RecMed2 - Lambol")

        titleBar = RecmedTitleBar(self)
        titleBar.setIcon(qApp.windowIcon())
        self.setTitleBar(titleBar)
        self.setMenuWidget(titleBar)

        self.setLabelIcon()

        self.setStyleSheet("""
            QMenuBar{background: #F0F0F0; padding: 5px 0}
            QTextEdit{border: none; font-size: 15px}
            QDialog > QLabel{font-size: 15px}
        """)

        self.initUi()

    def setLabelIcon(self) -> None:
        icon = getIcon(RMIconType.abacus)
        self.label.setPixmap(icon.pixmap(30, 30))

    def initUi(self) -> None:
        self.openedDock = OpenedDockWidget()
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.openedDock.getDockWidget(self))
