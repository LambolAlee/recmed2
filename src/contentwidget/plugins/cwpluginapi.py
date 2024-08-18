from pluggy import HookspecMarker, HookimplMarker
from PySide6.QtWidgets import QWidget
from typing import Protocol

from .templatetag import TemplateTag
from .viewport import Viewport


ContentWidgetId = "cwpluginapi"

cwspec: HookspecMarker = HookspecMarker(ContentWidgetId)
cwimpl: HookimplMarker = HookimplMarker(ContentWidgetId)


class IContentWidget(Protocol):
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

