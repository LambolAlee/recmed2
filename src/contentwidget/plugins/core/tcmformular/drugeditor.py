from typing import Optional

from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect

from .formularmodel import DrugObject, DrugUnit, Decoction
from ._ui.drugeditor_ui import Ui_DrugEditor



class DrugEditor(QWidget, Ui_DrugEditor):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet("DrugEditor{background-color:#f0f0f0;}")

        self.initUi()

        # important to solve the focus problem when first appears on the view
        self.setFocusProxy(self.nameEdit)
        self._setDropShadow()

    def initUi(self) -> None:
        self.unitComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.decoctionComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.unitComboBox.addItems(DrugUnit)
        self.decoctionComboBox.addItems(Decoction)
        self.nameEdit.setPlaceholderText("请输入药品名称")

    def _setDropShadow(self):
        e = QGraphicsDropShadowEffect(self)
        e.setColor(QColor(63,63,63,30))
        e.setBlurRadius(20)
        e.setXOffset(3)
        e.setYOffset(3)
        self.setGraphicsEffect(e)

    def setDrug(self, drugObj: DrugObject):
        self.drugObj = drugObj
        self.nameEdit.setText(drugObj.name)
        self.doseSpinBox.setValue(drugObj.dose)
        self.unitComboBox.setCurrentText(drugObj.unit)
        self.decoctionComboBox.setCurrentText(drugObj.decoction)

    def setGeometry(self, rect: QRect):
        self.setFixedWidth(rect.width())
        self.nameEdit.setFixedHeight(rect.height())
        self.doseSpinBox.setFixedHeight(rect.height())
        self.move(rect.topLeft())

    def submit(self) -> Optional[DrugObject]:
        name = self.nameEdit.text()
        if name == "":
            return None
        else:
            self.drugObj.name = name
        self.drugObj.dose = self.doseSpinBox.value()
        self.drugObj.unit = DrugUnit(self.unitComboBox.currentText())
        self.drugObj.decoction = Decoction(self.decoctionComboBox.currentText())
        return self.drugObj

    def focusNextPrevChild(self, next: bool) -> bool:
        """
        line 6808: https://github1s.com/qt/qtbase/blob/dev/src/widgets/kernel/qwidget.cpp
        along with the souce code of QStyledItemDelegate, QAbstractItemDelegate, QTableView and QAbstractItemView
        
        The editor created by delegate is not a window or subwindow, and meanwhile the parent of the editor is set to the view,
        so the default focusNextPrevChild() will call the view to handle focus changes and allows the view-related delegate to solve keypress event.
        It is right when the editor is a simple widget, but if the editor is a complex one, the tab and backtab will not work as expected.

        commands = {fw: {True: focusNext, False: focusPrev}}
        """
        def _focusOn(widget) -> bool:
            def wrapper():
                widget.setFocus()
                widget.selectAll()
                return True
            return wrapper

        fw = self.focusWidget()
        commands = {
            self.nameEdit: {
                True: _focusOn(self.doseSpinBox),
                False: lambda: False
            },
            self.doseSpinBox: {
                True: lambda: False,
                False: _focusOn(self.nameEdit)
            }
        }
        return commands.get(fw, {}).get(next, lambda: super().focusNextPrevChild(next))()
