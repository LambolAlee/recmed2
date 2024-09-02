from types import MappingProxyType
from functools import wraps

from PySide6.QtWidgets import QWidget


descriptiveDunderMethod = "__descriptive_controls__"

class DescriptiveAttr:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{owner.__name__}_{name}'

    def __get__(self, obj, cls):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)


class DescriptiveWidget(QWidget):
    def setData(self, **kwargs):
        pass

    def data(self):
        pass



def getDesciptor(obj: DescriptiveAttr, attr: str) -> DescriptiveAttr:
    return type(obj).__dict__[attr]


def getDesciptors(obj: DescriptiveAttr) -> MappingProxyType[str, DescriptiveAttr]:
    return getattr(obj, descriptiveDunderMethod)



def descriptiveContainer(cls):
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
