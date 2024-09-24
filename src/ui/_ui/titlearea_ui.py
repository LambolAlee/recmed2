# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'titlearea.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_TitleArea(object):
    def setupUi(self, TitleArea):
        if not TitleArea.objectName():
            TitleArea.setObjectName(u"TitleArea")
        TitleArea.resize(381, 21)
        self.verticalLayout = QVBoxLayout(TitleArea)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(TitleArea)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.showLabel = QLabel(self.page)
        self.showLabel.setObjectName(u"showLabel")

        self.verticalLayout_2.addWidget(self.showLabel)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.editLine = QLineEdit(self.page_2)
        self.editLine.setObjectName(u"editLine")

        self.verticalLayout_3.addWidget(self.editLine)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(TitleArea)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TitleArea)
    # setupUi

    def retranslateUi(self, TitleArea):
        TitleArea.setWindowTitle(QCoreApplication.translate("TitleArea", u"Form", None))
        self.showLabel.setText(QCoreApplication.translate("TitleArea", u"TextLabel", None))
    # retranslateUi

