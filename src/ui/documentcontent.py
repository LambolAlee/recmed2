from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy

from .docmetadatawidget import DocMetadataWidget
from .contentarea import ContentArea
from .fieldarea import FieldArea



class DocumentContent(QWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout = QVBoxLayout()
        layout.setSpacing(2)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinAndMaxSize)

        self.metadataWidget = DocMetadataWidget(self)
        layout.addWidget(self.metadataWidget)

        self.contentArea = ContentArea(self)
        layout.addWidget(self.contentArea, stretch=1)

        self.fieldArea = FieldArea(self)
        layout.addWidget(self.fieldArea)

        self.setLayout(layout)

        self.metadataWidget.showFieldSignal.connect(self.fieldArea.setVisible)
