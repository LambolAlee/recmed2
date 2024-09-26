# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fieldkey.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QToolButton, QWidget)

class Ui_FieldKey(object):
    def setupUi(self, FieldKey):
        if not FieldKey.objectName():
            FieldKey.setObjectName(u"FieldKey")
        FieldKey.resize(338, 51)
        self.horizontalLayout = QHBoxLayout(FieldKey)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.deleteButton = QToolButton(FieldKey)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.deleteButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(FieldKey)

        QMetaObject.connectSlotsByName(FieldKey)
    # setupUi

    def retranslateUi(self, FieldKey):
        FieldKey.setWindowTitle(QCoreApplication.translate("FieldKey", u"Form", None))
        self.deleteButton.setText(QCoreApplication.translate("FieldKey", u"...", None))
    # retranslateUi

