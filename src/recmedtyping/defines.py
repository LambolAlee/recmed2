from pathlib import Path
from enum import Enum, auto

from attrs import define, field, frozen
from attrs import validators, Attribute

from utils import Singleton


class ConfigKeys(Enum):
    configFolder: str = ".recmed"
    appConfigName: str = "recmed.ini"


def _check_create_dirs(instance, attribute: Attribute, value: Path) -> None:
    if not value.exists():
        value.mkdir(parents=True)
    return value

@Singleton
@define
class PathManager:
    executablePath: Path = field(init=False, validator=validators.instance_of(Path))
    rootPath: Path = field(init=False)
    workDir: Path = field(init=False, on_setattr=_check_create_dirs)
    appConfigFile: Path = field(init=False)

    def init(self, executablePath: Path):
        self.executablePath = executablePath
        self.rootPath = executablePath.parent.parent
        self.workDir = self.rootPath / ConfigKeys.configFolder.value
        self.appConfigFile = self.workDir / ConfigKeys.appConfigName.value


class ThemeMode(Enum):
    light = auto()
    dark = auto()

class Language(Enum):
    en = auto()
    zh = auto()
