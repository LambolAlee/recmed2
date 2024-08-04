from PySide6.QtWidgets import QWidget
from ... import IViewport


class PatientInfoViewport(QWidget, IViewport):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
