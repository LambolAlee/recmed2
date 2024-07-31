from pluggy import HookspecMarker, HookimplMarker
from PySide6.QtWidgets import QWidget

from recmedtyping import PluginApiNamespace


cwspec: HookspecMarker = HookspecMarker(PluginApiNamespace.contentWidget)
cwimpl: HookimplMarker = HookimplMarker(PluginApiNamespace.contentWidget)


class IContentWidget:
    @cwspec
    def viewport(self, parent: QWidget):
        pass

    @cwspec
    def templateTag(self):
        pass

    @cwspec
    def parseTag(self, tag):
        pass

    @cwspec
    def displayWidget(self, parent: QWidget):
        pass

