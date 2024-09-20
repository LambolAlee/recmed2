from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow
from ui.colorpicker import ColorPicker, ColorHSSelector, ColorPreview, ColorValueSelector


class Test:
    def test(self):
        self.w = QMainWindow()
        # self.c = ColorHSSelector(self.w)
        # self.c = ColorPreview(parent=self.w)
        # self.c = ColorValueSelector(parent=self.w)
        # self.c.setWidth(200)
        # self.c.move(100, 100)
        self.c = ColorPicker(parent=self.w)
        self.c.setColor(QColor("#3389bb"))
        self.w.setCentralWidget(self.c)
        self.w.show()
