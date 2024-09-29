from PySide6.QtWidgets import QWidget, QStackedLayout

from .contentwidgetcontainer import ContentWidgetContainer
from .contenttemplateeditor import ContentTemplateEditor



class ContentArea(QWidget):
    def __init__(self, parent: QWidget | None=None):
        super().__init__(parent)

        layout = QStackedLayout()

        self.contentWidgetContainer = ContentWidgetContainer(self)
        layout.addWidget(self.contentWidgetContainer)

        self.contentTemplateEditor = ContentTemplateEditor(self)
        layout.addWidget(self.contentTemplateEditor)

        layout.setCurrentIndex(0)
        self.setLayout(layout)
