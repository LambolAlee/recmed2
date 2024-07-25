from enum import Enum

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QIcon


class RMIconType(Enum):
    """Icons for the RecMed app"""
    arrowsMaximize = "\uf31d"


def getIcon(icon: RMIconType) -> QIcon:
    """Returns a QPixmap for the given icon enum"""

    font = qApp.getRMFont()
    font.setPixelSize(25)

    pix = QPixmap(30, 30)
    pix.fill(Qt.GlobalColor.transparent)

    painter = QPainter()
    painter.begin(pix)
    painter.setFont(font)
    painter.drawText(pix.rect(), Qt.AlignmentFlag.AlignCenter, icon.value)
    painter.end()

    return QIcon(pix)
