from PySide6.QtCore import Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QToolButton, QMenu, QHBoxLayout

from recmedtyping import getIcon, RMIconType


class ToolArea(QWidget):
    editTitleSignal = Signal(bool)
    newTagSignal = Signal()
    editTagSignal = Signal(bool)
    showFieldSignal = Signal(bool)


    def __init__(self, parent: QWidget | None=None) -> None:
        super().__init__(parent)

        self._initActions()
        self._build()

    def _initActions(self) -> None:
        self._moreMenu = QMenu(self)
        self._moreAction = QAction(getIcon(RMIconType.arrowDown), "More", self)

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
        # self._deleteDocAction = more.addAction("Delete Document")

        self._moreAction.setMenu(self._moreMenu)

    def _build(self):
        layout = QHBoxLayout()
        layout.setSpacing(6)

        moreButton = QToolButton(self)
        moreButton.setDefaultAction(self._moreAction)
        moreButton.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        layout.addWidget(moreButton)

        for action in self._moreMenu.actions():
            if action.isSeparator(): continue
            button = QToolButton(self)
            button.setDefaultAction(action)
            layout.addWidget(button)

        self.setLayout(layout)
