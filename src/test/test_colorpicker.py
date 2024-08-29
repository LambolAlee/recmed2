from descriptivecontrol.dcolor import DColor
from PySide6.QtWidgets import QWidget


class Test:
    def test(self):
        self.w = QWidget()
        self.c = DColor()
        self.c.setParent(self.w)
        self.w.show()
