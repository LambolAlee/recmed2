# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewport.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_PatientInfoViewport(object):
    def setupUi(self, PatientInfoViewport):
        if not PatientInfoViewport.objectName():
            PatientInfoViewport.setObjectName(u"PatientInfoViewport")
        PatientInfoViewport.resize(460, 149)
        self.verticalLayout = QVBoxLayout(PatientInfoViewport)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.viewportSwitcher = QStackedWidget(PatientInfoViewport)
        self.viewportSwitcher.setObjectName(u"viewportSwitcher")
        self.editPage = QWidget()
        self.editPage.setObjectName(u"editPage")
        self.verticalLayout_2 = QVBoxLayout(self.editPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cardWidget = QWidget(self.editPage)
        self.cardWidget.setObjectName(u"cardWidget")
        self.horizontalLayout = QHBoxLayout(self.cardWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(self.cardWidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.cardWidget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.ageLabel = QLabel(self.cardWidget)
        self.ageLabel.setObjectName(u"ageLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.ageLabel)

        self.ageSpinBox = QSpinBox(self.cardWidget)
        self.ageSpinBox.setObjectName(u"ageSpinBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ageSpinBox)

        self.genderLabel = QLabel(self.cardWidget)
        self.genderLabel.setObjectName(u"genderLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.genderLabel)

        self.genderComboBox = QComboBox(self.cardWidget)
        self.genderComboBox.setObjectName(u"genderComboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.genderComboBox)

        self.birthdayLabel = QLabel(self.cardWidget)
        self.birthdayLabel.setObjectName(u"birthdayLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.birthdayLabel)

        self.birthdayDateEdit = QDateEdit(self.cardWidget)
        self.birthdayDateEdit.setObjectName(u"birthdayDateEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.birthdayDateEdit)

        self.ethnicGroupLabel = QLabel(self.cardWidget)
        self.ethnicGroupLabel.setObjectName(u"ethnicGroupLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.ethnicGroupLabel)

        self.ethnicGroupComboBox = QComboBox(self.cardWidget)
        self.ethnicGroupComboBox.setObjectName(u"ethnicGroupComboBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.ethnicGroupComboBox)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.heightLabel = QLabel(self.cardWidget)
        self.heightLabel.setObjectName(u"heightLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.heightLabel)

        self.heightSpinBox = QSpinBox(self.cardWidget)
        self.heightSpinBox.setObjectName(u"heightSpinBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.heightSpinBox)

        self.weightLabel = QLabel(self.cardWidget)
        self.weightLabel.setObjectName(u"weightLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.weightLabel)

        self.weightSpinBox = QSpinBox(self.cardWidget)
        self.weightSpinBox.setObjectName(u"weightSpinBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.weightSpinBox)

        self.bMILabel = QLabel(self.cardWidget)
        self.bMILabel.setObjectName(u"bMILabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.bMILabel)

        self.waistLabel = QLabel(self.cardWidget)
        self.waistLabel.setObjectName(u"waistLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.waistLabel)

        self.waistSpinBox = QSpinBox(self.cardWidget)
        self.waistSpinBox.setObjectName(u"waistSpinBox")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.waistSpinBox)

        self.MHLabel = QLabel(self.cardWidget)
        self.MHLabel.setObjectName(u"MHLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.MHLabel)

        self.MHLineEdit = QSpinBox(self.cardWidget)
        self.MHLineEdit.setObjectName(u"MHLineEdit")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.MHLineEdit)

        self.BMIValueLineEdit = QLineEdit(self.cardWidget)
        self.BMIValueLineEdit.setObjectName(u"BMIValueLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.BMIValueLineEdit)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.horizontalLayout.setStretch(0, 43)
        self.horizontalLayout.setStretch(1, 14)
        self.horizontalLayout.setStretch(2, 43)

        self.verticalLayout_2.addWidget(self.cardWidget)

        self.viewportSwitcher.addWidget(self.editPage)
        self.previewPage = QWidget()
        self.previewPage.setObjectName(u"previewPage")
        self.gridLayout_2 = QGridLayout(self.previewPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.viewportSwitcher.addWidget(self.previewPage)

        self.verticalLayout.addWidget(self.viewportSwitcher)


        self.retranslateUi(PatientInfoViewport)

        QMetaObject.connectSlotsByName(PatientInfoViewport)
    # setupUi

    def retranslateUi(self, PatientInfoViewport):
        PatientInfoViewport.setWindowTitle(QCoreApplication.translate("PatientInfoViewport", u"Form", None))
        self.nameLabel.setText(QCoreApplication.translate("PatientInfoViewport", u"name", None))
        self.ageLabel.setText(QCoreApplication.translate("PatientInfoViewport", u"age", None))
        self.genderLabel.setText(QCoreApplication.translate("PatientInfoViewport", u"gender", None))
        self.birthdayLabel.setText(QCoreApplication.translate("PatientInfoViewport", u"birthday", None))
        self.ethnicGroupLabel.setText(QCoreApplication.translate("PatientInfoViewport", u"ethnic", None))
        self.heightLabel.setText(QCoreApplication.translate("PatientInfoViewport", u"height (cm)", None))
        self.weightLabel.setText(QCoreApplication.translate("PatientInfoViewport", u"weight (kg)", None))
        self.bMILabel.setText(QCoreApplication.translate("PatientInfoViewport", u"BMI (kg/m2)", None))
        self.waistLabel.setText(QCoreApplication.translate("PatientInfoViewport", u"W (cm)", None))
        self.MHLabel.setText(QCoreApplication.translate("PatientInfoViewport", u"MH (cm)", None))
    # retranslateUi

