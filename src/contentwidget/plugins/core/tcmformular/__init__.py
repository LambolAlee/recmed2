from attrs import define, field

from PySide6.QtWidgets import QWidget

from ... import cwimpl
from .viewport import TCMFormularViewport



@define
class TCMFomularPlugin:
    _viewport: TCMFormularViewport = None
    _pluginHelper = field(init=False)

    @cwimpl
    def viewport(self, parent: QWidget=None):
        self._viewport = TCMFormularViewport(parent)
        return self._viewport

    @cwimpl
    def setPluginHelper(self, pluginHelper):
        self._pluginHelper = pluginHelper
