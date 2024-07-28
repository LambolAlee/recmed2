# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'documentwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QScrollArea, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_DocumentWidget(object):
    def setupUi(self, DocumentWidget):
        if not DocumentWidget.objectName():
            DocumentWidget.setObjectName(u"DocumentWidget")
        DocumentWidget.resize(1096, 659)
        self.gridLayout = QGridLayout(DocumentWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(352, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(DocumentWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.content = QWidget()
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(0, 0, 354, 639))
        self.gridLayout_2 = QGridLayout(self.content)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea.setWidget(self.content)

        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(352, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.retranslateUi(DocumentWidget)

        QMetaObject.connectSlotsByName(DocumentWidget)
    # setupUi

    def retranslateUi(self, DocumentWidget):
        DocumentWidget.setWindowTitle(QCoreApplication.translate("DocumentWidget", u"Form", None))
    # retranslateUi

