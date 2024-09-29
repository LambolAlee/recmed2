from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSizePolicy



class SideSpace(QWidget):
    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)
        self.setMinimumWidth(80)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
