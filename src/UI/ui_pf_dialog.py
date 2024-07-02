# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pf_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)
import rc_resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(226, 132)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"background: white;")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 0, 15, 15)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.title_Label = QLabel(Dialog)
        self.title_Label.setObjectName(u"title_Label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        font.setBold(True)
        self.title_Label.setFont(font)
        self.title_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.title_Label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cf_SpinBox = QSpinBox(Dialog)
        self.cf_SpinBox.setObjectName(u"cf_SpinBox")
        self.cf_SpinBox.setMinimumSize(QSize(0, 0))
        self.cf_SpinBox.setMaximumSize(QSize(16777215, 21))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        self.cf_SpinBox.setFont(font1)
        self.cf_SpinBox.setMinimum(1)
        self.cf_SpinBox.setMaximum(100)
        self.cf_SpinBox.setValue(20)

        self.verticalLayout_2.addWidget(self.cf_SpinBox)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.options_HorizontalLayout = QHBoxLayout()
        self.options_HorizontalLayout.setSpacing(10)
        self.options_HorizontalLayout.setObjectName(u"options_HorizontalLayout")
        self.options_HorizontalLayout.setContentsMargins(0, 20, 0, 0)
        self.cancel_Button = QPushButton(Dialog)
        self.cancel_Button.setObjectName(u"cancel_Button")
        self.cancel_Button.setFont(font1)
        self.cancel_Button.setStyleSheet(u"background: #FF0000;\n"
"color: white;\n"
"padding: 8px 0px 8px 0px;")
        icon = QIcon()
        icon.addFile(u":/resources/images/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_Button.setIcon(icon)
        self.cancel_Button.setIconSize(QSize(20, 20))
        self.cancel_Button.setAutoDefault(False)

        self.options_HorizontalLayout.addWidget(self.cancel_Button)

        self.save_Button = QPushButton(Dialog)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setEnabled(True)
        self.save_Button.setFont(font1)
        self.save_Button.setStyleSheet(u"background-color: #1B5E5E;\n"
"color: white;\n"
"padding: 8px 0px 8px 0px;")
        icon1 = QIcon()
        icon1.addFile(u":/resources/images/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_Button.setIcon(icon1)
        self.save_Button.setIconSize(QSize(20, 20))
        self.save_Button.setAutoDefault(False)

        self.options_HorizontalLayout.addWidget(self.save_Button)


        self.verticalLayout_3.addLayout(self.options_HorizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_Label.setText(QCoreApplication.translate("Dialog", u"Productivity Factor", None))
        self.cancel_Button.setText(QCoreApplication.translate("Dialog", u"  Cancel", None))
        self.save_Button.setText(QCoreApplication.translate("Dialog", u"  Save", None))
    # retranslateUi

