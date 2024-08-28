# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tageditor.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QSizePolicy, QWidget)

class Ui_TagEditor(object):
    def setupUi(self, TagEditor):
        if not TagEditor.objectName():
            TagEditor.setObjectName(u"TagEditor")
        TagEditor.resize(513, 316)
        self.tagItemLayout = QFormLayout(TagEditor)
        self.tagItemLayout.setObjectName(u"tagItemLayout")

        self.retranslateUi(TagEditor)

        QMetaObject.connectSlotsByName(TagEditor)
    # setupUi

    def retranslateUi(self, TagEditor):
        TagEditor.setWindowTitle(QCoreApplication.translate("TagEditor", u"Form", None))
    # retranslateUi

