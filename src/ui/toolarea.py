from PySide6.QtCore import QEvent, Qt, QSize
from PySide6.QtGui import QAction, QEnterEvent
from PySide6.QtWidgets import QWidget, QLabel, QToolButton, QMenu, QHBoxLayout, QSpacerItem, QSizePolicy

from recmedtyping import getIcon, RMIconType


class ToolArea(QWidget):
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
        self._moreMenu.addSeparator()
        self._addTagsAction = self._moreMenu.addAction(getIcon(RMIconType.tag), "Add Tags")
        self._editTagsAction = self._moreMenu.addAction(getIcon(RMIconType.pencil), "Edit Tags")
        self._editTagsAction.setCheckable(True)
        self._editTagsAction.setChecked(False)
        self._moreMenu.addSeparator()
        self._showFieldsAction = self._moreMenu.addAction(getIcon(RMIconType.eye), "Show Fields")
        self._showFieldsAction.setCheckable(True)
        self._showFieldsAction.setChecked(False)
        self._moreMenu.addSeparator()
        # self._deleteDocAction = more.addAction("Delete Document")
        self._discardAction = self._moreMenu.addAction(getIcon(RMIconType.xmark), "Discard Meatadata")
        self._discardAction.setVisible(False)
        self._saveAction = self._moreMenu.addAction(getIcon(RMIconType.check), "Save Metadata")
        self._saveAction.setVisible(False)

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
            button.setVisible(action.isVisible())
            action.visibleChanged.connect(lambda button=button, action=action: button.setVisible(action.isVisible()))
            layout.addWidget(button)

        self.setLayout(layout)
