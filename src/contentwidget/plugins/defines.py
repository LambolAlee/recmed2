from enum import StrEnum, auto


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
