from PySide6.QtWidgets import QWidget, QHBoxLayout

from .documentcontent import DocumentContent
from .sidespace import SideSpace



class DocumentWidget(QWidget):
    def __init__(self, parent: QWidget | None=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        layout.setSpacing(0)

        self.leftSideSpace = SideSpace(self)
        layout.addWidget(self.leftSideSpace, stretch=1)

        self.content = DocumentContent(self)
        layout.addWidget(self.content, stretch=2)

        self.rightSideSpace = SideSpace(self)
        layout.addWidget(self.rightSideSpace, stretch=1)

        self.setLayout(layout)
