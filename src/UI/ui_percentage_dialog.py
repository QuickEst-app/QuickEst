# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'percentage_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QGridLayout,
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QWidget)
import rc_resources

class Ui_PercentageDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 386)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"background:white;")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(20, 20, 20, 30)
        self.overloading_SpinBox = QDoubleSpinBox(Dialog)
        self.overloading_SpinBox.setObjectName(u"overloading_SpinBox")
        font = QFont()
        font.setFamilies([u"Arial"])
        self.overloading_SpinBox.setFont(font)
        self.overloading_SpinBox.setMaximum(100.000000000000000)
        self.overloading_SpinBox.setSingleStep(5.000000000000000)

        self.gridLayout.addWidget(self.overloading_SpinBox, 5, 1, 1, 1)

        self.totalPercentage_ProgressBar = QProgressBar(Dialog)
        self.totalPercentage_ProgressBar.setObjectName(u"totalPercentage_ProgressBar")
        self.totalPercentage_ProgressBar.setMinimumSize(QSize(0, 0))
        self.totalPercentage_ProgressBar.setValue(0)

        self.gridLayout.addWidget(self.totalPercentage_ProgressBar, 6, 0, 1, 3)

        self.testing_SpinBox = QDoubleSpinBox(Dialog)
        self.testing_SpinBox.setObjectName(u"testing_SpinBox")
        self.testing_SpinBox.setMinimumSize(QSize(70, 0))
        self.testing_SpinBox.setFont(font)
        self.testing_SpinBox.setMaximum(100.000000000000000)
        self.testing_SpinBox.setSingleStep(5.000000000000000)

        self.gridLayout.addWidget(self.testing_SpinBox, 4, 1, 1, 1)

        self.design_SpinBox = QDoubleSpinBox(Dialog)
        self.design_SpinBox.setObjectName(u"design_SpinBox")
        self.design_SpinBox.setFont(font)
        self.design_SpinBox.setMaximum(100.000000000000000)
        self.design_SpinBox.setSingleStep(5.000000000000000)

        self.gridLayout.addWidget(self.design_SpinBox, 2, 1, 1, 1)

        self.analysis_SpinBox = QDoubleSpinBox(Dialog)
        self.analysis_SpinBox.setObjectName(u"analysis_SpinBox")
        self.analysis_SpinBox.setFont(font)
        self.analysis_SpinBox.setMaximum(100.000000000000000)
        self.analysis_SpinBox.setSingleStep(5.000000000000000)

        self.gridLayout.addWidget(self.analysis_SpinBox, 1, 1, 1, 1)

        self.programming_Label = QLabel(Dialog)
        self.programming_Label.setObjectName(u"programming_Label")
        self.programming_Label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.programming_Label.setFont(font1)
        self.programming_Label.setStyleSheet(u"")
        self.programming_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.programming_Label, 3, 0, 1, 1)

        self.overloading_Label = QLabel(Dialog)
        self.overloading_Label.setObjectName(u"overloading_Label")
        self.overloading_Label.setMaximumSize(QSize(16777215, 16777215))
        self.overloading_Label.setFont(font1)
        self.overloading_Label.setStyleSheet(u"")
        self.overloading_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.overloading_Label, 5, 0, 1, 1)

        self.title_Label = QLabel(Dialog)
        self.title_Label.setObjectName(u"title_Label")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.title_Label.setFont(font2)
        self.title_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title_Label, 0, 0, 1, 3)

        self.design_Label = QLabel(Dialog)
        self.design_Label.setObjectName(u"design_Label")
        self.design_Label.setMaximumSize(QSize(16777215, 16777215))
        self.design_Label.setFont(font1)
        self.design_Label.setStyleSheet(u"")
        self.design_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.design_Label, 2, 0, 1, 1)

        self.testing_Label = QLabel(Dialog)
        self.testing_Label.setObjectName(u"testing_Label")
        self.testing_Label.setMaximumSize(QSize(16777215, 16777215))
        self.testing_Label.setFont(font1)
        self.testing_Label.setStyleSheet(u"")
        self.testing_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.testing_Label, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.cancel_Button = QPushButton(Dialog)
        self.cancel_Button.setObjectName(u"cancel_Button")
        self.cancel_Button.setMinimumSize(QSize(0, 38))
        self.cancel_Button.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(15)
        self.cancel_Button.setFont(font3)
        self.cancel_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_Button.setFocusPolicy(Qt.NoFocus)
        self.cancel_Button.setStyleSheet(u"background: #FF0000;\n"
"color: white;\n"
"padding: 8px 0px 8px 0px;")
        icon = QIcon()
        icon.addFile(u":/resources/images/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_Button.setIcon(icon)
        self.cancel_Button.setIconSize(QSize(20, 20))
        self.cancel_Button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.cancel_Button)

        self.save_Button = QPushButton(Dialog)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setMinimumSize(QSize(0, 38))
        self.save_Button.setMaximumSize(QSize(16777215, 16777215))
        self.save_Button.setFont(font3)
        self.save_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_Button.setFocusPolicy(Qt.NoFocus)
        self.save_Button.setStyleSheet(u"background-color: #1B5E5E;\n"
"color:white;\n"
"padding: 8px 0px 8px 0px;")
        icon1 = QIcon()
        icon1.addFile(u":/resources/images/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_Button.setIcon(icon1)
        self.save_Button.setIconSize(QSize(20, 20))
        self.save_Button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.save_Button)


        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 3)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(25, 25))
        self.label.setFont(font)
        self.label.setStyleSheet(u"QToolTip{\n"
"	border: 2px solid black;\n"
"	background: white;\n"
"	padding: 4px;\n"
"}")
        self.label.setPixmap(QPixmap(u":/resources/images/info_blue.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 3, 2, 1, 1)

        self.programming_SpinBox = QDoubleSpinBox(Dialog)
        self.programming_SpinBox.setObjectName(u"programming_SpinBox")
        self.programming_SpinBox.setMinimumSize(QSize(70, 0))
        self.programming_SpinBox.setFont(font)
        self.programming_SpinBox.setStyleSheet(u"")
        self.programming_SpinBox.setMinimum(20.000000000000000)
        self.programming_SpinBox.setMaximum(100.000000000000000)
        self.programming_SpinBox.setSingleStep(5.000000000000000)

        self.gridLayout.addWidget(self.programming_SpinBox, 3, 1, 1, 1)

        self.analysis_Label = QLabel(Dialog)
        self.analysis_Label.setObjectName(u"analysis_Label")
        self.analysis_Label.setMaximumSize(QSize(16777215, 16777215))
        self.analysis_Label.setFont(font1)
        self.analysis_Label.setStyleSheet(u"")
        self.analysis_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.analysis_Label, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.totalPercentage_ProgressBar.setFormat(QCoreApplication.translate("Dialog", u"%p%", None))
        self.programming_Label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Programming<br><span style=\" font-size:12pt; color: grey;\">(Default: 40%)</span></p></body></html>", None))
        self.overloading_Label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Overloading<br><span style=\" font-size:12pt; color: grey;\">(Default: 15%)</span></p></body></html>", None))
        self.title_Label.setText(QCoreApplication.translate("Dialog", u"% Percentage", None))
        self.design_Label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Design<br><span style=\" font-size:12pt; color: grey;\">(Default: 20%)</span></p></body></html>", None))
        self.testing_Label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Testing<br><span style=\" font-size:12pt; color: grey;\">(Default: 15%)</span></p></body></html>", None))
        self.cancel_Button.setText(QCoreApplication.translate("Dialog", u"  Cancel", None))
        self.save_Button.setText(QCoreApplication.translate("Dialog", u"  Save", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"justify\"><span style=\" font-family:'Arial'; font-size:12pt; color:#000000;\">To ensure a realistic and accurate estimation of the effort required for software development, the minimum assignable value for the coding (programming) phase is 20%. This is because coding is an essential part of the development of any software project and, in most cases, represents a significant portion of the total effort. Assigning a lower percentage to coding could result in underestimating the necessary work and affect project planning and management.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText("")
        self.analysis_Label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Analysis<br><span style=\" font-size:12pt; color: grey;\">(Default: 10%)</span></p></body></html>", None))
    # retranslateUi

