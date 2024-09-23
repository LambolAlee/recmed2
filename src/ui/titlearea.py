from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget


class TitleArea(QWidget):
    def __init__(self, parent: QWidget | None=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        layout.setSpacing(4)
        self.showLabel = QLabel(self)
        layout.addWidget(self.showLabel)

        self.editLine = QLineEdit(self)
        self.editLine.hide()
        layout.addWidget(self.editLine)

        self.setLayout(layout)

    def showTitle(self):
        self.editLine.hide()
        self.showLabel.setText(self.editLine.text())

    def editTitle(self):
        self.editLine.setText(self.showLabel.text())
        self.showLabel.setText(' ')
        self.editLine.show()
