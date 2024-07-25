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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMdiArea,
    QSizePolicy, QStatusBar, QWidget)

class Ui_RecMedWindow(object):
    def setupUi(self, RecMedWindow):
        if not RecMedWindow.objectName():
            RecMedWindow.setObjectName(u"RecMedWindow")
        RecMedWindow.resize(1045, 712)
        self.centralwidget = QWidget(RecMedWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setGeometry(QRect(370, 120, 640, 360))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 130, 311, 341))
        RecMedWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(RecMedWindow)
        self.statusBar.setObjectName(u"statusBar")
        RecMedWindow.setStatusBar(self.statusBar)

        self.retranslateUi(RecMedWindow)

        QMetaObject.connectSlotsByName(RecMedWindow)
    # setupUi

    def retranslateUi(self, RecMedWindow):
        RecMedWindow.setWindowTitle(QCoreApplication.translate("RecMedWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("RecMedWindow", u"TextLabel", None))
    # retranslateUi

