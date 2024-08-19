from pathlib import Path
from enum import StrEnum, Enum, auto
from typing import List

from attrs import define, field
from attrs import validators, Attribute

from utils import Singleton
from contentwidget.plugins import defines as cwDefines



# type alias
RecentVaultList = List[str]


class ConfigKeys(StrEnum):
    configFolder = ".recmed"
    appConfigName = "recmed.ini"


def _check_create_dirs(instance, attribute: Attribute, value: Path) -> Path:
    if not value.exists():
        value.mkdir(parents=True)
    return value

@Singleton
@define
class PathManager:
    executablePath: Path = field(init=False, validator=validators.instance_of(Path))
    rootPath: Path = field(init=False)
    workDir: Path = field(init=False, on_setattr=_check_create_dirs)
    logDir: Path = field(init=False, on_setattr=_check_create_dirs)
    appConfigFile: Path = field(init=False)

    def init(self, executablePath: Path):
        self.executablePath = executablePath
        self.rootPath = executablePath.parent.parent
        self.workDir = self.rootPath / ConfigKeys.configFolder.value
        self.logDir = self.rootPath / "logs"
        self.appConfigFile = self.workDir / ConfigKeys.appConfigName.value


class ThemeMode(Enum):
    light = auto()
    dark = auto()

class Language(Enum):
    en = auto()
    zh = auto()


# Enums from ContentWidget package
Genders = cwDefines.Genders
EthnicGroup = cwDefines.EthnicGroup
AgeUnit = cwDefines.AgeUnit
