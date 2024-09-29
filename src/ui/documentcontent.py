from PySide6.QtWidgets import QWidget, QVBoxLayout

from .docmetadatawidget import DocMetadataWidget
from .contentarea import ContentArea
from .fieldarea import FieldArea



class DocumentContent(QWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setMinimumWidth(650)

        layout = QVBoxLayout()
        layout.setSpacing(0)

        self.metadataWidget = DocMetadataWidget(self)
        layout.addWidget(self.metadataWidget, stretch=0)

        self.contentArea = ContentArea(self)
        layout.addWidget(self.contentArea, stretch=1)

        self.fieldArea = FieldArea(self)
        layout.addWidget(self.fieldArea, stretch=0)

        self.setLayout(layout)

        self.metadataWidget.showFieldSignal.connect(self.fieldArea.setVisible)
