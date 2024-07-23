import sys
import _rc

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from ui import RecMedWindow


def main():
    app = QApplication(sys.argv)
    app.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
    app.setWindowIcon(QIcon(":/logo/recmed2.png"))
    app.setApplicationName("RecMed2")
    app.setApplicationVersion("0.1.0")
    app.setOrganizationName("Lambol.RecMed2")
    app.setOrganizationDomain("recmed2.com")

    recmed = RecMedWindow()
    recmed.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
