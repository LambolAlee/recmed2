import sys
import _rc

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QFontDatabase, QFont
from PySide6.QtWidgets import QApplication

from recmedtyping import PathManager
from logger import LoggingServer, configLogEnviron


class RecMedApp(QApplication):
    def __init__(self, argv: list[str]):
        super().__init__(argv)

        self.initAppSettings()
        self.initAppFont()

    def initAppSettings(self) -> None:
        self.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        self.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
        self.setWindowIcon(QIcon(":/logo/recmed2.png"))
        self.setApplicationName("RecMed2")
        self.setApplicationVersion("0.1.0")
        self.setOrganizationName("Lambol.RecMed2")
        self.setOrganizationDomain("recmed2.com")

    def initAppFont(self) -> None:
        self.IconFontName = "recmed-fa6"
        self.RecMedFontID = QFontDatabase.addApplicationFont(f":/font/{self.IconFontName}")
        font: QFont = self.font()
        font.setPointSize(10)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.setFont(font)

    def launch(self) -> None:
        from .recmed import RecMedWindow
        with LoggingServer(PathManager().logDir) as server:
            configLogEnviron(server.message_queue)

            recmed = RecMedWindow()
            recmed.show()

            self.runForever()
    
    def testUi(self) -> None:
        from test.test_toolarea import Test
        t = Test()
        t.test()
        self.runForever()

    def getRMFont(self) -> QFont:
        return QFont(self.IconFontName)

    def runForever(self) -> None:
        sys.exit(self.exec())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type, exc_value, traceback)
