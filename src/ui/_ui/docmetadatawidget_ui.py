# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'docmetadatawidget.ui'
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
    QLineEdit, QSizePolicy, QSpacerItem, QStackedWidget,
    QToolButton, QWidget)

class Ui_DocMetadataWidget(object):
    def setupUi(self, DocMetadataWidget):
        if not DocMetadataWidget.objectName():
            DocMetadataWidget.setObjectName(u"DocMetadataWidget")
        DocMetadataWidget.resize(474, 123)
        self.gridLayout_3 = QGridLayout(DocMetadataWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tagsWidget = QWidget(DocMetadataWidget)
        self.tagsWidget.setObjectName(u"tagsWidget")

        self.gridLayout_3.addWidget(self.tagsWidget, 2, 0, 1, 1)

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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.titleEdit, 0, 0, 1, 1)

        self.title.addWidget(self.editPage)

        self.gridLayout_3.addWidget(self.title, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(DocMetadataWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(258, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.metadataEditButtons = QWidget(DocMetadataWidget)
        self.metadataEditButtons.setObjectName(u"metadataEditButtons")
        self.horizontalLayout_2 = QHBoxLayout(self.metadataEditButtons)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.discardButton = QToolButton(self.metadataEditButtons)
        self.discardButton.setObjectName(u"discardButton")

        self.horizontalLayout_2.addWidget(self.discardButton)

        self.saveButton = QToolButton(self.metadataEditButtons)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)


        self.horizontalLayout.addWidget(self.metadataEditButtons)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(DocMetadataWidget)

        self.title.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DocMetadataWidget)
    # setupUi

    def retranslateUi(self, DocMetadataWidget):
        DocMetadataWidget.setWindowTitle(QCoreApplication.translate("DocMetadataWidget", u"Form", None))
        self.titleLabel.setText(QCoreApplication.translate("DocMetadataWidget", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("DocMetadataWidget", u"Metadata", None))
        self.discardButton.setText(QCoreApplication.translate("DocMetadataWidget", u"...", None))
        self.saveButton.setText(QCoreApplication.translate("DocMetadataWidget", u"...", None))
    # retranslateUi

