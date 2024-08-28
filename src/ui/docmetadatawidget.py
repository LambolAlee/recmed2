from PySide6.QtWidgets import QWidget

from ._ui.docmetadatawidget_ui import Ui_DocMetadataWidget
from recmedtyping import getIcon, RMIconType
from utils import fillPlaceholderWidget


class DocMetadataWidget(QWidget, Ui_DocMetadataWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setupUi(self)
        self.title.setFixedHeight(30)   # FIXME: change the name of the stackedwidget to a more reliable one

        self.saveButton.setIcon(getIcon(RMIconType.circleCheck))
        self.discardButton.setIcon(getIcon(RMIconType.circleXmark))

    def setTitle(self, title: str):
        self.titleLabel.setText(title)
        self.titleEdit.setText(title)

    def setTagsWidget(self, tagsWidget: QWidget):
        tagsWidget.setParent(self)
        self.tagsWidget = fillPlaceholderWidget(self.tagsWidget, tagsWidget, self.layout())


def main():
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    w = DocMetadataWidget()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()
