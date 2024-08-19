from pathlib import Path

from pluggy import PluginManager

from . import ContentWidgetPluginApi
from pluginhelper import PluginImporter


class CWLoader:
    def __init__(self) -> None:
        self.pluginFolder = Path(__file__).parent / "plugins"
        self.loadContentPlugins()

    def loadContentPlugins(self) -> None:
        self.pm = PluginManager(ContentWidgetPluginApi.ContentWidgetId)
        self.pm.add_hookspecs(ContentWidgetPluginApi.IContentWidget)

        with PluginImporter(self.pluginFolder) as importer:
            for plugin, metadata in importer.importAllPlugins():
                self.pm.register(plugin, metadata.getPluginNsName())

    def getPlugin(self, name: str, namespace: str="global"):
        return self.pm.get_plugin(f"{namespace}::{name}")
