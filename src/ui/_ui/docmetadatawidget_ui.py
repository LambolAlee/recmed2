# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'docmetadatawidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)

class Ui_DocMetadataWidget(object):
    def setupUi(self, DocMetadataWidget):
        if not DocMetadataWidget.objectName():
            DocMetadataWidget.setObjectName(u"DocMetadataWidget")
        DocMetadataWidget.resize(474, 79)
        self.docmetadataLayout = QVBoxLayout(DocMetadataWidget)
        self.docmetadataLayout.setSpacing(3)
        self.docmetadataLayout.setObjectName(u"docmetadataLayout")
        self.operationWidget = QWidget(DocMetadataWidget)
        self.operationWidget.setObjectName(u"operationWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.operationWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.editToolButton = QToolButton(self.operationWidget)
        self.editToolButton.setObjectName(u"editToolButton")

        self.horizontalLayout.addWidget(self.editToolButton)

        self.discardToolButton = QToolButton(self.operationWidget)
        self.discardToolButton.setObjectName(u"discardToolButton")

        self.horizontalLayout.addWidget(self.discardToolButton)

        self.saveToolButton = QToolButton(self.operationWidget)
        self.saveToolButton.setObjectName(u"saveToolButton")

        self.horizontalLayout.addWidget(self.saveToolButton)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.docmetadataLayout.addWidget(self.operationWidget)

        self.title = QStackedWidget(DocMetadataWidget)
        self.title.setObjectName(u"title")
        self.viewPage = QWidget()
        self.viewPage.setObjectName(u"viewPage")
        self.gridLayout = QGridLayout(self.viewPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.viewPage)
        self.titleLabel.setObjectName(u"titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.title.addWidget(self.viewPage)
        self.editPage = QWidget()
        self.editPage.setObjectName(u"editPage")
        self.gridLayout_2 = QGridLayout(self.editPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleEdit = QLineEdit(self.editPage)
        self.titleEdit.setObjectName(u"titleEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.titleEdit, 0, 0, 1, 1)

        self.title.addWidget(self.editPage)

        self.docmetadataLayout.addWidget(self.title)


        self.retranslateUi(DocMetadataWidget)

        self.title.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(DocMetadataWidget)
    # setupUi

    def retranslateUi(self, DocMetadataWidget):
        DocMetadataWidget.setWindowTitle(QCoreApplication.translate("DocMetadataWidget", u"Form", None))
        self.editToolButton.setText(QCoreApplication.translate("DocMetadataWidget", u"...", None))
        self.discardToolButton.setText(QCoreApplication.translate("DocMetadataWidget", u"...", None))
        self.saveToolButton.setText(QCoreApplication.translate("DocMetadataWidget", u"...", None))
        self.titleLabel.setText(QCoreApplication.translate("DocMetadataWidget", u"TextLabel", None))
    # retranslateUi

