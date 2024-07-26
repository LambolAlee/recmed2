from typing import Optional

from attrs import define
from PySide6.QtCore import QSettings

from recmedtyping import PathManager, ThemeMode, Language


@define
class ConfigItem:
    key: str
    section: str = "General"
    default: Optional[str] = None

    def __attrs_post_init__(self) -> None:
        self.item_name = f"{self.section}/{self.key}"

    def __get__(self, instance, owner: QSettings) -> Optional[str]:
        return instance.value(self.item_name, self.default)

    def __set__(self, instance, value: Optional[str]):
        instance.setValue(self.item_name, value)


class AppConfig(QSettings):
    geometry = ConfigItem("geometry")
    theme = ConfigItem("theme", default=ThemeMode.light)
    language = ConfigItem("language", default=Language.en)
    recentFiles = ConfigItem("recentFiles", "File", [])

    def __init__(self) -> None:
        super().__init__(PathManager.instance().appConfigFile, QSettings.Format.IniFormat)
