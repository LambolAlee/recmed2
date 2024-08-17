# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drugcell.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)

class Ui_DrugCell(object):
    def setupUi(self, DrugCell):
        if not DrugCell.objectName():
            DrugCell.setObjectName(u"DrugCell")
        DrugCell.resize(366, 38)
        self.horizontalLayout_2 = QHBoxLayout(DrugCell)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cellShowcaseSwitcher = QStackedWidget(DrugCell)
        self.cellShowcaseSwitcher.setObjectName(u"cellShowcaseSwitcher")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 0, 4, 0)
        self.nameLabel = QLabel(self.page)
        self.nameLabel.setObjectName(u"nameLabel")

        self.horizontalLayout.addWidget(self.nameLabel)

        self.horizontalSpacer_2 = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.decoctionIconLabel = QLabel(self.page)
        self.decoctionIconLabel.setObjectName(u"decoctionIconLabel")

        self.horizontalLayout.addWidget(self.decoctionIconLabel)

        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.doseAndUnitLabel = QLabel(self.page)
        self.doseAndUnitLabel.setObjectName(u"doseAndUnitLabel")

        self.horizontalLayout.addWidget(self.doseAndUnitLabel)

        self.cellShowcaseSwitcher.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.cellShowcaseSwitcher.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.cellShowcaseSwitcher)


        self.retranslateUi(DrugCell)

        QMetaObject.connectSlotsByName(DrugCell)
    # setupUi

    def retranslateUi(self, DrugCell):
        DrugCell.setWindowTitle(QCoreApplication.translate("DrugCell", u"Form", None))
        self.nameLabel.setText(QCoreApplication.translate("DrugCell", u"TextLabel", None))
        self.decoctionIconLabel.setText(QCoreApplication.translate("DrugCell", u"TextLabel", None))
        self.doseAndUnitLabel.setText(QCoreApplication.translate("DrugCell", u"TextLabel", None))
    # retranslateUi

