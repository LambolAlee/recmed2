from typing import List, Self

from PySide6.QtCore import Qt, QPoint, Signal, QSize
from PySide6.QtGui import QCloseEvent, QFocusEvent, QKeyEvent
from PySide6.QtWidgets import QWidget, QFormLayout

from ._ui.tageditor_ui import Ui_TagEditor
from .pilltagwidget import PillTagWidget
from utils import getMaxMinimumSize
from descriptivecontrol import getDesciptors



class TagEditor(QWidget, Ui_TagEditor):
    editingFinished = Signal(PillTagWidget, dict)

    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.Popup)

        self.tagItemLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.tagItemLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.tagItemLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.tagItemLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        self._widgetList: List[QWidget] = []
        self._pill = None

    def sizeHint(self) -> QSize:
        return getMaxMinimumSize(self._widgetList, self)

    def move(self, pos: QPoint) -> Self:
        super().move(pos)
        return self

    def clearLayout(self) -> None:
        while self.tagItemLayout.count() > 0:
            self.tagItemLayout.removeRow(0)
        self._widgetList.clear()

    def build(self, pill: PillTagWidget) -> Self:
        self._pill = pill
        self.clearLayout()
        for name, dattr in getDesciptors(pill.tag).items():
            widget = dattr.widget(self)
            widget.setData(**{name: pill.tag[name]})
            self._widgetList.append(widget)
            self.tagItemLayout.addRow(dattr.text, widget)
        self.resize(self.sizeHint())
        return self

    def closeEvent(self, event: QCloseEvent) -> None:
        changes = {}
        for widget in self._widgetList:
            changes.update(widget.data())

        self.editingFinished.emit(self._pill, changes)
        return super().closeEvent(event)
