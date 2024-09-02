from qframelesswindow import FramelessMainWindow
from PySide6.QtCore import Qt

from .recmedtitlebar import RecmedTitleBar
from ._ui import Ui_RecMedWindow
from .documentbrowser import DocumentBrowser
from .document import Document
from .openeddockwidget import OpenedDockWidget
from utils import fillPlaceholderWidget

from recmedtyping import RMIconType, getIcon


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
            QStatusBar{background: #00FF00}
        """)    # TEMP: for test purpose

        self.initUi()

    def setLabelIcon(self) -> None:
        icon = getIcon(RMIconType.airplay)
        self.label.setPixmap(icon.pixmap(30, 30))

    def initUi(self) -> None:
        self.browserMdiArea = fillPlaceholderWidget(self.browserMdiArea, DocumentBrowser(self), self.docsPage.layout())

        # 0 -> empty document welcome page
        # 1 -> document browser page
        self.browserStackedPage.setCurrentIndex(1)
        self.browserMdiArea.test_view()

        self.openedDock = OpenedDockWidget()
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.openedDock.getDockWidget(self))
