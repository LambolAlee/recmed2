# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'metadatawidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)

class Ui_MetadataWidget(object):
    def setupUi(self, MetadataWidget):
        if not MetadataWidget.objectName():
            MetadataWidget.setObjectName(u"MetadataWidget")
        MetadataWidget.resize(617, 227)
        self.gridLayout_3 = QGridLayout(MetadataWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(MetadataWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(258, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(MetadataWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.viewPage = QWidget()
        self.viewPage.setObjectName(u"viewPage")
        self.gridLayout = QGridLayout(self.viewPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.viewPage)
        self.titleLabel.setObjectName(u"titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.viewPage)
        self.editPage = QWidget()
        self.editPage.setObjectName(u"editPage")
        self.gridLayout_2 = QGridLayout(self.editPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleEdit = QLineEdit(self.editPage)
        self.titleEdit.setObjectName(u"titleEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.titleEdit, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.editPage)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.tagsWidget = QWidget(MetadataWidget)
        self.tagsWidget.setObjectName(u"tagsWidget")

        self.gridLayout_3.addWidget(self.tagsWidget, 2, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(MetadataWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_3.addWidget(self.plainTextEdit, 3, 0, 1, 1)

        self.pushButton = QPushButton(MetadataWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 4, 0, 1, 1)


        self.retranslateUi(MetadataWidget)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MetadataWidget)
    # setupUi

    def retranslateUi(self, MetadataWidget):
        MetadataWidget.setWindowTitle(QCoreApplication.translate("MetadataWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("MetadataWidget", u"Metadata", None))
        self.titleLabel.setText(QCoreApplication.translate("MetadataWidget", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MetadataWidget", u"PushButton", None))
    # retranslateUi

