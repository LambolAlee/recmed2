from pathlib import Path

from pluggy import PluginManager

from recmedtyping import PluginApiNamespace
from .cwpluginapi import cwspec
from pluginhelper import PluginFinder, PluginMetadata


class CWLoader:
    def __init__(self) -> None:
        self.pluginFolder = Path(__file__).parent / "plugins"
        self.loadContentPlugins()

    def loadContentPlugins(self) -> None:
        self.pm = PluginManager(PluginApiNamespace.contentWidget)
        self.pm.add_hookspecs(cwspec)
        
        finder = PluginFinder()
        for plugin in finder.findPlugins(self.pluginFolder):
            metadata: PluginMetadata = plugin.metadata
            self.pm.register(plugin, metadata.getPluginNsName())

    def getPlugin(self, name: str, namespace: str="global"):
        return self.pm.get_plugin(f"{namespace}::{name}")
