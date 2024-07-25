from qframelesswindow import FramelessMainWindow

from .recmedtitlebar import RecmedTitleBar
from ._ui import Ui_RecMedWindow

from recmedtyping import RMIconType, getIcon


class RecMedWindow(FramelessMainWindow, Ui_RecMedWindow):
    def __init__(self):
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

    def setLabelIcon(self):
        # self.label.setScaledContents(True)
        icon = getIcon(RMIconType.arrowsMaximize)
        # self.label.setPixmap(QPixmap("D:\Lambol\Downloads\skadi_by_pradaestrada_ddsfm8i.png"))
        self.label.setPixmap(icon.pixmap(30, 30))
