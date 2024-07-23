from qframelesswindow import FramelessMainWindow

from .recmedtitlebar import RecmedTitleBar
from .recmed_ui import Ui_RecMedWindow


class RecMedWindow(FramelessMainWindow, Ui_RecMedWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("RecMed2 - Lambol")

        titleBar = RecmedTitleBar(self)
        titleBar.setIcon(qApp.windowIcon())
        self.setTitleBar(titleBar)
        self.setMenuWidget(titleBar)

        self.setStyleSheet("""
            QMenuBar{background: #F0F0F0; padding: 5px 0}
            QTextEdit{border: none; font-size: 15px}
            QDialog > QLabel{font-size: 15px}
        """)
