# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fieldline.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QSizePolicy,
    QToolButton, QWidget)

class Ui_FieldLine(object):
    def setupUi(self, FieldLine):
        if not FieldLine.objectName():
            FieldLine.setObjectName(u"FieldLine")
        FieldLine.resize(228, 21)
        self.horizontalLayout = QHBoxLayout(FieldLine)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.valueLineEdit = QLineEdit(FieldLine)
        self.valueLineEdit.setObjectName(u"valueLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueLineEdit.sizePolicy().hasHeightForWidth())
        self.valueLineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.valueLineEdit)

        self.deleteButton = QToolButton(FieldLine)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.deleteButton)


        self.retranslateUi(FieldLine)

        QMetaObject.connectSlotsByName(FieldLine)
    # setupUi

    def retranslateUi(self, FieldLine):
        FieldLine.setWindowTitle(QCoreApplication.translate("FieldLine", u"Form", None))
        self.deleteButton.setText(QCoreApplication.translate("FieldLine", u"...", None))
    # retranslateUi

