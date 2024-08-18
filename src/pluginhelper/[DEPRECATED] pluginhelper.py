"""
DEPRECATED - DO NOT USE
The plugin helper class uses the customed ModuleFinder to handle the customized import-statement inside each plugin
"""
import sys

from re import compile
from keyword import iskeyword
from pathlib import Path
from typing import Iterator, Sequence, cast, Optional, Self, Tuple
from types import ModuleType

from importlib import import_module
from importlib.machinery import ModuleSpec, SourceFileLoader
from importlib.abc import MetaPathFinder

from attrs import define, field, Attribute, asdict
from ujson import loads



class ModuleFinder(MetaPathFinder):
    """
    Handles the customized directly and relatively import-statement inside each plugin
    """
    def __init__(self, pluginFolder: Path):
        self.pluginFolder = pluginFolder
        self._prefix = "plugins"

    def find_spec(self, fullname: str, path: Sequence[str] | None, target: ModuleType | None = None) -> Optional[ModuleSpec]:
        if not fullname.startswith(self._prefix):    # filter using plugins namespace
            return None     # None means this turn of the finder is not responsible for this module

        nameParts = fullname.split('.')

        # build path of plugin module or package
        filename = self.pluginFolder.joinpath(*nameParts[1:])
        if filename.is_dir():
            filename = filename / "__init__.py"
            is_package = True
        else:
            filename = filename.with_suffix('.py')
            is_package = False
        
        if filename.exists():
            return ModuleSpec(fullname, SourceFileLoader(fullname, str(filename)), is_package=is_package)
        else:
            return None



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
    entryPoint: str = field(default="plugin", validator=_isValidName)
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
            return None     # TODO add log



@define
class PluginImporter:
    """
    Exact plugin importer class, discover and load plugins in the given plugins folder
    - pluginFolder: the folder that contains all plugins

    when using doImport method to really import a plugin, the method call must be put into a `with` block to adapt the original
    python import system to the custom plugin import process and restore it to the normal automatically.
    """
    pluginFolder: Path
    _modFinder: ModuleFinder = field(init=False, alias="_modFinder", default=None)
    _inWithBlock: bool = field(init=False, alias="_inWithBlock", default=False)

    def __attrs_post_init__(self):
        self._modFinder = ModuleFinder(self.pluginFolder)

    def findPluginsInPath(self, pluginFolder: Path, _packageMetadata: PluginMetadata=PluginMetadata("","","",""), _inSubPackage: bool=False) -> Iterator[Tuple[Path, PluginMetadata]]:
        for metadataFile in pluginFolder.glob("*/metadata.json"):
            metadata = cast(PluginMetadata, PluginMetadata.fromPath(metadataFile))
            if metadata.isPackage:
                if _inSubPackage:
                    # the package is a subpackage of a package of a plugin, don't resolve it
                    continue
                else:
                    # the current folder is a package of plugins
                    yield from self.findPluginsInPath(metadataFile.parent, metadata, metadata.isPackage)
            else:
                if _inSubPackage:
                    # the current folder is a single plugin in a parent package
                    metadata = _packageMetadata.mergeMetadata(metadata)
                # the current folder is a single plugin
                yield metadataFile.parent, metadata

    def findPlugin(self, pluginPath: Path) -> Optional[Tuple[Path, PluginMetadata]]:
        metadata = PluginMetadata.fromPath(pluginPath / "metadata.json")
        return (pluginPath, metadata) if metadata is not None else None

    def findPluginsInPackage(self, packagePath: Path) -> Iterator[Tuple[Path, PluginMetadata]]:
        metadata = PluginMetadata.fromPath(packagePath / "metadata.json")
        if metadata is None:
            return
        if metadata.isPackage:
            yield from self.findPluginsInPath(packagePath, _packageMetadata=metadata, _inSubPackage=True)

    def path2Fullname(self, pluginPath: Path, metadata: PluginMetadata) -> str:
        p = pluginPath.relative_to(self.pluginFolder)
        p = self.pluginFolder.name / p / metadata.entryPoint
        return '.'.join(p.parts)

    def doImport(self, pluginPath: Path, metadata: PluginMetadata) -> Optional[ModuleType]:
        if not self._inWithBlock:
            raise RuntimeError("When do import operation, PluginHelper must be in a 'with' block!")

        try:
            module = import_module(self.path2Fullname(pluginPath, metadata))
        except Exception as e:
            raise
            return None     # TODO: log error when finished writing log system, can also add load failed to the user interface
        else:
            setattr(module, "metadata", metadata)
            return module

    def __enter__(self):
        self._inWithBlock = True
        sys.meta_path.insert(0, self._modFinder)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._inWithBlock = False
        sys.meta_path.remove(self._modFinder)
        return False
