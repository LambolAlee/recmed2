from attrs import Factory
from PySide6.QtCore import QSettings

from .configitem import ConfigItem
from recmedtyping import PathManager, ThemeMode, Language, RecentVaultList



class AppConfig(QSettings):
    geometry:    ConfigItem[str]              = ConfigItem("geometry")
    theme:       ConfigItem[ThemeMode]        = ConfigItem("theme", default=ThemeMode.light)
    language:    ConfigItem[Language]         = ConfigItem("language", default=Language.en)
    recentFiles: ConfigItem[RecentVaultList]  = ConfigItem("recentVault", section="Vaults", default=Factory(list))

    def __init__(self) -> None:
        super().__init__(PathManager.instance().appConfigFile, QSettings.Format.IniFormat)
