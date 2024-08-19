from enum import StrEnum, auto
from typing import TypedDict


class Genders(StrEnum):
    male = auto()
    female = auto()


class EthnicGroup(StrEnum):
    white = auto()


class AgeUnit(StrEnum):
    year = auto()
    month = auto()
    week = auto()
    day = auto()


class Decoction(StrEnum):
    normal = "无"
    first = "先煎"
    last = "后下"


class DrugUnit(StrEnum):
    g = "g"


class DrugDict(TypedDict):
    name: str
    dose: int
    unit: str
    decoction: str
