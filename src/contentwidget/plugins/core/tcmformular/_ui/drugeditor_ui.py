# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drugeditor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_DrugEditor(object):
    def setupUi(self, DrugEditor):
        if not DrugEditor.objectName():
            DrugEditor.setObjectName(u"DrugEditor")
        DrugEditor.resize(221, 96)
        self.gridLayout = QGridLayout(DrugEditor)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.backgroundWidget = QWidget(DrugEditor)
        self.backgroundWidget.setObjectName(u"backgroundWidget")
        self.verticalLayout = QVBoxLayout(self.backgroundWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nameEdit = QLineEdit(self.backgroundWidget)
        self.nameEdit.setObjectName(u"nameEdit")

        self.horizontalLayout.addWidget(self.nameEdit)

        self.doseSpinBox = QSpinBox(self.backgroundWidget)
        self.doseSpinBox.setObjectName(u"doseSpinBox")

        self.horizontalLayout.addWidget(self.doseSpinBox)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(17, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(3)
        self.label = QLabel(self.backgroundWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.unitComboBox = QComboBox(self.backgroundWidget)
        self.unitComboBox.setObjectName(u"unitComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.unitComboBox)

        self.label_2 = QLabel(self.backgroundWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.decoctionComboBox = QComboBox(self.backgroundWidget)
        self.decoctionComboBox.setObjectName(u"decoctionComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.decoctionComboBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(2, 1)

        self.gridLayout.addWidget(self.backgroundWidget, 0, 0, 1, 1)


        self.retranslateUi(DrugEditor)

        QMetaObject.connectSlotsByName(DrugEditor)
    # setupUi

    def retranslateUi(self, DrugEditor):
        DrugEditor.setWindowTitle(QCoreApplication.translate("DrugEditor", u"Form", None))
        self.label.setText(QCoreApplication.translate("DrugEditor", u"Unit", None))
        self.label_2.setText(QCoreApplication.translate("DrugEditor", u"Decoction", None))
    # retranslateUi

