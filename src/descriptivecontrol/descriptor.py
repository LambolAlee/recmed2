from types import MappingProxyType
from typing import Self, Mapping

from blinker import signal
from PySide6.QtWidgets import QWidget



descriptiveDunderMethod = "__descriptors__"


class DescriptiveAttr:
    """
    base class for descriptive attributes
    must implement the widget method
    """
    def __init__(self, sendEvent: bool=False):
        self._sendEvent = sendEvent

    def widget(self, parent: QWidget | None=None) -> "DescriptiveWidget":
        raise NotImplementedError

    def displayName(self) -> str:
        return ""

    def default(self):
        return None

    def setter(self, obj, value):
        return value

    def emit(self, **kwargs) -> Mapping:
        return {}

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{owner.__name__}_{name}'

        self._event = signal(f'{self.public_name}.changed') if self._sendEvent else None

    def __get__(self, obj, cls):
        return getattr(obj, self.private_name, self.default())

    def __set__(self, obj, value):
        setattr(obj, self.private_name, self.setter(obj, value))
        if self._sendEvent:
            self._event.send(self.public_name, **self.emit())



class DescriptiveWidget(QWidget):
    """
    widget created by a descriptive attribute for configuring the value contained by the attribute
    """
    def __init__(self, obj: "DescriptiveAttr", parent: QWidget | None=None):
        super().__init__(parent)
        self.attr = obj

    def build(self) -> Self:
        raise NotImplementedError

    def setData(self, **kwargs) -> None:
        raise NotImplementedError

    def data(self) -> dict:
        raise NotImplementedError
    
    def attributeName(self) -> str:
        return self.attr.public_name



class ContainerMeta(type):
    def __call__(cls, *args, **kwds):
        dattrs = {}
        instance = super().__call__(*args, **kwds)
        for attr, obj in cls.__dict__.items():
            if isinstance(obj, DescriptiveAttr):
                dattrs[attr] = obj
                if obj._event is not None:
                    obj._event.connect(instance.handleEvent)
        setattr(instance, descriptiveDunderMethod, MappingProxyType(dattrs))
        return instance


class DescriptiveContainer(metaclass=ContainerMeta):
    """
    for classes that have descriptive attributes
    it can collect the descriptive attributes and allow the users to get and set them via the []operator
    """
    def handleEvent(self, sender, **kwargs):
        pass

    def __getitem__(self, item: str):
        if item in self.__descriptors__:
            return getattr(self, item)
        else:
            raise KeyError(f"{item} is not a valid descriptive attribute")

    def __setitem__(self, item: str, value):
        if item in self.__descriptors__:
            setattr(self, item, value)
        else:
            raise KeyError(f"{item} is not a valid descriptive attribute")



# Helper functions to get DescriptiveAttrs from an instance decorated with descriptiveContainer
def getDesciptor(obj, attr: str) -> DescriptiveAttr:
    return type(obj).__dict__[attr]

def getDesciptors(obj) -> MappingProxyType[str, DescriptiveAttr]:
    return getattr(obj, descriptiveDunderMethod)
