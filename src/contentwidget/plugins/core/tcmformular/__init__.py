from PySide6.QtWidgets import QWidget

from ... import cwimpl, IContentWidget
from .viewport import TCMFormularViewport



class TCMFomularPlugin(IContentWidget):
    @cwimpl
    def init(self, pluginHelper):
        self._helper = pluginHelper

        self._viewport = TCMFormularViewport()
        self._viewport.setPluginHelper(pluginHelper)
        self._viewport.initActionIcons()

    @cwimpl
    def viewport(self, parent: QWidget=None):
        self._viewport.setParent(parent)
        return self._viewport



def entry():
    return TCMFomularPlugin()
