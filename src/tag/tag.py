from typing import Optional, Self, Union

from PySide6.QtGui import QColor

from recmedtyping import RMIconType
from descriptivecontrol import descriptiveContainer, dtypes



@descriptiveContainer
class Tag:
    name: str = dtypes.DStr("tag name")
    bg: QColor = dtypes.DColor(text="background-color", default="#18b868")
    fg: QColor = dtypes.DColor(text="font-color", default="#000000")
    icon: RMIconType = dtypes.DIcon("icon")
    iconOnly: bool = dtypes.DBool("icon-only", default=False)

    def __init__(self, 
                 name: str, 
                 bg: Union[str, QColor, None]=None, 
                 fg: Union[str, QColor, None]=None, 
                 icon: Optional[RMIconType]=None,
                 iconOnly: bool=False) -> None:
        """
        fix the appearnce of both icon and textIcon, use icon first
        """
        self.name = name
        self.bg = bg
        self.fg = fg
        self.icon = icon
        self.iconOnly = iconOnly

        self.setTextIcon()

    def setTextIcon(self):
        if self.icon is None:
            self.icon = self._parseTextIcon()
            self._textIcon = True
        else:
            self._textIcon = False

    def _parseTextIcon(self) -> Optional[RMIconType]:
        if self.name.startswith(":") and self.name.endswith(">"):
            try:
                iconEnum = RMIconType[self.name[1:-1]]
            except KeyError:    # invalid icon name
                return None
            else:
                return iconEnum

    def isTextIconTag(self) -> bool:
        return self._textIcon

    @classmethod
    def fromDict(cls, d: dict) -> Optional[Self]:
        try:
            return cls(**d)
        except TypeError:   # invalid tag dictionary
            return None

    def hasIcon(self) -> bool:
        return self.icon is not None
