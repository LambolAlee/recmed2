from PySide6.QtWidgets import QWidget


class DocumentContent(QWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        # TODO Add MetadataWidget and ContentBox widgets to a vertical layout
