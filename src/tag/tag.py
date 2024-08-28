from typing import Optional, Self, Any, Dict

from attrs import define, field
from PySide6.QtGui import QColor

from recmedtyping import RMIconType



@define
class Tag:
    name: str
    bg: QColor = field(converter=QColor, default="#18b868")
    fg: QColor = field(converter=QColor, default="#000000")
    metadata: str = ""
    icon: Optional[RMIconType] = None
    _textIcon: bool = field(init=False, alias='_textIcon')

    def __attrs_post_init__(self) -> None:
        """
        fix the appearnce of both icon and textIcon, use icon first
        """
        icon_ = self._parseTextIcon()
        if self.icon is None:
            self.icon = icon_
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
