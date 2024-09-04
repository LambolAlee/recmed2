from enum import IntEnum

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QRegion
from PySide6.QtWidgets import QWidget, QStyleOptionViewItem, QFrame

from ._ui.drugcell_ui import Ui_DrugCell
from .formularmodel import DrugObject, Decoction



class DrugCell(QWidget, Ui_DrugCell):
    class CellState(IntEnum):
        show = 0
        hide = 1

    decoctionIconColor = {
        Decoction.first: "red",
        Decoction.last: "blue"
    }

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.build()

    def build(self):
        self.decoctionIconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        decoctionIconSize = min(self.nameLabel.height(), 16)
        self.decoctionIconLabel.setFixedSize(decoctionIconSize, decoctionIconSize)
        self.decoctionIconLabel.setFrameShape(QFrame.Shape.Box)

    def renderCell(self, drugObj: DrugObject, painter: QPainter, option: QStyleOptionViewItem):
        self._setDrug(drugObj)
        self._drawDecoctionIcon(drugObj.decoction)
        self.setFixedSize(option.rect.size())

        painter.save()
        painter.translate(option.rect.topLeft())
        self.render(painter, QPoint(), QRegion(), QWidget.RenderFlag.DrawChildren)
        painter.restore()

    def _setDrug(self, drugObj: DrugObject):
        if drugObj.isPlaceholder():
            self.cellShowcaseSwitcher.setCurrentIndex(DrugCell.CellState.hide)
            return
        else:
            self.cellShowcaseSwitcher.setCurrentIndex(DrugCell.CellState.show)

        self.nameLabel.setText(drugObj.name)
        self.doseAndUnitLabel.setText(f"{drugObj.dose}{drugObj.unit}")

        decoction = drugObj.decoction
        self.decoctionIconLabel.setVisible(decoction is not Decoction.normal)
        self.decoctionIconLabel.setText(decoction[0])

    def _drawDecoctionIcon(self, decoction: Decoction):
        if decoction is Decoction.normal:
            return
        color = self.decoctionIconColor[decoction]
        self.decoctionIconLabel.setStyleSheet(f"border-color:{color}; color:{color};")
