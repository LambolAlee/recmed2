from typing import Optional, Generic, TypeVar, Any

from attrs import define, field
from PySide6.QtCore import QSettings


T = TypeVar('T')

@define
class ConfigItem(Generic[T]):
    key: str
    section: str = field(default="General", kw_only=True)
    default: Optional[T] = field(default=None, kw_only=True)
    item_name: str = field(init=False, repr=False)

    def __attrs_post_init__(self) -> None:
        self.item_name = f"{self.section}/{self.key}"

    def __get__(self, instance: QSettings, owner: QSettings) -> object:
        # owner is a QSettings derived object
        # type of the return value need to be determined by the type of self.default, and need to cast it manually
        if isinstance(self.default, list):
            size = instance.beginReadArray(self.section)
            if size == 0:
                return None
            else:
                val: Any = []
            
            for i in range(size):
                instance.setArrayIndex(i)
                try:
                    current_default = self.default[i]
                except IndexError:
                    current_default = None
                finally:
                    val.append(instance.value(self.key, current_default))
            instance.endArray()
        else:
            val = instance.value(self.item_name, self.default)
        return val

    def __set__(self, instance: QSettings, value: Optional[T]):
        if isinstance(value, list):
            size = instance.beginReadArray(self.section)
            instance.endArray()
            instance.beginWriteArray(self.section)
            for i in range(size, len(value)):
                instance.setArrayIndex(i)
                instance.setValue(self.key, value[i])
            instance.endArray()
        else:
            instance.setValue(self.item_name, value)
