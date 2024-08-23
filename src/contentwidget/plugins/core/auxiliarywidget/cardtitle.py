from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class CardTitle(QWidget):
    def __init__(self, title: str="", parent: QWidget = None):
        super().__init__(parent)
        self.title = QLabel(title, self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.title)
        self.title.setContentsMargins(0, 4, 4, 4)
        self.setLayout(layout)

        self.setStyleSheet("background: transparent; border-bottom: 2px solid #2d82f2;")    # TODO: color need to be managed together

    def setTitle(self, title: str):
        self.title.setText(title)
