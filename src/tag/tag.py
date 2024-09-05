from typing import Optional, Self, Union

from PySide6.QtGui import QColor

from recmedtyping import RMIconType
from descriptivecontrol import DescriptiveContainer, dtypes



class Tag(DescriptiveContainer):
    name: str = dtypes.DStr("tag name", sendEvent=True)
    bg: QColor = dtypes.DColor(text="background-color", default="#18b868")
    fg: QColor = dtypes.DColor(text="font-color", default="#000000")
    icon: Optional[RMIconType] = dtypes.DIcon("icon")
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

        self._textIcon = None
        self.updateTextIcon()

    def updateTextIcon(self) -> None:
        """
        need to be called after the tag being modified
        """
        if self.name.startswith(":") and self.name.endswith(">"):
            try:
                self._textIcon = RMIconType[self.name[1:-1]]
            except KeyError:    # invalid icon name
                self._textIcon = None

    def handleEvent(self, sender, **kwargs):
        self.updateTextIcon()

    @classmethod
    def fromDict(cls, d: dict) -> Optional[Self]:
        try:
            return cls(**d)
        except TypeError:   # invalid tag dictionary
            return None

    def hasIcon(self) -> bool:
        return bool(self.icon or self._textIcon)

    def hasTextIcon(self) -> bool:
        return bool(self._textIcon)

    def getIcon(self) -> Optional[RMIconType]:
        if self.icon:
            return self.icon
        else:
            return self._textIcon
