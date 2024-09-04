from PySide6.QtCore import QAbstractListModel, QObject, QModelIndex, Qt, QPersistentModelIndex

from recmedtyping import RMIconType



class IconModel(QAbstractListModel):
    def __init__(self, parent: QObject | None=None) -> None:
        super().__init__(parent)
        self._raw = [i.name for i in RMIconType]
        self._source = {False: self._raw, True: []}
        self._searchMode = False
        self._rowCount = len(self._source[self._searchMode])

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        return self._rowCount

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int=Qt.ItemDataRole.DisplayRole):
        if role in (Qt.ItemDataRole.UserRole, Qt.ItemDataRole.ToolTipRole):
            if index.row() >= self._rowCount:
                return
            else:
                return self._source[self._searchMode][index.row()]

    def setSearchMode(self, searchMode: bool):
        self._searchMode = searchMode

    def setSearchText(self, text: str):
        self.beginResetModel()
        if self._searchMode:
            self._source[self._searchMode] = [name for name in self._raw if text in name]
        self._rowCount = len(self._source[self._searchMode])
        self.endResetModel()
