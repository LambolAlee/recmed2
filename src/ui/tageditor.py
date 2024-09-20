from typing import List, Self

from PySide6.QtCore import Qt, QPoint, Signal, QSize, QEvent
from PySide6.QtGui import QCloseEvent, QKeyEvent
from PySide6.QtWidgets import QWidget, QFormLayout, QMessageBox

from ._ui.tageditor_ui import Ui_TagEditor
from .pilltagwidget import PillTagWidget
from utils import getMaxMinimumSize
from descriptivecontrol import DescriptiveWidget



class TagEditor(QWidget, Ui_TagEditor):
    editingFinished = Signal(PillTagWidget, dict)
    tagRemoveRequest = Signal(PillTagWidget)

    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.tagItemLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.tagItemLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.tagItemLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.tagItemLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        self._widgetList: List[DescriptiveWidget] = []
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
        for name, dattr in pill.tag.getDescriptors().items():
            widget = dattr.widget(self)
            widget.setData(**{name: pill.tag[name]})
            self._widgetList.append(widget)
            self.tagItemLayout.addRow(dattr.displayName(), widget)
        self.setFixedSize(self.sizeHint())
        return self
    
    def changeEvent(self, event: QEvent) -> None:
        if event.type() == QEvent.Type.ActivationChange:
            if not self.isActiveWindow():   # lost focus and close editor
                self.close()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Escape:    # press esc to close editor
            self.close()
        else:
            return super().keyPressEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.checkAndSubmitChanges():
            event.accept()
        else:
            event.ignore()

    def checkAndSubmitChanges(self) -> bool:
        """
        True: changes submitted
        False: invalid data found
        """
        changes = {}
        for widget in self._widgetList:
            if widget.attributeName() == 'name' and widget.data()['name'] == '':    # tag name cannot be empty
                answer = QMessageBox.information(self, "Invalid Data", "Tag name is empty, do you want to delete the tag?", QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
                if answer == QMessageBox.StandardButton.Yes:
                    self.tagRemoveRequest.emit(self._pill)
                    return True
                else:
                    return False
            changes.update(widget.data())

        self.editingFinished.emit(self._pill, changes)
        return True
