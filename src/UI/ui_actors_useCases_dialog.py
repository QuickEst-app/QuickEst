# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actors_useCases_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_ActorsUCDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(355, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 15, 20, 20)
        self.name_HorizontalLayout = QHBoxLayout()
        self.name_HorizontalLayout.setSpacing(10)
        self.name_HorizontalLayout.setObjectName(u"name_HorizontalLayout")
        self.name_Label = QLabel(Dialog)
        self.name_Label.setObjectName(u"name_Label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        font.setBold(True)
        self.name_Label.setFont(font)

        self.name_HorizontalLayout.addWidget(self.name_Label)

        self.name_LineEdit = QLineEdit(Dialog)
        self.name_LineEdit.setObjectName(u"name_LineEdit")
        self.name_LineEdit.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        self.name_LineEdit.setFont(font1)
        self.name_LineEdit.setMouseTracking(False)
        self.name_LineEdit.setFocusPolicy(Qt.WheelFocus)
        self.name_LineEdit.setAcceptDrops(False)
        self.name_LineEdit.setStyleSheet(u"background:white;\n"
"color: black;")
        self.name_LineEdit.setMaxLength(20)
        self.name_LineEdit.setCursorPosition(0)

        self.name_HorizontalLayout.addWidget(self.name_LineEdit)

        self.nameCounter_Label = QLabel(Dialog)
        self.nameCounter_Label.setObjectName(u"nameCounter_Label")
        self.nameCounter_Label.setMinimumSize(QSize(50, 25))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(13)
        self.nameCounter_Label.setFont(font2)
        self.nameCounter_Label.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border: 1px solid black;")
        self.nameCounter_Label.setAlignment(Qt.AlignCenter)

        self.name_HorizontalLayout.addWidget(self.nameCounter_Label)


        self.gridLayout.addLayout(self.name_HorizontalLayout, 2, 0, 1, 1)

        self.code_HorizontalLayout = QHBoxLayout()
        self.code_HorizontalLayout.setSpacing(0)
        self.code_HorizontalLayout.setObjectName(u"code_HorizontalLayout")
        self.code_HorizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.code_Label_2 = QLabel(Dialog)
        self.code_Label_2.setObjectName(u"code_Label_2")
        self.code_Label_2.setMaximumSize(QSize(50, 50))
        self.code_Label_2.setFont(font)
        self.code_Label_2.setStyleSheet(u"")

        self.code_HorizontalLayout.addWidget(self.code_Label_2)

        self.horizontalSpacer_2 = QSpacerItem(14, 12, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.code_HorizontalLayout.addItem(self.horizontalSpacer_2)

        self.code_Label = QLabel(Dialog)
        self.code_Label.setObjectName(u"code_Label")
        self.code_Label.setMinimumSize(QSize(0, 0))
        self.code_Label.setMaximumSize(QSize(16777215, 16777215))
        self.code_Label.setStyleSheet(u"color:black;")
        self.code_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.code_HorizontalLayout.addWidget(self.code_Label)

        self.code_SpinBox = QSpinBox(Dialog)
        self.code_SpinBox.setObjectName(u"code_SpinBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.code_SpinBox.sizePolicy().hasHeightForWidth())
        self.code_SpinBox.setSizePolicy(sizePolicy1)
        self.code_SpinBox.setMinimumSize(QSize(0, 0))
        self.code_SpinBox.setFocusPolicy(Qt.WheelFocus)
        self.code_SpinBox.setStyleSheet(u"background:white;\n"
"color: black;")
        self.code_SpinBox.setMinimum(1)
        self.code_SpinBox.setMaximum(9999)
        self.code_SpinBox.setStepType(QAbstractSpinBox.DefaultStepType)

        self.code_HorizontalLayout.addWidget(self.code_SpinBox)

        self.horizontalSpacer_3 = QSpacerItem(150, 12, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.code_HorizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.code_HorizontalLayout, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comment_Label = QLabel(Dialog)
        self.comment_Label.setObjectName(u"comment_Label")
        self.comment_Label.setFont(font)

        self.verticalLayout.addWidget(self.comment_Label)

        self.comment_PlainTextEdit = QPlainTextEdit(Dialog)
        self.comment_PlainTextEdit.setObjectName(u"comment_PlainTextEdit")
        self.comment_PlainTextEdit.setFont(font1)
        self.comment_PlainTextEdit.setFocusPolicy(Qt.WheelFocus)
        self.comment_PlainTextEdit.setAcceptDrops(False)
        self.comment_PlainTextEdit.setStyleSheet(u"background:white;\n"
"color: black;")
        self.comment_PlainTextEdit.setInputMethodHints(Qt.ImhMultiLine)
        self.comment_PlainTextEdit.setTabChangesFocus(True)
        self.comment_PlainTextEdit.setMaximumBlockCount(0)

        self.verticalLayout.addWidget(self.comment_PlainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.commentCounter_Label = QLabel(Dialog)
        self.commentCounter_Label.setObjectName(u"commentCounter_Label")
        self.commentCounter_Label.setMinimumSize(QSize(60, 25))
        self.commentCounter_Label.setMaximumSize(QSize(50, 16777215))
        self.commentCounter_Label.setFont(font2)
        self.commentCounter_Label.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border: 1px solid black;")
        self.commentCounter_Label.setAlignment(Qt.AlignCenter)
        self.commentCounter_Label.setMargin(1)

        self.horizontalLayout.addWidget(self.commentCounter_Label)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 6, 0, 1, 1)

        self.complexity_HorizontalLayout = QHBoxLayout()
        self.complexity_HorizontalLayout.setSpacing(10)
        self.complexity_HorizontalLayout.setObjectName(u"complexity_HorizontalLayout")
        self.complexity_HorizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.complexity_Label = QLabel(Dialog)
        self.complexity_Label.setObjectName(u"complexity_Label")
        self.complexity_Label.setFont(font)

        self.complexity_HorizontalLayout.addWidget(self.complexity_Label)

        self.complexity_ComboBox = QComboBox(Dialog)
        self.complexity_ComboBox.addItem("")
        self.complexity_ComboBox.addItem("")
        self.complexity_ComboBox.addItem("")
        self.complexity_ComboBox.setObjectName(u"complexity_ComboBox")
        sizePolicy1.setHeightForWidth(self.complexity_ComboBox.sizePolicy().hasHeightForWidth())
        self.complexity_ComboBox.setSizePolicy(sizePolicy1)
        self.complexity_ComboBox.setFont(font1)
        self.complexity_ComboBox.setFocusPolicy(Qt.WheelFocus)
        self.complexity_ComboBox.setStyleSheet(u"QComboBox {\n"
"	background-color: white;\n"
"	color:black;\n"
"	combobox-popup: 0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"	selection-background-color: #E6E6E6;\n"
"	selection-color: black;\n"
"	color:black;\n"
"}")

        self.complexity_HorizontalLayout.addWidget(self.complexity_ComboBox)


        self.gridLayout.addLayout(self.complexity_HorizontalLayout, 4, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 10, 5)
        self.icono_Label = QLabel(Dialog)
        self.icono_Label.setObjectName(u"icono_Label")
        self.icono_Label.setMaximumSize(QSize(30, 30))
        self.icono_Label.setFont(font1)
        self.icono_Label.setStyleSheet(u"")
        self.icono_Label.setScaledContents(True)
        self.icono_Label.setAlignment(Qt.AlignCenter)
        self.icono_Label.setWordWrap(False)
        self.icono_Label.setMargin(1)
        self.icono_Label.setIndent(-1)

        self.horizontalLayout_6.addWidget(self.icono_Label)

        self.titulo_Label = QLabel(Dialog)
        self.titulo_Label.setObjectName(u"titulo_Label")
        self.titulo_Label.setFont(font)
        self.titulo_Label.setStyleSheet(u"")
        self.titulo_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.titulo_Label)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.options_HorizontalLayout = QHBoxLayout()
        self.options_HorizontalLayout.setSpacing(20)
        self.options_HorizontalLayout.setObjectName(u"options_HorizontalLayout")
        self.options_HorizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.cancel_Button = QPushButton(Dialog)
        self.cancel_Button.setObjectName(u"cancel_Button")
        self.cancel_Button.setFont(font1)
        self.cancel_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel_Button.setFocusPolicy(Qt.NoFocus)
        self.cancel_Button.setStyleSheet(u"background: #FF0000;\n"
"color: white;\n"
"padding: 8px 0px 8px 0px;")
        icon = QIcon()
        icon.addFile(u":/resources/images/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancel_Button.setIcon(icon)
        self.cancel_Button.setIconSize(QSize(20, 20))
        self.cancel_Button.setAutoDefault(False)

        self.options_HorizontalLayout.addWidget(self.cancel_Button)

        self.save_Button = QPushButton(Dialog)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setFont(font1)
        self.save_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_Button.setFocusPolicy(Qt.NoFocus)
        self.save_Button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/resources/images/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_Button.setIcon(icon1)
        self.save_Button.setIconSize(QSize(20, 20))
        self.save_Button.setAutoDefault(False)

        self.options_HorizontalLayout.addWidget(self.save_Button)


        self.gridLayout.addLayout(self.options_HorizontalLayout, 7, 0, 1, 1)

        self.transactions_Widget = QWidget(Dialog)
        self.transactions_Widget.setObjectName(u"transactions_Widget")
        self.transactions_HorizontalLayout = QHBoxLayout(self.transactions_Widget)
        self.transactions_HorizontalLayout.setSpacing(10)
        self.transactions_HorizontalLayout.setObjectName(u"transactions_HorizontalLayout")
        self.transactions_HorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.transactions_Label = QLabel(self.transactions_Widget)
        self.transactions_Label.setObjectName(u"transactions_Label")
        self.transactions_Label.setFont(font)

        self.transactions_HorizontalLayout.addWidget(self.transactions_Label)

        self.transactions_SpinBox = QSpinBox(self.transactions_Widget)
        self.transactions_SpinBox.setObjectName(u"transactions_SpinBox")
        sizePolicy1.setHeightForWidth(self.transactions_SpinBox.sizePolicy().hasHeightForWidth())
        self.transactions_SpinBox.setSizePolicy(sizePolicy1)
        self.transactions_SpinBox.setMinimumSize(QSize(0, 0))
        self.transactions_SpinBox.setFocusPolicy(Qt.WheelFocus)
        self.transactions_SpinBox.setStyleSheet(u"background:white;\n"
"color: black;")
        self.transactions_SpinBox.setMinimum(1)
        self.transactions_SpinBox.setMaximum(100)

        self.transactions_HorizontalLayout.addWidget(self.transactions_SpinBox)

        self.info_label = QLabel(self.transactions_Widget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setMaximumSize(QSize(25, 25))
        self.info_label.setStyleSheet(u"QToolTip{\n"
"	background: white;\n"
"	color: black;\n"
" 	border: 1px solid black;\n"
"	padding: 5px;\n"
"}\n"
"")
        self.info_label.setScaledContents(True)

        self.transactions_HorizontalLayout.addWidget(self.info_label)


        self.gridLayout.addWidget(self.transactions_Widget, 5, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.complexity_ComboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.name_Label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.name_LineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Required field", None))
        self.nameCounter_Label.setText(QCoreApplication.translate("Dialog", u"0/20", None))
        self.code_Label_2.setText(QCoreApplication.translate("Dialog", u"Code", None))
        self.code_Label.setText(QCoreApplication.translate("Dialog", u"ACT-", None))
        self.code_SpinBox.setPrefix("")
        self.comment_Label.setText(QCoreApplication.translate("Dialog", u"Comment", None))
        self.commentCounter_Label.setText(QCoreApplication.translate("Dialog", u"0/300", None))
        self.complexity_Label.setText(QCoreApplication.translate("Dialog", u"Complexity", None))
        self.complexity_ComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Simple", None))
        self.complexity_ComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Average", None))
        self.complexity_ComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Complex", None))

        self.complexity_ComboBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Required field", None))
        self.icono_Label.setText("")
        self.titulo_Label.setText("")
        self.cancel_Button.setText(QCoreApplication.translate("Dialog", u"  Cancel", None))
        self.save_Button.setText(QCoreApplication.translate("Dialog", u"  Save", None))
        self.transactions_Label.setText(QCoreApplication.translate("Dialog", u"Transactions", None))
#if QT_CONFIG(tooltip)
        self.info_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body>\u2013 For 'Simple' complexity use cases, transactions range from 1 to 3. <br/>\u2013 For 'Medium' complexity, the range is 4 to 7.<br/>\u2013 For 'Complex' complexity, it is more than 7, with a maximum of up to 100 transactions for extremely complex cases.</body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.info_label.setText("")
    # retranslateUi

