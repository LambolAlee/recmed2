from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMenuBar, QMenu, QLabel

from qframelesswindow import TitleBar



class MenuGroup:
    def __init__(self, titleBar: TitleBar) -> None:
        self.__menuBar = QMenuBar(titleBar)
        parent = titleBar.window()

        # init file menu
        self.fileMenu = QMenu("File(&F)", parent)
        self.__menuBar.addMenu(self.fileMenu)

        # init edit menu
        self.editMenu = QMenu("Edit(&E)", parent)
        self.__menuBar.addMenu(self.editMenu)

        # init Select menu
        self.selectMenu = QMenu("Select(&S)", parent)
        self.__menuBar.addMenu(self.selectMenu)

        # init view menu
        self.viewMenu = QMenu("View(&V)", parent)
        self.__menuBar.addMenu(self.viewMenu)

        # init help menu
        self.helpMenu = QMenu("Help(&H)", parent)
        self.helpMenu.addAction("About &Qt", qApp.aboutQt)
        self.__menuBar.addMenu(self.helpMenu)

    def menuBar(self) -> QMenuBar:
        return self.__menuBar


class RecmedTitleBar(TitleBar):
    def __init__(self, parent=None):
        super().__init__(parent)


        # the index are shown below:
        # 0: white space (fixed)
        # 1: app logo
        # 2: menu bar
        # 3: white space (scalable)

        # add app logo
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(20, 20)
        self.layout().insertSpacing(0, 10)
        self.layout().insertWidget(1, self.iconLabel, 0, Qt.AlignmentFlag.AlignLeft)
        self.window().windowIconChanged.connect(self.setIcon)

        # add menu bar
        self.__menuGroup = MenuGroup(self)
        self.layout().insertWidget(2, self.__menuGroup.menuBar(), Qt.AlignmentFlag.AlignLeft)
        self.layout().insertStretch(3, 1)

    def menuBar(self) -> QMenuBar:
        return self.__menuGroup.menuBar()
    
    def setIcon(self, icon: QIcon):
        self.iconLabel.setPixmap(icon.pixmap(20, 20))


__all__ = ["RecmedTitleBar"]
