# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fieldarea.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_FieldArea(object):
    def setupUi(self, FieldArea):
        if not FieldArea.objectName():
            FieldArea.setObjectName(u"FieldArea")
        FieldArea.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(FieldArea)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(FieldArea)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 118, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.stackedWidget = QStackedWidget(FieldArea)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.previewPage = QWidget()
        self.previewPage.setObjectName(u"previewPage")
        self.stackedWidget.addWidget(self.previewPage)
        self.editPage = QWidget()
        self.editPage.setObjectName(u"editPage")
        self.editPageLayout = QVBoxLayout(self.editPage)
        self.editPageLayout.setObjectName(u"editPageLayout")
        self.stackedWidget.addWidget(self.editPage)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(FieldArea)

        QMetaObject.connectSlotsByName(FieldArea)
    # setupUi

    def retranslateUi(self, FieldArea):
        FieldArea.setWindowTitle(QCoreApplication.translate("FieldArea", u"Form", None))
        self.label.setText(QCoreApplication.translate("FieldArea", u"Fields:", None))
    # retranslateUi

