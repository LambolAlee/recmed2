from ui.colorwheel import ColorWheel
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QWidget, QPushButton



class Test:
    def test(self):
        self.w = QWidget()
        b = QPushButton("popup", self.w)
        self.c = ColorWheel.popup(QPoint(100, 100))
        b.clicked.connect(self.c.show)
        self.c.colorSelectionChanged.connect(print)
        self.w.show()
