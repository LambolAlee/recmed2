from PySide6.QtWidgets import QWidget

from ._ui.titlearea_ui import Ui_TitleArea



class TitleArea(QWidget, Ui_TitleArea):
    def __init__(self, title: str='New Document', parent: QWidget | None=None):
        super().__init__(parent)
        self.setupUi(self)
        self.showLabel.setText(title)
        self.editLine.setText(title)

        self.showLabel.setFixedHeight(30)
        self.editLine.setFixedHeight(30)

    def setEditMode(self, editMode: bool):
        self.stackedWidget.setCurrentIndex(int(editMode))
        if editMode:
            self.editLine.setText(self.showLabel.text())
        else:
            self.showLabel.setText(self.editLine.text())

    def showTitle(self):
        self.editLine.hide()
        self.showLabel.setText(self.editLine.text())

    def editTitle(self):
        self.editLine.setText(self.showLabel.text())
        self.showLabel.setText(' ')
        self.editLine.show()
