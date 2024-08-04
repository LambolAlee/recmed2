from pathlib import Path

from pluggy import PluginManager

from recmedtyping import PluginApiNamespace
from .cwpluginapi import cwspec
from pluginhelper import PluginImporter


class CWLoader:
    def __init__(self) -> None:
        self.pluginFolder = Path(__file__).parent / "plugins"
        self.loadContentPlugins()

    def loadContentPlugins(self) -> None:
        self.pm = PluginManager(PluginApiNamespace.contentWidget)
        self.pm.add_hookspecs(cwspec)

        with PluginImporter(self.pluginFolder) as importer:
            for pluginPath, metadata in importer.findPluginsInPath(self.pluginFolder):
                plugin = importer.doImport(pluginPath, metadata)
                if plugin is not None:
                    self.pm.register(plugin, metadata.getPluginNsName())

    def getPlugin(self, name: str, namespace: str="global"):
        return self.pm.get_plugin(f"{namespace}::{name}")
