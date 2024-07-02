# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weight_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import rc_resources

class Ui_WeightDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(377, 431)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"background: white;")
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(20)
        self.gridLayout_3.setContentsMargins(20, 20, 20, 20)
        self.icon_Label = QLabel(Dialog)
        self.icon_Label.setObjectName(u"icon_Label")
        self.icon_Label.setMaximumSize(QSize(35, 35))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        self.icon_Label.setFont(font)
        self.icon_Label.setPixmap(QPixmap(u":/resources/images/weight.png"))
        self.icon_Label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.icon_Label, 0, 0, 1, 1)

        self.title_Label = QLabel(Dialog)
        self.title_Label.setObjectName(u"title_Label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.title_Label.setFont(font1)
        self.title_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.title_Label, 0, 1, 1, 1)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"	border: 2px solid #FFE606;\n"
"	background: #FEFFE4;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 85))
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 311, 394))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 291))
        self.label.setMaximumSize(QSize(800, 500))
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(0)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.simple_Label = QLabel(Dialog)
        self.simple_Label.setObjectName(u"simple_Label")
        self.simple_Label.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(15)
        font2.setBold(False)
        self.simple_Label.setFont(font2)
        self.simple_Label.setStyleSheet(u"")
        self.simple_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.simple_Label)

        self.simpleRange_Label = QLabel(Dialog)
        self.simpleRange_Label.setObjectName(u"simpleRange_Label")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.simpleRange_Label.setFont(font3)
        self.simpleRange_Label.setStyleSheet(u"color: grey;")
        self.simpleRange_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.simpleRange_Label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.simple_DoubleSpinBox = QDoubleSpinBox(Dialog)
        self.simple_DoubleSpinBox.setObjectName(u"simple_DoubleSpinBox")
        self.simple_DoubleSpinBox.setMinimumSize(QSize(0, 0))
        self.simple_DoubleSpinBox.setMaximumSize(QSize(16777215, 21))
        self.simple_DoubleSpinBox.setFont(font)
        self.simple_DoubleSpinBox.setFocusPolicy(Qt.WheelFocus)
        self.simple_DoubleSpinBox.setToolTipDuration(-1)
        self.simple_DoubleSpinBox.setAlignment(Qt.AlignCenter)
        self.simple_DoubleSpinBox.setMinimum(1.000000000000000)
        self.simple_DoubleSpinBox.setMaximum(10.000000000000000)
        self.simple_DoubleSpinBox.setSingleStep(0.500000000000000)

        self.horizontalLayout.addWidget(self.simple_DoubleSpinBox)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.average_Label = QLabel(Dialog)
        self.average_Label.setObjectName(u"average_Label")
        self.average_Label.setMaximumSize(QSize(16777215, 16777215))
        self.average_Label.setFont(font2)
        self.average_Label.setStyleSheet(u"")
        self.average_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.average_Label)

        self.averageRange_Label = QLabel(Dialog)
        self.averageRange_Label.setObjectName(u"averageRange_Label")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        self.averageRange_Label.setFont(font4)
        self.averageRange_Label.setStyleSheet(u"color: grey;")
        self.averageRange_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.averageRange_Label)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.average_DoubleSpinBox = QDoubleSpinBox(Dialog)
        self.average_DoubleSpinBox.setObjectName(u"average_DoubleSpinBox")
        self.average_DoubleSpinBox.setMaximumSize(QSize(16777215, 21))
        self.average_DoubleSpinBox.setFont(font)
        self.average_DoubleSpinBox.setFocusPolicy(Qt.WheelFocus)
        self.average_DoubleSpinBox.setAlignment(Qt.AlignCenter)
        self.average_DoubleSpinBox.setSingleStep(0.500000000000000)

        self.horizontalLayout_2.addWidget(self.average_DoubleSpinBox)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.complex_Label = QLabel(Dialog)
        self.complex_Label.setObjectName(u"complex_Label")
        self.complex_Label.setMaximumSize(QSize(16777215, 16777215))
        self.complex_Label.setFont(font2)
        self.complex_Label.setStyleSheet(u"")
        self.complex_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.complex_Label)

        self.complexRange_Label = QLabel(Dialog)
        self.complexRange_Label.setObjectName(u"complexRange_Label")
        self.complexRange_Label.setFont(font4)
        self.complexRange_Label.setStyleSheet(u"color: grey;")
        self.complexRange_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.complexRange_Label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.complex_DoubleSpinBox = QDoubleSpinBox(Dialog)
        self.complex_DoubleSpinBox.setObjectName(u"complex_DoubleSpinBox")
        self.complex_DoubleSpinBox.setMaximumSize(QSize(16777215, 21))
        self.complex_DoubleSpinBox.setFont(font)
        self.complex_DoubleSpinBox.setFocusPolicy(Qt.WheelFocus)
        self.complex_DoubleSpinBox.setAlignment(Qt.AlignCenter)
        self.complex_DoubleSpinBox.setSingleStep(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.complex_DoubleSpinBox)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.cancel_Button = QPushButton(Dialog)
        self.cancel_Button.setObjectName(u"cancel_Button")
        self.cancel_Button.setFont(font)
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

        self.horizontalLayout_4.addWidget(self.cancel_Button)

        self.save_Button = QPushButton(Dialog)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setEnabled(True)
        self.save_Button.setFont(font)
        self.save_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_Button.setFocusPolicy(Qt.NoFocus)
        self.save_Button.setStyleSheet(u"background-color: #1B5E5E;\n"
"color: white;\n"
"padding: 8px 0px 8px 0px;")
        icon1 = QIcon()
        icon1.addFile(u":/resources/images/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_Button.setIcon(icon1)
        self.save_Button.setIconSize(QSize(20, 20))
        self.save_Button.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.save_Button)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 5, 0, 1, 2)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.icon_Label.setText("")
        self.title_Label.setText(QCoreApplication.translate("Dialog", u"Weight Factors ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html>\n"
"<head/>\n"
"<body>\n"
"<div style=\"text-align: center;\">\n"
"    <table align=\"center\">\n"
"        <tr>\n"
"            <td>\n"
"                <img src=\":/resources/images/warning.png\" width=\"35\" height=\"35\"/>\n"
"            </td>\n"
"            <td style=\"vertical-align: middle; padding-left: 10px;\">\n"
"                <span style=\"font-weight: 700; font-size: 14px;\">Weight Adjustment Notice</span>\n"
"            </td>\n"
"        </tr>\n"
"    </table>\n"
"</div>\n"
"<p align=\"justify\">\n"
"    This functionality is intended for users with experience in the UCP methodology. Modifying these values without adequate knowledge can affect the accuracy of the estimates.\n"
"</p>\n"
"<p align=\"justify\">\n"
"    To maintain the consistency and integrity of the UCP methodology, we ensure the following:<br/><br/>\n"
"    <span style=\"font-weight:700;\">1. Order of Complexity:</span><br/>\n"
"    &nbsp;&nbsp;&nbsp;&nbsp;The weights follow a logical order:<br/> &nbsp;&nbsp;&nbsp;&nbs"
                        "p;Simple &lt; Average &lt; Complex<br/><br/>\n"
"    <span style=\"font-weight:700;\">2. Minimum Differences:</span><br/>\n"
"   &nbsp;&nbsp;&nbsp;&nbsp;- The weight for 'Average' must be at least &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.5 points higher than 'Simple'.<br/>\n"
"    &nbsp;&nbsp;&nbsp;&nbsp;- The weight for 'Complex' must be at least &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.5 points higher than 'Average'.<br/><br/>\n"
"    <span style=\"font-weight:700;\">3. Range of Values:</span><br/>\n"
"    &nbsp;&nbsp;&nbsp;&nbsp;Each weight type has a coherent value range.\n"
"</p>\n"
"</body>\n"
"</html>\n"
"", None))
        self.simple_Label.setText(QCoreApplication.translate("Dialog", u"Simple ", None))
        self.simpleRange_Label.setText("")
#if QT_CONFIG(tooltip)
        self.simple_DoubleSpinBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.average_Label.setText(QCoreApplication.translate("Dialog", u"Average", None))
        self.averageRange_Label.setText("")
        self.complex_Label.setText(QCoreApplication.translate("Dialog", u"Complex", None))
        self.complexRange_Label.setText("")
        self.cancel_Button.setText(QCoreApplication.translate("Dialog", u"  Cancel", None))
        self.save_Button.setText(QCoreApplication.translate("Dialog", u"  Save", None))
    # retranslateUi

