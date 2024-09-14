from enum import Enum, auto
from math import ceil
from typing import List, Iterable, Self
from collections import UserList
from itertools import chain

from attrs import define, field, Factory
from PySide6.QtCore import Qt, Signal
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QItemSelectionModel

from ...defines import Decoction, DrugDict, DrugUnit



class Placeholder(Enum):
    BLANK = auto()
    EDITING = auto()


def _updateData(instance, attribute, value):
    if getattr(instance, "data") is Placeholder.BLANK and value != '':
        setattr(instance, "data", Placeholder.EDITING)
    return value

@define
class DrugObject:
    data: DrugDict | Placeholder = Placeholder.BLANK

    name: str = field(init=False, default="", on_setattr=_updateData)
    dose: int = field(init=False, default=0)
    unit: DrugUnit = field(init=False, default=DrugUnit.g)
    decoction: Decoction = field(init=False, default=Decoction.normal)

    length: int = field(init=False, default=0)

    def __attrs_post_init__(self) -> None:
        if self.data is Placeholder.BLANK:
            return
        self.name = self.data["name"]
        self.dose = self.data["dose"]
        self.unit = DrugUnit(self.data.get("unit", "g"))
        self.decoction = Decoction(self.data.get("decoction", "无"))

    def isPlaceholder(self) -> bool:
        return self.data is Placeholder.BLANK

    def clear(self) -> None:
        self.data = Placeholder.BLANK

    @classmethod
    def map(cls, arow: Iterable[DrugDict | Self | str | None]) -> List[Self]:
        makeObj = lambda data: data if isinstance(data, cls) else cls(data)
        return list(map(makeObj, arow))

    def __str__(self) -> str:
        if self.isPlaceholder():
            return ""
        return f"{self.name} {self.dose}{self.unit}{'' if self.decoction is Decoction.normal else self.decoction}"
    
    def __len__(self) -> int:
        if self.isPlaceholder():
            return 0
        return len(self.name) + len(str(self.dose)) + len(self.unit) + len(self.decoction)
    
    def __lt__(self, other: Self) -> bool:
        return len(self) < len(other)



@define
class Formular(UserList):
    _formularData: List[DrugDict] = field(alias='_formularData', default=Factory(list))
    rows: int = field(init=False, default=1)
    columns: int = field(init=False, default=4)

    def __attrs_post_init__(self) -> None:
        self._resetWithData(self._formularData)

    def _resetWithData(self, data):
        self.data = []
        self.rows = 0
        rows = max(1, ceil(len(data) / self.columns))
        for i in range(rows):
            arow = data[i * self.columns:(i + 1) * self.columns]
            if len(arow) < 4:
                arow.extend([Placeholder.BLANK] * (self.columns - len(arow)))
            self.addRow(arow)

    def setData(self, formularData: List[DrugDict]):
        self._formularData = formularData
        self._resetWithData(formularData)

    def addRow(self, arow: List[str]):
        self.data.append(DrugObject.map(arow))
        self.rows += 1

    def appendEmptyRow(self):
        self.addRow([Placeholder.BLANK] * self.columns)

    def cap(self) -> int:
        return len(chain(*self.data))

    def tidy(self):
        cleanData = []
        for drugObj in chain(*self.data):
            if drugObj.isPlaceholder(): continue
            cleanData.append(drugObj)
        self._resetWithData(cleanData)

    def __getitem__(self, index: QModelIndex | int) -> DrugObject | List[DrugObject]:
        """
        slicing is not supported
        """
        if isinstance(index, QModelIndex):
            return self.data[index.row()][index.column()]
        elif isinstance(index, int):
            return self.data[index]

    def __setitem__(self, index: QModelIndex, value: DrugObject):
        self.data[index.row()][index.column()] = value

    def __iter__(self):
        return chain(*self.data)

    def __len__(self) -> int:
        return sum(not i.isPlaceholder() for i in chain(*self.data))



class FormularTableModel(QAbstractTableModel):
    drugCountChanged = Signal(int)

    def setFormularData(self, formularData: List[DrugDict] | None=None):
        self._formular = Formular([] if formularData is None else formularData)
        self._updateDrugCount()

    def _updateDrugCount(self):
        self.drugCountChanged.emit(len(self._formular))

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        _flags = super().flags(index)
        if not index.isValid():
            return Qt.ItemFlag.ItemIsDropEnabled | _flags
        else:
            return Qt.ItemFlag.ItemIsDragEnabled | Qt.ItemFlag.ItemIsDropEnabled | Qt.ItemFlag.ItemIsEditable | _flags

    def rowCount(self, parent: QModelIndex) -> int:
        """
        calculate row count, hardcoded 4 drugs in one row
        """
        return self._formular.rows if not parent.isValid() else 0

    def columnCount(self, parent: QModelIndex) -> int:
        """
        need the table to be in shape of 4 columns
        """
        return self._formular.columns if not parent.isValid() else 0

    def data(self, index: QModelIndex, role: Qt.ItemDataRole):
        if not index.isValid():
            return None

        match role:
            case Qt.ItemDataRole.DisplayRole:
                return self._formular[index]
            case Qt.ItemDataRole.EditRole:
                return self._formular[index]
            case Qt.ItemDataRole.TextAlignmentRole:
                return Qt.AlignmentFlag.AlignCenter
            case _:
                return None

    def setData(self, index: QModelIndex, value, role: Qt.ItemDataRole) -> bool:
        if not index.isValid():
            return False
        if role == Qt.ItemDataRole.EditRole:
            self._formular[index] = value
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.DisplayRole])
            self._updateDrugCount()
        return True
    
    def insertRows(self, row: int, count: int, parent: QModelIndex=QModelIndex()) -> bool:
        """Only used by add method when appending a new row for now"""
        self.beginInsertRows(parent, row, row + count -1)
        self._formular.appendEmptyRow()
        self.endInsertRows()
        return True
    
    def appendEmptyRow(self) -> None:
        self.insertRow(self._formular.rows)

    def maxLengthDrug(self) -> DrugObject:
        return max(self._formular)

    def tidy(self) -> None:
        self.beginResetModel()
        self._formular.tidy()
        self.endResetModel()

    def removeDrugs(self, selectionModel: QItemSelectionModel):
        if not selectionModel.hasSelection():
            return

        selectedIndexes = selectionModel.selectedIndexes()
        for index in selectedIndexes:
            self._formular[index].clear()
        self.dataChanged.emit(selectedIndexes[0], selectedIndexes[-1], [Qt.ItemDataRole.DisplayRole])
        self._updateDrugCount()

    def addNewDrug(self) -> QModelIndex:
        """
        Find the first empty cell in the drug table, if no empty cell found, append a new row
        """
        column = 0
        for drugObj in self._formular[-1]:
            if drugObj.isPlaceholder(): break
            column += 1
        else:
            self.appendEmptyRow()
            column = 0
        return self.index(self._formular.rows - 1, column)
