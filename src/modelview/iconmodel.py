from PySide6.QtCore import QAbstractListModel, QObject, QModelIndex, Qt, QPersistentModelIndex

from recmedtyping import RMIconType



class IconModel(QAbstractListModel):
    def __init__(self, parent: QObject | None=None) -> None:
        super().__init__(parent)
        self.rmicontype =  [i.name for i in RMIconType]
        self._rowCount = len(self.rmicontype) -1

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        return self._rowCount

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.UserRole:
            return self.rmicontype[index.row()]

