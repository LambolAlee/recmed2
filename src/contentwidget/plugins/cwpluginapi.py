from pluggy import HookspecMarker, HookimplMarker
from PySide6.QtWidgets import QWidget



ContentWidgetId = "cwpluginapi"

cwspec: HookspecMarker = HookspecMarker(ContentWidgetId)
cwimpl: HookimplMarker = HookimplMarker(ContentWidgetId)



class IViewport(QWidget):
    def getDataSpec(self):
        pass

    def setData(self, data):
        pass

    def save(self):
        pass

    def switchTo(self, preview: bool=False):
        pass

    def setPluginHelper(self, pluginHelper):
        pass



class ITemplateTag:
    def tagName(self):
        pass

    def parseTag(self, tag):
        pass



class IDisplayWindowWidget(QWidget):
    pass



class IContentWidget:
    @cwspec
    def init(self, pluginHelper):
        pass
    
    @cwspec
    def viewport(self, parent: QWidget) -> IViewport:
        pass

    @cwspec
    def templateTag(self) -> ITemplateTag:
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

