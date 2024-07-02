# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cf_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)
import rc_resources

class Ui_CFDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(371, 319)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"background: white;")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(13)
        font.setWeight(QFont.Thin)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"margin-top: 7px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.cancel_Button = QPushButton(Dialog)
        self.cancel_Button.setObjectName(u"cancel_Button")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        self.cancel_Button.setFont(font1)
        self.cancel_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel_Button.setFocusPolicy(Qt.ClickFocus)
        self.cancel_Button.setStyleSheet(u"background: #FF0000;\n"
"color: white;\n"
"padding: 8px 0px 8px 0px;")
        icon = QIcon()
        icon.addFile(u":/resources/images/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancel_Button.setIcon(icon)
        self.cancel_Button.setIconSize(QSize(20, 20))
        self.cancel_Button.setAutoDefault(False)

        self.gridLayout.addWidget(self.cancel_Button, 4, 0, 1, 1)

        self.cf_DoubleSpinBox = QDoubleSpinBox(Dialog)
        self.cf_DoubleSpinBox.setObjectName(u"cf_DoubleSpinBox")
        self.cf_DoubleSpinBox.setMinimumSize(QSize(0, 20))
        self.cf_DoubleSpinBox.setMaximumSize(QSize(130, 21))
        self.cf_DoubleSpinBox.setFont(font1)
        self.cf_DoubleSpinBox.setStyleSheet(u"")
        self.cf_DoubleSpinBox.setAlignment(Qt.AlignCenter)
        self.cf_DoubleSpinBox.setMinimum(1.000000000000000)
        self.cf_DoubleSpinBox.setMaximum(40.000000000000000)
        self.cf_DoubleSpinBox.setSingleStep(1.000000000000000)
        self.cf_DoubleSpinBox.setValue(20.000000000000000)

        self.gridLayout.addWidget(self.cf_DoubleSpinBox, 3, 1, 1, 1)

        self.save_Button = QPushButton(Dialog)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setEnabled(True)
        self.save_Button.setFont(font1)
        self.save_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_Button.setFocusPolicy(Qt.ClickFocus)
        self.save_Button.setStyleSheet(u"background-color: #1B5E5E;\n"
"color: white;\n"
"padding: 8px 0px 8px 0px;")
        icon1 = QIcon()
        icon1.addFile(u":/resources/images/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_Button.setIcon(icon1)
        self.save_Button.setIconSize(QSize(20, 20))
        self.save_Button.setAutoDefault(False)

        self.gridLayout.addWidget(self.save_Button, 4, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border: 2px solid #22577A;\n"
"background: #EAFCFF;\n"
"padding: 10px;")
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(0)
        self.label.setIndent(0)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.title_Label = QLabel(Dialog)
        self.title_Label.setObjectName(u"title_Label")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.title_Label.setFont(font2)
        self.title_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title_Label, 0, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Person-Hours / UCP:<br><span style=\" font-size:12pt; color: grey;\">Allowed range: [1, 40]</span></p></body></html>", None))
        self.cancel_Button.setText(QCoreApplication.translate("Dialog", u"  Cancel", None))
        self.save_Button.setText(QCoreApplication.translate("Dialog", u"  Save", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"The Conversion Factor (CF) is a ratio of the number of person hours per use case point based on past projects. If no historical data has been collected, a figure between 15 and 30 is suggested by industry experts. A typical value is 20.", None))
        self.title_Label.setText(QCoreApplication.translate("Dialog", u"Conversion Factor (Productivity)", None))
    # retranslateUi

