from datetime import date as Date

from attrs import define, field
from ...defines import Genders, EthnicGroup, AgeUnit


@define
class DataPipe:
    name: str = ""
    age: int = 0
    ageUnit: AgeUnit = AgeUnit.year
    gender: Genders = Genders.male
    birthday: Date = Date.today()
    ethnicGroup: EthnicGroup = EthnicGroup.white
    height: int = 0
    weight: int = 0
    bmi: int = field(init=False)
    W: int = 0
    MH: int = 0

    def useMapping(table: str):
        pass
