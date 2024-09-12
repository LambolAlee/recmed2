# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fieldarea.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_FieldArea(object):
    def setupUi(self, FieldArea):
        if not FieldArea.objectName():
            FieldArea.setObjectName(u"FieldArea")
        FieldArea.resize(636, 260)
        self.verticalLayout = QVBoxLayout(FieldArea)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fieldContainerView = QTableView(FieldArea)
        self.fieldContainerView.setObjectName(u"fieldContainerView")
        self.fieldContainerView.horizontalHeader().setVisible(False)
        self.fieldContainerView.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.fieldContainerView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(FieldArea)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.keyLineEdit = QLineEdit(FieldArea)
        self.keyLineEdit.setObjectName(u"keyLineEdit")

        self.horizontalLayout.addWidget(self.keyLineEdit)

        self.valueLineEdit = QLineEdit(FieldArea)
        self.valueLineEdit.setObjectName(u"valueLineEdit")

        self.horizontalLayout.addWidget(self.valueLineEdit)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.addButton = QPushButton(FieldArea)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_2.addWidget(self.addButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(FieldArea)

        QMetaObject.connectSlotsByName(FieldArea)
    # setupUi

    def retranslateUi(self, FieldArea):
        FieldArea.setWindowTitle(QCoreApplication.translate("FieldArea", u"Form", None))
        self.label.setText(QCoreApplication.translate("FieldArea", u"Add Field:", None))
        self.addButton.setText(QCoreApplication.translate("FieldArea", u"Add", None))
    # retranslateUi

