# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ProjectDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(359, 466)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"background: white;")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 5, 10, 10)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 10, 5)
        self.icono_Label = QLabel(Dialog)
        self.icono_Label.setObjectName(u"icono_Label")
        self.icono_Label.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        self.icono_Label.setFont(font)
        self.icono_Label.setStyleSheet(u"")
        self.icono_Label.setPixmap(QPixmap(u":/resources/images/newProject.png"))
        self.icono_Label.setScaledContents(True)
        self.icono_Label.setAlignment(Qt.AlignCenter)
        self.icono_Label.setWordWrap(False)
        self.icono_Label.setMargin(0)
        self.icono_Label.setIndent(0)

        self.horizontalLayout_6.addWidget(self.icono_Label)

        self.titulo_Label = QLabel(Dialog)
        self.titulo_Label.setObjectName(u"titulo_Label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.titulo_Label.setFont(font1)
        self.titulo_Label.setStyleSheet(u"")
        self.titulo_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.titulo_Label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_Label = QLabel(Dialog)
        self.name_Label.setObjectName(u"name_Label")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(15)
        font2.setBold(False)
        self.name_Label.setFont(font2)

        self.verticalLayout.addWidget(self.name_Label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.name_LineEdit = QLineEdit(Dialog)
        self.name_LineEdit.setObjectName(u"name_LineEdit")
        self.name_LineEdit.setMinimumSize(QSize(0, 25))
        self.name_LineEdit.setFont(font)
        self.name_LineEdit.setFocusPolicy(Qt.WheelFocus)
        self.name_LineEdit.setStyleSheet(u"background:white;")
        self.name_LineEdit.setMaxLength(20)

        self.horizontalLayout_2.addWidget(self.name_LineEdit)

        self.nameCounter_Label = QLabel(Dialog)
        self.nameCounter_Label.setObjectName(u"nameCounter_Label")
        self.nameCounter_Label.setMinimumSize(QSize(50, 25))
        self.nameCounter_Label.setMaximumSize(QSize(16777215, 25))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(13)
        self.nameCounter_Label.setFont(font3)
        self.nameCounter_Label.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border: 1px solid black;")
        self.nameCounter_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.nameCounter_Label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_2.setSpacing(-1)
#endif
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.location_Label = QLabel(Dialog)
        self.location_Label.setObjectName(u"location_Label")
        self.location_Label.setFont(font2)

        self.verticalLayout_2.addWidget(self.location_Label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.description_PlainTextEdit = QPlainTextEdit(Dialog)
        self.description_PlainTextEdit.setObjectName(u"description_PlainTextEdit")
        self.description_PlainTextEdit.setFocusPolicy(Qt.WheelFocus)
        self.description_PlainTextEdit.setTabChangesFocus(True)

        self.verticalLayout_4.addWidget(self.description_PlainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.descriptionCounter_Label = QLabel(Dialog)
        self.descriptionCounter_Label.setObjectName(u"descriptionCounter_Label")
        self.descriptionCounter_Label.setMinimumSize(QSize(60, 25))
        self.descriptionCounter_Label.setMaximumSize(QSize(60, 25))
        self.descriptionCounter_Label.setFont(font3)
        self.descriptionCounter_Label.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border: 1px solid black;")
        self.descriptionCounter_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.descriptionCounter_Label)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.options_HorizontalLayout = QHBoxLayout()
        self.options_HorizontalLayout.setSpacing(10)
        self.options_HorizontalLayout.setObjectName(u"options_HorizontalLayout")
        self.options_HorizontalLayout.setContentsMargins(-1, 15, -1, -1)
        self.cancel_Button = QPushButton(Dialog)
        self.cancel_Button.setObjectName(u"cancel_Button")
        self.cancel_Button.setEnabled(True)
        self.cancel_Button.setFont(font)
        self.cancel_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel_Button.setFocusPolicy(Qt.NoFocus)
        self.cancel_Button.setStyleSheet(u"background: #FF0000;\n"
"color: white;\n"
"padding: 8px 0px 8px 0px;\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/resources/images/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancel_Button.setIcon(icon)
        self.cancel_Button.setIconSize(QSize(20, 20))
        self.cancel_Button.setAutoDefault(False)

        self.options_HorizontalLayout.addWidget(self.cancel_Button)

        self.save_Button = QPushButton(Dialog)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setEnabled(True)
        self.save_Button.setFont(font)
        self.save_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_Button.setFocusPolicy(Qt.NoFocus)
        self.save_Button.setStyleSheet(u"background-color: #1B5E5E;\n"
"color: white;\n"
"padding: 8px 0px 8px 0px;")
        self.save_Button.setAutoDefault(False)

        self.options_HorizontalLayout.addWidget(self.save_Button)


        self.verticalLayout_3.addLayout(self.options_HorizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.icono_Label.setText("")
        self.titulo_Label.setText(QCoreApplication.translate("Dialog", u"New Project", None))
        self.name_Label.setText(QCoreApplication.translate("Dialog", u"Project Name", None))
        self.name_LineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Required field", None))
        self.nameCounter_Label.setText(QCoreApplication.translate("Dialog", u"0/20", None))
        self.location_Label.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.descriptionCounter_Label.setText(QCoreApplication.translate("Dialog", u"0/300", None))
        self.cancel_Button.setText(QCoreApplication.translate("Dialog", u"  Cancel", None))
        self.save_Button.setText(QCoreApplication.translate("Dialog", u"  Save", None))
    # retranslateUi

