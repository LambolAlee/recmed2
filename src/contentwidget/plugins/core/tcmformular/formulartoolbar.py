from typing import Dict

from PySide6.QtCore import Signal, Qt, QEvent
from PySide6.QtGui import QAction, QMouseEvent
from PySide6.QtWidgets import QToolBar, QWidget, QHBoxLayout, QCheckBox, QLabel



class FormularToolBar(QToolBar):
    selectAllSignal = Signal()

    def __init__(self, parent: QWidget | None=None):
        super().__init__(parent)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        drugCountWidget = QWidget(self)
        layout = QHBoxLayout()
        label = QLabel("Total: ", self)
        layout.addWidget(label)
        self.drugCountLabel = QLabel("0", self)
        layout.addWidget(self.drugCountLabel)
        drugCountWidget.setLayout(layout)
        drugCountWidget.setStyleSheet("background-color: #2d82f2; border-radius: 5px;")
        drugCountWidget.installEventFilter(self)

        self.addWidget(drugCountWidget)
        self.addSeparator()

    def setDrugCount(self, count: int):     # FIXME: drug count not updated
        self.drugCountLabel.setNum(count)

    def eventFilter(self, obj, event) -> bool:
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                self.selectAllSignal.emit()
                return True
        return super().eventFilter(obj, event)
