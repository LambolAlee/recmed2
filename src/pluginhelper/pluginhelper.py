from re import compile
from keyword import iskeyword
from pathlib import Path
from typing import Iterator, cast, Optional, Self
from types import ModuleType
from importlib.util import spec_from_file_location, module_from_spec
from importlib.abc import Loader

from attrs import define, field, Attribute, asdict
from ujson import loads


namePattern = compile(r'^[a-z][a-z0-9_]*$')


def _isValidName(instance, attribute: Attribute, name: str) -> bool:
    if not namePattern.match(name):
        return False
    if iskeyword(name):
        return False
    if name in dir(__builtins__):
        return False
    if '__' in name:
        return False
    return True


@define
class PluginMetadata:
    name: str = field(validator=_isValidName)
    version: str
    source: str
    author: str
    description: str = "Plugin description here"
    namespace: str = field(default="global", validator=_isValidName)
    entryPoint: str = field(default="plugin", validator=_isValidName)
    isPackage: bool = False

    def getPluginNsName(self) -> str:
        return f"{self.namespace}::{self.name}"
    
    def mergeMetadata(self, metadata: Self) -> Self:
        return self.__class__(**{**asdict(self), **asdict(metadata)})

    @classmethod
    def fromPath(cls, metadataFile: Path) -> Optional[Self]:
        try:
            data = loads(metadataFile.read_text(encoding='utf-8'))
            return cls(**data)
        except Exception:
            return None


@define
class PluginFinder:
    # loadWhenFind: bool = True
    def findPluginsInPath(self, pluginFolder: Path, _packageMetadata: PluginMetadata=PluginMetadata("","","",""), _inSubPackage: bool=False) -> Iterator[Optional[ModuleType]]:
        for metadataFile in pluginFolder.glob("*/metadata.json"):
            metadata = cast(PluginMetadata, PluginMetadata.fromPath(metadataFile))
            if metadata.isPackage:
                if _inSubPackage:
                    # the package is a subpackage of a package of plugins, don't resolve it
                    continue
                else:
                    # the current folder is a package of plugins
                    yield from self.findPluginsInPath(metadataFile.parent, metadata, metadata.isPackage)
            else:
                if _inSubPackage:
                    metadata = _packageMetadata.mergeMetadata(metadata)
                # the current folder is a single plugin
                yield self._loadPlugin(metadataFile.parent, metadata)

    def findPlugin(self, pluginPath: Path) -> Optional[ModuleType]:
        metadata = PluginMetadata.fromPath(pluginPath / "metadata.json")
        return self._loadPlugin(pluginPath, metadata) if metadata is not None else None

    def findPluginsInPackage(self, packagePath: Path) -> Iterator[Optional[ModuleType]]:
        metadata = PluginMetadata.fromPath(packagePath / "metadata.json")
        if metadata is None:
            return
        if metadata.isPackage:
            yield from self.findPluginsInPath(packagePath, _packageMetadata=metadata, _inSubPackage=True)

    def _loadPlugin(self, pluginPath: Path, metadata: PluginMetadata) -> Optional[ModuleType]:
        module = None
        spec = spec_from_file_location(metadata.name, pluginPath / f"{metadata.entryPoint}.py")
        if spec is not None:
            module = module_from_spec(spec)
            loader = cast(Loader, spec.loader)
            loader.exec_module(module)
            setattr(module, "metadata", metadata)
        return module
