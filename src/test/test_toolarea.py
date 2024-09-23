from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QGridLayout, QWidget
from ui.toolarea import ToolArea

class Test:
    def test(self):
        self.ww = QWidget()
        layout = QGridLayout()
        self.w = ToolArea(parent=self.ww)
        self.l = QLabel("Temp Title Label", self.ww)
        layout.addWidget(self.l, 0, 0, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.w, 0, 0, Qt.AlignmentFlag.AlignRight)
        self.ww.setLayout(layout)
        self.ww.show()
