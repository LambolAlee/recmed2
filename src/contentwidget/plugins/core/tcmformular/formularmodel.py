from enum import Enum, auto
from math import ceil
from typing import List, Iterable, Self
from collections import UserList
from itertools import chain

from attrs import define, field
from PySide6.QtCore import QObject, Qt
from PySide6.QtCore import QAbstractTableModel, QModelIndex

from ... import Decoction, DrugDict, DrugUnit



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

    @classmethod
    def map(cls, arow: Iterable[DrugDict | str | None]) -> List[Self]:
        return list(map(cls, arow))

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
    _formularData: DrugDict = field(alias='_formularData')
    rows: int = field(init=False, default=1)
    columns: int = field(init=False, default=4)

    def __attrs_post_init__(self) -> None:
        self._resetObjectWithData()

    def _resetObjectWithData(self):
        self.data = []
        self.rows = max(1, ceil(len(self._formularData) / self.columns))
        for i in range(self.rows):
            arow = self._formularData[i * self.columns:(i + 1) * self.columns]
            if len(arow) < 4:
                arow.extend([Placeholder.BLANK] * (self.columns - len(arow)))
            self.addRow(arow)

    def addRow(self, arow: List[str]):
        self.data.append(DrugObject.map(arow))

    def __getitem__(self, index: QModelIndex) -> DrugObject:
        """
        slicing is not supported
        """
        return self.data[index.row()][index.column()]

    def __setitem__(self, index: QModelIndex, value: DrugObject):
        self.data[index.row()][index.column()] = value

    def __iter__(self):
        return chain(*self.data)

    def __len__(self) -> int:
        return len(chain(*self.data))



class FormularTableModel(QAbstractTableModel):
    def __init__(self, formularData, parent: QObject=None):
        super().__init__(parent)

        self._formular = Formular(formularData)

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
        when the count of the drugs less than 4, use the length of the formular instead
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
        return True

    def maxLengthDrug(self) -> DrugObject:
        return max(self._formular)
