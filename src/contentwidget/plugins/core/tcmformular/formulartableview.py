from PySide6.QtWidgets import QTableView, QWidget, QHeaderView

from .formulardelegate import FormularDelegate



class FormularTableView(QTableView):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setMinimumWidth(600)
        self.delegate = FormularDelegate(self)
        self.setItemDelegate(self.delegate)

        self.verticalHeader().hide()
        self.horizontalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
