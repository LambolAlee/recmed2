from PySide6.QtWidgets import QMdiSubWindow, QWidget


class Document(QMdiSubWindow):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setWindowTitle("test doc")

        self.initPage()


    def initPage(self) -> None:
        ...
