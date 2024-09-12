from typing import Union

from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt
from PySide6.QtGui import QStandardItemModel



class FieldModel(QStandardItemModel):
    def flags(self, index: Union[QModelIndex, QPersistentModelIndex]) -> Qt.ItemFlag:
        if index.isValid():
            if index.column() == 0:
                return Qt.ItemFlag.ItemIsEnabled
        return super().flags(index)

    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int) -> Union[str, None]:
        if role == Qt.ItemDataRole.TextAlignmentRole:
            if index.column() == 0: 
                return Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            else:
                return Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        return super().data(index, role)
