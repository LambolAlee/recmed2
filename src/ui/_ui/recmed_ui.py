# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recmed.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_RecMedWindow(object):
    def setupUi(self, RecMedWindow):
        if not RecMedWindow.objectName():
            RecMedWindow.setObjectName(u"RecMedWindow")
        RecMedWindow.resize(1045, 712)
        self.centralwidget = QWidget(RecMedWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.browserStackedPage = QStackedWidget(self.centralwidget)
        self.browserStackedPage.setObjectName(u"browserStackedPage")
        self.emptyDocWelcomePage = QWidget()
        self.emptyDocWelcomePage.setObjectName(u"emptyDocWelcomePage")
        self.gridLayout_2 = QGridLayout(self.emptyDocWelcomePage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.emptyDocWelcomePage)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.emptyDocWelcomWidget = QWidget(self.emptyDocWelcomePage)
        self.emptyDocWelcomWidget.setObjectName(u"emptyDocWelcomWidget")

        self.gridLayout_2.addWidget(self.emptyDocWelcomWidget, 1, 0, 1, 1)

        self.browserStackedPage.addWidget(self.emptyDocWelcomePage)
        self.docsPage = QWidget()
        self.docsPage.setObjectName(u"docsPage")
        self.gridLayout = QGridLayout(self.docsPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.browserMdiArea = QWidget(self.docsPage)
        self.browserMdiArea.setObjectName(u"browserMdiArea")

        self.gridLayout.addWidget(self.browserMdiArea, 0, 0, 1, 1)

        self.browserStackedPage.addWidget(self.docsPage)

        self.verticalLayout.addWidget(self.browserStackedPage)

        RecMedWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(RecMedWindow)
        self.statusBar.setObjectName(u"statusBar")
        RecMedWindow.setStatusBar(self.statusBar)

        self.retranslateUi(RecMedWindow)

        self.browserStackedPage.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(RecMedWindow)
    # setupUi

    def retranslateUi(self, RecMedWindow):
        RecMedWindow.setWindowTitle(QCoreApplication.translate("RecMedWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("RecMedWindow", u"TextLabel", None))
    # retranslateUi

