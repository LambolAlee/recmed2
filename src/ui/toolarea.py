from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMenu, QToolBar

from recmedtyping import getIcon, RMIconType



class ToolArea(QToolBar):
    editTitleSignal = Signal(bool)
    newTagSignal = Signal()
    editTagSignal = Signal(bool)
    showFieldSignal = Signal(bool)

    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)

        self._initActions()
        self.addActions(self._moreMenu.actions())

    def _initActions(self) -> None:
        self._moreMenu = QMenu(self)

        self._editTitleAction = self._moreMenu.addAction(getIcon(RMIconType.book), "Edit Title")
        self._editTitleAction.setCheckable(True)
        self._editTitleAction.setChecked(False)
        self._editTitleAction.toggled.connect(self.editTitleSignal)
        self._moreMenu.addSeparator()
        self._addTagsAction = self._moreMenu.addAction(getIcon(RMIconType.tag), "Add Tags")
        self._addTagsAction.triggered.connect(self.newTagSignal)
        self._editTagsAction = self._moreMenu.addAction(getIcon(RMIconType.pencil), "Edit Tags")
        self._editTagsAction.setCheckable(True)
        self._editTagsAction.setChecked(False)
        self._editTagsAction.toggled.connect(self.editTagSignal)
        self._moreMenu.addSeparator()
        self._showFieldsAction = self._moreMenu.addAction(getIcon(RMIconType.eye), "Show Fields")
        self._showFieldsAction.setCheckable(True)
        self._showFieldsAction.setChecked(False)
        self._showFieldsAction.toggled.connect(self.showFieldSignal)
        self._moreMenu.addSeparator()
