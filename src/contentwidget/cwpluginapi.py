from pluggy import HookspecMarker, HookimplMarker
from PySide6.QtWidgets import QWidget

from recmedtyping import PluginApiNamespace
from .templatetag import TemplateTag
from .viewport import Viewport


cwspec: HookspecMarker = HookspecMarker(PluginApiNamespace.contentWidget)
cwimpl: HookimplMarker = HookimplMarker(PluginApiNamespace.contentWidget)


class IContentWidget:
    @cwspec
    def viewport(self, parent: QWidget) -> Viewport:
        pass

    @cwspec
    def templateTag(self) -> TemplateTag:
        pass

    @cwspec
    def displayWindowWidget(self, parent: QWidget):
        pass

    @cwspec
    def enabled(self) -> bool:
        pass

    @cwspec
    def setDisabled(self, disabled: bool):
        pass

