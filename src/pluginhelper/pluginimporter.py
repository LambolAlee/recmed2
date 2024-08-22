import sys

from re import compile
from keyword import iskeyword
from pathlib import Path
from typing import Iterator, Optional, Self, Tuple
from typing_extensions import Literal
from types import ModuleType
from functools import wraps

from importlib import import_module

from attrs import define, field, Attribute, asdict
from ujson import loads



namePattern = compile(r'^[a-z][a-z0-9_]*$')
def _isValidName(instance, attribute: Attribute, name: str) -> bool:
    """
    A private attrs-validator function that is used to ensure the plugin name conforms the python naming conventions
    """
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
    """
    Metadata of a plugin, helps to locate and load a plugin
    """
    name: str = field(validator=_isValidName)
    version: str
    source: str
    author: str
    description: str = "Plugin description here"
    namespace: str = field(default="global", validator=_isValidName)
    # entryPoint: str = field(default="plugin", validator=_isValidName)
    isPackage: bool = False

    def getPluginNsName(self) -> str:
        return f"{self.namespace}::{self.name}"
    
    def mergeMetadata(self, metadata: Self) -> Self:
        packageMetadata = asdict(self)
        moduleMetadata = asdict(metadata)
        del moduleMetadata["namespace"]
        return self.__class__(**{**packageMetadata, **moduleMetadata})

    @classmethod
    def fromPath(cls, metadataFile: Path) -> Optional[Self]:
        try:
            data: dict = loads(metadataFile.read_text(encoding='utf-8'))
            return cls(**data)
        except Exception:
            return None     # TODO: add log



@define
class PluginImporter:
    """
    Exact plugin importer class, discover and load plugins in the given plugins folder
    - basePluginsFolder: the folder that contains all plugins

    when using import_ method to really import a plugin, the method call must be put into a `with` block to adapt the original
    python import system to the customed plugin import procedure and restore it to the normal automatically.
    """
    basePluginsFolder: Path
    _inWithBlock: bool = field(init=False, alias="_inWithBlock", default=False)

    @staticmethod
    def _ensure(method):
        @wraps(method)
        def wrapper(self, pluginsFolder: Optional[Path], packageInfo: Optional[PluginMetadata]=None):
            if self._inWithBlock is False:
                raise RuntimeError("When do import operation, PluginHelper must be in a 'with' block!")
            if  pluginsFolder is not None \
            and pluginsFolder.is_relative_to(self.basePluginsFolder) is False:
                raise ValueError(f"The given plugins folder({pluginsFolder}) is not in the base folder({self.basePluginsFolder})!")

            yield from method(self, pluginsFolder, packageInfo)
        return wrapper

    def importAllPlugins(self) -> Iterator[Tuple[PluginMetadata, ModuleType]]:
        try:
            yield from self.import_(None)
        except TypeError:
            return list()   # TODO: add log

    @_ensure
    def import_(self, pluginsFolder: Optional[Path], packageInfo: Optional[PluginMetadata]=None) -> Iterator[Tuple[ModuleType, PluginMetadata]]:
        for p, metadata in self._findPluginsInPath(pluginsFolder, packageInfo):
            if metadata.isPackage:
                yield from self.import_(p, metadata) # load package
            else:
                yield self._loadPlugin(p, metadata) # load single plugin

    def _findPluginsInPath(self, pluginsFolder: Optional[Path], packageInfo: Optional[PluginMetadata]=None) -> Iterator[Tuple[Path, PluginMetadata]]:
        if pluginsFolder is None:
            pluginsFolder = self.basePluginsFolder

        for metadataFile in pluginsFolder.glob("*/metadata.json"):
            metadata = PluginMetadata.fromPath(metadataFile)
            if metadata is None: continue
            if packageInfo is not None: 
                if metadata.isPackage: continue
                metadata = packageInfo.mergeMetadata(metadata)
            yield metadataFile.parent, metadata

    def _loadPlugin(self, pluginFolder: Path, metadata: PluginMetadata) -> Tuple[ModuleType, PluginMetadata]:
        return import_module(f".{self._path2Fullname(pluginFolder)}", package="plugins"), metadata

    def _path2Fullname(self, pluginPath: Path) -> str:
        p = pluginPath.relative_to(self.basePluginsFolder)
        return '.'.join(p.parts)

    def __enter__(self) -> Self:
        self._inWithBlock = True
        sys.path.append(str(self.basePluginsFolder.parent))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> Literal[False]:
        self._inWithBlock = False
        sys.path.pop()
        return False
