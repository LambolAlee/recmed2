# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'openeddockwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_OpenedDock(object):
    def setupUi(self, OpenedDock):
        if not OpenedDock.objectName():
            OpenedDock.setObjectName(u"OpenedDock")
        OpenedDock.resize(231, 328)
        self.verticalLayout = QVBoxLayout(OpenedDock)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.openedDocumentWidget = QWidget(OpenedDock)
        self.openedDocumentWidget.setObjectName(u"openedDocumentWidget")

        self.verticalLayout.addWidget(self.openedDocumentWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.closeAllOtherBtn = QPushButton(OpenedDock)
        self.closeAllOtherBtn.setObjectName(u"closeAllOtherBtn")

        self.horizontalLayout.addWidget(self.closeAllOtherBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.closeAllBtn = QPushButton(OpenedDock)
        self.closeAllBtn.setObjectName(u"closeAllBtn")

        self.horizontalLayout_2.addWidget(self.closeAllBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(OpenedDock)

        QMetaObject.connectSlotsByName(OpenedDock)
    # setupUi

    def retranslateUi(self, OpenedDock):
        OpenedDock.setWindowTitle(QCoreApplication.translate("OpenedDock", u"Form", None))
        self.closeAllOtherBtn.setText(QCoreApplication.translate("OpenedDock", u"Close Others", None))
        self.closeAllBtn.setText(QCoreApplication.translate("OpenedDock", u"Close All", None))
    # retranslateUi

