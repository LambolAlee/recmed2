# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewport.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_TCMFormularViewport(object):
    def setupUi(self, TCMFormularViewport):
        if not TCMFormularViewport.objectName():
            TCMFormularViewport.setObjectName(u"TCMFormularViewport")
        TCMFormularViewport.resize(830, 523)
        self.verticalLayout = QVBoxLayout(TCMFormularViewport)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.viewportSwitcher = QStackedWidget(TCMFormularViewport)
        self.viewportSwitcher.setObjectName(u"viewportSwitcher")
        self.editPage = QWidget()
        self.editPage.setObjectName(u"editPage")
        self.verticalLayout_2 = QVBoxLayout(self.editPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.viewportSwitcher.addWidget(self.editPage)
        self.previewPage = QWidget()
        self.previewPage.setObjectName(u"previewPage")
        self.gridLayout = QGridLayout(self.previewPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.viewportSwitcher.addWidget(self.previewPage)

        self.verticalLayout.addWidget(self.viewportSwitcher)


        self.retranslateUi(TCMFormularViewport)

        QMetaObject.connectSlotsByName(TCMFormularViewport)
    # setupUi

    def retranslateUi(self, TCMFormularViewport):
        TCMFormularViewport.setWindowTitle(QCoreApplication.translate("TCMFormularViewport", u"Form", None))
    # retranslateUi

