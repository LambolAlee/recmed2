from types import MappingProxyType
from typing import Self
from functools import wraps

from PySide6.QtWidgets import QWidget



descriptiveDunderMethod = "__descriptors__"


class DescriptiveAttr:
    """
    base class for descriptive attributes
    must implement the widget method
    """

    def widget(self, parent: QWidget | None=None) -> "DescriptiveWidget":
        raise NotImplementedError

    def displayName(self) -> str:
        return ""

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{owner.__name__}_{name}'

    def __get__(self, obj, cls):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)



class DescriptiveWidget(QWidget):
    """
    widget created by a descriptive attribute for configuring the value contained by the attribute
    """
    def build(self) -> Self:
        raise NotImplementedError

    def setData(self, **kwargs) -> None:
        raise NotImplementedError

    def data(self) -> dict:
        raise NotImplementedError



def descriptiveContainer(cls):
    """
    class decrator for classes that have descriptive attributes
    it can collect the descriptive attributes and allow the users to get and set them via the []operator
    """
    dattrs = {}

    class WrapperSubscriptable(cls):
        def __getitem__(self, item: str):
            if item in dattrs:
                return getattr(self, item)
            else:
                raise KeyError(f"{item} is not a valid descriptive attribute")
            
        def __setitem__(self, item: str, value):
            if item in dattrs:
                setattr(self, item, value)
            else:
                raise KeyError(f"{item} is not a valid descriptive attribute")

    @wraps(cls)
    def wrapper(*arg, **kwargs):
        for attr, obj in cls.__dict__.items():
            if isinstance(obj, DescriptiveAttr):
                dattrs[attr] = obj
        instance = WrapperSubscriptable(*arg, **kwargs)
        setattr(instance, descriptiveDunderMethod, MappingProxyType(dattrs))
        return instance
    return wrapper



# Helper functions to get DescriptiveAttrs from an instance decorated with descriptiveContainer
def getDesciptor(obj, attr: str) -> DescriptiveAttr:
    return type(obj).__dict__[attr]

def getDesciptors(obj) -> MappingProxyType[str, DescriptiveAttr]:
    return getattr(obj, descriptiveDunderMethod)
