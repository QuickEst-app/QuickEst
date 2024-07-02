# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDoubleSpinBox, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setEnabled(True)
        Main.resize(1350, 820)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setMinimumSize(QSize(1150, 800))
        font = QFont()
        font.setFamilies([u"Arial"])
        Main.setFont(font)
        Main.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        Main.setTabletTracking(False)
        Main.setFocusPolicy(Qt.NoFocus)
        Main.setStyleSheet(u"background-color: #173A51;")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setFocusPolicy(Qt.ClickFocus)
        self.stackedWidget.setStyleSheet(u"background:#4F4493")
        self.quickestHub_Page = QWidget()
        self.quickestHub_Page.setObjectName(u"quickestHub_Page")
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.quickestHub_Page.setFont(font2)
        self.quickestHub_Page.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.quickestHub_Page.setMouseTracking(False)
        self.quickestHub_Page.setTabletTracking(False)
        self.quickestHub_Page.setFocusPolicy(Qt.NoFocus)
        self.gridLayout_37 = QGridLayout(self.quickestHub_Page)
        self.gridLayout_37.setSpacing(20)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(20)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(40, 15, -1, 40)
        self.label_12 = QLabel(self.quickestHub_Page)
        self.label_12.setObjectName(u"label_12")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(22)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setUnderline(False)
        font3.setKerning(True)
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"color:white;")
        self.label_12.setMargin(0)
        self.label_12.setIndent(0)

        self.verticalLayout_28.addWidget(self.label_12)

        self.projectsSearch_LineEdit = QLineEdit(self.quickestHub_Page)
        self.projectsSearch_LineEdit.setObjectName(u"projectsSearch_LineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.projectsSearch_LineEdit.sizePolicy().hasHeightForWidth())
        self.projectsSearch_LineEdit.setSizePolicy(sizePolicy2)
        self.projectsSearch_LineEdit.setMinimumSize(QSize(211, 41))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(15)
        self.projectsSearch_LineEdit.setFont(font4)
        self.projectsSearch_LineEdit.setFocusPolicy(Qt.ClickFocus)
        self.projectsSearch_LineEdit.setStyleSheet(u"color:white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.projectsSearch_LineEdit.setClearButtonEnabled(True)

        self.verticalLayout_28.addWidget(self.projectsSearch_LineEdit)

        self.projects_TableWidget = QTableWidget(self.quickestHub_Page)
        if (self.projects_TableWidget.columnCount() < 7):
            self.projects_TableWidget.setColumnCount(7)
        font5 = QFont()
        font5.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.projects_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.projects_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(15)
        font6.setBold(True)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font6);
        self.projects_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6);
        self.projects_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem4.setFont(font6);
        self.projects_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem5.setFont(font6);
        self.projects_TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.projects_TableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.projects_TableWidget.setObjectName(u"projects_TableWidget")
        sizePolicy.setHeightForWidth(self.projects_TableWidget.sizePolicy().hasHeightForWidth())
        self.projects_TableWidget.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(15)
        font7.setBold(False)
        font7.setHintingPreference(QFont.PreferDefaultHinting)
        self.projects_TableWidget.setFont(font7)
        self.projects_TableWidget.setMouseTracking(False)
        self.projects_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.projects_TableWidget.setLayoutDirection(Qt.LeftToRight)
        self.projects_TableWidget.setStyleSheet(u"QTableWidget{\n"
"    border:none;\n"
"}\n"
"QHeaderView::section{\n"
"    border: 1px solid white;\n"
"    background: rgba(0,0,0,0.25);\n"
"    color: white;\n"
"    height: 45px;\n"
"    padding-left: 15px;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QTableWidget::Item{\n"
"    color: white;\n"
"}\n"
"QTableWidget::Item:selected{\n"
"    background: rgba(0,0,0,0.25);\n"
"}\n"
"QHeaderView::down-arrow {\n"
"	image: url(:/resources/images/whiteDownArrow.png); \n"
"}\n"
"QHeaderView::up-arrow {\n"
"	image: url(:/resources/images/whiteUpArrow.png);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"     background: #3B4252;\n"
"     width: 20px;\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: #9FF0FF;\n"
"     min-height: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"\n"
""
                        "QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #3B4252;\n"
"     height: 20px;\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: #9FF0FF;\n"
"     min-width: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}")
        self.projects_TableWidget.setFrameShape(QFrame.NoFrame)
        self.projects_TableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.projects_TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.projects_TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.projects_TableWidget.setAutoScroll(False)
        self.projects_TableWidget.setAutoScrollMargin(100)
        self.projects_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.projects_TableWidget.setTabKeyNavigation(True)
        self.projects_TableWidget.setProperty("showDropIndicator", False)
        self.projects_TableWidget.setDragEnabled(False)
        self.projects_TableWidget.setDragDropOverwriteMode(False)
        self.projects_TableWidget.setAlternatingRowColors(False)
        self.projects_TableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.projects_TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.projects_TableWidget.setTextElideMode(Qt.ElideRight)
        self.projects_TableWidget.setShowGrid(False)
        self.projects_TableWidget.setGridStyle(Qt.SolidLine)
        self.projects_TableWidget.setSortingEnabled(True)
        self.projects_TableWidget.setWordWrap(True)
        self.projects_TableWidget.setCornerButtonEnabled(False)
        self.projects_TableWidget.setRowCount(0)
        self.projects_TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.projects_TableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.projects_TableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.projects_TableWidget.horizontalHeader().setHighlightSections(True)
        self.projects_TableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.projects_TableWidget.horizontalHeader().setStretchLastSection(False)
        self.projects_TableWidget.verticalHeader().setVisible(False)
        self.projects_TableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.projects_TableWidget.verticalHeader().setMinimumSectionSize(0)
        self.projects_TableWidget.verticalHeader().setDefaultSectionSize(50)
        self.projects_TableWidget.verticalHeader().setHighlightSections(True)
        self.projects_TableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_28.addWidget(self.projects_TableWidget)


        self.gridLayout_37.addLayout(self.verticalLayout_28, 1, 0, 1, 1)

        self.widget_6 = QWidget(self.quickestHub_Page)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QWidget{\n"
"    background-color:#5A0084;\n"
"    border-bottom: 2px solid white;\n"
"}")
        self.gridLayout_39 = QGridLayout(self.widget_6)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.horizontalSpacer_9 = QSpacerItem(196, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)

        self.quickestHub_Button = QPushButton(self.widget_6)
        self.quickestHub_Button.setObjectName(u"quickestHub_Button")
        self.quickestHub_Button.setFont(font)
        self.quickestHub_Button.setFocusPolicy(Qt.NoFocus)
        self.quickestHub_Button.setStyleSheet(u"QPushButton{\n"
"    margin: 10px 0px 10px 0px;  \n"
"    border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/resources/images/quickestHub.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quickestHub_Button.setIcon(icon)
        self.quickestHub_Button.setIconSize(QSize(60, 55))
        self.quickestHub_Button.setCheckable(True)
        self.quickestHub_Button.setChecked(False)
        self.quickestHub_Button.setAutoExclusive(True)

        self.gridLayout_39.addWidget(self.quickestHub_Button, 0, 0, 1, 1)

        self.quickestHubName_Label = QLabel(self.widget_6)
        self.quickestHubName_Label.setObjectName(u"quickestHubName_Label")
        self.quickestHubName_Label.setFont(font4)
        self.quickestHubName_Label.setStyleSheet(u"color:white;\n"
"border:none;")

        self.gridLayout_39.addWidget(self.quickestHubName_Label, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.widget_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/resources/images/powerOff.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(80, 45))

        self.gridLayout_39.addWidget(self.pushButton, 0, 3, 1, 1)


        self.gridLayout_37.addWidget(self.widget_6, 0, 0, 1, 2)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(40)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(40, 40, 40, 40)
        self.createProject_Widget = QWidget(self.quickestHub_Page)
        self.createProject_Widget.setObjectName(u"createProject_Widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.createProject_Widget.sizePolicy().hasHeightForWidth())
        self.createProject_Widget.setSizePolicy(sizePolicy3)
        self.createProject_Widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.createProject_Widget.setStyleSheet(u"QWidget{\n"
"    background-color: rgba(0,0,0,0.25);\n"
"    color: white;\n"
"    border-radius: 0px;\n"
"    padding: 6px 0px 6px 6px;\n"
"}\n"
"QWidget:hover{\n"
"    background-color: #341D64;\n"
"    border: 2px solid #7000FF;\n"
"}   \n"
"")
        self.gridLayout_4 = QGridLayout(self.createProject_Widget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 0, 45, 0)
        self.createProject_Button = QPushButton(self.createProject_Widget)
        self.createProject_Button.setObjectName(u"createProject_Button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.createProject_Button.sizePolicy().hasHeightForWidth())
        self.createProject_Button.setSizePolicy(sizePolicy4)
        self.createProject_Button.setMinimumSize(QSize(0, 0))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(18)
        font8.setBold(True)
        self.createProject_Button.setFont(font8)
        self.createProject_Button.setFocusPolicy(Qt.NoFocus)
        self.createProject_Button.setStyleSheet(u"background:none;\n"
"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/resources/images/createProject.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.createProject_Button.setIcon(icon2)
        self.createProject_Button.setIconSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.createProject_Button, 0, 0, 2, 1)

        self.label_14 = QLabel(self.createProject_Widget)
        self.label_14.setObjectName(u"label_14")
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(14)
        self.label_14.setFont(font9)
        self.label_14.setStyleSheet(u"background:none;\n"
"border: none;")
        self.label_14.setTextFormat(Qt.AutoText)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_14.setIndent(0)

        self.gridLayout_4.addWidget(self.label_14, 1, 1, 1, 1)

        self.label_13 = QLabel(self.createProject_Widget)
        self.label_13.setObjectName(u"label_13")
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(20)
        font10.setBold(True)
        self.label_13.setFont(font10)
        self.label_13.setStyleSheet(u"background:none;\n"
"border: none;")
        self.label_13.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_13.setIndent(0)

        self.gridLayout_4.addWidget(self.label_13, 0, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.createProject_Widget)

        self.openProject_Widget = QWidget(self.quickestHub_Page)
        self.openProject_Widget.setObjectName(u"openProject_Widget")
        self.openProject_Widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.openProject_Widget.setStyleSheet(u"QWidget{\n"
"    background-color: rgba(0,0,0,0.25);\n"
"    color: white;\n"
"    border-radius: 0px;\n"
"    padding: 6px 0px 6px 6px;\n"
"}\n"
"QWidget:hover{\n"
"    background-color: #341D64;\n"
"    border: 2px solid #7000FF;\n"
"}   \n"
"")
        self.gridLayout_5 = QGridLayout(self.openProject_Widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(15)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(28, 0, 30, 0)
        self.label_15 = QLabel(self.openProject_Widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font10)
        self.label_15.setStyleSheet(u"background:none;\n"
"border: none;")
        self.label_15.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_15.setIndent(0)

        self.gridLayout_5.addWidget(self.label_15, 0, 1, 1, 1)

        self.label_16 = QLabel(self.openProject_Widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font9)
        self.label_16.setStyleSheet(u"background:none;\n"
"border: none;")
        self.label_16.setTextFormat(Qt.AutoText)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_16.setIndent(0)

        self.gridLayout_5.addWidget(self.label_16, 1, 1, 1, 1)

        self.createProject_Button_2 = QPushButton(self.openProject_Widget)
        self.createProject_Button_2.setObjectName(u"createProject_Button_2")
        sizePolicy4.setHeightForWidth(self.createProject_Button_2.sizePolicy().hasHeightForWidth())
        self.createProject_Button_2.setSizePolicy(sizePolicy4)
        self.createProject_Button_2.setMinimumSize(QSize(0, 0))
        self.createProject_Button_2.setFont(font8)
        self.createProject_Button_2.setFocusPolicy(Qt.NoFocus)
        self.createProject_Button_2.setStyleSheet(u"background:none;\n"
"border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/resources/images/openProject.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.createProject_Button_2.setIcon(icon3)
        self.createProject_Button_2.setIconSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.createProject_Button_2, 0, 0, 2, 1)


        self.verticalLayout_11.addWidget(self.openProject_Widget)

        self.exportProjects_Widget = QWidget(self.quickestHub_Page)
        self.exportProjects_Widget.setObjectName(u"exportProjects_Widget")
        self.exportProjects_Widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exportProjects_Widget.setStyleSheet(u"QWidget{\n"
"    background-color: rgba(0,0,0,0.25);\n"
"    color: white;\n"
"    border-radius: 0px;\n"
"    padding: 6px 0px 6px 6px;\n"
"}\n"
"QWidget:hover{\n"
"    background-color: #341D64;\n"
"    border: 2px solid #7000FF;\n"
"}   \n"
"")
        self.gridLayout_36 = QGridLayout(self.exportProjects_Widget)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setHorizontalSpacing(15)
        self.gridLayout_36.setVerticalSpacing(0)
        self.gridLayout_36.setContentsMargins(15, 0, 68, 0)
        self.createProject_Button_3 = QPushButton(self.exportProjects_Widget)
        self.createProject_Button_3.setObjectName(u"createProject_Button_3")
        sizePolicy4.setHeightForWidth(self.createProject_Button_3.sizePolicy().hasHeightForWidth())
        self.createProject_Button_3.setSizePolicy(sizePolicy4)
        self.createProject_Button_3.setMinimumSize(QSize(0, 0))
        self.createProject_Button_3.setFont(font8)
        self.createProject_Button_3.setFocusPolicy(Qt.NoFocus)
        self.createProject_Button_3.setStyleSheet(u"background:none;\n"
"border: none;")
        icon4 = QIcon()
        icon4.addFile(u":/resources/images/exportProjects.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.createProject_Button_3.setIcon(icon4)
        self.createProject_Button_3.setIconSize(QSize(80, 80))

        self.gridLayout_36.addWidget(self.createProject_Button_3, 0, 0, 2, 1)

        self.label_21 = QLabel(self.exportProjects_Widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font10)
        self.label_21.setStyleSheet(u"background:none;\n"
"border: none;")
        self.label_21.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_21.setIndent(0)

        self.gridLayout_36.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_22 = QLabel(self.exportProjects_Widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font9)
        self.label_22.setStyleSheet(u"background:none;\n"
"border: none;")
        self.label_22.setTextFormat(Qt.AutoText)
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_22.setIndent(0)

        self.gridLayout_36.addWidget(self.label_22, 1, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.exportProjects_Widget)


        self.gridLayout_37.addLayout(self.verticalLayout_11, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.quickestHub_Page)
        self.quickest_Page = QWidget()
        self.quickest_Page.setObjectName(u"quickest_Page")
        self.gridLayout_17 = QGridLayout(self.quickest_Page)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.quickest_Page)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.widget_2.setStyleSheet(u"QWidget#widget_2{\n"
"    background-color:#22577A;\n"
"    border-bottom: 2px solid white;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.projectName_Label = QLabel(self.widget_2)
        self.projectName_Label.setObjectName(u"projectName_Label")
        sizePolicy4.setHeightForWidth(self.projectName_Label.sizePolicy().hasHeightForWidth())
        self.projectName_Label.setSizePolicy(sizePolicy4)
        self.projectName_Label.setFont(font1)
        self.projectName_Label.setStyleSheet(u"color:white;\n"
"border:none;\n"
"background-color:#22577A;")
        self.projectName_Label.setTextFormat(Qt.PlainText)
        self.projectName_Label.setScaledContents(False)
        self.projectName_Label.setAlignment(Qt.AlignCenter)
        self.projectName_Label.setWordWrap(False)
        self.projectName_Label.setMargin(20)
        self.projectName_Label.setIndent(0)

        self.gridLayout_2.addWidget(self.projectName_Label, 1, 5, 1, 1)

        self.quickest_Button = QPushButton(self.widget_2)
        self.quickest_Button.setObjectName(u"quickest_Button")
        self.quickest_Button.setFont(font)
        self.quickest_Button.setFocusPolicy(Qt.NoFocus)
        self.quickest_Button.setStyleSheet(u"QPushButton{\n"
"    margin: 10px 0px 10px 0px;  \n"
"    border:none;\n"
"    background-color:#22577A;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/resources/images/quickest.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quickest_Button.setIcon(icon5)
        self.quickest_Button.setIconSize(QSize(60, 55))
        self.quickest_Button.setCheckable(False)
        self.quickest_Button.setChecked(False)
        self.quickest_Button.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.quickest_Button, 1, 0, 1, 1)

        self.comment_tableWidget = QTableWidget(self.widget_2)
        if (self.comment_tableWidget.columnCount() < 1):
            self.comment_tableWidget.setColumnCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.comment_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        if (self.comment_tableWidget.rowCount() < 1):
            self.comment_tableWidget.setRowCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.comment_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFlags(Qt.NoItemFlags);
        self.comment_tableWidget.setItem(0, 0, __qtablewidgetitem9)
        self.comment_tableWidget.setObjectName(u"comment_tableWidget")
        self.comment_tableWidget.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.comment_tableWidget.sizePolicy().hasHeightForWidth())
        self.comment_tableWidget.setSizePolicy(sizePolicy2)
        self.comment_tableWidget.setMaximumSize(QSize(40, 75))
        self.comment_tableWidget.setFont(font)
        self.comment_tableWidget.viewport().setProperty("cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.comment_tableWidget.setFocusPolicy(Qt.NoFocus)
        self.comment_tableWidget.setStyleSheet(u"background-color:#22577A;\n"
"border: none;")
        self.comment_tableWidget.setFrameShape(QFrame.NoFrame)
        self.comment_tableWidget.setLineWidth(0)
        self.comment_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.comment_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.comment_tableWidget.setAutoScroll(False)
        self.comment_tableWidget.setTabKeyNavigation(False)
        self.comment_tableWidget.setProperty("showDropIndicator", False)
        self.comment_tableWidget.setDragDropOverwriteMode(False)
        self.comment_tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.comment_tableWidget.setShowGrid(False)
        self.comment_tableWidget.setGridStyle(Qt.NoPen)
        self.comment_tableWidget.setWordWrap(False)
        self.comment_tableWidget.setCornerButtonEnabled(False)
        self.comment_tableWidget.horizontalHeader().setVisible(False)
        self.comment_tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.comment_tableWidget.horizontalHeader().setDefaultSectionSize(40)
        self.comment_tableWidget.horizontalHeader().setHighlightSections(False)
        self.comment_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.comment_tableWidget.verticalHeader().setVisible(False)
        self.comment_tableWidget.verticalHeader().setMinimumSectionSize(75)
        self.comment_tableWidget.verticalHeader().setDefaultSectionSize(75)
        self.comment_tableWidget.verticalHeader().setHighlightSections(False)
        self.comment_tableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.comment_tableWidget, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(196, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, -1, 0, -1)
        self.file_ToolButton = QToolButton(self.widget_2)
        self.file_ToolButton.setObjectName(u"file_ToolButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.file_ToolButton.sizePolicy().hasHeightForWidth())
        self.file_ToolButton.setSizePolicy(sizePolicy5)
        font11 = QFont()
        font11.setFamilies([u"Arial"])
        font11.setPointSize(20)
        font11.setBold(False)
        self.file_ToolButton.setFont(font11)
        self.file_ToolButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.file_ToolButton.setStyleSheet(u"border: 3px solid #173A51;\n"
"border-radius: 5px;\n"
"background-color:#7FE9FD;\n"
"color:#173A51;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/resources/images/file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.file_ToolButton.setIcon(icon6)
        self.file_ToolButton.setIconSize(QSize(20, 20))
        self.file_ToolButton.setPopupMode(QToolButton.InstantPopup)
        self.file_ToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.file_ToolButton.setAutoRaise(False)

        self.horizontalLayout.addWidget(self.file_ToolButton)

        self.help_ToolButton = QToolButton(self.widget_2)
        self.help_ToolButton.setObjectName(u"help_ToolButton")
        sizePolicy5.setHeightForWidth(self.help_ToolButton.sizePolicy().hasHeightForWidth())
        self.help_ToolButton.setSizePolicy(sizePolicy5)
        self.help_ToolButton.setFont(font1)
        self.help_ToolButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.help_ToolButton.setStyleSheet(u"border: 3px solid #173A51;\n"
"border-radius: 5px;\n"
"background-color:#7FE9FD;\n"
"color:#173A51;\n"
"padding: 6px 0px 6px 6px;")
        icon7 = QIcon()
        icon7.addFile(u":/resources/images/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.help_ToolButton.setIcon(icon7)
        self.help_ToolButton.setIconSize(QSize(20, 20))
        self.help_ToolButton.setPopupMode(QToolButton.InstantPopup)
        self.help_ToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.help_ToolButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 2, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(200, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_21, 1, 7, 1, 1)

        self.exit_pushButton_1 = QPushButton(self.widget_2)
        self.exit_pushButton_1.setObjectName(u"exit_pushButton_1")
        self.exit_pushButton_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exit_pushButton_1.setFocusPolicy(Qt.NoFocus)
        self.exit_pushButton_1.setStyleSheet(u"border: none;\n"
"background-color:#22577A;")
        self.exit_pushButton_1.setIcon(icon1)
        self.exit_pushButton_1.setIconSize(QSize(80, 45))

        self.gridLayout_2.addWidget(self.exit_pushButton_1, 1, 8, 1, 1)

        self.warning_Button = QPushButton(self.widget_2)
        self.warning_Button.setObjectName(u"warning_Button")
        sizePolicy5.setHeightForWidth(self.warning_Button.sizePolicy().hasHeightForWidth())
        self.warning_Button.setSizePolicy(sizePolicy5)
        self.warning_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.warning_Button.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"QToolTip{\n"
"	border: 2px solid #FFE606;\n"
"	background-color: #FEFFE4;\n"
"	color: black;\n"
"	font-family: 'Arial';\n"
"	font-size: 12px;\n"
"	padding: 8px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/resources/images/warning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.warning_Button.setIcon(icon8)
        self.warning_Button.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.warning_Button, 1, 6, 1, 1)

        self.quickestName_Label = QLabel(self.widget_2)
        self.quickestName_Label.setObjectName(u"quickestName_Label")
        self.quickestName_Label.setFont(font9)
        self.quickestName_Label.setStyleSheet(u"color:white;\n"
"border:none;\n"
"background-color:#22577A;")

        self.gridLayout_2.addWidget(self.quickestName_Label, 1, 1, 1, 1)


        self.gridLayout_17.addWidget(self.widget_2, 0, 0, 1, 3)

        self.iconMenu_Widget = QWidget(self.quickest_Page)
        self.iconMenu_Widget.setObjectName(u"iconMenu_Widget")
        self.iconMenu_Widget.setFocusPolicy(Qt.NoFocus)
        self.iconMenu_Widget.setStyleSheet(u"QWidget{\n"
"    background-color:#22577A;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: white;\n"
"    height:50px;\n"
"    border:none;\n"
"    text-align:left;\n"
"    height:50px;\n"
"    padding-left:10px;\n"
"    padding-right:15px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:#173A51;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.iconMenu_Widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, -1, 0, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.hide_Button = QPushButton(self.iconMenu_Widget)
        self.hide_Button.setObjectName(u"hide_Button")
        self.hide_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hide_Button.setFocusPolicy(Qt.NoFocus)
        self.hide_Button.setStyleSheet(u"QPushButton:checked{\n"
"    background-color:#22577A;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/resources/images/hide.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hide_Button.setIcon(icon9)
        self.hide_Button.setIconSize(QSize(30, 30))
        self.hide_Button.setCheckable(True)

        self.verticalLayout.addWidget(self.hide_Button)

        self.dashboard_Button = QPushButton(self.iconMenu_Widget)
        self.dashboard_Button.setObjectName(u"dashboard_Button")
        self.dashboard_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_Button.setFocusPolicy(Qt.NoFocus)
        icon10 = QIcon()
        icon10.addFile(u":/resources/images/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboard_Button.setIcon(icon10)
        self.dashboard_Button.setIconSize(QSize(30, 30))
        self.dashboard_Button.setCheckable(True)
        self.dashboard_Button.setChecked(True)
        self.dashboard_Button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_Button)

        self.actors_Button = QPushButton(self.iconMenu_Widget)
        self.actors_Button.setObjectName(u"actors_Button")
        self.actors_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.actors_Button.setFocusPolicy(Qt.NoFocus)
        icon11 = QIcon()
        icon11.addFile(u":/resources/images/actors.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actors_Button.setIcon(icon11)
        self.actors_Button.setIconSize(QSize(30, 30))
        self.actors_Button.setCheckable(True)
        self.actors_Button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.actors_Button)

        self.useCases_Button = QPushButton(self.iconMenu_Widget)
        self.useCases_Button.setObjectName(u"useCases_Button")
        self.useCases_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.useCases_Button.setFocusPolicy(Qt.NoFocus)
        icon12 = QIcon()
        icon12.addFile(u":/resources/images/useCases.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.useCases_Button.setIcon(icon12)
        self.useCases_Button.setIconSize(QSize(30, 30))
        self.useCases_Button.setCheckable(True)
        self.useCases_Button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.useCases_Button)

        self.technicalFactors_Button = QPushButton(self.iconMenu_Widget)
        self.technicalFactors_Button.setObjectName(u"technicalFactors_Button")
        self.technicalFactors_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.technicalFactors_Button.setFocusPolicy(Qt.NoFocus)
        icon13 = QIcon()
        icon13.addFile(u":/resources/images/technicalFactors.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.technicalFactors_Button.setIcon(icon13)
        self.technicalFactors_Button.setIconSize(QSize(30, 30))
        self.technicalFactors_Button.setCheckable(True)
        self.technicalFactors_Button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.technicalFactors_Button)

        self.environmentalFactors_Button = QPushButton(self.iconMenu_Widget)
        self.environmentalFactors_Button.setObjectName(u"environmentalFactors_Button")
        self.environmentalFactors_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.environmentalFactors_Button.setFocusPolicy(Qt.NoFocus)
        icon14 = QIcon()
        icon14.addFile(u":/resources/images/environmentalFactors.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.environmentalFactors_Button.setIcon(icon14)
        self.environmentalFactors_Button.setIconSize(QSize(30, 30))
        self.environmentalFactors_Button.setCheckable(True)
        self.environmentalFactors_Button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.environmentalFactors_Button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.close_Button = QPushButton(self.iconMenu_Widget)
        self.close_Button.setObjectName(u"close_Button")
        font12 = QFont()
        self.close_Button.setFont(font12)
        self.close_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_Button.setFocusPolicy(Qt.NoFocus)
        icon15 = QIcon()
        icon15.addFile(u":/resources/images/closeWindow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_Button.setIcon(icon15)
        self.close_Button.setIconSize(QSize(25, 25))
        self.close_Button.setCheckable(False)
        self.close_Button.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.close_Button)


        self.gridLayout_17.addWidget(self.iconMenu_Widget, 1, 0, 1, 1)

        self.fullMenu_Widget = QWidget(self.quickest_Page)
        self.fullMenu_Widget.setObjectName(u"fullMenu_Widget")
        font13 = QFont()
        font13.setPointSize(15)
        font13.setBold(False)
        self.fullMenu_Widget.setFont(font13)
        self.fullMenu_Widget.setFocusPolicy(Qt.NoFocus)
        self.fullMenu_Widget.setStyleSheet(u"QWidget{\n"
"    background-color:#22577A;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: white;\n"
"    text-align:left;\n"
"    height:50px;\n"
"    width:150px;\n"
"    border:none;\n"
"    padding-left:10px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"    font-family: 'Arial';\n"
"    font-size: 14px; \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:#173A51;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.fullMenu_Widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.hide_Button_2 = QPushButton(self.fullMenu_Widget)
        self.hide_Button_2.setObjectName(u"hide_Button_2")
        self.hide_Button_2.setFont(font)
        self.hide_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hide_Button_2.setFocusPolicy(Qt.NoFocus)
        self.hide_Button_2.setStyleSheet(u"QPushButton:checked{\n"
"    background-color:#22577A;\n"
"}")
        self.hide_Button_2.setIcon(icon9)
        self.hide_Button_2.setIconSize(QSize(30, 30))
        self.hide_Button_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.hide_Button_2)

        self.dashboard_Button_2 = QPushButton(self.fullMenu_Widget)
        self.dashboard_Button_2.setObjectName(u"dashboard_Button_2")
        self.dashboard_Button_2.setFont(font)
        self.dashboard_Button_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.dashboard_Button_2.setMouseTracking(True)
        self.dashboard_Button_2.setTabletTracking(False)
        self.dashboard_Button_2.setFocusPolicy(Qt.NoFocus)
        self.dashboard_Button_2.setStyleSheet(u"")
        self.dashboard_Button_2.setIcon(icon10)
        self.dashboard_Button_2.setIconSize(QSize(30, 30))
        self.dashboard_Button_2.setCheckable(True)
        self.dashboard_Button_2.setChecked(True)
        self.dashboard_Button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_Button_2)

        self.actors_Button_2 = QPushButton(self.fullMenu_Widget)
        self.actors_Button_2.setObjectName(u"actors_Button_2")
        self.actors_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.actors_Button_2.setFocusPolicy(Qt.NoFocus)
        self.actors_Button_2.setIcon(icon11)
        self.actors_Button_2.setIconSize(QSize(30, 30))
        self.actors_Button_2.setCheckable(True)
        self.actors_Button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.actors_Button_2)

        self.useCases_Button_2 = QPushButton(self.fullMenu_Widget)
        self.useCases_Button_2.setObjectName(u"useCases_Button_2")
        self.useCases_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.useCases_Button_2.setFocusPolicy(Qt.NoFocus)
        self.useCases_Button_2.setIcon(icon12)
        self.useCases_Button_2.setIconSize(QSize(30, 30))
        self.useCases_Button_2.setCheckable(True)
        self.useCases_Button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.useCases_Button_2)

        self.technicalFactors_Button_2 = QPushButton(self.fullMenu_Widget)
        self.technicalFactors_Button_2.setObjectName(u"technicalFactors_Button_2")
        self.technicalFactors_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.technicalFactors_Button_2.setFocusPolicy(Qt.NoFocus)
        self.technicalFactors_Button_2.setIcon(icon13)
        self.technicalFactors_Button_2.setIconSize(QSize(30, 30))
        self.technicalFactors_Button_2.setCheckable(True)
        self.technicalFactors_Button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.technicalFactors_Button_2)

        self.environmentalFactors_Button_2 = QPushButton(self.fullMenu_Widget)
        self.environmentalFactors_Button_2.setObjectName(u"environmentalFactors_Button_2")
        self.environmentalFactors_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.environmentalFactors_Button_2.setFocusPolicy(Qt.NoFocus)
        self.environmentalFactors_Button_2.setIcon(icon14)
        self.environmentalFactors_Button_2.setIconSize(QSize(30, 30))
        self.environmentalFactors_Button_2.setCheckable(True)
        self.environmentalFactors_Button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.environmentalFactors_Button_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.close_Button_2 = QPushButton(self.fullMenu_Widget)
        self.close_Button_2.setObjectName(u"close_Button_2")
        self.close_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_Button_2.setFocusPolicy(Qt.NoFocus)
        self.close_Button_2.setStyleSheet(u"QPushButton{\n"
"    font-family: 'Arial';\n"
"    font-size: 14px; \n"
"}\n"
"")
        self.close_Button_2.setIcon(icon15)
        self.close_Button_2.setIconSize(QSize(25, 25))
        self.close_Button_2.setCheckable(False)
        self.close_Button_2.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.close_Button_2)


        self.gridLayout_17.addWidget(self.fullMenu_Widget, 1, 1, 1, 1)

        self.stackedWidget_2 = QStackedWidget(self.quickest_Page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy6)
        self.stackedWidget_2.setMinimumSize(QSize(0, 0))
        self.stackedWidget_2.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget_2.setFont(font9)
        self.stackedWidget_2.setStyleSheet(u"background-color:#173A51;")
        self.dashboard_Page = QWidget()
        self.dashboard_Page.setObjectName(u"dashboard_Page")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.dashboard_Page.sizePolicy().hasHeightForWidth())
        self.dashboard_Page.setSizePolicy(sizePolicy7)
        self.dashboard_Page.setMinimumSize(QSize(0, 16))
        self.dashboard_Page.setMaximumSize(QSize(16777215, 16777215))
        self.dashboard_Page.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.dashboard_Page.setMouseTracking(False)
        self.dashboard_Page.setFocusPolicy(Qt.NoFocus)
        self.gridLayout_45 = QGridLayout(self.dashboard_Page)
        self.gridLayout_45.setSpacing(15)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 10)
        self.label = QLabel(self.dashboard_Page)
        self.label.setObjectName(u"label")
        font14 = QFont()
        font14.setFamilies([u"Arial"])
        font14.setPointSize(18)
        font14.setBold(True)
        font14.setItalic(False)
        self.label.setFont(font14)
        self.label.setStyleSheet(u"color:white;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_18.addWidget(self.label)

        self.horizontalSpacer_6 = QSpacerItem(758, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)

        self.generateReport_PushButton = QPushButton(self.dashboard_Page)
        self.generateReport_PushButton.setObjectName(u"generateReport_PushButton")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.generateReport_PushButton.sizePolicy().hasHeightForWidth())
        self.generateReport_PushButton.setSizePolicy(sizePolicy8)
        self.generateReport_PushButton.setMinimumSize(QSize(0, 0))
        self.generateReport_PushButton.setMaximumSize(QSize(16777215, 35))
        self.generateReport_PushButton.setBaseSize(QSize(0, 0))
        font15 = QFont()
        font15.setFamilies([u"Arial"])
        font15.setPointSize(14)
        font15.setBold(False)
        self.generateReport_PushButton.setFont(font15)
        self.generateReport_PushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.generateReport_PushButton.setFocusPolicy(Qt.NoFocus)
        self.generateReport_PushButton.setStyleSheet(u"background-color:#27FFE5;\n"
"color:#094646;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/resources/images/report.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.generateReport_PushButton.setIcon(icon16)
        self.generateReport_PushButton.setIconSize(QSize(28, 28))

        self.horizontalLayout_18.addWidget(self.generateReport_PushButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.widget_19 = QWidget(self.dashboard_Page)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy9)
        self.widget_19.setMinimumSize(QSize(225, 0))
        self.widget_19.setMaximumSize(QSize(16777215, 200))
        self.widget_19.setFont(font)
        self.widget_19.setStyleSheet(u"QWidget{\n"
"    border-radius:10px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #98FAC5, stop:1 #019BA5);\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white;\n"
"}\n"
"\n"
"QFrame{\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"}")
        self.gridLayout_22 = QGridLayout(self.widget_19)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_17 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_17, 2, 2, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_20, 0, 4, 2, 1)

        self.totalActors_Label = QLabel(self.widget_19)
        self.totalActors_Label.setObjectName(u"totalActors_Label")
        sizePolicy5.setHeightForWidth(self.totalActors_Label.sizePolicy().hasHeightForWidth())
        self.totalActors_Label.setSizePolicy(sizePolicy5)
        font16 = QFont()
        font16.setFamilies([u"Arial"])
        font16.setPointSize(30)
        self.totalActors_Label.setFont(font16)
        self.totalActors_Label.setScaledContents(True)

        self.gridLayout_22.addWidget(self.totalActors_Label, 2, 3, 1, 2)

        self.label_129 = QLabel(self.widget_19)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(71, 16))
        self.label_129.setMaximumSize(QSize(16777215, 16777215))
        self.label_129.setSizeIncrement(QSize(0, 0))
        self.label_129.setBaseSize(QSize(0, 0))
        font17 = QFont()
        font17.setFamilies([u"Arial"])
        font17.setPointSize(20)
        font17.setBold(True)
        font17.setKerning(True)
        self.label_129.setFont(font17)
        self.label_129.setStyleSheet(u"")
        self.label_129.setAlignment(Qt.AlignCenter)
        self.label_129.setWordWrap(True)

        self.gridLayout_22.addWidget(self.label_129, 0, 1, 1, 3)

        self.label_124 = QLabel(self.widget_19)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(0, 0))
        self.label_124.setMaximumSize(QSize(40, 40))
        self.label_124.setFont(font)
        self.label_124.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgba(0,0,0,0.40);")
        self.label_124.setPixmap(QPixmap(u":/resources/images/actors.png"))
        self.label_124.setScaledContents(True)
        self.label_124.setMargin(6)
        self.label_124.setIndent(1)

        self.gridLayout_22.addWidget(self.label_124, 0, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(14, -1, 0, -1)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, -1, 5, -1)
        self.count_simpleActors_Label = QLabel(self.widget_19)
        self.count_simpleActors_Label.setObjectName(u"count_simpleActors_Label")
        self.count_simpleActors_Label.setMaximumSize(QSize(16777215, 16777215))
        font18 = QFont()
        font18.setFamilies([u"Arial"])
        font18.setPointSize(16)
        self.count_simpleActors_Label.setFont(font18)
        self.count_simpleActors_Label.setScaledContents(False)
        self.count_simpleActors_Label.setAlignment(Qt.AlignCenter)
        self.count_simpleActors_Label.setIndent(0)

        self.verticalLayout_20.addWidget(self.count_simpleActors_Label)

        self.count_averageActors_Label = QLabel(self.widget_19)
        self.count_averageActors_Label.setObjectName(u"count_averageActors_Label")
        self.count_averageActors_Label.setFont(font18)
        self.count_averageActors_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.count_averageActors_Label)

        self.count_complexActors_Label = QLabel(self.widget_19)
        self.count_complexActors_Label.setObjectName(u"count_complexActors_Label")
        self.count_complexActors_Label.setFont(font18)
        self.count_complexActors_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.count_complexActors_Label)


        self.horizontalLayout_16.addLayout(self.verticalLayout_20)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, -1, 0, -1)
        self.label_53 = QLabel(self.widget_19)
        self.label_53.setObjectName(u"label_53")
        font19 = QFont()
        font19.setFamilies([u"Arial"])
        font19.setPointSize(16)
        font19.setBold(False)
        font19.setKerning(True)
        self.label_53.setFont(font19)
        self.label_53.setStyleSheet(u"")
        self.label_53.setTextFormat(Qt.AutoText)
        self.label_53.setScaledContents(False)
        self.label_53.setWordWrap(False)

        self.verticalLayout_26.addWidget(self.label_53)

        self.label_54 = QLabel(self.widget_19)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font19)
        self.label_54.setStyleSheet(u"")
        self.label_54.setTextFormat(Qt.AutoText)
        self.label_54.setScaledContents(False)
        self.label_54.setWordWrap(False)

        self.verticalLayout_26.addWidget(self.label_54)

        self.label_55 = QLabel(self.widget_19)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font19)
        self.label_55.setStyleSheet(u"")
        self.label_55.setTextFormat(Qt.AutoText)
        self.label_55.setScaledContents(False)
        self.label_55.setWordWrap(False)

        self.verticalLayout_26.addWidget(self.label_55)


        self.horizontalLayout_16.addLayout(self.verticalLayout_26)


        self.gridLayout_22.addLayout(self.horizontalLayout_16, 1, 0, 2, 2)


        self.horizontalLayout_2.addWidget(self.widget_19)

        self.widget_18 = QWidget(self.dashboard_Page)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy9.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy9)
        self.widget_18.setMinimumSize(QSize(225, 0))
        self.widget_18.setMaximumSize(QSize(16777215, 200))
        self.widget_18.setFont(font)
        self.widget_18.setStyleSheet(u"QWidget{\n"
"    border-radius:10px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #7FE9FD, stop:1 #0669FE);\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white;\n"
"}\n"
"\n"
"QFrame{\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"}")
        self.gridLayout_21 = QGridLayout(self.widget_18)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.verticalSpacer_19 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_19, 0, 4, 2, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(14, -1, 0, -1)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, 5, -1)
        self.count_simpleUC_Label = QLabel(self.widget_18)
        self.count_simpleUC_Label.setObjectName(u"count_simpleUC_Label")
        self.count_simpleUC_Label.setFont(font18)
        self.count_simpleUC_Label.setScaledContents(False)
        self.count_simpleUC_Label.setAlignment(Qt.AlignCenter)
        self.count_simpleUC_Label.setIndent(0)

        self.verticalLayout_17.addWidget(self.count_simpleUC_Label)

        self.count_averageUC_Label = QLabel(self.widget_18)
        self.count_averageUC_Label.setObjectName(u"count_averageUC_Label")
        self.count_averageUC_Label.setFont(font18)
        self.count_averageUC_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.count_averageUC_Label)

        self.count_complexUC_Label = QLabel(self.widget_18)
        self.count_complexUC_Label.setObjectName(u"count_complexUC_Label")
        self.count_complexUC_Label.setFont(font18)
        self.count_complexUC_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.count_complexUC_Label)


        self.horizontalLayout_15.addLayout(self.verticalLayout_17)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, -1, 0, -1)
        self.label_50 = QLabel(self.widget_18)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font19)
        self.label_50.setStyleSheet(u"")
        self.label_50.setTextFormat(Qt.AutoText)
        self.label_50.setScaledContents(False)
        self.label_50.setWordWrap(False)

        self.verticalLayout_25.addWidget(self.label_50)

        self.label_51 = QLabel(self.widget_18)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font19)
        self.label_51.setStyleSheet(u"")
        self.label_51.setTextFormat(Qt.AutoText)
        self.label_51.setScaledContents(False)
        self.label_51.setWordWrap(False)

        self.verticalLayout_25.addWidget(self.label_51)

        self.label_52 = QLabel(self.widget_18)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font19)
        self.label_52.setStyleSheet(u"")
        self.label_52.setTextFormat(Qt.AutoText)
        self.label_52.setScaledContents(False)
        self.label_52.setWordWrap(False)

        self.verticalLayout_25.addWidget(self.label_52)


        self.horizontalLayout_15.addLayout(self.verticalLayout_25)


        self.gridLayout_21.addLayout(self.horizontalLayout_15, 1, 0, 2, 2)

        self.horizontalSpacer_16 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_16, 2, 2, 1, 1)

        self.totalUC_Label = QLabel(self.widget_18)
        self.totalUC_Label.setObjectName(u"totalUC_Label")
        sizePolicy5.setHeightForWidth(self.totalUC_Label.sizePolicy().hasHeightForWidth())
        self.totalUC_Label.setSizePolicy(sizePolicy5)
        self.totalUC_Label.setFont(font16)
        self.totalUC_Label.setScaledContents(True)

        self.gridLayout_21.addWidget(self.totalUC_Label, 2, 3, 1, 2)

        self.label_122 = QLabel(self.widget_18)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(0, 0))
        self.label_122.setMaximumSize(QSize(40, 40))
        self.label_122.setFont(font)
        self.label_122.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgba(0,0,0,0.40);")
        self.label_122.setPixmap(QPixmap(u":/resources/images/useCases.png"))
        self.label_122.setScaledContents(True)
        self.label_122.setMargin(6)
        self.label_122.setIndent(1)

        self.gridLayout_21.addWidget(self.label_122, 0, 0, 1, 1)

        self.label_123 = QLabel(self.widget_18)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(71, 16))
        self.label_123.setMaximumSize(QSize(16777215, 16777215))
        self.label_123.setSizeIncrement(QSize(0, 0))
        self.label_123.setBaseSize(QSize(0, 0))
        self.label_123.setFont(font17)
        self.label_123.setStyleSheet(u"")
        self.label_123.setAlignment(Qt.AlignCenter)
        self.label_123.setWordWrap(True)

        self.gridLayout_21.addWidget(self.label_123, 0, 1, 1, 3)


        self.horizontalLayout_2.addWidget(self.widget_18)

        self.widget_16 = QWidget(self.dashboard_Page)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy9.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy9)
        self.widget_16.setMinimumSize(QSize(200, 0))
        self.widget_16.setMaximumSize(QSize(16777215, 200))
        self.widget_16.setFont(font)
        self.widget_16.setStyleSheet(u"QWidget{\n"
"    border-radius:10px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFBD5B, stop:1 #E86C3F);\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white;\n"
"}\n"
"\n"
"QFrame{\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"}")
        self.gridLayout_19 = QGridLayout(self.widget_16)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(14, -1, 0, -1)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, 5, -1)
        self.count_irrelevantTF_Label = QLabel(self.widget_16)
        self.count_irrelevantTF_Label.setObjectName(u"count_irrelevantTF_Label")
        self.count_irrelevantTF_Label.setFont(font18)
        self.count_irrelevantTF_Label.setScaledContents(False)
        self.count_irrelevantTF_Label.setAlignment(Qt.AlignCenter)
        self.count_irrelevantTF_Label.setIndent(0)

        self.verticalLayout_12.addWidget(self.count_irrelevantTF_Label)

        self.count_mediumTF_Label = QLabel(self.widget_16)
        self.count_mediumTF_Label.setObjectName(u"count_mediumTF_Label")
        self.count_mediumTF_Label.setFont(font18)
        self.count_mediumTF_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.count_mediumTF_Label)

        self.count_essentialTF_Label = QLabel(self.widget_16)
        self.count_essentialTF_Label.setObjectName(u"count_essentialTF_Label")
        self.count_essentialTF_Label.setFont(font18)
        self.count_essentialTF_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.count_essentialTF_Label)


        self.horizontalLayout_13.addLayout(self.verticalLayout_12)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, -1, 0, -1)
        self.label_44 = QLabel(self.widget_16)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font19)
        self.label_44.setStyleSheet(u"")
        self.label_44.setTextFormat(Qt.AutoText)
        self.label_44.setScaledContents(False)
        self.label_44.setWordWrap(False)

        self.verticalLayout_23.addWidget(self.label_44)

        self.label_45 = QLabel(self.widget_16)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font19)
        self.label_45.setStyleSheet(u"")
        self.label_45.setTextFormat(Qt.AutoText)
        self.label_45.setScaledContents(False)
        self.label_45.setWordWrap(False)

        self.verticalLayout_23.addWidget(self.label_45)

        self.label_46 = QLabel(self.widget_16)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font19)
        self.label_46.setStyleSheet(u"")
        self.label_46.setTextFormat(Qt.AutoText)
        self.label_46.setScaledContents(False)
        self.label_46.setWordWrap(False)

        self.verticalLayout_23.addWidget(self.label_46)


        self.horizontalLayout_13.addLayout(self.verticalLayout_23)


        self.gridLayout_19.addLayout(self.horizontalLayout_13, 1, 0, 2, 2)

        self.totalTF_Label = QLabel(self.widget_16)
        self.totalTF_Label.setObjectName(u"totalTF_Label")
        sizePolicy5.setHeightForWidth(self.totalTF_Label.sizePolicy().hasHeightForWidth())
        self.totalTF_Label.setSizePolicy(sizePolicy5)
        self.totalTF_Label.setFont(font16)
        self.totalTF_Label.setScaledContents(True)

        self.gridLayout_19.addWidget(self.totalTF_Label, 2, 3, 1, 2)

        self.label_110 = QLabel(self.widget_16)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(0, 0))
        self.label_110.setMaximumSize(QSize(40, 40))
        self.label_110.setFont(font)
        self.label_110.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgba(0,0,0,0.40);")
        self.label_110.setPixmap(QPixmap(u":/resources/images/technicalFactors.png"))
        self.label_110.setScaledContents(True)
        self.label_110.setMargin(8)
        self.label_110.setIndent(1)

        self.gridLayout_19.addWidget(self.label_110, 0, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_17, 0, 4, 2, 1)

        self.label_109 = QLabel(self.widget_16)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMinimumSize(QSize(71, 16))
        self.label_109.setMaximumSize(QSize(16777215, 16777215))
        self.label_109.setSizeIncrement(QSize(0, 0))
        self.label_109.setBaseSize(QSize(0, 0))
        self.label_109.setFont(font17)
        self.label_109.setStyleSheet(u"")
        self.label_109.setAlignment(Qt.AlignCenter)
        self.label_109.setWordWrap(True)

        self.gridLayout_19.addWidget(self.label_109, 0, 1, 1, 3)

        self.horizontalSpacer_14 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_14, 2, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.dashboard_Page)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy9.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy9)
        self.widget_17.setMinimumSize(QSize(200, 0))
        self.widget_17.setMaximumSize(QSize(16777215, 200))
        self.widget_17.setFont(font)
        self.widget_17.setStyleSheet(u"QWidget{\n"
"    border-radius:10px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FF9FE4, stop:1 #9002FF);\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white;\n"
"}\n"
"\n"
"QFrame{\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"}")
        self.gridLayout_20 = QGridLayout(self.widget_17)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(14, -1, 0, -1)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, 5, -1)
        self.count_irrelevantEF_Label = QLabel(self.widget_17)
        self.count_irrelevantEF_Label.setObjectName(u"count_irrelevantEF_Label")
        self.count_irrelevantEF_Label.setFont(font18)
        self.count_irrelevantEF_Label.setScaledContents(False)
        self.count_irrelevantEF_Label.setIndent(0)

        self.verticalLayout_16.addWidget(self.count_irrelevantEF_Label)

        self.count_mediumEF_Label = QLabel(self.widget_17)
        self.count_mediumEF_Label.setObjectName(u"count_mediumEF_Label")
        self.count_mediumEF_Label.setFont(font18)

        self.verticalLayout_16.addWidget(self.count_mediumEF_Label)

        self.count_essentialEF_Label = QLabel(self.widget_17)
        self.count_essentialEF_Label.setObjectName(u"count_essentialEF_Label")
        self.count_essentialEF_Label.setFont(font18)

        self.verticalLayout_16.addWidget(self.count_essentialEF_Label)


        self.horizontalLayout_14.addLayout(self.verticalLayout_16)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, -1, 0, -1)
        self.label_47 = QLabel(self.widget_17)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font19)
        self.label_47.setStyleSheet(u"")
        self.label_47.setTextFormat(Qt.AutoText)
        self.label_47.setScaledContents(False)
        self.label_47.setWordWrap(False)

        self.verticalLayout_24.addWidget(self.label_47)

        self.label_48 = QLabel(self.widget_17)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font19)
        self.label_48.setStyleSheet(u"")
        self.label_48.setTextFormat(Qt.AutoText)
        self.label_48.setScaledContents(False)
        self.label_48.setWordWrap(False)

        self.verticalLayout_24.addWidget(self.label_48)

        self.label_49 = QLabel(self.widget_17)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font19)
        self.label_49.setStyleSheet(u"")
        self.label_49.setTextFormat(Qt.AutoText)
        self.label_49.setScaledContents(False)
        self.label_49.setWordWrap(False)

        self.verticalLayout_24.addWidget(self.label_49)


        self.horizontalLayout_14.addLayout(self.verticalLayout_24)


        self.gridLayout_20.addLayout(self.horizontalLayout_14, 1, 0, 2, 2)

        self.label_117 = QLabel(self.widget_17)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(140, 40))
        self.label_117.setMaximumSize(QSize(16777215, 16777215))
        self.label_117.setSizeIncrement(QSize(0, 0))
        self.label_117.setBaseSize(QSize(0, 0))
        self.label_117.setFont(font17)
        self.label_117.setStyleSheet(u"")
        self.label_117.setAlignment(Qt.AlignCenter)
        self.label_117.setWordWrap(True)

        self.gridLayout_20.addWidget(self.label_117, 0, 1, 1, 3)

        self.verticalSpacer_18 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_18, 0, 4, 2, 1)

        self.label_116 = QLabel(self.widget_17)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(0, 0))
        self.label_116.setMaximumSize(QSize(40, 40))
        self.label_116.setFont(font)
        self.label_116.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgba(0,0,0,0.40);")
        self.label_116.setPixmap(QPixmap(u":/resources/images/environmentalFactors.png"))
        self.label_116.setScaledContents(True)
        self.label_116.setAlignment(Qt.AlignCenter)
        self.label_116.setMargin(7)
        self.label_116.setIndent(1)

        self.gridLayout_20.addWidget(self.label_116, 0, 0, 1, 1)

        self.totalEF_Label = QLabel(self.widget_17)
        self.totalEF_Label.setObjectName(u"totalEF_Label")
        sizePolicy5.setHeightForWidth(self.totalEF_Label.sizePolicy().hasHeightForWidth())
        self.totalEF_Label.setSizePolicy(sizePolicy5)
        self.totalEF_Label.setFont(font16)
        self.totalEF_Label.setScaledContents(True)

        self.gridLayout_20.addWidget(self.totalEF_Label, 2, 3, 1, 2)

        self.horizontalSpacer_15 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_15, 2, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_17)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)


        self.gridLayout_45.addLayout(self.verticalLayout_9, 0, 0, 1, 2)

        self.widget_3 = QWidget(self.dashboard_Page)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.widget_3.setStyleSheet(u"background:#22577A;")
        self.gridLayout_7 = QGridLayout(self.widget_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(10)
        self.widget_13 = QWidget(self.widget_3)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy)
        self.widget_13.setMaximumSize(QSize(16777215, 16777215))
        self.widget_13.setStyleSheet(u"background:#B2F3FF;")
        self.gridLayout_15 = QGridLayout(self.widget_13)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(15)
        self.gridLayout_15.setContentsMargins(12, -1, -1, -1)
        self.label_95 = QLabel(self.widget_13)
        self.label_95.setObjectName(u"label_95")
        font20 = QFont()
        font20.setFamilies([u"Arial"])
        font20.setPointSize(14)
        font20.setBold(True)
        self.label_95.setFont(font20)
        self.label_95.setStyleSheet(u"color:#22577A;")

        self.gridLayout_15.addWidget(self.label_95, 0, 0, 1, 1)

        self.CF_LineEdit = QLineEdit(self.widget_13)
        self.CF_LineEdit.setObjectName(u"CF_LineEdit")
        sizePolicy9.setHeightForWidth(self.CF_LineEdit.sizePolicy().hasHeightForWidth())
        self.CF_LineEdit.setSizePolicy(sizePolicy9)
        self.CF_LineEdit.setMinimumSize(QSize(0, 20))
        self.CF_LineEdit.setFont(font9)
        self.CF_LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.CF_LineEdit.setFocusPolicy(Qt.NoFocus)
        self.CF_LineEdit.setStyleSheet(u"background: #9DCAE2;\n"
"border: 1px solid black;")
        self.CF_LineEdit.setReadOnly(True)

        self.gridLayout_15.addWidget(self.CF_LineEdit, 0, 1, 1, 1)

        self.label_90 = QLabel(self.widget_13)
        self.label_90.setObjectName(u"label_90")
        font21 = QFont()
        font21.setFamilies([u"Arial"])
        font21.setPointSize(13)
        font21.setWeight(QFont.Thin)
        self.label_90.setFont(font21)

        self.gridLayout_15.addWidget(self.label_90, 0, 2, 1, 1)

        self.editCF_Button = QPushButton(self.widget_13)
        self.editCF_Button.setObjectName(u"editCF_Button")
        sizePolicy4.setHeightForWidth(self.editCF_Button.sizePolicy().hasHeightForWidth())
        self.editCF_Button.setSizePolicy(sizePolicy4)
        self.editCF_Button.setMinimumSize(QSize(0, 0))
        self.editCF_Button.setMaximumSize(QSize(16777215, 16777215))
        self.editCF_Button.setBaseSize(QSize(0, 0))
        self.editCF_Button.setFont(font15)
        self.editCF_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.editCF_Button.setFocusPolicy(Qt.NoFocus)
        self.editCF_Button.setStyleSheet(u"border: None;")
        icon17 = QIcon()
        icon17.addFile(u":/resources/images/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editCF_Button.setIcon(icon17)
        self.editCF_Button.setIconSize(QSize(25, 25))

        self.gridLayout_15.addWidget(self.editCF_Button, 0, 3, 1, 1)


        self.gridLayout_7.addWidget(self.widget_13, 6, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.widget_12 = QWidget(self.widget_3)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.widget_12.setMaximumSize(QSize(16777215, 16777215))
        self.widget_12.setStyleSheet(u"background: #CFF2F0;")
        self.gridLayout_13 = QGridLayout(self.widget_12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(14)
        self.gridLayout_13.setVerticalSpacing(15)
        self.gridLayout_13.setContentsMargins(12, 12, 12, 20)
        self.label_70 = QLabel(self.widget_12)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(0, 20))
        font22 = QFont()
        font22.setFamilies([u"Arial"])
        font22.setPointSize(12)
        font22.setBold(False)
        self.label_70.setFont(font22)

        self.gridLayout_13.addWidget(self.label_70, 2, 0, 1, 1)

        self.label_68 = QLabel(self.widget_12)
        self.label_68.setObjectName(u"label_68")
        sizePolicy5.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy5)
        self.label_68.setMinimumSize(QSize(0, 16))
        self.label_68.setFont(font20)

        self.gridLayout_13.addWidget(self.label_68, 0, 0, 1, 1)

        self.TCF_LineEdit = QLineEdit(self.widget_12)
        self.TCF_LineEdit.setObjectName(u"TCF_LineEdit")
        sizePolicy9.setHeightForWidth(self.TCF_LineEdit.sizePolicy().hasHeightForWidth())
        self.TCF_LineEdit.setSizePolicy(sizePolicy9)
        self.TCF_LineEdit.setMinimumSize(QSize(0, 20))
        self.TCF_LineEdit.setFont(font9)
        self.TCF_LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.TCF_LineEdit.setMouseTracking(False)
        self.TCF_LineEdit.setFocusPolicy(Qt.NoFocus)
        self.TCF_LineEdit.setStyleSheet(u"background: #C4DEDF;\n"
"border: 1px solid black;")
        self.TCF_LineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.TCF_LineEdit, 3, 1, 1, 1)

        self.label_69 = QLabel(self.widget_12)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(0, 20))
        self.label_69.setFont(font22)

        self.gridLayout_13.addWidget(self.label_69, 1, 0, 1, 1)

        self.label_84 = QLabel(self.widget_12)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(0, 20))
        self.label_84.setFont(font22)

        self.gridLayout_13.addWidget(self.label_84, 4, 0, 1, 1)

        self.EFactor_LineEdit = QLineEdit(self.widget_12)
        self.EFactor_LineEdit.setObjectName(u"EFactor_LineEdit")
        sizePolicy9.setHeightForWidth(self.EFactor_LineEdit.sizePolicy().hasHeightForWidth())
        self.EFactor_LineEdit.setSizePolicy(sizePolicy9)
        self.EFactor_LineEdit.setMinimumSize(QSize(0, 20))
        self.EFactor_LineEdit.setFont(font9)
        self.EFactor_LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.EFactor_LineEdit.setMouseTracking(False)
        self.EFactor_LineEdit.setFocusPolicy(Qt.NoFocus)
        self.EFactor_LineEdit.setStyleSheet(u"background: #C4DEDF;\n"
"border: 1px solid black;")
        self.EFactor_LineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.EFactor_LineEdit, 2, 1, 1, 1)

        self.ECF_LineEdit = QLineEdit(self.widget_12)
        self.ECF_LineEdit.setObjectName(u"ECF_LineEdit")
        sizePolicy9.setHeightForWidth(self.ECF_LineEdit.sizePolicy().hasHeightForWidth())
        self.ECF_LineEdit.setSizePolicy(sizePolicy9)
        self.ECF_LineEdit.setMinimumSize(QSize(0, 20))
        self.ECF_LineEdit.setFont(font9)
        self.ECF_LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ECF_LineEdit.setMouseTracking(False)
        self.ECF_LineEdit.setFocusPolicy(Qt.NoFocus)
        self.ECF_LineEdit.setStyleSheet(u"background: #C4DEDF;\n"
"border: 1px solid black;")
        self.ECF_LineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.ECF_LineEdit, 4, 1, 1, 1)

        self.UCP_LineEdit = QLineEdit(self.widget_12)
        self.UCP_LineEdit.setObjectName(u"UCP_LineEdit")
        sizePolicy9.setHeightForWidth(self.UCP_LineEdit.sizePolicy().hasHeightForWidth())
        self.UCP_LineEdit.setSizePolicy(sizePolicy9)
        self.UCP_LineEdit.setMinimumSize(QSize(0, 20))
        self.UCP_LineEdit.setFont(font9)
        self.UCP_LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.UCP_LineEdit.setMouseTracking(False)
        self.UCP_LineEdit.setFocusPolicy(Qt.NoFocus)
        self.UCP_LineEdit.setStyleSheet(u"background: #C4DEDF;\n"
"border: 1px solid black;")
        self.UCP_LineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.UCP_LineEdit, 5, 1, 1, 1)

        self.label_85 = QLabel(self.widget_12)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(0, 20))
        self.label_85.setFont(font22)

        self.gridLayout_13.addWidget(self.label_85, 3, 0, 1, 1)

        self.TFactor_LineEdit = QLineEdit(self.widget_12)
        self.TFactor_LineEdit.setObjectName(u"TFactor_LineEdit")
        sizePolicy9.setHeightForWidth(self.TFactor_LineEdit.sizePolicy().hasHeightForWidth())
        self.TFactor_LineEdit.setSizePolicy(sizePolicy9)
        self.TFactor_LineEdit.setMinimumSize(QSize(0, 20))
        self.TFactor_LineEdit.setFont(font9)
        self.TFactor_LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.TFactor_LineEdit.setMouseTracking(False)
        self.TFactor_LineEdit.setFocusPolicy(Qt.NoFocus)
        self.TFactor_LineEdit.setStyleSheet(u"background: #C4DEDF;\n"
"border: 1px solid black;")
        self.TFactor_LineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.TFactor_LineEdit, 1, 1, 1, 1)

        self.label_83 = QLabel(self.widget_12)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(0, 20))
        self.label_83.setFont(font22)

        self.gridLayout_13.addWidget(self.label_83, 5, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_12, 5, 0, 1, 1)

        self.line = QFrame(self.widget_3)
        self.line.setObjectName(u"line")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy10)
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color:white;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line, 1, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setMaximumSize(QSize(16777215, 16777215))
        self.widget_11.setStyleSheet(u"background: #CFF2F0;")
        self.gridLayout_6 = QGridLayout(self.widget_11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(25)
        self.gridLayout_6.setVerticalSpacing(15)
        self.gridLayout_6.setContentsMargins(12, 12, 12, 12)
        self.label_26 = QLabel(self.widget_11)
        self.label_26.setObjectName(u"label_26")
        sizePolicy5.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy5)
        self.label_26.setFont(font20)

        self.gridLayout_6.addWidget(self.label_26, 1, 0, 1, 2)

        self.UUCP_LineEdit = QLineEdit(self.widget_11)
        self.UUCP_LineEdit.setObjectName(u"UUCP_LineEdit")
        sizePolicy4.setHeightForWidth(self.UUCP_LineEdit.sizePolicy().hasHeightForWidth())
        self.UUCP_LineEdit.setSizePolicy(sizePolicy4)
        self.UUCP_LineEdit.setMinimumSize(QSize(0, 20))
        self.UUCP_LineEdit.setFont(font9)
        self.UUCP_LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.UUCP_LineEdit.setMouseTracking(False)
        self.UUCP_LineEdit.setFocusPolicy(Qt.NoFocus)
        self.UUCP_LineEdit.setStyleSheet(u"background: #C4DEDF;\n"
"border: 1px solid black;")
        self.UUCP_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.UUCP_LineEdit, 4, 1, 1, 1)

        self.UAW_LineEdit = QLineEdit(self.widget_11)
        self.UAW_LineEdit.setObjectName(u"UAW_LineEdit")
        sizePolicy9.setHeightForWidth(self.UAW_LineEdit.sizePolicy().hasHeightForWidth())
        self.UAW_LineEdit.setSizePolicy(sizePolicy9)
        self.UAW_LineEdit.setMinimumSize(QSize(0, 20))
        self.UAW_LineEdit.setFont(font9)
        self.UAW_LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.UAW_LineEdit.setMouseTracking(False)
        self.UAW_LineEdit.setFocusPolicy(Qt.NoFocus)
        self.UAW_LineEdit.setStyleSheet(u"background: #C4DEDF;\n"
"border: 1px solid black;")
        self.UAW_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.UAW_LineEdit, 2, 1, 1, 1)

        self.UUCW_LineEdit = QLineEdit(self.widget_11)
        self.UUCW_LineEdit.setObjectName(u"UUCW_LineEdit")
        sizePolicy4.setHeightForWidth(self.UUCW_LineEdit.sizePolicy().hasHeightForWidth())
        self.UUCW_LineEdit.setSizePolicy(sizePolicy4)
        self.UUCW_LineEdit.setMinimumSize(QSize(0, 20))
        self.UUCW_LineEdit.setFont(font9)
        self.UUCW_LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.UUCW_LineEdit.setMouseTracking(False)
        self.UUCW_LineEdit.setFocusPolicy(Qt.NoFocus)
        self.UUCW_LineEdit.setStyleSheet(u"background: #C4DEDF;\n"
"border: 1px solid black;")
        self.UUCW_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.UUCW_LineEdit, 3, 1, 1, 1)

        self.label_66 = QLabel(self.widget_11)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(0, 20))
        self.label_66.setFont(font22)

        self.gridLayout_6.addWidget(self.label_66, 3, 0, 1, 1)

        self.label_67 = QLabel(self.widget_11)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(0, 20))
        self.label_67.setFont(font22)

        self.gridLayout_6.addWidget(self.label_67, 4, 0, 1, 1)

        self.label_31 = QLabel(self.widget_11)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 20))
        self.label_31.setFont(font22)

        self.gridLayout_6.addWidget(self.label_31, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_11, 3, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_27 = QLabel(self.widget_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(30, 30))
        self.label_27.setSizeIncrement(QSize(0, 1))
        self.label_27.setBaseSize(QSize(0, 0))
        self.label_27.setPixmap(QPixmap(u":/resources/images/estimationResults.png"))
        self.label_27.setScaledContents(True)

        self.gridLayout_12.addWidget(self.label_27, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.label_28 = QLabel(self.widget_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 16777215))
        self.label_28.setFont(font14)
        self.label_28.setStyleSheet(u"color:white;")

        self.gridLayout_12.addWidget(self.label_28, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.widget_3)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.widget_14.setMaximumSize(QSize(16777215, 16777215))
        self.widget_14.setStyleSheet(u"background: #93F3E3;")
        self.gridLayout_14 = QGridLayout(self.widget_14)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(15)
        self.gridLayout_14.setContentsMargins(-1, -1, 12, -1)
        self.label_91 = QLabel(self.widget_14)
        self.label_91.setObjectName(u"label_91")
        sizePolicy4.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy4)
        font23 = QFont()
        font23.setFamilies([u"Arial"])
        font23.setPointSize(13)
        self.label_91.setFont(font23)

        self.gridLayout_14.addWidget(self.label_91, 0, 3, 1, 1)

        self.label_92 = QLabel(self.widget_14)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font20)
        self.label_92.setStyleSheet(u"color:#245151;")

        self.gridLayout_14.addWidget(self.label_92, 0, 1, 1, 1)

        self.E_LineEdit = QLineEdit(self.widget_14)
        self.E_LineEdit.setObjectName(u"E_LineEdit")
        sizePolicy9.setHeightForWidth(self.E_LineEdit.sizePolicy().hasHeightForWidth())
        self.E_LineEdit.setSizePolicy(sizePolicy9)
        self.E_LineEdit.setMinimumSize(QSize(0, 20))
        self.E_LineEdit.setFont(font9)
        self.E_LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.E_LineEdit.setFocusPolicy(Qt.NoFocus)
        self.E_LineEdit.setStyleSheet(u"background: #7DCEC1;\n"
"border: 1px solid black;")
        self.E_LineEdit.setReadOnly(True)

        self.gridLayout_14.addWidget(self.E_LineEdit, 0, 2, 1, 1)

        self.E_Button = QPushButton(self.widget_14)
        self.E_Button.setObjectName(u"E_Button")
        self.E_Button.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.E_Button.sizePolicy().hasHeightForWidth())
        self.E_Button.setSizePolicy(sizePolicy4)
        self.E_Button.setMinimumSize(QSize(0, 0))
        self.E_Button.setMaximumSize(QSize(16777215, 16777215))
        self.E_Button.setBaseSize(QSize(0, 0))
        self.E_Button.setFont(font15)
        self.E_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.E_Button.setFocusPolicy(Qt.NoFocus)
        self.E_Button.setStyleSheet(u"border: None;")
        icon18 = QIcon()
        icon18.addFile(u":/resources/images/estimatedEffort.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.E_Button.setIcon(icon18)
        self.E_Button.setIconSize(QSize(28, 28))

        self.gridLayout_14.addWidget(self.E_Button, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_14, 7, 0, 1, 1)


        self.gridLayout_45.addWidget(self.widget_3, 1, 0, 2, 1)

        self.widget_4 = QWidget(self.dashboard_Page)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QSize(16777215, 16777215))
        self.widget_4.setStyleSheet(u"background:#22577A;")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.effortDistribution_TableWidget = QTableWidget(self.widget_4)
        if (self.effortDistribution_TableWidget.columnCount() < 3):
            self.effortDistribution_TableWidget.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font4);
        __qtablewidgetitem10.setBackground(QColor(216, 216, 216));
        self.effortDistribution_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        icon19 = QIcon()
        icon19.addFile(u":/resources/images/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font4);
        __qtablewidgetitem11.setBackground(QColor(217, 217, 217));
        __qtablewidgetitem11.setIcon(icon19);
        self.effortDistribution_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        font24 = QFont()
        font24.setFamilies([u"Arial"])
        font24.setPointSize(15)
        font24.setStyleStrategy(QFont.PreferDefault)
        font24.setHintingPreference(QFont.PreferDefaultHinting)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font24);
        __qtablewidgetitem12.setBackground(QColor(217, 217, 217));
        self.effortDistribution_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        if (self.effortDistribution_TableWidget.rowCount() < 5):
            self.effortDistribution_TableWidget.setRowCount(5)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setBackground(QColor(0, 0, 0));
        __qtablewidgetitem13.setForeground(brush);
        self.effortDistribution_TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem13)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setForeground(brush1);
        self.effortDistribution_TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.effortDistribution_TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.effortDistribution_TableWidget.setVerticalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.effortDistribution_TableWidget.setVerticalHeaderItem(4, __qtablewidgetitem17)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        brush3 = QBrush(QColor(255, 164, 164, 255))
        brush3.setStyle(Qt.SolidPattern)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font4);
        __qtablewidgetitem18.setBackground(brush3);
        __qtablewidgetitem18.setForeground(brush2);
        self.effortDistribution_TableWidget.setItem(0, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font4);
        self.effortDistribution_TableWidget.setItem(0, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font4);
        self.effortDistribution_TableWidget.setItem(0, 2, __qtablewidgetitem20)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        brush5 = QBrush(QColor(253, 222, 162, 255))
        brush5.setStyle(Qt.SolidPattern)
        font25 = QFont()
        font25.setFamilies([u"Arial"])
        font25.setPointSize(15)
        font25.setKerning(True)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font25);
        __qtablewidgetitem21.setBackground(brush5);
        __qtablewidgetitem21.setForeground(brush4);
        self.effortDistribution_TableWidget.setItem(1, 0, __qtablewidgetitem21)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font4);
        __qtablewidgetitem22.setForeground(brush6);
        self.effortDistribution_TableWidget.setItem(1, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font4);
        self.effortDistribution_TableWidget.setItem(1, 2, __qtablewidgetitem23)
        brush7 = QBrush(QColor(147, 243, 227, 255))
        brush7.setStyle(Qt.SolidPattern)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFont(font4);
        __qtablewidgetitem24.setBackground(brush7);
        self.effortDistribution_TableWidget.setItem(2, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem25.setFont(font4);
        __qtablewidgetitem25.setBackground(brush7);
        self.effortDistribution_TableWidget.setItem(2, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem26.setFont(font4);
        __qtablewidgetitem26.setBackground(brush7);
        self.effortDistribution_TableWidget.setItem(2, 2, __qtablewidgetitem26)
        brush8 = QBrush(QColor(253, 255, 170, 255))
        brush8.setStyle(Qt.SolidPattern)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem27.setFont(font4);
        __qtablewidgetitem27.setBackground(brush8);
        self.effortDistribution_TableWidget.setItem(3, 0, __qtablewidgetitem27)
        font26 = QFont()
        font26.setFamilies([u"Arial"])
        font26.setPointSize(15)
        font26.setUnderline(False)
        font26.setStrikeOut(False)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem28.setFont(font26);
        self.effortDistribution_TableWidget.setItem(3, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setFont(font4);
        self.effortDistribution_TableWidget.setItem(3, 2, __qtablewidgetitem29)
        brush9 = QBrush(QColor(124, 224, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setFont(font4);
        __qtablewidgetitem30.setBackground(brush9);
        self.effortDistribution_TableWidget.setItem(4, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem31.setFont(font4);
        self.effortDistribution_TableWidget.setItem(4, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFont(font4);
        self.effortDistribution_TableWidget.setItem(4, 2, __qtablewidgetitem32)
        self.effortDistribution_TableWidget.setObjectName(u"effortDistribution_TableWidget")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.effortDistribution_TableWidget.sizePolicy().hasHeightForWidth())
        self.effortDistribution_TableWidget.setSizePolicy(sizePolicy11)
        self.effortDistribution_TableWidget.setMinimumSize(QSize(0, 200))
        self.effortDistribution_TableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.effortDistribution_TableWidget.setFont(font4)
        self.effortDistribution_TableWidget.viewport().setProperty("cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.effortDistribution_TableWidget.setMouseTracking(True)
        self.effortDistribution_TableWidget.setTabletTracking(True)
        self.effortDistribution_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.effortDistribution_TableWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.effortDistribution_TableWidget.setLayoutDirection(Qt.LeftToRight)
        self.effortDistribution_TableWidget.setStyleSheet(u"QTableWidget{\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"    gridline-color: #9C9C9C; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    height:35px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"     background: #3B4252;\n"
"     width: 20px;\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: white;\n"
"     min-height: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #3B4252;\n"
"     height: 20px;\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: white;\n"
"     min-width: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"QScrollBar"
                        "::sub-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}")
        self.effortDistribution_TableWidget.setFrameShape(QFrame.NoFrame)
        self.effortDistribution_TableWidget.setFrameShadow(QFrame.Plain)
        self.effortDistribution_TableWidget.setLineWidth(-1)
        self.effortDistribution_TableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.effortDistribution_TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.effortDistribution_TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.effortDistribution_TableWidget.setAutoScroll(False)
        self.effortDistribution_TableWidget.setAutoScrollMargin(0)
        self.effortDistribution_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.effortDistribution_TableWidget.setTabKeyNavigation(False)
        self.effortDistribution_TableWidget.setProperty("showDropIndicator", False)
        self.effortDistribution_TableWidget.setDragDropOverwriteMode(False)
        self.effortDistribution_TableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.effortDistribution_TableWidget.setTextElideMode(Qt.ElideRight)
        self.effortDistribution_TableWidget.setShowGrid(True)
        self.effortDistribution_TableWidget.setGridStyle(Qt.SolidLine)
        self.effortDistribution_TableWidget.setSortingEnabled(False)
        self.effortDistribution_TableWidget.setWordWrap(True)
        self.effortDistribution_TableWidget.setCornerButtonEnabled(True)
        self.effortDistribution_TableWidget.horizontalHeader().setVisible(True)
        self.effortDistribution_TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.effortDistribution_TableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.effortDistribution_TableWidget.horizontalHeader().setDefaultSectionSize(110)
        self.effortDistribution_TableWidget.horizontalHeader().setHighlightSections(False)
        self.effortDistribution_TableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.effortDistribution_TableWidget.horizontalHeader().setStretchLastSection(True)
        self.effortDistribution_TableWidget.verticalHeader().setVisible(False)
        self.effortDistribution_TableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.effortDistribution_TableWidget.verticalHeader().setMinimumSectionSize(0)
        self.effortDistribution_TableWidget.verticalHeader().setDefaultSectionSize(30)
        self.effortDistribution_TableWidget.verticalHeader().setHighlightSections(False)
        self.effortDistribution_TableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.effortDistribution_TableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.effortDistribution_TableWidget, 3, 0, 1, 1)

        self.line_4 = QFrame(self.widget_4)
        self.line_4.setObjectName(u"line_4")
        sizePolicy10.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy10)
        self.line_4.setMinimumSize(QSize(0, 0))
        self.line_4.setMaximumSize(QSize(16777215, 1))
        self.line_4.setStyleSheet(u"background-color:white;")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_29 = QLabel(self.widget_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(35, 35))
        self.label_29.setPixmap(QPixmap(u":/resources/images/effortDistribution.png"))
        self.label_29.setScaledContents(True)

        self.gridLayout_16.addWidget(self.label_29, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.label_30 = QLabel(self.widget_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 16777215))
        self.label_30.setFont(font14)
        self.label_30.setStyleSheet(u"color:white;")

        self.gridLayout_16.addWidget(self.label_30, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_16, 0, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.widget_4)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy9.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy9)
        self.graphicsView.setMinimumSize(QSize(0, 0))
        self.graphicsView.setMaximumSize(QSize(16777215, 300))
        self.graphicsView.setFont(font)
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setFocusPolicy(Qt.NoFocus)
        self.graphicsView.setFrameShape(QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QFrame.Plain)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphicsView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.graphicsView.setInteractive(False)
        self.graphicsView.setRenderHints(QPainter.Antialiasing|QPainter.TextAntialiasing)
        self.graphicsView.setViewportUpdateMode(QGraphicsView.MinimalViewportUpdate)

        self.gridLayout_3.addWidget(self.graphicsView, 4, 0, 1, 1)


        self.gridLayout_45.addWidget(self.widget_4, 1, 1, 2, 1)

        self.stackedWidget_2.addWidget(self.dashboard_Page)
        self.actors_Page = QWidget()
        self.actors_Page.setObjectName(u"actors_Page")
        sizePolicy2.setHeightForWidth(self.actors_Page.sizePolicy().hasHeightForWidth())
        self.actors_Page.setSizePolicy(sizePolicy2)
        self.gridLayout_40 = QGridLayout(self.actors_Page)
        self.gridLayout_40.setSpacing(15)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(15, 15, 15, 15)
        self.label_2 = QLabel(self.actors_Page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font14)
        self.label_2.setStyleSheet(u"color:white;")

        self.gridLayout_40.addWidget(self.label_2, 0, 0, 1, 1)

        self.widget_23 = QWidget(self.actors_Page)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy)
        self.widget_23.setStyleSheet(u"background:#22577A;")
        self.gridLayout_27 = QGridLayout(self.widget_23)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setHorizontalSpacing(0)
        self.gridLayout_27.setVerticalSpacing(12)
        self.gridLayout_27.setContentsMargins(20, 20, 20, 20)
        self.actors_TableWidget = QTableWidget(self.widget_23)
        if (self.actors_TableWidget.columnCount() < 6):
            self.actors_TableWidget.setColumnCount(6)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.actors_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font4);
        self.actors_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font4);
        self.actors_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font4);
        self.actors_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font4);
        self.actors_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font4);
        self.actors_TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem38)
        self.actors_TableWidget.setObjectName(u"actors_TableWidget")
        sizePolicy.setHeightForWidth(self.actors_TableWidget.sizePolicy().hasHeightForWidth())
        self.actors_TableWidget.setSizePolicy(sizePolicy)
        self.actors_TableWidget.setFont(font7)
        self.actors_TableWidget.setMouseTracking(False)
        self.actors_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.actors_TableWidget.setLayoutDirection(Qt.LeftToRight)
        self.actors_TableWidget.setStyleSheet(u"QTableWidget{\n"
"    border:none;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"    height: 36px;\n"
"}\n"
"\n"
"QTableWidget::Item{\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(0,0,0,0.25);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"     background: #3B4252;\n"
"     width: 20px;\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: white;\n"
"     min-height: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #3B4252;\n"
"     height: 20px;\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: white;\n"
"     min-width: 20px;\n"
"  "
                        "   border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}")
        self.actors_TableWidget.setFrameShape(QFrame.NoFrame)
        self.actors_TableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.actors_TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.actors_TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.actors_TableWidget.setAutoScroll(True)
        self.actors_TableWidget.setAutoScrollMargin(0)
        self.actors_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.actors_TableWidget.setTabKeyNavigation(True)
        self.actors_TableWidget.setProperty("showDropIndicator", False)
        self.actors_TableWidget.setDragEnabled(False)
        self.actors_TableWidget.setDragDropOverwriteMode(False)
        self.actors_TableWidget.setAlternatingRowColors(False)
        self.actors_TableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.actors_TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.actors_TableWidget.setTextElideMode(Qt.ElideRight)
        self.actors_TableWidget.setShowGrid(False)
        self.actors_TableWidget.setGridStyle(Qt.SolidLine)
        self.actors_TableWidget.setSortingEnabled(True)
        self.actors_TableWidget.setWordWrap(True)
        self.actors_TableWidget.setCornerButtonEnabled(False)
        self.actors_TableWidget.setRowCount(0)
        self.actors_TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.actors_TableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.actors_TableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.actors_TableWidget.horizontalHeader().setHighlightSections(True)
        self.actors_TableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.actors_TableWidget.horizontalHeader().setStretchLastSection(False)
        self.actors_TableWidget.verticalHeader().setVisible(False)
        self.actors_TableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.actors_TableWidget.verticalHeader().setMinimumSectionSize(0)
        self.actors_TableWidget.verticalHeader().setDefaultSectionSize(45)
        self.actors_TableWidget.verticalHeader().setHighlightSections(True)
        self.actors_TableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_27.addWidget(self.actors_TableWidget, 1, 0, 1, 1)

        self.actorsSearch_LineEdit = QLineEdit(self.widget_23)
        self.actorsSearch_LineEdit.setObjectName(u"actorsSearch_LineEdit")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.actorsSearch_LineEdit.sizePolicy().hasHeightForWidth())
        self.actorsSearch_LineEdit.setSizePolicy(sizePolicy12)
        self.actorsSearch_LineEdit.setMinimumSize(QSize(0, 35))
        self.actorsSearch_LineEdit.setMaximumSize(QSize(211, 16777215))
        self.actorsSearch_LineEdit.setFont(font4)
        self.actorsSearch_LineEdit.setFocusPolicy(Qt.ClickFocus)
        self.actorsSearch_LineEdit.setStyleSheet(u"color:white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.actorsSearch_LineEdit.setClearButtonEnabled(True)

        self.gridLayout_27.addWidget(self.actorsSearch_LineEdit, 0, 0, 1, 1)


        self.gridLayout_40.addWidget(self.widget_23, 1, 0, 1, 1)

        self.widget_31 = QWidget(self.actors_Page)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy)
        self.widget_31.setMaximumSize(QSize(300, 16777215))
        self.widget_31.setStyleSheet(u"background:#22577A;")
        self.gridLayout_10 = QGridLayout(self.widget_31)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(15, 20, 15, 20)
        self.gridLayout_46 = QGridLayout()
        self.gridLayout_46.setSpacing(0)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(-1, -1, 0, 10)
        self.label_76 = QLabel(self.widget_31)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(35, 35))
        self.label_76.setFont(font)
        self.label_76.setPixmap(QPixmap(u":/resources/images/options.png"))
        self.label_76.setScaledContents(True)

        self.gridLayout_46.addWidget(self.label_76, 0, 0, 1, 1)

        self.horizontalSpacer_37 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_37, 0, 1, 1, 1)

        self.label_77 = QLabel(self.widget_31)
        self.label_77.setObjectName(u"label_77")
        sizePolicy4.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy4)
        self.label_77.setMaximumSize(QSize(16777215, 16777215))
        self.label_77.setFont(font14)
        self.label_77.setStyleSheet(u"color:white;")

        self.gridLayout_46.addWidget(self.label_77, 0, 2, 1, 1)

        self.horizontalSpacer_38 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_38, 0, 3, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_46, 0, 0, 1, 1)

        self.line_15 = QFrame(self.widget_31)
        self.line_15.setObjectName(u"line_15")
        sizePolicy10.setHeightForWidth(self.line_15.sizePolicy().hasHeightForWidth())
        self.line_15.setSizePolicy(sizePolicy10)
        self.line_15.setMinimumSize(QSize(0, 0))
        self.line_15.setMaximumSize(QSize(16777215, 1))
        self.line_15.setStyleSheet(u"background-color:white;")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_15, 1, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.newActor_Button = QPushButton(self.widget_31)
        self.newActor_Button.setObjectName(u"newActor_Button")
        sizePolicy.setHeightForWidth(self.newActor_Button.sizePolicy().hasHeightForWidth())
        self.newActor_Button.setSizePolicy(sizePolicy)
        self.newActor_Button.setMinimumSize(QSize(0, 0))
        font27 = QFont()
        font27.setFamilies([u"Arial"])
        font27.setPointSize(16)
        font27.setBold(False)
        self.newActor_Button.setFont(font27)
        self.newActor_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.newActor_Button.setFocusPolicy(Qt.NoFocus)
        self.newActor_Button.setStyleSheet(u"background-color: #5AFFA6;\n"
"color: #094646;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        icon20 = QIcon()
        icon20.addFile(u":/resources/images/new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.newActor_Button.setIcon(icon20)
        self.newActor_Button.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.newActor_Button)

        self.editActor_Button = QPushButton(self.widget_31)
        self.editActor_Button.setObjectName(u"editActor_Button")
        sizePolicy.setHeightForWidth(self.editActor_Button.sizePolicy().hasHeightForWidth())
        self.editActor_Button.setSizePolicy(sizePolicy)
        self.editActor_Button.setMinimumSize(QSize(0, 0))
        self.editActor_Button.setFont(font27)
        self.editActor_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.editActor_Button.setFocusPolicy(Qt.NoFocus)
        self.editActor_Button.setStyleSheet(u"background-color: #48F4FF;\n"
"color:#22577A;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        self.editActor_Button.setIcon(icon17)
        self.editActor_Button.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.editActor_Button)

        self.deleteActor_Button = QPushButton(self.widget_31)
        self.deleteActor_Button.setObjectName(u"deleteActor_Button")
        sizePolicy.setHeightForWidth(self.deleteActor_Button.sizePolicy().hasHeightForWidth())
        self.deleteActor_Button.setSizePolicy(sizePolicy)
        self.deleteActor_Button.setMinimumSize(QSize(0, 0))
        self.deleteActor_Button.setFont(font27)
        self.deleteActor_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.deleteActor_Button.setFocusPolicy(Qt.NoFocus)
        self.deleteActor_Button.setStyleSheet(u"background-color: #FF0000;\n"
"color: white;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        icon21 = QIcon()
        icon21.addFile(u":/resources/images/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteActor_Button.setIcon(icon21)
        self.deleteActor_Button.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.deleteActor_Button)


        self.gridLayout_10.addLayout(self.verticalLayout_6, 2, 0, 1, 1)


        self.gridLayout_40.addWidget(self.widget_31, 1, 1, 1, 1)

        self.widget_8 = QWidget(self.actors_Page)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy4.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy4)
        self.widget_8.setMinimumSize(QSize(0, 0))
        self.widget_8.setFont(font23)
        self.widget_8.setStyleSheet(u"background:#22577A;")
        self.gridLayout_8 = QGridLayout(self.widget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(12)
        self.gridLayout_8.setContentsMargins(12, 12, 12, 12)
        self.line_5 = QFrame(self.widget_8)
        self.line_5.setObjectName(u"line_5")
        sizePolicy12.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy12)
        self.line_5.setMinimumSize(QSize(0, 0))
        self.line_5.setMaximumSize(QSize(16777215, 1))
        self.line_5.setStyleSheet(u"background-color:white;")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_8.addWidget(self.line_5, 1, 0, 1, 1)

        self.actorsSummary_TableWidget = QTableWidget(self.widget_8)
        if (self.actorsSummary_TableWidget.columnCount() < 5):
            self.actorsSummary_TableWidget.setColumnCount(5)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font4);
        __qtablewidgetitem39.setBackground(QColor(216, 216, 216));
        self.actorsSummary_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font4);
        __qtablewidgetitem40.setBackground(QColor(217, 217, 217));
        self.actorsSummary_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font24);
        __qtablewidgetitem41.setBackground(QColor(217, 217, 217));
        __qtablewidgetitem41.setIcon(icon19);
        self.actorsSummary_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font4);
        __qtablewidgetitem42.setBackground(QColor(217, 217, 217));
        self.actorsSummary_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font4);
        __qtablewidgetitem43.setBackground(QColor(217, 217, 217));
        self.actorsSummary_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem43)
        if (self.actorsSummary_TableWidget.rowCount() < 4):
            self.actorsSummary_TableWidget.setRowCount(4)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setBackground(QColor(0, 0, 0));
        __qtablewidgetitem44.setForeground(brush10);
        self.actorsSummary_TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem44)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setForeground(brush11);
        self.actorsSummary_TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.actorsSummary_TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.actorsSummary_TableWidget.setVerticalHeaderItem(3, __qtablewidgetitem47)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.NoBrush)
        brush13 = QBrush(QColor(152, 250, 197, 255))
        brush13.setStyle(Qt.SolidPattern)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem48.setFont(font4);
        __qtablewidgetitem48.setBackground(brush13);
        __qtablewidgetitem48.setForeground(brush12);
        self.actorsSummary_TableWidget.setItem(0, 0, __qtablewidgetitem48)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        brush15 = QBrush(QColor(210, 255, 230, 255))
        brush15.setStyle(Qt.SolidPattern)
        font28 = QFont()
        font28.setFamilies([u"Arial"])
        font28.setPointSize(14)
        font28.setBold(False)
        font28.setItalic(False)
        font28.setStrikeOut(False)
        font28.setKerning(True)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem49.setFont(font28);
        __qtablewidgetitem49.setBackground(brush15);
        __qtablewidgetitem49.setForeground(brush14);
        self.actorsSummary_TableWidget.setItem(0, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem50.setFont(font4);
        __qtablewidgetitem50.setBackground(brush15);
        self.actorsSummary_TableWidget.setItem(0, 2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem51.setFont(font4);
        __qtablewidgetitem51.setBackground(brush15);
        self.actorsSummary_TableWidget.setItem(0, 3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem52.setFont(font4);
        __qtablewidgetitem52.setBackground(brush15);
        self.actorsSummary_TableWidget.setItem(0, 4, __qtablewidgetitem52)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.NoBrush)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem53.setFont(font25);
        __qtablewidgetitem53.setBackground(brush5);
        __qtablewidgetitem53.setForeground(brush16);
        self.actorsSummary_TableWidget.setItem(1, 0, __qtablewidgetitem53)
        brush17 = QBrush(QColor(0, 0, 0, 255))
        brush17.setStyle(Qt.NoBrush)
        brush18 = QBrush(QColor(255, 233, 191, 255))
        brush18.setStyle(Qt.SolidPattern)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem54.setFont(font9);
        __qtablewidgetitem54.setBackground(brush18);
        __qtablewidgetitem54.setForeground(brush17);
        self.actorsSummary_TableWidget.setItem(1, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem55.setFont(font4);
        __qtablewidgetitem55.setBackground(brush18);
        self.actorsSummary_TableWidget.setItem(1, 2, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem56.setFont(font4);
        __qtablewidgetitem56.setBackground(brush18);
        self.actorsSummary_TableWidget.setItem(1, 3, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem57.setFont(font4);
        __qtablewidgetitem57.setBackground(brush18);
        self.actorsSummary_TableWidget.setItem(1, 4, __qtablewidgetitem57)
        brush19 = QBrush(QColor(243, 147, 147, 255))
        brush19.setStyle(Qt.SolidPattern)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem58.setFont(font4);
        __qtablewidgetitem58.setBackground(brush19);
        self.actorsSummary_TableWidget.setItem(2, 0, __qtablewidgetitem58)
        brush20 = QBrush(QColor(255, 201, 201, 255))
        brush20.setStyle(Qt.SolidPattern)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem59.setFont(font9);
        __qtablewidgetitem59.setBackground(brush20);
        self.actorsSummary_TableWidget.setItem(2, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem60.setFont(font4);
        __qtablewidgetitem60.setBackground(brush20);
        self.actorsSummary_TableWidget.setItem(2, 2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem61.setFont(font4);
        __qtablewidgetitem61.setBackground(brush20);
        self.actorsSummary_TableWidget.setItem(2, 3, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem62.setFont(font4);
        __qtablewidgetitem62.setBackground(brush20);
        self.actorsSummary_TableWidget.setItem(2, 4, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem63.setFont(font6);
        self.actorsSummary_TableWidget.setItem(3, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem64.setFont(font6);
        self.actorsSummary_TableWidget.setItem(3, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.actorsSummary_TableWidget.setItem(3, 2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.actorsSummary_TableWidget.setItem(3, 3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.actorsSummary_TableWidget.setItem(3, 4, __qtablewidgetitem67)
        self.actorsSummary_TableWidget.setObjectName(u"actorsSummary_TableWidget")
        sizePolicy4.setHeightForWidth(self.actorsSummary_TableWidget.sizePolicy().hasHeightForWidth())
        self.actorsSummary_TableWidget.setSizePolicy(sizePolicy4)
        self.actorsSummary_TableWidget.setMinimumSize(QSize(0, 229))
        self.actorsSummary_TableWidget.setMaximumSize(QSize(16777215, 16777215))
        font29 = QFont()
        font29.setFamilies([u"Arial"])
        font29.setPointSize(15)
        font29.setBold(False)
        font29.setKerning(True)
        self.actorsSummary_TableWidget.setFont(font29)
        self.actorsSummary_TableWidget.viewport().setProperty("cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.actorsSummary_TableWidget.setMouseTracking(False)
        self.actorsSummary_TableWidget.setTabletTracking(False)
        self.actorsSummary_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.actorsSummary_TableWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.actorsSummary_TableWidget.setLayoutDirection(Qt.LeftToRight)
        self.actorsSummary_TableWidget.setStyleSheet(u"QTableWidget{\n"
"    background-color: white;\n"
"    margin: 5px 5px 5px 3px;\n"
"    gridline-color: #9C9C9C; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    height:35px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"     background: #3B4252;\n"
"     width: 20px;\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: white;\n"
"     min-height: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #3B4252;\n"
"     height: 20px;\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: white;\n"
"     min-width: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"QScrollBar"
                        "::sub-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}")
        self.actorsSummary_TableWidget.setFrameShape(QFrame.NoFrame)
        self.actorsSummary_TableWidget.setFrameShadow(QFrame.Raised)
        self.actorsSummary_TableWidget.setLineWidth(0)
        self.actorsSummary_TableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.actorsSummary_TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.actorsSummary_TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.actorsSummary_TableWidget.setAutoScroll(False)
        self.actorsSummary_TableWidget.setAutoScrollMargin(0)
        self.actorsSummary_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.actorsSummary_TableWidget.setTabKeyNavigation(False)
        self.actorsSummary_TableWidget.setProperty("showDropIndicator", False)
        self.actorsSummary_TableWidget.setDragDropOverwriteMode(False)
        self.actorsSummary_TableWidget.setAlternatingRowColors(False)
        self.actorsSummary_TableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.actorsSummary_TableWidget.setTextElideMode(Qt.ElideMiddle)
        self.actorsSummary_TableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.actorsSummary_TableWidget.setShowGrid(True)
        self.actorsSummary_TableWidget.setGridStyle(Qt.SolidLine)
        self.actorsSummary_TableWidget.setSortingEnabled(False)
        self.actorsSummary_TableWidget.setWordWrap(True)
        self.actorsSummary_TableWidget.setCornerButtonEnabled(True)
        self.actorsSummary_TableWidget.horizontalHeader().setVisible(True)
        self.actorsSummary_TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.actorsSummary_TableWidget.horizontalHeader().setMinimumSectionSize(130)
        self.actorsSummary_TableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.actorsSummary_TableWidget.horizontalHeader().setHighlightSections(False)
        self.actorsSummary_TableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.actorsSummary_TableWidget.horizontalHeader().setStretchLastSection(True)
        self.actorsSummary_TableWidget.verticalHeader().setVisible(False)
        self.actorsSummary_TableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.actorsSummary_TableWidget.verticalHeader().setMinimumSectionSize(0)
        self.actorsSummary_TableWidget.verticalHeader().setDefaultSectionSize(45)
        self.actorsSummary_TableWidget.verticalHeader().setHighlightSections(False)
        self.actorsSummary_TableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.actorsSummary_TableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_8.addWidget(self.actorsSummary_TableWidget, 2, 0, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(-1, -1, -1, 0)
        self.label_39 = QLabel(self.widget_8)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(35, 35))
        self.label_39.setFont(font)
        self.label_39.setPixmap(QPixmap(u":/resources/images/summary.png"))
        self.label_39.setScaledContents(True)

        self.gridLayout_25.addWidget(self.label_39, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_12, 0, 1, 1, 1)

        self.label_40 = QLabel(self.widget_8)
        self.label_40.setObjectName(u"label_40")
        sizePolicy4.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy4)
        self.label_40.setMaximumSize(QSize(161, 30))
        self.label_40.setFont(font14)
        self.label_40.setStyleSheet(u"color:white;")

        self.gridLayout_25.addWidget(self.label_40, 0, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_13, 0, 3, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_25, 0, 0, 1, 1)


        self.gridLayout_40.addWidget(self.widget_8, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.actors_Page)
        self.useCases_Page = QWidget()
        self.useCases_Page.setObjectName(u"useCases_Page")
        self.gridLayout_42 = QGridLayout(self.useCases_Page)
        self.gridLayout_42.setSpacing(15)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(15, 15, 15, 15)
        self.widget_10 = QWidget(self.useCases_Page)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setStyleSheet(u"background:#22577A;")
        self.gridLayout_41 = QGridLayout(self.widget_10)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setHorizontalSpacing(0)
        self.gridLayout_41.setVerticalSpacing(12)
        self.gridLayout_41.setContentsMargins(20, 20, 20, 20)
        self.useCasesSearch_LineEdit = QLineEdit(self.widget_10)
        self.useCasesSearch_LineEdit.setObjectName(u"useCasesSearch_LineEdit")
        sizePolicy12.setHeightForWidth(self.useCasesSearch_LineEdit.sizePolicy().hasHeightForWidth())
        self.useCasesSearch_LineEdit.setSizePolicy(sizePolicy12)
        self.useCasesSearch_LineEdit.setMinimumSize(QSize(0, 35))
        self.useCasesSearch_LineEdit.setMaximumSize(QSize(211, 16777215))
        self.useCasesSearch_LineEdit.setFont(font4)
        self.useCasesSearch_LineEdit.setFocusPolicy(Qt.ClickFocus)
        self.useCasesSearch_LineEdit.setStyleSheet(u"color:white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.useCasesSearch_LineEdit.setClearButtonEnabled(True)

        self.gridLayout_41.addWidget(self.useCasesSearch_LineEdit, 0, 0, 1, 1)

        self.useCases_TableWidget = QTableWidget(self.widget_10)
        if (self.useCases_TableWidget.columnCount() < 7):
            self.useCases_TableWidget.setColumnCount(7)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.useCases_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setFont(font4);
        self.useCases_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setFont(font4);
        self.useCases_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setFont(font4);
        self.useCases_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setFont(font4);
        self.useCases_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setFont(font4);
        self.useCases_TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setFont(font4);
        self.useCases_TableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem74)
        self.useCases_TableWidget.setObjectName(u"useCases_TableWidget")
        self.useCases_TableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.useCases_TableWidget.setFont(font7)
        self.useCases_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.useCases_TableWidget.setStyleSheet(u"QTableWidget{\n"
"    border:none;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"    height: 35px;\n"
"}\n"
"\n"
"QTableWidget::Item{\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(0,0,0,0.25);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"     background: #3B4252;\n"
"     width: 20px;\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: white;\n"
"     min-height: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #3B4252;\n"
"     height: 20px;\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: white;\n"
"     min-width: 20px;\n"
"  "
                        "   border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}")
        self.useCases_TableWidget.setFrameShape(QFrame.NoFrame)
        self.useCases_TableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.useCases_TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.useCases_TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.useCases_TableWidget.setAutoScroll(True)
        self.useCases_TableWidget.setAutoScrollMargin(0)
        self.useCases_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.useCases_TableWidget.setTabKeyNavigation(True)
        self.useCases_TableWidget.setProperty("showDropIndicator", False)
        self.useCases_TableWidget.setDragEnabled(False)
        self.useCases_TableWidget.setDragDropOverwriteMode(False)
        self.useCases_TableWidget.setAlternatingRowColors(False)
        self.useCases_TableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.useCases_TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.useCases_TableWidget.setTextElideMode(Qt.ElideRight)
        self.useCases_TableWidget.setShowGrid(False)
        self.useCases_TableWidget.setSortingEnabled(True)
        self.useCases_TableWidget.setWordWrap(True)
        self.useCases_TableWidget.setCornerButtonEnabled(False)
        self.useCases_TableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.useCases_TableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.useCases_TableWidget.horizontalHeader().setHighlightSections(True)
        self.useCases_TableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.useCases_TableWidget.horizontalHeader().setStretchLastSection(False)
        self.useCases_TableWidget.verticalHeader().setVisible(False)
        self.useCases_TableWidget.verticalHeader().setMinimumSectionSize(0)
        self.useCases_TableWidget.verticalHeader().setDefaultSectionSize(45)
        self.useCases_TableWidget.verticalHeader().setHighlightSections(True)

        self.gridLayout_41.addWidget(self.useCases_TableWidget, 1, 0, 1, 1)


        self.gridLayout_42.addWidget(self.widget_10, 1, 0, 1, 1)

        self.widget_24 = QWidget(self.useCases_Page)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy)
        self.widget_24.setMaximumSize(QSize(300, 16777215))
        self.widget_24.setStyleSheet(u"background:#22577A;")
        self.gridLayout_11 = QGridLayout(self.widget_24)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(15, 20, 15, 20)
        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(-1, -1, 0, 10)
        self.label_61 = QLabel(self.widget_24)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(35, 35))
        self.label_61.setFont(font)
        self.label_61.setPixmap(QPixmap(u":/resources/images/options.png"))
        self.label_61.setScaledContents(True)

        self.gridLayout_30.addWidget(self.label_61, 0, 0, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_26, 0, 1, 1, 1)

        self.label_62 = QLabel(self.widget_24)
        self.label_62.setObjectName(u"label_62")
        sizePolicy4.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy4)
        self.label_62.setMaximumSize(QSize(16777215, 16777215))
        self.label_62.setFont(font14)
        self.label_62.setStyleSheet(u"color:white;")

        self.gridLayout_30.addWidget(self.label_62, 0, 2, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_27, 0, 3, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_30, 0, 0, 1, 1)

        self.line_10 = QFrame(self.widget_24)
        self.line_10.setObjectName(u"line_10")
        sizePolicy10.setHeightForWidth(self.line_10.sizePolicy().hasHeightForWidth())
        self.line_10.setSizePolicy(sizePolicy10)
        self.line_10.setMinimumSize(QSize(0, 0))
        self.line_10.setMaximumSize(QSize(16777215, 1))
        self.line_10.setStyleSheet(u"background-color:white;")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line_10, 1, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 20, 0, 0)
        self.newUseCase_Button = QPushButton(self.widget_24)
        self.newUseCase_Button.setObjectName(u"newUseCase_Button")
        sizePolicy.setHeightForWidth(self.newUseCase_Button.sizePolicy().hasHeightForWidth())
        self.newUseCase_Button.setSizePolicy(sizePolicy)
        self.newUseCase_Button.setFont(font27)
        self.newUseCase_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.newUseCase_Button.setFocusPolicy(Qt.NoFocus)
        self.newUseCase_Button.setStyleSheet(u"background-color: #5AFFA6;\n"
"color: #094646;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        self.newUseCase_Button.setIcon(icon20)
        self.newUseCase_Button.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.newUseCase_Button)

        self.editUseCase_Button = QPushButton(self.widget_24)
        self.editUseCase_Button.setObjectName(u"editUseCase_Button")
        sizePolicy.setHeightForWidth(self.editUseCase_Button.sizePolicy().hasHeightForWidth())
        self.editUseCase_Button.setSizePolicy(sizePolicy)
        self.editUseCase_Button.setFont(font27)
        self.editUseCase_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.editUseCase_Button.setFocusPolicy(Qt.NoFocus)
        self.editUseCase_Button.setStyleSheet(u"background-color: #48F4FF;\n"
"color:#22577A;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        self.editUseCase_Button.setIcon(icon17)
        self.editUseCase_Button.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.editUseCase_Button)

        self.deleteUseCase_Button = QPushButton(self.widget_24)
        self.deleteUseCase_Button.setObjectName(u"deleteUseCase_Button")
        sizePolicy.setHeightForWidth(self.deleteUseCase_Button.sizePolicy().hasHeightForWidth())
        self.deleteUseCase_Button.setSizePolicy(sizePolicy)
        self.deleteUseCase_Button.setFont(font27)
        self.deleteUseCase_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.deleteUseCase_Button.setFocusPolicy(Qt.NoFocus)
        self.deleteUseCase_Button.setStyleSheet(u"background-color: #FF0000;\n"
"color: white;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        self.deleteUseCase_Button.setIcon(icon21)
        self.deleteUseCase_Button.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.deleteUseCase_Button)


        self.gridLayout_11.addLayout(self.verticalLayout_7, 2, 0, 1, 1)


        self.gridLayout_42.addWidget(self.widget_24, 1, 1, 1, 1)

        self.label_5 = QLabel(self.useCases_Page)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font14)
        self.label_5.setStyleSheet(u"color:white;")
        self.label_5.setIndent(0)

        self.gridLayout_42.addWidget(self.label_5, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.useCases_Page)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy5.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy5)
        self.widget_9.setMinimumSize(QSize(0, 314))
        self.widget_9.setFont(font23)
        self.widget_9.setStyleSheet(u"background:#22577A;")
        self.gridLayout_9 = QGridLayout(self.widget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setVerticalSpacing(12)
        self.gridLayout_9.setContentsMargins(12, 12, 12, 12)
        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_41 = QLabel(self.widget_9)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(35, 35))
        self.label_41.setFont(font)
        self.label_41.setPixmap(QPixmap(u":/resources/images/summary.png"))
        self.label_41.setScaledContents(True)

        self.gridLayout_26.addWidget(self.label_41, 0, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_18, 0, 1, 1, 1)

        self.label_42 = QLabel(self.widget_9)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(161, 30))
        self.label_42.setFont(font14)
        self.label_42.setStyleSheet(u"color:white;")

        self.gridLayout_26.addWidget(self.label_42, 0, 2, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_19, 0, 3, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_26, 0, 0, 1, 1)

        self.line_6 = QFrame(self.widget_9)
        self.line_6.setObjectName(u"line_6")
        sizePolicy12.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy12)
        self.line_6.setMinimumSize(QSize(0, 0))
        self.line_6.setMaximumSize(QSize(16777215, 1))
        self.line_6.setStyleSheet(u"background-color:white;")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_6, 1, 0, 1, 1)

        self.useCasesSummary_TableWidget = QTableWidget(self.widget_9)
        if (self.useCasesSummary_TableWidget.columnCount() < 5):
            self.useCasesSummary_TableWidget.setColumnCount(5)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setFont(font4);
        __qtablewidgetitem75.setBackground(QColor(216, 216, 216));
        self.useCasesSummary_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setFont(font4);
        __qtablewidgetitem76.setBackground(QColor(217, 217, 217));
        self.useCasesSummary_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setFont(font24);
        __qtablewidgetitem77.setBackground(QColor(217, 217, 217));
        __qtablewidgetitem77.setIcon(icon19);
        self.useCasesSummary_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setFont(font4);
        __qtablewidgetitem78.setBackground(QColor(217, 217, 217));
        self.useCasesSummary_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setFont(font4);
        __qtablewidgetitem79.setBackground(QColor(217, 217, 217));
        self.useCasesSummary_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem79)
        if (self.useCasesSummary_TableWidget.rowCount() < 4):
            self.useCasesSummary_TableWidget.setRowCount(4)
        brush21 = QBrush(QColor(0, 0, 0, 255))
        brush21.setStyle(Qt.NoBrush)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setBackground(QColor(0, 0, 0));
        __qtablewidgetitem80.setForeground(brush21);
        self.useCasesSummary_TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem80)
        brush22 = QBrush(QColor(0, 0, 0, 255))
        brush22.setStyle(Qt.NoBrush)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setForeground(brush22);
        self.useCasesSummary_TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.useCasesSummary_TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.useCasesSummary_TableWidget.setVerticalHeaderItem(3, __qtablewidgetitem83)
        brush23 = QBrush(QColor(0, 0, 0, 255))
        brush23.setStyle(Qt.NoBrush)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem84.setFont(font4);
        __qtablewidgetitem84.setBackground(brush13);
        __qtablewidgetitem84.setForeground(brush23);
        self.useCasesSummary_TableWidget.setItem(0, 0, __qtablewidgetitem84)
        brush24 = QBrush(QColor(0, 0, 0, 255))
        brush24.setStyle(Qt.NoBrush)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem85.setFont(font28);
        __qtablewidgetitem85.setBackground(brush15);
        __qtablewidgetitem85.setForeground(brush24);
        self.useCasesSummary_TableWidget.setItem(0, 1, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem86.setFont(font4);
        __qtablewidgetitem86.setBackground(brush15);
        self.useCasesSummary_TableWidget.setItem(0, 2, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem87.setFont(font4);
        __qtablewidgetitem87.setBackground(brush15);
        self.useCasesSummary_TableWidget.setItem(0, 3, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem88.setFont(font4);
        __qtablewidgetitem88.setBackground(brush15);
        self.useCasesSummary_TableWidget.setItem(0, 4, __qtablewidgetitem88)
        brush25 = QBrush(QColor(0, 0, 0, 255))
        brush25.setStyle(Qt.NoBrush)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem89.setFont(font25);
        __qtablewidgetitem89.setBackground(brush5);
        __qtablewidgetitem89.setForeground(brush25);
        self.useCasesSummary_TableWidget.setItem(1, 0, __qtablewidgetitem89)
        brush26 = QBrush(QColor(0, 0, 0, 255))
        brush26.setStyle(Qt.NoBrush)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem90.setFont(font9);
        __qtablewidgetitem90.setBackground(brush18);
        __qtablewidgetitem90.setForeground(brush26);
        self.useCasesSummary_TableWidget.setItem(1, 1, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem91.setFont(font4);
        __qtablewidgetitem91.setBackground(brush18);
        self.useCasesSummary_TableWidget.setItem(1, 2, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem92.setFont(font4);
        __qtablewidgetitem92.setBackground(brush18);
        self.useCasesSummary_TableWidget.setItem(1, 3, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem93.setFont(font4);
        __qtablewidgetitem93.setBackground(brush18);
        self.useCasesSummary_TableWidget.setItem(1, 4, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem94.setFont(font4);
        __qtablewidgetitem94.setBackground(brush19);
        self.useCasesSummary_TableWidget.setItem(2, 0, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem95.setFont(font9);
        __qtablewidgetitem95.setBackground(brush20);
        self.useCasesSummary_TableWidget.setItem(2, 1, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem96.setFont(font4);
        __qtablewidgetitem96.setBackground(brush20);
        self.useCasesSummary_TableWidget.setItem(2, 2, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem97.setFont(font4);
        __qtablewidgetitem97.setBackground(brush20);
        self.useCasesSummary_TableWidget.setItem(2, 3, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem98.setFont(font4);
        __qtablewidgetitem98.setBackground(brush20);
        self.useCasesSummary_TableWidget.setItem(2, 4, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem99.setFont(font6);
        self.useCasesSummary_TableWidget.setItem(3, 0, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem100.setFont(font6);
        self.useCasesSummary_TableWidget.setItem(3, 1, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.useCasesSummary_TableWidget.setItem(3, 2, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        self.useCasesSummary_TableWidget.setItem(3, 3, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignCenter);
        self.useCasesSummary_TableWidget.setItem(3, 4, __qtablewidgetitem103)
        self.useCasesSummary_TableWidget.setObjectName(u"useCasesSummary_TableWidget")
        sizePolicy7.setHeightForWidth(self.useCasesSummary_TableWidget.sizePolicy().hasHeightForWidth())
        self.useCasesSummary_TableWidget.setSizePolicy(sizePolicy7)
        self.useCasesSummary_TableWidget.setMinimumSize(QSize(0, 229))
        self.useCasesSummary_TableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.useCasesSummary_TableWidget.setFont(font29)
        self.useCasesSummary_TableWidget.viewport().setProperty("cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.useCasesSummary_TableWidget.setMouseTracking(False)
        self.useCasesSummary_TableWidget.setTabletTracking(False)
        self.useCasesSummary_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.useCasesSummary_TableWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.useCasesSummary_TableWidget.setLayoutDirection(Qt.LeftToRight)
        self.useCasesSummary_TableWidget.setStyleSheet(u"QTableWidget{\n"
"    background-color: white;\n"
"    margin: 5px 5px 5px 3px;\n"
"    gridline-color: #9C9C9C; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    height:35px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"     background: #3B4252;\n"
"     width: 20px;\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: white;\n"
"     min-height: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #3B4252;\n"
"     height: 20px;\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: white;\n"
"     min-width: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"QScrollBar"
                        "::sub-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}")
        self.useCasesSummary_TableWidget.setFrameShape(QFrame.NoFrame)
        self.useCasesSummary_TableWidget.setFrameShadow(QFrame.Raised)
        self.useCasesSummary_TableWidget.setLineWidth(0)
        self.useCasesSummary_TableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.useCasesSummary_TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.useCasesSummary_TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.useCasesSummary_TableWidget.setAutoScroll(False)
        self.useCasesSummary_TableWidget.setAutoScrollMargin(0)
        self.useCasesSummary_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.useCasesSummary_TableWidget.setTabKeyNavigation(False)
        self.useCasesSummary_TableWidget.setProperty("showDropIndicator", False)
        self.useCasesSummary_TableWidget.setDragDropOverwriteMode(False)
        self.useCasesSummary_TableWidget.setAlternatingRowColors(False)
        self.useCasesSummary_TableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.useCasesSummary_TableWidget.setTextElideMode(Qt.ElideMiddle)
        self.useCasesSummary_TableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.useCasesSummary_TableWidget.setShowGrid(True)
        self.useCasesSummary_TableWidget.setGridStyle(Qt.SolidLine)
        self.useCasesSummary_TableWidget.setSortingEnabled(False)
        self.useCasesSummary_TableWidget.setWordWrap(True)
        self.useCasesSummary_TableWidget.setCornerButtonEnabled(True)
        self.useCasesSummary_TableWidget.horizontalHeader().setVisible(True)
        self.useCasesSummary_TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.useCasesSummary_TableWidget.horizontalHeader().setMinimumSectionSize(130)
        self.useCasesSummary_TableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.useCasesSummary_TableWidget.horizontalHeader().setHighlightSections(False)
        self.useCasesSummary_TableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.useCasesSummary_TableWidget.horizontalHeader().setStretchLastSection(True)
        self.useCasesSummary_TableWidget.verticalHeader().setVisible(False)
        self.useCasesSummary_TableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.useCasesSummary_TableWidget.verticalHeader().setMinimumSectionSize(0)
        self.useCasesSummary_TableWidget.verticalHeader().setDefaultSectionSize(45)
        self.useCasesSummary_TableWidget.verticalHeader().setHighlightSections(False)
        self.useCasesSummary_TableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.useCasesSummary_TableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_9.addWidget(self.useCasesSummary_TableWidget, 2, 0, 1, 1)


        self.gridLayout_42.addWidget(self.widget_9, 2, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.useCases_Page)
        self.technicalFactors_Page = QWidget()
        self.technicalFactors_Page.setObjectName(u"technicalFactors_Page")
        self.gridLayout_43 = QGridLayout(self.technicalFactors_Page)
        self.gridLayout_43.setSpacing(15)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(15, 15, 15, 15)
        self.label_4 = QLabel(self.technicalFactors_Page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font14)
        self.label_4.setStyleSheet(u"color:white;")

        self.gridLayout_43.addWidget(self.label_4, 0, 0, 1, 1)

        self.widget_26 = QWidget(self.technicalFactors_Page)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy)
        self.widget_26.setMaximumSize(QSize(16777215, 16777215))
        self.widget_26.setStyleSheet(u"background:#22577A;\n"
"color:white;")
        self.gridLayout_44 = QGridLayout(self.widget_26)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.technicalFactors_TableWidget = QTableWidget(self.widget_26)
        if (self.technicalFactors_TableWidget.columnCount() < 7):
            self.technicalFactors_TableWidget.setColumnCount(7)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setFont(font9);
        self.technicalFactors_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setFont(font9);
        self.technicalFactors_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setFont(font9);
        self.technicalFactors_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setFont(font9);
        self.technicalFactors_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setFont(font9);
        self.technicalFactors_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setFont(font9);
        self.technicalFactors_TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setFont(font9);
        self.technicalFactors_TableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem110)
        if (self.technicalFactors_TableWidget.rowCount() < 14):
            self.technicalFactors_TableWidget.setRowCount(14)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(3, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(4, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(5, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(6, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(7, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(8, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(9, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(10, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(11, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(12, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.technicalFactors_TableWidget.setVerticalHeaderItem(13, __qtablewidgetitem124)
        brush27 = QBrush(QColor(0, 0, 0, 255))
        brush27.setStyle(Qt.NoBrush)
        brush28 = QBrush(QColor(222, 255, 250, 255))
        brush28.setStyle(Qt.SolidPattern)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem125.setBackground(brush28);
        __qtablewidgetitem125.setForeground(brush27);
        self.technicalFactors_TableWidget.setItem(0, 1, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem126.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(0, 2, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem127.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(0, 3, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem128.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(0, 4, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        __qtablewidgetitem129.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem129.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(0, 5, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        __qtablewidgetitem130.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem130.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(0, 6, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        __qtablewidgetitem131.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem131.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(1, 1, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        __qtablewidgetitem132.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem132.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(1, 2, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        __qtablewidgetitem133.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem133.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(1, 3, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        __qtablewidgetitem134.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem134.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(1, 4, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        __qtablewidgetitem135.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem135.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(1, 5, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        __qtablewidgetitem136.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem136.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(1, 6, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        __qtablewidgetitem137.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem137.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(2, 1, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        __qtablewidgetitem138.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem138.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(2, 2, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        __qtablewidgetitem139.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem139.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(2, 3, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        __qtablewidgetitem140.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem140.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(2, 4, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        __qtablewidgetitem141.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem141.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(2, 5, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        __qtablewidgetitem142.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem142.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(2, 6, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        __qtablewidgetitem143.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem143.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(3, 1, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        __qtablewidgetitem144.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem144.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(3, 2, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        __qtablewidgetitem145.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem145.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(3, 3, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        __qtablewidgetitem146.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem146.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(3, 4, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        __qtablewidgetitem147.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem147.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(3, 5, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        __qtablewidgetitem148.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem148.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(3, 6, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        __qtablewidgetitem149.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem149.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(4, 1, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        __qtablewidgetitem150.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem150.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(4, 2, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        __qtablewidgetitem151.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem151.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(4, 3, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        __qtablewidgetitem152.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem152.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(4, 4, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        __qtablewidgetitem153.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem153.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(4, 5, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        __qtablewidgetitem154.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem154.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(4, 6, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        __qtablewidgetitem155.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem155.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(5, 1, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        __qtablewidgetitem156.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem156.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(5, 2, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        __qtablewidgetitem157.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem157.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(5, 3, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        __qtablewidgetitem158.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem158.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(5, 4, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        __qtablewidgetitem159.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem159.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(5, 5, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        __qtablewidgetitem160.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem160.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(5, 6, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        __qtablewidgetitem161.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem161.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(6, 1, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        __qtablewidgetitem162.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem162.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(6, 2, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        __qtablewidgetitem163.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem163.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(6, 3, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        __qtablewidgetitem164.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem164.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(6, 4, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        __qtablewidgetitem165.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem165.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(6, 5, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        __qtablewidgetitem166.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem166.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(6, 6, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        __qtablewidgetitem167.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem167.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(7, 1, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        __qtablewidgetitem168.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem168.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(7, 2, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        __qtablewidgetitem169.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem169.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(7, 3, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        __qtablewidgetitem170.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem170.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(7, 4, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        __qtablewidgetitem171.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem171.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(7, 5, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        __qtablewidgetitem172.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem172.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(7, 6, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        __qtablewidgetitem173.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem173.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(8, 1, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        __qtablewidgetitem174.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem174.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(8, 2, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        __qtablewidgetitem175.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem175.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(8, 3, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        __qtablewidgetitem176.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem176.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(8, 4, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        __qtablewidgetitem177.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem177.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(8, 5, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        __qtablewidgetitem178.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem178.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(8, 6, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        __qtablewidgetitem179.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem179.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(9, 1, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        __qtablewidgetitem180.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem180.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(9, 2, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        __qtablewidgetitem181.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem181.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(9, 3, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        __qtablewidgetitem182.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem182.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(9, 4, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        __qtablewidgetitem183.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem183.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(9, 5, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        __qtablewidgetitem184.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem184.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(9, 6, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        __qtablewidgetitem185.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem185.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(10, 1, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        __qtablewidgetitem186.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem186.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(10, 2, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        __qtablewidgetitem187.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem187.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(10, 3, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        __qtablewidgetitem188.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem188.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(10, 4, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        __qtablewidgetitem189.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem189.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(10, 5, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        __qtablewidgetitem190.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem190.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(10, 6, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        __qtablewidgetitem191.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem191.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(11, 1, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        __qtablewidgetitem192.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem192.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(11, 2, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        __qtablewidgetitem193.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem193.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(11, 3, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        __qtablewidgetitem194.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem194.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(11, 4, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        __qtablewidgetitem195.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem195.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(11, 5, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        __qtablewidgetitem196.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem196.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(11, 6, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        __qtablewidgetitem197.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem197.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(12, 1, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        __qtablewidgetitem198.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem198.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(12, 2, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        __qtablewidgetitem199.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem199.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(12, 3, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        __qtablewidgetitem200.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem200.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(12, 4, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        __qtablewidgetitem201.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem201.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(12, 5, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        __qtablewidgetitem202.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem202.setBackground(brush28);
        self.technicalFactors_TableWidget.setItem(12, 6, __qtablewidgetitem202)
        brush29 = QBrush(QColor(35, 202, 178, 255))
        brush29.setStyle(Qt.SolidPattern)
        __qtablewidgetitem203 = QTableWidgetItem()
        __qtablewidgetitem203.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem203.setBackground(brush29);
        self.technicalFactors_TableWidget.setItem(13, 0, __qtablewidgetitem203)
        self.technicalFactors_TableWidget.setObjectName(u"technicalFactors_TableWidget")
        sizePolicy.setHeightForWidth(self.technicalFactors_TableWidget.sizePolicy().hasHeightForWidth())
        self.technicalFactors_TableWidget.setSizePolicy(sizePolicy)
        self.technicalFactors_TableWidget.setMinimumSize(QSize(0, 0))
        self.technicalFactors_TableWidget.setSizeIncrement(QSize(0, 0))
        self.technicalFactors_TableWidget.setBaseSize(QSize(0, -1))
        font30 = QFont()
        font30.setFamilies([u"Arial"])
        font30.setPointSize(14)
        font30.setBold(False)
        font30.setHintingPreference(QFont.PreferDefaultHinting)
        self.technicalFactors_TableWidget.setFont(font30)
        self.technicalFactors_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.technicalFactors_TableWidget.setLayoutDirection(Qt.LeftToRight)
        self.technicalFactors_TableWidget.setStyleSheet(u"QTableView{\n"
"    border: 1px solid  #22577A;\n"
"}\n"
"QHeaderView::section{\n"
"    background: #51EDC6;\n"
"    padding: 3px 5px 3px 5px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTableWidget::Item{\n"
"    padding: 0px ;\n"
"    color: black;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"	image: url(:/resources/images/blackDownArrow.png); \n"
"}\n"
"QHeaderView::up-arrow {\n"
"	image: url(:/resources/images/blackUpArrow.png);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"     background: #3B4252;\n"
"     width: 20px;\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: white;\n"
"     min-height: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #3B4252;\n"
"     height: 20px;\n"
"     margin: 3px 0px 3px 0"
                        "px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: white;\n"
"     min-width: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"")
        self.technicalFactors_TableWidget.setFrameShape(QFrame.NoFrame)
        self.technicalFactors_TableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.technicalFactors_TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.technicalFactors_TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.technicalFactors_TableWidget.setAutoScroll(False)
        self.technicalFactors_TableWidget.setAutoScrollMargin(100)
        self.technicalFactors_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.technicalFactors_TableWidget.setTabKeyNavigation(True)
        self.technicalFactors_TableWidget.setProperty("showDropIndicator", False)
        self.technicalFactors_TableWidget.setDragEnabled(False)
        self.technicalFactors_TableWidget.setDragDropOverwriteMode(False)
        self.technicalFactors_TableWidget.setAlternatingRowColors(False)
        self.technicalFactors_TableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.technicalFactors_TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.technicalFactors_TableWidget.setTextElideMode(Qt.ElideRight)
        self.technicalFactors_TableWidget.setShowGrid(True)
        self.technicalFactors_TableWidget.setGridStyle(Qt.SolidLine)
        self.technicalFactors_TableWidget.setSortingEnabled(True)
        self.technicalFactors_TableWidget.setWordWrap(True)
        self.technicalFactors_TableWidget.setCornerButtonEnabled(False)
        self.technicalFactors_TableWidget.setRowCount(14)
        self.technicalFactors_TableWidget.horizontalHeader().setVisible(True)
        self.technicalFactors_TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.technicalFactors_TableWidget.horizontalHeader().setMinimumSectionSize(90)
        self.technicalFactors_TableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.technicalFactors_TableWidget.horizontalHeader().setHighlightSections(True)
        self.technicalFactors_TableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.technicalFactors_TableWidget.horizontalHeader().setStretchLastSection(False)
        self.technicalFactors_TableWidget.verticalHeader().setVisible(False)
        self.technicalFactors_TableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.technicalFactors_TableWidget.verticalHeader().setMinimumSectionSize(0)
        self.technicalFactors_TableWidget.verticalHeader().setDefaultSectionSize(0)
        self.technicalFactors_TableWidget.verticalHeader().setHighlightSections(True)
        self.technicalFactors_TableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.technicalFactors_TableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_44.addWidget(self.technicalFactors_TableWidget, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.widget_26, 1, 0, 2, 1)

        self.widget_25 = QWidget(self.technicalFactors_Page)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy9.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy9)
        self.widget_25.setMaximumSize(QSize(470, 16777215))
        self.widget_25.setStyleSheet(u"background:#22577A;\n"
"color:white;")
        self.gridLayout_18 = QGridLayout(self.widget_25)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(0)
        self.gridLayout_18.setVerticalSpacing(10)
        self.gridLayout_18.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cancelTechnicalFactor_Button = QPushButton(self.widget_25)
        self.cancelTechnicalFactor_Button.setObjectName(u"cancelTechnicalFactor_Button")
        sizePolicy4.setHeightForWidth(self.cancelTechnicalFactor_Button.sizePolicy().hasHeightForWidth())
        self.cancelTechnicalFactor_Button.setSizePolicy(sizePolicy4)
        self.cancelTechnicalFactor_Button.setFont(font15)
        self.cancelTechnicalFactor_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancelTechnicalFactor_Button.setFocusPolicy(Qt.NoFocus)
        self.cancelTechnicalFactor_Button.setStyleSheet(u"background-color: #FF0000;\n"
"color: white;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        icon22 = QIcon()
        icon22.addFile(u":/resources/images/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancelTechnicalFactor_Button.setIcon(icon22)
        self.cancelTechnicalFactor_Button.setIconSize(QSize(22, 23))

        self.horizontalLayout_4.addWidget(self.cancelTechnicalFactor_Button)

        self.saveTechnicalFactor_Button = QPushButton(self.widget_25)
        self.saveTechnicalFactor_Button.setObjectName(u"saveTechnicalFactor_Button")
        sizePolicy4.setHeightForWidth(self.saveTechnicalFactor_Button.sizePolicy().hasHeightForWidth())
        self.saveTechnicalFactor_Button.setSizePolicy(sizePolicy4)
        self.saveTechnicalFactor_Button.setFont(font15)
        self.saveTechnicalFactor_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.saveTechnicalFactor_Button.setFocusPolicy(Qt.NoFocus)
        self.saveTechnicalFactor_Button.setStyleSheet(u"background-color: #5AFFA6;\n"
"color: #094646;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        icon23 = QIcon()
        icon23.addFile(u":/resources/images/saveFactors.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveTechnicalFactor_Button.setIcon(icon23)
        self.saveTechnicalFactor_Button.setIconSize(QSize(22, 22))

        self.horizontalLayout_4.addWidget(self.saveTechnicalFactor_Button)


        self.gridLayout_18.addLayout(self.horizontalLayout_4, 8, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(39)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 8, 0, -1)
        self.label_6 = QLabel(self.widget_25)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font18)
        self.label_6.setIndent(0)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.technicalFactorsFactor_ComboBox = QComboBox(self.widget_25)
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.addItem("")
        self.technicalFactorsFactor_ComboBox.setObjectName(u"technicalFactorsFactor_ComboBox")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.technicalFactorsFactor_ComboBox.sizePolicy().hasHeightForWidth())
        self.technicalFactorsFactor_ComboBox.setSizePolicy(sizePolicy13)
        self.technicalFactorsFactor_ComboBox.setMinimumSize(QSize(0, 0))
        self.technicalFactorsFactor_ComboBox.setFont(font23)
        self.technicalFactorsFactor_ComboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.technicalFactorsFactor_ComboBox.setFocusPolicy(Qt.WheelFocus)
        self.technicalFactorsFactor_ComboBox.setContextMenuPolicy(Qt.NoContextMenu)
        self.technicalFactorsFactor_ComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    color:black;\n"
"    combobox-popup: 0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #E6E6E6;\n"
"    selection-color: black;\n"
"    color:black;\n"
"}")
        self.technicalFactorsFactor_ComboBox.setMaxVisibleItems(14)
        self.technicalFactorsFactor_ComboBox.setMaxCount(14)
        self.technicalFactorsFactor_ComboBox.setInsertPolicy(QComboBox.NoInsert)
        self.technicalFactorsFactor_ComboBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.technicalFactorsFactor_ComboBox.setMinimumContentsLength(0)
        self.technicalFactorsFactor_ComboBox.setIconSize(QSize(10, 10))
        self.technicalFactorsFactor_ComboBox.setFrame(False)

        self.horizontalLayout_5.addWidget(self.technicalFactorsFactor_ComboBox)


        self.gridLayout_18.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.widget_25)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font18)
        self.label_8.setIndent(0)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, 0, 10, -1)
        self.technicalFactors_RadioButton_0 = QRadioButton(self.widget_25)
        self.technicalFactors_RadioButton_0.setObjectName(u"technicalFactors_RadioButton_0")
        sizePolicy13.setHeightForWidth(self.technicalFactors_RadioButton_0.sizePolicy().hasHeightForWidth())
        self.technicalFactors_RadioButton_0.setSizePolicy(sizePolicy13)
        font31 = QFont()
        font31.setFamilies([u"Arial"])
        font31.setPointSize(12)
        self.technicalFactors_RadioButton_0.setFont(font31)
        self.technicalFactors_RadioButton_0.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.technicalFactors_RadioButton_0.setFocusPolicy(Qt.WheelFocus)
        self.technicalFactors_RadioButton_0.setCheckable(True)
        self.technicalFactors_RadioButton_0.setAutoRepeat(False)

        self.horizontalLayout_12.addWidget(self.technicalFactors_RadioButton_0)

        self.technicalFactors_RadioButton_1 = QRadioButton(self.widget_25)
        self.technicalFactors_RadioButton_1.setObjectName(u"technicalFactors_RadioButton_1")
        sizePolicy13.setHeightForWidth(self.technicalFactors_RadioButton_1.sizePolicy().hasHeightForWidth())
        self.technicalFactors_RadioButton_1.setSizePolicy(sizePolicy13)
        self.technicalFactors_RadioButton_1.setFont(font31)
        self.technicalFactors_RadioButton_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.technicalFactors_RadioButton_1.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_12.addWidget(self.technicalFactors_RadioButton_1)

        self.technicalFactors_RadioButton_2 = QRadioButton(self.widget_25)
        self.technicalFactors_RadioButton_2.setObjectName(u"technicalFactors_RadioButton_2")
        sizePolicy13.setHeightForWidth(self.technicalFactors_RadioButton_2.sizePolicy().hasHeightForWidth())
        self.technicalFactors_RadioButton_2.setSizePolicy(sizePolicy13)
        self.technicalFactors_RadioButton_2.setFont(font31)
        self.technicalFactors_RadioButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.technicalFactors_RadioButton_2.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_12.addWidget(self.technicalFactors_RadioButton_2)

        self.technicalFactors_RadioButton_3 = QRadioButton(self.widget_25)
        self.technicalFactors_RadioButton_3.setObjectName(u"technicalFactors_RadioButton_3")
        sizePolicy13.setHeightForWidth(self.technicalFactors_RadioButton_3.sizePolicy().hasHeightForWidth())
        self.technicalFactors_RadioButton_3.setSizePolicy(sizePolicy13)
        self.technicalFactors_RadioButton_3.setFont(font31)
        self.technicalFactors_RadioButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.technicalFactors_RadioButton_3.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_12.addWidget(self.technicalFactors_RadioButton_3)

        self.technicalFactors_RadioButton_4 = QRadioButton(self.widget_25)
        self.technicalFactors_RadioButton_4.setObjectName(u"technicalFactors_RadioButton_4")
        sizePolicy13.setHeightForWidth(self.technicalFactors_RadioButton_4.sizePolicy().hasHeightForWidth())
        self.technicalFactors_RadioButton_4.setSizePolicy(sizePolicy13)
        self.technicalFactors_RadioButton_4.setFont(font31)
        self.technicalFactors_RadioButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.technicalFactors_RadioButton_4.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_12.addWidget(self.technicalFactors_RadioButton_4)

        self.technicalFactors_RadioButton_5 = QRadioButton(self.widget_25)
        self.technicalFactors_RadioButton_5.setObjectName(u"technicalFactors_RadioButton_5")
        sizePolicy13.setHeightForWidth(self.technicalFactors_RadioButton_5.sizePolicy().hasHeightForWidth())
        self.technicalFactors_RadioButton_5.setSizePolicy(sizePolicy13)
        self.technicalFactors_RadioButton_5.setFont(font31)
        self.technicalFactors_RadioButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.technicalFactors_RadioButton_5.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_12.addWidget(self.technicalFactors_RadioButton_5)

        self.technicalFactorsInfo_Label = QLabel(self.widget_25)
        self.technicalFactorsInfo_Label.setObjectName(u"technicalFactorsInfo_Label")
        self.technicalFactorsInfo_Label.setMaximumSize(QSize(25, 25))
        self.technicalFactorsInfo_Label.setFont(font31)
        self.technicalFactorsInfo_Label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.technicalFactorsInfo_Label.setMouseTracking(False)
        self.technicalFactorsInfo_Label.setToolTipDuration(-1)
        self.technicalFactorsInfo_Label.setStyleSheet(u"QToolTip{\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-family: 'Arial'; \n"
"    font-size: 12px;\n"
"    padding: 8px;\n"
"}")
        self.technicalFactorsInfo_Label.setPixmap(QPixmap(u":/resources/images/helpTooltip.png"))
        self.technicalFactorsInfo_Label.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.technicalFactorsInfo_Label)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)


        self.gridLayout_18.addLayout(self.horizontalLayout_11, 3, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.label_9 = QLabel(self.widget_25)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font18)

        self.verticalLayout_8.addWidget(self.label_9)

        self.technicalFactorsComment_PlainTextEdit = QPlainTextEdit(self.widget_25)
        self.technicalFactorsComment_PlainTextEdit.setObjectName(u"technicalFactorsComment_PlainTextEdit")
        sizePolicy4.setHeightForWidth(self.technicalFactorsComment_PlainTextEdit.sizePolicy().hasHeightForWidth())
        self.technicalFactorsComment_PlainTextEdit.setSizePolicy(sizePolicy4)
        self.technicalFactorsComment_PlainTextEdit.setMinimumSize(QSize(0, 0))
        self.technicalFactorsComment_PlainTextEdit.setMaximumSize(QSize(16777215, 16777215))
        self.technicalFactorsComment_PlainTextEdit.setFont(font31)
        self.technicalFactorsComment_PlainTextEdit.setFocusPolicy(Qt.WheelFocus)
        self.technicalFactorsComment_PlainTextEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.technicalFactorsComment_PlainTextEdit.setAcceptDrops(False)
        self.technicalFactorsComment_PlainTextEdit.setStyleSheet(u"background:white;\n"
"color:black;")
        self.technicalFactorsComment_PlainTextEdit.setFrameShape(QFrame.NoFrame)
        self.technicalFactorsComment_PlainTextEdit.setFrameShadow(QFrame.Plain)
        self.technicalFactorsComment_PlainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.technicalFactorsComment_PlainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.technicalFactorsComment_PlainTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.technicalFactorsComment_PlainTextEdit.setTabChangesFocus(True)
        self.technicalFactorsComment_PlainTextEdit.setTabStopDistance(80.000000000000000)
        self.technicalFactorsComment_PlainTextEdit.setCursorWidth(1)

        self.verticalLayout_8.addWidget(self.technicalFactorsComment_PlainTextEdit)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_7)

        self.technicalFactorsCommentCounter_Label = QLabel(self.widget_25)
        self.technicalFactorsCommentCounter_Label.setObjectName(u"technicalFactorsCommentCounter_Label")
        sizePolicy4.setHeightForWidth(self.technicalFactorsCommentCounter_Label.sizePolicy().hasHeightForWidth())
        self.technicalFactorsCommentCounter_Label.setSizePolicy(sizePolicy4)
        self.technicalFactorsCommentCounter_Label.setMinimumSize(QSize(60, 0))
        self.technicalFactorsCommentCounter_Label.setMaximumSize(QSize(16777215, 16777215))
        self.technicalFactorsCommentCounter_Label.setFont(font23)
        self.technicalFactorsCommentCounter_Label.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border: 1px solid black;")
        self.technicalFactorsCommentCounter_Label.setAlignment(Qt.AlignCenter)
        self.technicalFactorsCommentCounter_Label.setMargin(1)

        self.horizontalLayout_19.addWidget(self.technicalFactorsCommentCounter_Label)


        self.verticalLayout_8.addLayout(self.horizontalLayout_19)


        self.gridLayout_18.addLayout(self.verticalLayout_8, 7, 0, 1, 1)

        self.line_11 = QFrame(self.widget_25)
        self.line_11.setObjectName(u"line_11")
        sizePolicy10.setHeightForWidth(self.line_11.sizePolicy().hasHeightForWidth())
        self.line_11.setSizePolicy(sizePolicy10)
        self.line_11.setMinimumSize(QSize(0, 0))
        self.line_11.setMaximumSize(QSize(16777215, 1))
        self.line_11.setStyleSheet(u"background-color:white;")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_18.addWidget(self.line_11, 1, 0, 1, 1)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_28, 0, 1, 1, 1)

        self.label_64 = QLabel(self.widget_25)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(16777215, 16777215))
        self.label_64.setFont(font14)
        self.label_64.setStyleSheet(u"color:white;")

        self.gridLayout_31.addWidget(self.label_64, 0, 2, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_29, 0, 3, 1, 1)

        self.label_63 = QLabel(self.widget_25)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(35, 35))
        self.label_63.setFont(font)
        self.label_63.setPixmap(QPixmap(u":/resources/images/options.png"))
        self.label_63.setScaledContents(True)

        self.gridLayout_31.addWidget(self.label_63, 0, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_31, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 160, -1)
        self.label_7 = QLabel(self.widget_25)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font18)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.horizontalSpacer_4 = QSpacerItem(25, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.technicalFactorsWeight_DoubleSpinBox = QDoubleSpinBox(self.widget_25)
        self.technicalFactorsWeight_DoubleSpinBox.setObjectName(u"technicalFactorsWeight_DoubleSpinBox")
        sizePolicy13.setHeightForWidth(self.technicalFactorsWeight_DoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.technicalFactorsWeight_DoubleSpinBox.setSizePolicy(sizePolicy13)
        self.technicalFactorsWeight_DoubleSpinBox.setFont(font)
        self.technicalFactorsWeight_DoubleSpinBox.setFocusPolicy(Qt.WheelFocus)
        self.technicalFactorsWeight_DoubleSpinBox.setMinimum(-10.000000000000000)
        self.technicalFactorsWeight_DoubleSpinBox.setMaximum(10.000000000000000)
        self.technicalFactorsWeight_DoubleSpinBox.setSingleStep(0.500000000000000)

        self.horizontalLayout_6.addWidget(self.technicalFactorsWeight_DoubleSpinBox)

        self.warning_TF_label = QLabel(self.widget_25)
        self.warning_TF_label.setObjectName(u"warning_TF_label")
        self.warning_TF_label.setMaximumSize(QSize(25, 25))
        self.warning_TF_label.setStyleSheet(u"QToolTip{\n"
"   border: 2px solid #FFE606;\n"
"    background-color: #FEFFE4;\n"
"    color: black;\n"
"    font-family: 'Arial'; \n"
"    font-size: 12px;\n"
"    padding: 8px;\n"
"}")
        self.warning_TF_label.setPixmap(QPixmap(u":/resources/images/warning.png"))
        self.warning_TF_label.setScaledContents(True)
        self.warning_TF_label.setAlignment(Qt.AlignCenter)
        self.warning_TF_label.setIndent(0)

        self.horizontalLayout_6.addWidget(self.warning_TF_label)


        self.gridLayout_18.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)


        self.gridLayout_43.addWidget(self.widget_25, 1, 1, 1, 1)

        self.widget_30 = QWidget(self.technicalFactors_Page)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy14)
        self.widget_30.setMinimumSize(QSize(0, 0))
        self.widget_30.setMaximumSize(QSize(470, 16777215))
        self.widget_30.setStyleSheet(u"background:#22577A;")
        self.gridLayout_32 = QGridLayout(self.widget_30)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(0)
        self.gridLayout_32.setVerticalSpacing(12)
        self.technicalFactorsSummary_TableWidget = QTableWidget(self.widget_30)
        if (self.technicalFactorsSummary_TableWidget.columnCount() < 3):
            self.technicalFactorsSummary_TableWidget.setColumnCount(3)
        __qtablewidgetitem204 = QTableWidgetItem()
        __qtablewidgetitem204.setFont(font4);
        __qtablewidgetitem204.setBackground(QColor(216, 216, 216));
        self.technicalFactorsSummary_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        __qtablewidgetitem205.setFont(font4);
        __qtablewidgetitem205.setBackground(QColor(217, 217, 217));
        self.technicalFactorsSummary_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        __qtablewidgetitem206.setFont(font4);
        __qtablewidgetitem206.setBackground(QColor(217, 217, 217));
        self.technicalFactorsSummary_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem206)
        if (self.technicalFactorsSummary_TableWidget.rowCount() < 4):
            self.technicalFactorsSummary_TableWidget.setRowCount(4)
        brush30 = QBrush(QColor(0, 0, 0, 255))
        brush30.setStyle(Qt.NoBrush)
        __qtablewidgetitem207 = QTableWidgetItem()
        __qtablewidgetitem207.setBackground(QColor(0, 0, 0));
        __qtablewidgetitem207.setForeground(brush30);
        self.technicalFactorsSummary_TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem207)
        brush31 = QBrush(QColor(0, 0, 0, 255))
        brush31.setStyle(Qt.NoBrush)
        __qtablewidgetitem208 = QTableWidgetItem()
        __qtablewidgetitem208.setForeground(brush31);
        self.technicalFactorsSummary_TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.technicalFactorsSummary_TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        self.technicalFactorsSummary_TableWidget.setVerticalHeaderItem(3, __qtablewidgetitem210)
        brush32 = QBrush(QColor(0, 0, 0, 255))
        brush32.setStyle(Qt.NoBrush)
        __qtablewidgetitem211 = QTableWidgetItem()
        __qtablewidgetitem211.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem211.setFont(font4);
        __qtablewidgetitem211.setBackground(brush13);
        __qtablewidgetitem211.setForeground(brush32);
        self.technicalFactorsSummary_TableWidget.setItem(0, 0, __qtablewidgetitem211)
        brush33 = QBrush(QColor(0, 0, 0, 255))
        brush33.setStyle(Qt.NoBrush)
        __qtablewidgetitem212 = QTableWidgetItem()
        __qtablewidgetitem212.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem212.setFont(font28);
        __qtablewidgetitem212.setBackground(brush15);
        __qtablewidgetitem212.setForeground(brush33);
        self.technicalFactorsSummary_TableWidget.setItem(0, 1, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        __qtablewidgetitem213.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem213.setFont(font4);
        __qtablewidgetitem213.setBackground(brush15);
        self.technicalFactorsSummary_TableWidget.setItem(0, 2, __qtablewidgetitem213)
        brush34 = QBrush(QColor(0, 0, 0, 255))
        brush34.setStyle(Qt.NoBrush)
        __qtablewidgetitem214 = QTableWidgetItem()
        __qtablewidgetitem214.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem214.setFont(font25);
        __qtablewidgetitem214.setBackground(brush5);
        __qtablewidgetitem214.setForeground(brush34);
        self.technicalFactorsSummary_TableWidget.setItem(1, 0, __qtablewidgetitem214)
        brush35 = QBrush(QColor(0, 0, 0, 255))
        brush35.setStyle(Qt.NoBrush)
        __qtablewidgetitem215 = QTableWidgetItem()
        __qtablewidgetitem215.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem215.setFont(font9);
        __qtablewidgetitem215.setBackground(brush18);
        __qtablewidgetitem215.setForeground(brush35);
        self.technicalFactorsSummary_TableWidget.setItem(1, 1, __qtablewidgetitem215)
        __qtablewidgetitem216 = QTableWidgetItem()
        __qtablewidgetitem216.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem216.setFont(font4);
        __qtablewidgetitem216.setBackground(brush18);
        self.technicalFactorsSummary_TableWidget.setItem(1, 2, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        __qtablewidgetitem217.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem217.setFont(font4);
        __qtablewidgetitem217.setBackground(brush19);
        self.technicalFactorsSummary_TableWidget.setItem(2, 0, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        __qtablewidgetitem218.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem218.setFont(font9);
        __qtablewidgetitem218.setBackground(brush20);
        self.technicalFactorsSummary_TableWidget.setItem(2, 1, __qtablewidgetitem218)
        __qtablewidgetitem219 = QTableWidgetItem()
        __qtablewidgetitem219.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem219.setFont(font4);
        __qtablewidgetitem219.setBackground(brush20);
        self.technicalFactorsSummary_TableWidget.setItem(2, 2, __qtablewidgetitem219)
        __qtablewidgetitem220 = QTableWidgetItem()
        __qtablewidgetitem220.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem220.setFont(font6);
        self.technicalFactorsSummary_TableWidget.setItem(3, 0, __qtablewidgetitem220)
        __qtablewidgetitem221 = QTableWidgetItem()
        __qtablewidgetitem221.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem221.setFont(font6);
        self.technicalFactorsSummary_TableWidget.setItem(3, 1, __qtablewidgetitem221)
        __qtablewidgetitem222 = QTableWidgetItem()
        __qtablewidgetitem222.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem222.setFont(font4);
        self.technicalFactorsSummary_TableWidget.setItem(3, 2, __qtablewidgetitem222)
        self.technicalFactorsSummary_TableWidget.setObjectName(u"technicalFactorsSummary_TableWidget")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.technicalFactorsSummary_TableWidget.sizePolicy().hasHeightForWidth())
        self.technicalFactorsSummary_TableWidget.setSizePolicy(sizePolicy15)
        self.technicalFactorsSummary_TableWidget.setMinimumSize(QSize(0, 0))
        self.technicalFactorsSummary_TableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.technicalFactorsSummary_TableWidget.setFont(font29)
        self.technicalFactorsSummary_TableWidget.viewport().setProperty("cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.technicalFactorsSummary_TableWidget.setMouseTracking(False)
        self.technicalFactorsSummary_TableWidget.setTabletTracking(False)
        self.technicalFactorsSummary_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.technicalFactorsSummary_TableWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.technicalFactorsSummary_TableWidget.setLayoutDirection(Qt.LeftToRight)
        self.technicalFactorsSummary_TableWidget.setStyleSheet(u"QTableWidget{\n"
"    background-color: white;\n"
"    margin: 5px 5px 5px 3px;\n"
"    gridline-color: #9C9C9C; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    height:24px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"     background: #3B4252;\n"
"     width: 20px;\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: white;\n"
"     min-height: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #3B4252;\n"
"     height: 20px;\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: white;\n"
"     min-width: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"QScrollBar"
                        "::sub-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}")
        self.technicalFactorsSummary_TableWidget.setFrameShape(QFrame.NoFrame)
        self.technicalFactorsSummary_TableWidget.setFrameShadow(QFrame.Raised)
        self.technicalFactorsSummary_TableWidget.setLineWidth(0)
        self.technicalFactorsSummary_TableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.technicalFactorsSummary_TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.technicalFactorsSummary_TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.technicalFactorsSummary_TableWidget.setAutoScroll(False)
        self.technicalFactorsSummary_TableWidget.setAutoScrollMargin(0)
        self.technicalFactorsSummary_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.technicalFactorsSummary_TableWidget.setTabKeyNavigation(False)
        self.technicalFactorsSummary_TableWidget.setProperty("showDropIndicator", False)
        self.technicalFactorsSummary_TableWidget.setDragDropOverwriteMode(False)
        self.technicalFactorsSummary_TableWidget.setAlternatingRowColors(False)
        self.technicalFactorsSummary_TableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.technicalFactorsSummary_TableWidget.setTextElideMode(Qt.ElideMiddle)
        self.technicalFactorsSummary_TableWidget.setShowGrid(True)
        self.technicalFactorsSummary_TableWidget.setGridStyle(Qt.SolidLine)
        self.technicalFactorsSummary_TableWidget.setSortingEnabled(False)
        self.technicalFactorsSummary_TableWidget.setWordWrap(True)
        self.technicalFactorsSummary_TableWidget.setCornerButtonEnabled(True)
        self.technicalFactorsSummary_TableWidget.horizontalHeader().setVisible(True)
        self.technicalFactorsSummary_TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.technicalFactorsSummary_TableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.technicalFactorsSummary_TableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.technicalFactorsSummary_TableWidget.horizontalHeader().setHighlightSections(False)
        self.technicalFactorsSummary_TableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.technicalFactorsSummary_TableWidget.horizontalHeader().setStretchLastSection(True)
        self.technicalFactorsSummary_TableWidget.verticalHeader().setVisible(False)
        self.technicalFactorsSummary_TableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.technicalFactorsSummary_TableWidget.verticalHeader().setMinimumSectionSize(0)
        self.technicalFactorsSummary_TableWidget.verticalHeader().setDefaultSectionSize(40)
        self.technicalFactorsSummary_TableWidget.verticalHeader().setHighlightSections(False)
        self.technicalFactorsSummary_TableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.technicalFactorsSummary_TableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_32.addWidget(self.technicalFactorsSummary_TableWidget, 2, 0, 1, 1)

        self.line_12 = QFrame(self.widget_30)
        self.line_12.setObjectName(u"line_12")
        sizePolicy10.setHeightForWidth(self.line_12.sizePolicy().hasHeightForWidth())
        self.line_12.setSizePolicy(sizePolicy10)
        self.line_12.setMinimumSize(QSize(0, 0))
        self.line_12.setMaximumSize(QSize(16777215, 1))
        self.line_12.setStyleSheet(u"background-color:white;")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_32.addWidget(self.line_12, 1, 0, 1, 1)

        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_65 = QLabel(self.widget_30)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(161, 30))
        self.label_65.setFont(font14)
        self.label_65.setStyleSheet(u"color:white;")

        self.gridLayout_35.addWidget(self.label_65, 0, 2, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_30, 0, 3, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_31, 0, 1, 1, 1)

        self.label_73 = QLabel(self.widget_30)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMaximumSize(QSize(35, 35))
        self.label_73.setFont(font)
        self.label_73.setPixmap(QPixmap(u":/resources/images/summary.png"))
        self.label_73.setScaledContents(True)

        self.gridLayout_35.addWidget(self.label_73, 0, 0, 1, 1)


        self.gridLayout_32.addLayout(self.gridLayout_35, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.widget_30, 2, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.technicalFactors_Page)
        self.environmentalFactors_Page = QWidget()
        self.environmentalFactors_Page.setObjectName(u"environmentalFactors_Page")
        self.gridLayout_23 = QGridLayout(self.environmentalFactors_Page)
        self.gridLayout_23.setSpacing(15)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(15, 15, 15, 15)
        self.widget_29 = QWidget(self.environmentalFactors_Page)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy14.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy14)
        self.widget_29.setMaximumSize(QSize(470, 16777215))
        self.widget_29.setStyleSheet(u"background:#22577A;")
        self.gridLayout_28 = QGridLayout(self.widget_29)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setHorizontalSpacing(0)
        self.gridLayout_28.setVerticalSpacing(12)
        self.environmentalFactorsSummary_TableWidget = QTableWidget(self.widget_29)
        if (self.environmentalFactorsSummary_TableWidget.columnCount() < 3):
            self.environmentalFactorsSummary_TableWidget.setColumnCount(3)
        __qtablewidgetitem223 = QTableWidgetItem()
        __qtablewidgetitem223.setFont(font4);
        __qtablewidgetitem223.setBackground(QColor(216, 216, 216));
        self.environmentalFactorsSummary_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem223)
        __qtablewidgetitem224 = QTableWidgetItem()
        __qtablewidgetitem224.setFont(font4);
        __qtablewidgetitem224.setBackground(QColor(217, 217, 217));
        self.environmentalFactorsSummary_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem224)
        __qtablewidgetitem225 = QTableWidgetItem()
        __qtablewidgetitem225.setFont(font4);
        __qtablewidgetitem225.setBackground(QColor(217, 217, 217));
        self.environmentalFactorsSummary_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem225)
        if (self.environmentalFactorsSummary_TableWidget.rowCount() < 4):
            self.environmentalFactorsSummary_TableWidget.setRowCount(4)
        brush36 = QBrush(QColor(0, 0, 0, 255))
        brush36.setStyle(Qt.NoBrush)
        __qtablewidgetitem226 = QTableWidgetItem()
        __qtablewidgetitem226.setBackground(QColor(0, 0, 0));
        __qtablewidgetitem226.setForeground(brush36);
        self.environmentalFactorsSummary_TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem226)
        brush37 = QBrush(QColor(0, 0, 0, 255))
        brush37.setStyle(Qt.NoBrush)
        __qtablewidgetitem227 = QTableWidgetItem()
        __qtablewidgetitem227.setForeground(brush37);
        self.environmentalFactorsSummary_TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem227)
        __qtablewidgetitem228 = QTableWidgetItem()
        self.environmentalFactorsSummary_TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem228)
        __qtablewidgetitem229 = QTableWidgetItem()
        self.environmentalFactorsSummary_TableWidget.setVerticalHeaderItem(3, __qtablewidgetitem229)
        brush38 = QBrush(QColor(0, 0, 0, 255))
        brush38.setStyle(Qt.NoBrush)
        __qtablewidgetitem230 = QTableWidgetItem()
        __qtablewidgetitem230.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem230.setFont(font4);
        __qtablewidgetitem230.setBackground(brush13);
        __qtablewidgetitem230.setForeground(brush38);
        self.environmentalFactorsSummary_TableWidget.setItem(0, 0, __qtablewidgetitem230)
        brush39 = QBrush(QColor(0, 0, 0, 255))
        brush39.setStyle(Qt.NoBrush)
        __qtablewidgetitem231 = QTableWidgetItem()
        __qtablewidgetitem231.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem231.setFont(font28);
        __qtablewidgetitem231.setBackground(brush15);
        __qtablewidgetitem231.setForeground(brush39);
        self.environmentalFactorsSummary_TableWidget.setItem(0, 1, __qtablewidgetitem231)
        __qtablewidgetitem232 = QTableWidgetItem()
        __qtablewidgetitem232.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem232.setFont(font4);
        __qtablewidgetitem232.setBackground(brush15);
        self.environmentalFactorsSummary_TableWidget.setItem(0, 2, __qtablewidgetitem232)
        brush40 = QBrush(QColor(0, 0, 0, 255))
        brush40.setStyle(Qt.NoBrush)
        __qtablewidgetitem233 = QTableWidgetItem()
        __qtablewidgetitem233.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem233.setFont(font25);
        __qtablewidgetitem233.setBackground(brush5);
        __qtablewidgetitem233.setForeground(brush40);
        self.environmentalFactorsSummary_TableWidget.setItem(1, 0, __qtablewidgetitem233)
        brush41 = QBrush(QColor(0, 0, 0, 255))
        brush41.setStyle(Qt.NoBrush)
        __qtablewidgetitem234 = QTableWidgetItem()
        __qtablewidgetitem234.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem234.setFont(font9);
        __qtablewidgetitem234.setBackground(brush18);
        __qtablewidgetitem234.setForeground(brush41);
        self.environmentalFactorsSummary_TableWidget.setItem(1, 1, __qtablewidgetitem234)
        __qtablewidgetitem235 = QTableWidgetItem()
        __qtablewidgetitem235.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem235.setFont(font4);
        __qtablewidgetitem235.setBackground(brush18);
        self.environmentalFactorsSummary_TableWidget.setItem(1, 2, __qtablewidgetitem235)
        __qtablewidgetitem236 = QTableWidgetItem()
        __qtablewidgetitem236.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem236.setFont(font4);
        __qtablewidgetitem236.setBackground(brush19);
        self.environmentalFactorsSummary_TableWidget.setItem(2, 0, __qtablewidgetitem236)
        __qtablewidgetitem237 = QTableWidgetItem()
        __qtablewidgetitem237.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem237.setFont(font9);
        __qtablewidgetitem237.setBackground(brush20);
        self.environmentalFactorsSummary_TableWidget.setItem(2, 1, __qtablewidgetitem237)
        __qtablewidgetitem238 = QTableWidgetItem()
        __qtablewidgetitem238.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem238.setFont(font4);
        __qtablewidgetitem238.setBackground(brush20);
        self.environmentalFactorsSummary_TableWidget.setItem(2, 2, __qtablewidgetitem238)
        __qtablewidgetitem239 = QTableWidgetItem()
        __qtablewidgetitem239.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem239.setFont(font6);
        self.environmentalFactorsSummary_TableWidget.setItem(3, 0, __qtablewidgetitem239)
        __qtablewidgetitem240 = QTableWidgetItem()
        __qtablewidgetitem240.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem240.setFont(font6);
        self.environmentalFactorsSummary_TableWidget.setItem(3, 1, __qtablewidgetitem240)
        __qtablewidgetitem241 = QTableWidgetItem()
        __qtablewidgetitem241.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem241.setFont(font4);
        self.environmentalFactorsSummary_TableWidget.setItem(3, 2, __qtablewidgetitem241)
        self.environmentalFactorsSummary_TableWidget.setObjectName(u"environmentalFactorsSummary_TableWidget")
        sizePolicy15.setHeightForWidth(self.environmentalFactorsSummary_TableWidget.sizePolicy().hasHeightForWidth())
        self.environmentalFactorsSummary_TableWidget.setSizePolicy(sizePolicy15)
        self.environmentalFactorsSummary_TableWidget.setMinimumSize(QSize(0, 0))
        self.environmentalFactorsSummary_TableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.environmentalFactorsSummary_TableWidget.setFont(font29)
        self.environmentalFactorsSummary_TableWidget.viewport().setProperty("cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.environmentalFactorsSummary_TableWidget.setMouseTracking(False)
        self.environmentalFactorsSummary_TableWidget.setTabletTracking(False)
        self.environmentalFactorsSummary_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.environmentalFactorsSummary_TableWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.environmentalFactorsSummary_TableWidget.setLayoutDirection(Qt.LeftToRight)
        self.environmentalFactorsSummary_TableWidget.setStyleSheet(u"QTableWidget{\n"
"    background-color: white;\n"
"    margin: 5px 5px 5px 3px;\n"
"    gridline-color: #9C9C9C; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    height:24px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"     background: #3B4252;\n"
"     width: 20px;\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: white;\n"
"     min-height: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #3B4252;\n"
"     height: 20px;\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: white;\n"
"     min-width: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"QScrollBar"
                        "::sub-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}")
        self.environmentalFactorsSummary_TableWidget.setFrameShape(QFrame.NoFrame)
        self.environmentalFactorsSummary_TableWidget.setFrameShadow(QFrame.Raised)
        self.environmentalFactorsSummary_TableWidget.setLineWidth(0)
        self.environmentalFactorsSummary_TableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.environmentalFactorsSummary_TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.environmentalFactorsSummary_TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.environmentalFactorsSummary_TableWidget.setAutoScroll(False)
        self.environmentalFactorsSummary_TableWidget.setAutoScrollMargin(0)
        self.environmentalFactorsSummary_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.environmentalFactorsSummary_TableWidget.setTabKeyNavigation(False)
        self.environmentalFactorsSummary_TableWidget.setProperty("showDropIndicator", False)
        self.environmentalFactorsSummary_TableWidget.setDragDropOverwriteMode(False)
        self.environmentalFactorsSummary_TableWidget.setAlternatingRowColors(False)
        self.environmentalFactorsSummary_TableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.environmentalFactorsSummary_TableWidget.setTextElideMode(Qt.ElideMiddle)
        self.environmentalFactorsSummary_TableWidget.setShowGrid(True)
        self.environmentalFactorsSummary_TableWidget.setGridStyle(Qt.SolidLine)
        self.environmentalFactorsSummary_TableWidget.setSortingEnabled(False)
        self.environmentalFactorsSummary_TableWidget.setWordWrap(True)
        self.environmentalFactorsSummary_TableWidget.setCornerButtonEnabled(True)
        self.environmentalFactorsSummary_TableWidget.horizontalHeader().setVisible(True)
        self.environmentalFactorsSummary_TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.environmentalFactorsSummary_TableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.environmentalFactorsSummary_TableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.environmentalFactorsSummary_TableWidget.horizontalHeader().setHighlightSections(False)
        self.environmentalFactorsSummary_TableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.environmentalFactorsSummary_TableWidget.horizontalHeader().setStretchLastSection(True)
        self.environmentalFactorsSummary_TableWidget.verticalHeader().setVisible(False)
        self.environmentalFactorsSummary_TableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.environmentalFactorsSummary_TableWidget.verticalHeader().setMinimumSectionSize(0)
        self.environmentalFactorsSummary_TableWidget.verticalHeader().setDefaultSectionSize(40)
        self.environmentalFactorsSummary_TableWidget.verticalHeader().setHighlightSections(False)
        self.environmentalFactorsSummary_TableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.environmentalFactorsSummary_TableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_28.addWidget(self.environmentalFactorsSummary_TableWidget, 2, 0, 1, 1)

        self.line_8 = QFrame(self.widget_29)
        self.line_8.setObjectName(u"line_8")
        sizePolicy10.setHeightForWidth(self.line_8.sizePolicy().hasHeightForWidth())
        self.line_8.setSizePolicy(sizePolicy10)
        self.line_8.setMinimumSize(QSize(0, 0))
        self.line_8.setMaximumSize(QSize(16777215, 1))
        self.line_8.setStyleSheet(u"background-color:white;")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_28.addWidget(self.line_8, 1, 0, 1, 1)

        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_57 = QLabel(self.widget_29)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(161, 30))
        self.label_57.setFont(font14)
        self.label_57.setStyleSheet(u"color:white;")

        self.gridLayout_34.addWidget(self.label_57, 0, 2, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_22, 0, 3, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_23, 0, 1, 1, 1)

        self.label_58 = QLabel(self.widget_29)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(35, 35))
        self.label_58.setFont(font)
        self.label_58.setPixmap(QPixmap(u":/resources/images/summary.png"))
        self.label_58.setScaledContents(True)

        self.gridLayout_34.addWidget(self.label_58, 0, 0, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_34, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.widget_29, 2, 1, 1, 1)

        self.widget_27 = QWidget(self.environmentalFactors_Page)
        self.widget_27.setObjectName(u"widget_27")
        sizePolicy.setHeightForWidth(self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy)
        self.widget_27.setStyleSheet(u"background:#22577A;\n"
"color:white;")
        self.gridLayout_33 = QGridLayout(self.widget_27)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.environmentalFactors_TableWidget = QTableWidget(self.widget_27)
        if (self.environmentalFactors_TableWidget.columnCount() < 7):
            self.environmentalFactors_TableWidget.setColumnCount(7)
        __qtablewidgetitem242 = QTableWidgetItem()
        __qtablewidgetitem242.setFont(font9);
        self.environmentalFactors_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem242)
        __qtablewidgetitem243 = QTableWidgetItem()
        __qtablewidgetitem243.setFont(font9);
        self.environmentalFactors_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem243)
        __qtablewidgetitem244 = QTableWidgetItem()
        __qtablewidgetitem244.setFont(font9);
        self.environmentalFactors_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem244)
        __qtablewidgetitem245 = QTableWidgetItem()
        __qtablewidgetitem245.setFont(font9);
        self.environmentalFactors_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem245)
        __qtablewidgetitem246 = QTableWidgetItem()
        __qtablewidgetitem246.setFont(font9);
        self.environmentalFactors_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem246)
        __qtablewidgetitem247 = QTableWidgetItem()
        __qtablewidgetitem247.setFont(font9);
        self.environmentalFactors_TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem247)
        __qtablewidgetitem248 = QTableWidgetItem()
        __qtablewidgetitem248.setFont(font9);
        self.environmentalFactors_TableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem248)
        if (self.environmentalFactors_TableWidget.rowCount() < 9):
            self.environmentalFactors_TableWidget.setRowCount(9)
        __qtablewidgetitem249 = QTableWidgetItem()
        self.environmentalFactors_TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem249)
        __qtablewidgetitem250 = QTableWidgetItem()
        self.environmentalFactors_TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem250)
        __qtablewidgetitem251 = QTableWidgetItem()
        self.environmentalFactors_TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem251)
        __qtablewidgetitem252 = QTableWidgetItem()
        self.environmentalFactors_TableWidget.setVerticalHeaderItem(3, __qtablewidgetitem252)
        __qtablewidgetitem253 = QTableWidgetItem()
        self.environmentalFactors_TableWidget.setVerticalHeaderItem(4, __qtablewidgetitem253)
        __qtablewidgetitem254 = QTableWidgetItem()
        self.environmentalFactors_TableWidget.setVerticalHeaderItem(5, __qtablewidgetitem254)
        __qtablewidgetitem255 = QTableWidgetItem()
        self.environmentalFactors_TableWidget.setVerticalHeaderItem(6, __qtablewidgetitem255)
        __qtablewidgetitem256 = QTableWidgetItem()
        self.environmentalFactors_TableWidget.setVerticalHeaderItem(7, __qtablewidgetitem256)
        __qtablewidgetitem257 = QTableWidgetItem()
        self.environmentalFactors_TableWidget.setVerticalHeaderItem(8, __qtablewidgetitem257)
        __qtablewidgetitem258 = QTableWidgetItem()
        __qtablewidgetitem258.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem258.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(0, 1, __qtablewidgetitem258)
        __qtablewidgetitem259 = QTableWidgetItem()
        __qtablewidgetitem259.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem259.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(0, 2, __qtablewidgetitem259)
        __qtablewidgetitem260 = QTableWidgetItem()
        __qtablewidgetitem260.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem260.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(0, 3, __qtablewidgetitem260)
        __qtablewidgetitem261 = QTableWidgetItem()
        __qtablewidgetitem261.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem261.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(0, 4, __qtablewidgetitem261)
        __qtablewidgetitem262 = QTableWidgetItem()
        __qtablewidgetitem262.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem262.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(0, 5, __qtablewidgetitem262)
        __qtablewidgetitem263 = QTableWidgetItem()
        __qtablewidgetitem263.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem263.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(0, 6, __qtablewidgetitem263)
        __qtablewidgetitem264 = QTableWidgetItem()
        __qtablewidgetitem264.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem264.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(1, 1, __qtablewidgetitem264)
        __qtablewidgetitem265 = QTableWidgetItem()
        __qtablewidgetitem265.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem265.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(1, 2, __qtablewidgetitem265)
        __qtablewidgetitem266 = QTableWidgetItem()
        __qtablewidgetitem266.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem266.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(1, 3, __qtablewidgetitem266)
        __qtablewidgetitem267 = QTableWidgetItem()
        __qtablewidgetitem267.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem267.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(1, 4, __qtablewidgetitem267)
        __qtablewidgetitem268 = QTableWidgetItem()
        __qtablewidgetitem268.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem268.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(1, 5, __qtablewidgetitem268)
        __qtablewidgetitem269 = QTableWidgetItem()
        __qtablewidgetitem269.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem269.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(1, 6, __qtablewidgetitem269)
        __qtablewidgetitem270 = QTableWidgetItem()
        __qtablewidgetitem270.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem270.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(2, 1, __qtablewidgetitem270)
        __qtablewidgetitem271 = QTableWidgetItem()
        __qtablewidgetitem271.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem271.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(2, 2, __qtablewidgetitem271)
        __qtablewidgetitem272 = QTableWidgetItem()
        __qtablewidgetitem272.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem272.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(2, 3, __qtablewidgetitem272)
        __qtablewidgetitem273 = QTableWidgetItem()
        __qtablewidgetitem273.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem273.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(2, 4, __qtablewidgetitem273)
        __qtablewidgetitem274 = QTableWidgetItem()
        __qtablewidgetitem274.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem274.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(2, 5, __qtablewidgetitem274)
        __qtablewidgetitem275 = QTableWidgetItem()
        __qtablewidgetitem275.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem275.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(2, 6, __qtablewidgetitem275)
        __qtablewidgetitem276 = QTableWidgetItem()
        __qtablewidgetitem276.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem276.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(3, 1, __qtablewidgetitem276)
        __qtablewidgetitem277 = QTableWidgetItem()
        __qtablewidgetitem277.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem277.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(3, 2, __qtablewidgetitem277)
        __qtablewidgetitem278 = QTableWidgetItem()
        __qtablewidgetitem278.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem278.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(3, 3, __qtablewidgetitem278)
        __qtablewidgetitem279 = QTableWidgetItem()
        __qtablewidgetitem279.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem279.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(3, 4, __qtablewidgetitem279)
        __qtablewidgetitem280 = QTableWidgetItem()
        __qtablewidgetitem280.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem280.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(3, 5, __qtablewidgetitem280)
        __qtablewidgetitem281 = QTableWidgetItem()
        __qtablewidgetitem281.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem281.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(3, 6, __qtablewidgetitem281)
        __qtablewidgetitem282 = QTableWidgetItem()
        __qtablewidgetitem282.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem282.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(4, 1, __qtablewidgetitem282)
        __qtablewidgetitem283 = QTableWidgetItem()
        __qtablewidgetitem283.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem283.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(4, 2, __qtablewidgetitem283)
        __qtablewidgetitem284 = QTableWidgetItem()
        __qtablewidgetitem284.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem284.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(4, 3, __qtablewidgetitem284)
        __qtablewidgetitem285 = QTableWidgetItem()
        __qtablewidgetitem285.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem285.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(4, 4, __qtablewidgetitem285)
        __qtablewidgetitem286 = QTableWidgetItem()
        __qtablewidgetitem286.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem286.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(4, 5, __qtablewidgetitem286)
        __qtablewidgetitem287 = QTableWidgetItem()
        __qtablewidgetitem287.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem287.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(4, 6, __qtablewidgetitem287)
        __qtablewidgetitem288 = QTableWidgetItem()
        __qtablewidgetitem288.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem288.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(5, 1, __qtablewidgetitem288)
        __qtablewidgetitem289 = QTableWidgetItem()
        __qtablewidgetitem289.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem289.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(5, 2, __qtablewidgetitem289)
        __qtablewidgetitem290 = QTableWidgetItem()
        __qtablewidgetitem290.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem290.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(5, 3, __qtablewidgetitem290)
        __qtablewidgetitem291 = QTableWidgetItem()
        __qtablewidgetitem291.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem291.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(5, 4, __qtablewidgetitem291)
        __qtablewidgetitem292 = QTableWidgetItem()
        __qtablewidgetitem292.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem292.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(5, 5, __qtablewidgetitem292)
        __qtablewidgetitem293 = QTableWidgetItem()
        __qtablewidgetitem293.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem293.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(5, 6, __qtablewidgetitem293)
        __qtablewidgetitem294 = QTableWidgetItem()
        __qtablewidgetitem294.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem294.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(6, 1, __qtablewidgetitem294)
        __qtablewidgetitem295 = QTableWidgetItem()
        __qtablewidgetitem295.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem295.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(6, 2, __qtablewidgetitem295)
        __qtablewidgetitem296 = QTableWidgetItem()
        __qtablewidgetitem296.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem296.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(6, 3, __qtablewidgetitem296)
        __qtablewidgetitem297 = QTableWidgetItem()
        __qtablewidgetitem297.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem297.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(6, 4, __qtablewidgetitem297)
        __qtablewidgetitem298 = QTableWidgetItem()
        __qtablewidgetitem298.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem298.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(6, 5, __qtablewidgetitem298)
        __qtablewidgetitem299 = QTableWidgetItem()
        __qtablewidgetitem299.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem299.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(6, 6, __qtablewidgetitem299)
        __qtablewidgetitem300 = QTableWidgetItem()
        __qtablewidgetitem300.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem300.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(7, 1, __qtablewidgetitem300)
        __qtablewidgetitem301 = QTableWidgetItem()
        __qtablewidgetitem301.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem301.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(7, 2, __qtablewidgetitem301)
        __qtablewidgetitem302 = QTableWidgetItem()
        __qtablewidgetitem302.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem302.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(7, 3, __qtablewidgetitem302)
        __qtablewidgetitem303 = QTableWidgetItem()
        __qtablewidgetitem303.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem303.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(7, 4, __qtablewidgetitem303)
        __qtablewidgetitem304 = QTableWidgetItem()
        __qtablewidgetitem304.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem304.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(7, 5, __qtablewidgetitem304)
        __qtablewidgetitem305 = QTableWidgetItem()
        __qtablewidgetitem305.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem305.setBackground(brush28);
        self.environmentalFactors_TableWidget.setItem(7, 6, __qtablewidgetitem305)
        __qtablewidgetitem306 = QTableWidgetItem()
        __qtablewidgetitem306.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem306.setBackground(brush29);
        self.environmentalFactors_TableWidget.setItem(8, 0, __qtablewidgetitem306)
        self.environmentalFactors_TableWidget.setObjectName(u"environmentalFactors_TableWidget")
        self.environmentalFactors_TableWidget.setFont(font30)
        self.environmentalFactors_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.environmentalFactors_TableWidget.setLayoutDirection(Qt.LeftToRight)
        self.environmentalFactors_TableWidget.setStyleSheet(u"QTableView{\n"
"    border: 1px solid  #22577A;\n"
"}\n"
"QHeaderView::section{\n"
"    background: #51EDC6;\n"
"    padding: 3px 5px 3px 5px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTableWidget::Item{\n"
"    padding: 0px 5px 0px 5px ;\n"
"    color: black;\n"
"}\n"
"QHeaderView::down-arrow {\n"
"	image: url(:/resources/images/blackDownArrow.png); \n"
"}\n"
"QHeaderView::up-arrow {\n"
"	image: url(:/resources/images/blackUpArrow.png);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"     background: #3B4252;\n"
"     width: 20px;\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: white;\n"
"     min-height: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #3B4252;\n"
"     height: 20px;\n"
"     margin: 3px 0p"
                        "x 3px 0px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: white;\n"
"     min-width: 20px;\n"
"     border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	background: none;\n"
"	width: 0px;\n"
"}")
        self.environmentalFactors_TableWidget.setFrameShape(QFrame.NoFrame)
        self.environmentalFactors_TableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.environmentalFactors_TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.environmentalFactors_TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.environmentalFactors_TableWidget.setAutoScroll(False)
        self.environmentalFactors_TableWidget.setAutoScrollMargin(100)
        self.environmentalFactors_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.environmentalFactors_TableWidget.setTabKeyNavigation(True)
        self.environmentalFactors_TableWidget.setProperty("showDropIndicator", False)
        self.environmentalFactors_TableWidget.setDragEnabled(False)
        self.environmentalFactors_TableWidget.setDragDropOverwriteMode(False)
        self.environmentalFactors_TableWidget.setAlternatingRowColors(False)
        self.environmentalFactors_TableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.environmentalFactors_TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.environmentalFactors_TableWidget.setTextElideMode(Qt.ElideRight)
        self.environmentalFactors_TableWidget.setShowGrid(True)
        self.environmentalFactors_TableWidget.setGridStyle(Qt.SolidLine)
        self.environmentalFactors_TableWidget.setSortingEnabled(True)
        self.environmentalFactors_TableWidget.setWordWrap(True)
        self.environmentalFactors_TableWidget.setCornerButtonEnabled(False)
        self.environmentalFactors_TableWidget.setRowCount(9)
        self.environmentalFactors_TableWidget.horizontalHeader().setVisible(True)
        self.environmentalFactors_TableWidget.horizontalHeader().setMinimumSectionSize(90)
        self.environmentalFactors_TableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.environmentalFactors_TableWidget.horizontalHeader().setHighlightSections(True)
        self.environmentalFactors_TableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.environmentalFactors_TableWidget.horizontalHeader().setStretchLastSection(False)
        self.environmentalFactors_TableWidget.verticalHeader().setVisible(False)
        self.environmentalFactors_TableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.environmentalFactors_TableWidget.verticalHeader().setMinimumSectionSize(0)
        self.environmentalFactors_TableWidget.verticalHeader().setDefaultSectionSize(0)
        self.environmentalFactors_TableWidget.verticalHeader().setHighlightSections(False)
        self.environmentalFactors_TableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.environmentalFactors_TableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_33.addWidget(self.environmentalFactors_TableWidget, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.widget_27, 1, 0, 2, 1)

        self.label_3 = QLabel(self.environmentalFactors_Page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font14)
        self.label_3.setStyleSheet(u"color:white;")

        self.gridLayout_23.addWidget(self.label_3, 0, 0, 1, 1)

        self.widget_32 = QWidget(self.environmentalFactors_Page)
        self.widget_32.setObjectName(u"widget_32")
        sizePolicy9.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy9)
        self.widget_32.setMaximumSize(QSize(470, 16777215))
        self.widget_32.setStyleSheet(u"background:#22577A;\n"
"color:white;")
        self.gridLayout_29 = QGridLayout(self.widget_32)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setHorizontalSpacing(0)
        self.gridLayout_29.setVerticalSpacing(10)
        self.gridLayout_29.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.cancelEnvironmentalFactor_Button = QPushButton(self.widget_32)
        self.cancelEnvironmentalFactor_Button.setObjectName(u"cancelEnvironmentalFactor_Button")
        sizePolicy4.setHeightForWidth(self.cancelEnvironmentalFactor_Button.sizePolicy().hasHeightForWidth())
        self.cancelEnvironmentalFactor_Button.setSizePolicy(sizePolicy4)
        self.cancelEnvironmentalFactor_Button.setFont(font15)
        self.cancelEnvironmentalFactor_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancelEnvironmentalFactor_Button.setFocusPolicy(Qt.NoFocus)
        self.cancelEnvironmentalFactor_Button.setStyleSheet(u"background-color: #FF0000;\n"
"color: white;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        self.cancelEnvironmentalFactor_Button.setIcon(icon22)
        self.cancelEnvironmentalFactor_Button.setIconSize(QSize(22, 23))

        self.horizontalLayout_10.addWidget(self.cancelEnvironmentalFactor_Button)

        self.saveEnvironmentalFactor_Button = QPushButton(self.widget_32)
        self.saveEnvironmentalFactor_Button.setObjectName(u"saveEnvironmentalFactor_Button")
        sizePolicy4.setHeightForWidth(self.saveEnvironmentalFactor_Button.sizePolicy().hasHeightForWidth())
        self.saveEnvironmentalFactor_Button.setSizePolicy(sizePolicy4)
        self.saveEnvironmentalFactor_Button.setFont(font15)
        self.saveEnvironmentalFactor_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.saveEnvironmentalFactor_Button.setFocusPolicy(Qt.NoFocus)
        self.saveEnvironmentalFactor_Button.setStyleSheet(u"background-color: #5AFFA6;\n"
"color: #094646;\n"
"padding: 6px 0px 6px 6px;\n"
"")
        self.saveEnvironmentalFactor_Button.setIcon(icon23)
        self.saveEnvironmentalFactor_Button.setIconSize(QSize(22, 22))

        self.horizontalLayout_10.addWidget(self.saveEnvironmentalFactor_Button)


        self.gridLayout_29.addLayout(self.horizontalLayout_10, 8, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(39)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 8, 0, -1)
        self.label_23 = QLabel(self.widget_32)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font18)
        self.label_23.setIndent(0)

        self.horizontalLayout_21.addWidget(self.label_23)

        self.environmentalFactorsFactor_ComboBox = QComboBox(self.widget_32)
        self.environmentalFactorsFactor_ComboBox.addItem("")
        self.environmentalFactorsFactor_ComboBox.addItem("")
        self.environmentalFactorsFactor_ComboBox.addItem("")
        self.environmentalFactorsFactor_ComboBox.addItem("")
        self.environmentalFactorsFactor_ComboBox.addItem("")
        self.environmentalFactorsFactor_ComboBox.addItem("")
        self.environmentalFactorsFactor_ComboBox.addItem("")
        self.environmentalFactorsFactor_ComboBox.addItem("")
        self.environmentalFactorsFactor_ComboBox.setObjectName(u"environmentalFactorsFactor_ComboBox")
        sizePolicy13.setHeightForWidth(self.environmentalFactorsFactor_ComboBox.sizePolicy().hasHeightForWidth())
        self.environmentalFactorsFactor_ComboBox.setSizePolicy(sizePolicy13)
        self.environmentalFactorsFactor_ComboBox.setMinimumSize(QSize(0, 0))
        self.environmentalFactorsFactor_ComboBox.setMaximumSize(QSize(16777215, 20))
        self.environmentalFactorsFactor_ComboBox.setFont(font23)
        self.environmentalFactorsFactor_ComboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.environmentalFactorsFactor_ComboBox.setFocusPolicy(Qt.WheelFocus)
        self.environmentalFactorsFactor_ComboBox.setContextMenuPolicy(Qt.NoContextMenu)
        self.environmentalFactorsFactor_ComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    color:black;\n"
"    combobox-popup: 0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #E6E6E6;\n"
"    selection-color: black;\n"
"    color:black;\n"
"}")
        self.environmentalFactorsFactor_ComboBox.setMaxVisibleItems(9)
        self.environmentalFactorsFactor_ComboBox.setMaxCount(9)
        self.environmentalFactorsFactor_ComboBox.setInsertPolicy(QComboBox.NoInsert)
        self.environmentalFactorsFactor_ComboBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.environmentalFactorsFactor_ComboBox.setMinimumContentsLength(0)
        self.environmentalFactorsFactor_ComboBox.setIconSize(QSize(10, 10))
        self.environmentalFactorsFactor_ComboBox.setFrame(False)

        self.horizontalLayout_21.addWidget(self.environmentalFactorsFactor_ComboBox)


        self.gridLayout_29.addLayout(self.horizontalLayout_21, 2, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_24 = QLabel(self.widget_32)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font18)
        self.label_24.setIndent(0)

        self.horizontalLayout_22.addWidget(self.label_24)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(20, 0, 10, -1)
        self.environmentalFactors_RadioButton_0 = QRadioButton(self.widget_32)
        self.environmentalFactors_RadioButton_0.setObjectName(u"environmentalFactors_RadioButton_0")
        sizePolicy13.setHeightForWidth(self.environmentalFactors_RadioButton_0.sizePolicy().hasHeightForWidth())
        self.environmentalFactors_RadioButton_0.setSizePolicy(sizePolicy13)
        self.environmentalFactors_RadioButton_0.setFont(font31)
        self.environmentalFactors_RadioButton_0.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.environmentalFactors_RadioButton_0.setFocusPolicy(Qt.WheelFocus)
        self.environmentalFactors_RadioButton_0.setCheckable(True)
        self.environmentalFactors_RadioButton_0.setAutoRepeat(False)

        self.horizontalLayout_28.addWidget(self.environmentalFactors_RadioButton_0)

        self.environmentalFactors_RadioButton_1 = QRadioButton(self.widget_32)
        self.environmentalFactors_RadioButton_1.setObjectName(u"environmentalFactors_RadioButton_1")
        sizePolicy13.setHeightForWidth(self.environmentalFactors_RadioButton_1.sizePolicy().hasHeightForWidth())
        self.environmentalFactors_RadioButton_1.setSizePolicy(sizePolicy13)
        self.environmentalFactors_RadioButton_1.setFont(font31)
        self.environmentalFactors_RadioButton_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.environmentalFactors_RadioButton_1.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_28.addWidget(self.environmentalFactors_RadioButton_1)

        self.environmentalFactors_RadioButton_2 = QRadioButton(self.widget_32)
        self.environmentalFactors_RadioButton_2.setObjectName(u"environmentalFactors_RadioButton_2")
        sizePolicy13.setHeightForWidth(self.environmentalFactors_RadioButton_2.sizePolicy().hasHeightForWidth())
        self.environmentalFactors_RadioButton_2.setSizePolicy(sizePolicy13)
        self.environmentalFactors_RadioButton_2.setFont(font31)
        self.environmentalFactors_RadioButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.environmentalFactors_RadioButton_2.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_28.addWidget(self.environmentalFactors_RadioButton_2)

        self.environmentalFactors_RadioButton_3 = QRadioButton(self.widget_32)
        self.environmentalFactors_RadioButton_3.setObjectName(u"environmentalFactors_RadioButton_3")
        sizePolicy13.setHeightForWidth(self.environmentalFactors_RadioButton_3.sizePolicy().hasHeightForWidth())
        self.environmentalFactors_RadioButton_3.setSizePolicy(sizePolicy13)
        self.environmentalFactors_RadioButton_3.setFont(font31)
        self.environmentalFactors_RadioButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.environmentalFactors_RadioButton_3.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_28.addWidget(self.environmentalFactors_RadioButton_3)

        self.environmentalFactors_RadioButton_4 = QRadioButton(self.widget_32)
        self.environmentalFactors_RadioButton_4.setObjectName(u"environmentalFactors_RadioButton_4")
        sizePolicy13.setHeightForWidth(self.environmentalFactors_RadioButton_4.sizePolicy().hasHeightForWidth())
        self.environmentalFactors_RadioButton_4.setSizePolicy(sizePolicy13)
        self.environmentalFactors_RadioButton_4.setFont(font31)
        self.environmentalFactors_RadioButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.environmentalFactors_RadioButton_4.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_28.addWidget(self.environmentalFactors_RadioButton_4)

        self.environmentalFactors_RadioButton_5 = QRadioButton(self.widget_32)
        self.environmentalFactors_RadioButton_5.setObjectName(u"environmentalFactors_RadioButton_5")
        sizePolicy13.setHeightForWidth(self.environmentalFactors_RadioButton_5.sizePolicy().hasHeightForWidth())
        self.environmentalFactors_RadioButton_5.setSizePolicy(sizePolicy13)
        self.environmentalFactors_RadioButton_5.setFont(font31)
        self.environmentalFactors_RadioButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.environmentalFactors_RadioButton_5.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_28.addWidget(self.environmentalFactors_RadioButton_5)

        self.environmentalFactorsInfo_Label = QLabel(self.widget_32)
        self.environmentalFactorsInfo_Label.setObjectName(u"environmentalFactorsInfo_Label")
        self.environmentalFactorsInfo_Label.setMaximumSize(QSize(25, 25))
        self.environmentalFactorsInfo_Label.setFont(font31)
        self.environmentalFactorsInfo_Label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.environmentalFactorsInfo_Label.setMouseTracking(False)
        self.environmentalFactorsInfo_Label.setToolTipDuration(-1)
        self.environmentalFactorsInfo_Label.setStyleSheet(u"QToolTip{\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-family: 'Arial'; \n"
"    font-size: 12px;\n"
"    padding: 8px;\n"
"}")
        self.environmentalFactorsInfo_Label.setPixmap(QPixmap(u":/resources/images/helpTooltip.png"))
        self.environmentalFactorsInfo_Label.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.environmentalFactorsInfo_Label)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_28)


        self.gridLayout_29.addLayout(self.horizontalLayout_22, 3, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, -1, -1, -1)
        self.label_25 = QLabel(self.widget_32)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font18)

        self.verticalLayout_15.addWidget(self.label_25)

        self.environmentalFactorsComment_PlainTextEdit = QPlainTextEdit(self.widget_32)
        self.environmentalFactorsComment_PlainTextEdit.setObjectName(u"environmentalFactorsComment_PlainTextEdit")
        sizePolicy4.setHeightForWidth(self.environmentalFactorsComment_PlainTextEdit.sizePolicy().hasHeightForWidth())
        self.environmentalFactorsComment_PlainTextEdit.setSizePolicy(sizePolicy4)
        self.environmentalFactorsComment_PlainTextEdit.setMinimumSize(QSize(0, 0))
        self.environmentalFactorsComment_PlainTextEdit.setMaximumSize(QSize(16777215, 16777215))
        self.environmentalFactorsComment_PlainTextEdit.setFont(font31)
        self.environmentalFactorsComment_PlainTextEdit.setFocusPolicy(Qt.WheelFocus)
        self.environmentalFactorsComment_PlainTextEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.environmentalFactorsComment_PlainTextEdit.setAcceptDrops(False)
        self.environmentalFactorsComment_PlainTextEdit.setStyleSheet(u"background:white;\n"
"color:black;")
        self.environmentalFactorsComment_PlainTextEdit.setFrameShape(QFrame.NoFrame)
        self.environmentalFactorsComment_PlainTextEdit.setFrameShadow(QFrame.Plain)
        self.environmentalFactorsComment_PlainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.environmentalFactorsComment_PlainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.environmentalFactorsComment_PlainTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.environmentalFactorsComment_PlainTextEdit.setTabChangesFocus(True)
        self.environmentalFactorsComment_PlainTextEdit.setTabStopDistance(80.000000000000000)
        self.environmentalFactorsComment_PlainTextEdit.setCursorWidth(1)

        self.verticalLayout_15.addWidget(self.environmentalFactorsComment_PlainTextEdit)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_24)

        self.environmentalFactorsCommentCounter_Label = QLabel(self.widget_32)
        self.environmentalFactorsCommentCounter_Label.setObjectName(u"environmentalFactorsCommentCounter_Label")
        sizePolicy4.setHeightForWidth(self.environmentalFactorsCommentCounter_Label.sizePolicy().hasHeightForWidth())
        self.environmentalFactorsCommentCounter_Label.setSizePolicy(sizePolicy4)
        self.environmentalFactorsCommentCounter_Label.setMinimumSize(QSize(60, 0))
        self.environmentalFactorsCommentCounter_Label.setMaximumSize(QSize(16777215, 16777215))
        self.environmentalFactorsCommentCounter_Label.setFont(font23)
        self.environmentalFactorsCommentCounter_Label.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border: 1px solid black;")
        self.environmentalFactorsCommentCounter_Label.setAlignment(Qt.AlignCenter)
        self.environmentalFactorsCommentCounter_Label.setMargin(1)

        self.horizontalLayout_29.addWidget(self.environmentalFactorsCommentCounter_Label)


        self.verticalLayout_15.addLayout(self.horizontalLayout_29)


        self.gridLayout_29.addLayout(self.verticalLayout_15, 7, 0, 1, 1)

        self.line_14 = QFrame(self.widget_32)
        self.line_14.setObjectName(u"line_14")
        sizePolicy10.setHeightForWidth(self.line_14.sizePolicy().hasHeightForWidth())
        self.line_14.setSizePolicy(sizePolicy10)
        self.line_14.setMinimumSize(QSize(0, 0))
        self.line_14.setMaximumSize(QSize(16777215, 1))
        self.line_14.setStyleSheet(u"background-color:white;")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_29.addWidget(self.line_14, 1, 0, 1, 1)

        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_38.addItem(self.horizontalSpacer_35, 0, 1, 1, 1)

        self.label_71 = QLabel(self.widget_32)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(16777215, 16777215))
        self.label_71.setFont(font14)
        self.label_71.setStyleSheet(u"color:white;")

        self.gridLayout_38.addWidget(self.label_71, 0, 2, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_38.addItem(self.horizontalSpacer_36, 0, 3, 1, 1)

        self.label_72 = QLabel(self.widget_32)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMaximumSize(QSize(35, 35))
        self.label_72.setFont(font)
        self.label_72.setPixmap(QPixmap(u":/resources/images/options.png"))
        self.label_72.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_72, 0, 0, 1, 1)


        self.gridLayout_29.addLayout(self.gridLayout_38, 0, 0, 1, 1)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, -1, 160, -1)
        self.label_32 = QLabel(self.widget_32)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font18)

        self.horizontalLayout_30.addWidget(self.label_32)

        self.horizontalSpacer_25 = QSpacerItem(25, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_25)

        self.environmentalFactorsWeight_DoubleSpinBox = QDoubleSpinBox(self.widget_32)
        self.environmentalFactorsWeight_DoubleSpinBox.setObjectName(u"environmentalFactorsWeight_DoubleSpinBox")
        sizePolicy13.setHeightForWidth(self.environmentalFactorsWeight_DoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.environmentalFactorsWeight_DoubleSpinBox.setSizePolicy(sizePolicy13)
        self.environmentalFactorsWeight_DoubleSpinBox.setFont(font)
        self.environmentalFactorsWeight_DoubleSpinBox.setFocusPolicy(Qt.WheelFocus)
        self.environmentalFactorsWeight_DoubleSpinBox.setMinimum(-10.000000000000000)
        self.environmentalFactorsWeight_DoubleSpinBox.setMaximum(10.000000000000000)
        self.environmentalFactorsWeight_DoubleSpinBox.setSingleStep(0.500000000000000)

        self.horizontalLayout_30.addWidget(self.environmentalFactorsWeight_DoubleSpinBox)

        self.warning_EF_label = QLabel(self.widget_32)
        self.warning_EF_label.setObjectName(u"warning_EF_label")
        self.warning_EF_label.setMaximumSize(QSize(25, 25))
        self.warning_EF_label.setStyleSheet(u"QToolTip{\n"
"   border: 2px solid #FFE606;\n"
"    background-color: #FEFFE4;\n"
"    color: black;\n"
"    font-family: 'Arial'; \n"
"    font-size: 12px;\n"
"    padding: 8px;\n"
"}")
        self.warning_EF_label.setPixmap(QPixmap(u":/resources/images/warning.png"))
        self.warning_EF_label.setScaledContents(True)
        self.warning_EF_label.setAlignment(Qt.AlignCenter)
        self.warning_EF_label.setIndent(0)

        self.horizontalLayout_30.addWidget(self.warning_EF_label)


        self.gridLayout_29.addLayout(self.horizontalLayout_30, 5, 0, 1, 1)


        self.gridLayout_23.addWidget(self.widget_32, 1, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.environmentalFactors_Page)

        self.gridLayout_17.addWidget(self.stackedWidget_2, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.quickest_Page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        self.useCases_Button_2.toggled.connect(self.useCases_Button.setChecked)
        self.environmentalFactors_Button_2.toggled.connect(self.environmentalFactors_Button.setChecked)
        self.technicalFactors_Button.toggled.connect(self.technicalFactors_Button_2.setChecked)
        self.hide_Button.toggled.connect(self.iconMenu_Widget.setHidden)
        self.hide_Button_2.toggled.connect(self.iconMenu_Widget.setVisible)
        self.useCases_Button.toggled.connect(self.useCases_Button_2.setChecked)
        self.hide_Button_2.toggled.connect(self.fullMenu_Widget.setHidden)
        self.technicalFactors_Button_2.toggled.connect(self.technicalFactors_Button.setChecked)
        self.dashboard_Button_2.toggled.connect(self.dashboard_Button.setChecked)
        self.hide_Button.toggled.connect(self.fullMenu_Widget.setVisible)
        self.dashboard_Button.toggled.connect(self.dashboard_Button_2.setChecked)
        self.exit_pushButton_1.clicked.connect(Main.close)
        self.environmentalFactors_Button.toggled.connect(self.environmentalFactors_Button_2.setChecked)
        self.actors_Button.toggled.connect(self.actors_Button_2.setChecked)
        self.actors_Button_2.toggled.connect(self.actors_Button.setChecked)
        self.pushButton.clicked.connect(Main.close)

        self.stackedWidget_2.setCurrentIndex(0)
        self.technicalFactorsFactor_ComboBox.setCurrentIndex(-1)
        self.environmentalFactorsFactor_ComboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.label_12.setText(QCoreApplication.translate("Main", u"PROJECTS", None))
        self.projectsSearch_LineEdit.setPlaceholderText(QCoreApplication.translate("Main", u" Search project...", None))
        ___qtablewidgetitem = self.projects_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Main", u"PROJECT_ID", None));
        ___qtablewidgetitem1 = self.projects_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Main", u"NAME", None));
        ___qtablewidgetitem2 = self.projects_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Main", u"DESCRIPTION", None));
        ___qtablewidgetitem3 = self.projects_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Main", u"CREATED AT ", None));
        ___qtablewidgetitem4 = self.projects_TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Main", u"LAST ACCESS", None));
        self.quickestHub_Button.setText("")
        self.quickestHubName_Label.setText(QCoreApplication.translate("Main", u"   QUICKEST HUB", None))
        self.pushButton.setText("")
        self.createProject_Button.setText("")
        self.label_14.setText(QCoreApplication.translate("Main", u"Create a new estimating project", None))
        self.label_13.setText(QCoreApplication.translate("Main", u"Create project", None))
        self.label_15.setText(QCoreApplication.translate("Main", u"Import project", None))
        self.label_16.setText(QCoreApplication.translate("Main", u"Open a QuickEst project from disk", None))
        self.createProject_Button_2.setText("")
        self.createProject_Button_3.setText("")
        self.label_21.setText(QCoreApplication.translate("Main", u"Export all projects", None))
        self.label_22.setText(QCoreApplication.translate("Main", u"Export all existing projects", None))
        self.projectName_Label.setText("")
        self.quickest_Button.setText("")
        ___qtablewidgetitem5 = self.comment_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem6 = self.comment_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Main", u"New Row", None));

        __sortingEnabled = self.comment_tableWidget.isSortingEnabled()
        self.comment_tableWidget.setSortingEnabled(False)
        self.comment_tableWidget.setSortingEnabled(__sortingEnabled)

        self.file_ToolButton.setText(QCoreApplication.translate("Main", u"      File    ", None))
        self.help_ToolButton.setText(QCoreApplication.translate("Main", u"    Help  ", None))
        self.exit_pushButton_1.setText("")
#if QT_CONFIG(tooltip)
        self.warning_Button.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">WARNING!</span></p><p align=\"justify\">The project estimate has reached 20000 Person-Hours. This indicates that the project is extremely large and complex.</p><p align=\"justify\">It is recommended to conduct a detailed review to assess risks, ensure feasibility, and consider possible adjustments in the scope or planning of the project to ensure its success.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.warning_Button.setText("")
        self.quickestName_Label.setText(QCoreApplication.translate("Main", u"   QUICKEST", None))
        self.hide_Button.setText("")
        self.dashboard_Button.setText("")
        self.actors_Button.setText("")
        self.useCases_Button.setText("")
        self.technicalFactors_Button.setText("")
        self.environmentalFactors_Button.setText("")
        self.close_Button.setText("")
        self.hide_Button_2.setText(QCoreApplication.translate("Main", u"  Hide", None))
        self.dashboard_Button_2.setText(QCoreApplication.translate("Main", u"  Dashboard", None))
        self.actors_Button_2.setText(QCoreApplication.translate("Main", u"  Actors", None))
        self.useCases_Button_2.setText(QCoreApplication.translate("Main", u"  Use Cases", None))
        self.technicalFactors_Button_2.setText(QCoreApplication.translate("Main", u"  Technical\n"
"  Factors", None))
        self.environmentalFactors_Button_2.setText(QCoreApplication.translate("Main", u"  Environmental\n"
"  Factors ", None))
        self.close_Button_2.setText(QCoreApplication.translate("Main", u"   Close Project", None))
        self.label.setText(QCoreApplication.translate("Main", u"Dashboard", None))
        self.generateReport_PushButton.setText(QCoreApplication.translate("Main", u"  Generate Report    ", None))
        self.totalActors_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_129.setText(QCoreApplication.translate("Main", u"Actors", None))
        self.label_124.setText("")
        self.count_simpleActors_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.count_averageActors_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.count_complexActors_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_53.setText(QCoreApplication.translate("Main", u"Simple", None))
        self.label_54.setText(QCoreApplication.translate("Main", u"Average", None))
        self.label_55.setText(QCoreApplication.translate("Main", u"Complex", None))
        self.count_simpleUC_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.count_averageUC_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.count_complexUC_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_50.setText(QCoreApplication.translate("Main", u"Simple", None))
        self.label_51.setText(QCoreApplication.translate("Main", u"Average", None))
        self.label_52.setText(QCoreApplication.translate("Main", u"Complex", None))
        self.totalUC_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_122.setText("")
        self.label_123.setText(QCoreApplication.translate("Main", u"Use Cases", None))
        self.count_irrelevantTF_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.count_mediumTF_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.count_essentialTF_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_44.setText(QCoreApplication.translate("Main", u"Irrelevant", None))
        self.label_45.setText(QCoreApplication.translate("Main", u"Medium", None))
        self.label_46.setText(QCoreApplication.translate("Main", u"Essential", None))
        self.totalTF_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_110.setText("")
        self.label_109.setText(QCoreApplication.translate("Main", u"Technical Factors", None))
        self.count_irrelevantEF_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.count_mediumEF_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.count_essentialEF_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_47.setText(QCoreApplication.translate("Main", u"Irrelevant", None))
        self.label_48.setText(QCoreApplication.translate("Main", u"Medium", None))
        self.label_49.setText(QCoreApplication.translate("Main", u"Essential", None))
        self.label_117.setText(QCoreApplication.translate("Main", u"Environmental Factors", None))
        self.label_116.setText("")
        self.totalEF_Label.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_95.setText(QCoreApplication.translate("Main", u"  Conversion Factor [CF]", None))
        self.CF_LineEdit.setText(QCoreApplication.translate("Main", u"20", None))
        self.label_90.setText(QCoreApplication.translate("Main", u"Person-Hours / UCP", None))
        self.editCF_Button.setText("")
        self.label_70.setText(QCoreApplication.translate("Main", u"Environmental Factor [EFactor]", None))
        self.label_68.setText(QCoreApplication.translate("Main", u"Adjusted Use Case Points (UCP)", None))
        self.TCF_LineEdit.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_69.setText(QCoreApplication.translate("Main", u"Technical Factor [TFactor]", None))
        self.label_84.setText(QCoreApplication.translate("Main", u"Environmental Complexity Factor [ECF]", None))
        self.EFactor_LineEdit.setText(QCoreApplication.translate("Main", u"0", None))
        self.ECF_LineEdit.setText(QCoreApplication.translate("Main", u"0", None))
        self.UCP_LineEdit.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_85.setText(QCoreApplication.translate("Main", u"Technical Complexity Factor [TCF]", None))
        self.TFactor_LineEdit.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_83.setText(QCoreApplication.translate("Main", u"Adjusted Use Case Point [UCP]", None))
        self.label_26.setText(QCoreApplication.translate("Main", u"Unadjusted Use Case Points (UUCP)", None))
        self.UUCP_LineEdit.setText(QCoreApplication.translate("Main", u"0", None))
        self.UAW_LineEdit.setText(QCoreApplication.translate("Main", u"0", None))
        self.UUCW_LineEdit.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_66.setText(QCoreApplication.translate("Main", u"Unadjusted Use Case Weight [UUCW]", None))
        self.label_67.setText(QCoreApplication.translate("Main", u"Unadjusted Use Case Points [UUCP] ", None))
        self.label_31.setText(QCoreApplication.translate("Main", u"Unadjusted Actor Weight  [UAW]", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("Main", u"Estimation Results", None))
        self.label_91.setText(QCoreApplication.translate("Main", u"Person-Hours", None))
        self.label_92.setText(QCoreApplication.translate("Main", u"Estimated Effort [E]", None))
        self.E_LineEdit.setText(QCoreApplication.translate("Main", u"0", None))
        self.E_Button.setText("")
        ___qtablewidgetitem7 = self.effortDistribution_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Main", u"Activity", None));
        ___qtablewidgetitem8 = self.effortDistribution_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Main", u"%    ", None));
        ___qtablewidgetitem9 = self.effortDistribution_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Main", u"Person-Hours", None));

        __sortingEnabled1 = self.effortDistribution_TableWidget.isSortingEnabled()
        self.effortDistribution_TableWidget.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.effortDistribution_TableWidget.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Main", u"Analysis", None));
        ___qtablewidgetitem11 = self.effortDistribution_TableWidget.item(0, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Main", u"10.0", None));
        ___qtablewidgetitem12 = self.effortDistribution_TableWidget.item(0, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem13 = self.effortDistribution_TableWidget.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Main", u"Design", None));
        ___qtablewidgetitem14 = self.effortDistribution_TableWidget.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Main", u"20.0", None));
        ___qtablewidgetitem15 = self.effortDistribution_TableWidget.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem16 = self.effortDistribution_TableWidget.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Main", u"Programming", None));
        ___qtablewidgetitem17 = self.effortDistribution_TableWidget.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Main", u"40.0", None));
        ___qtablewidgetitem18 = self.effortDistribution_TableWidget.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem19 = self.effortDistribution_TableWidget.item(3, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Main", u"Testing", None));
        ___qtablewidgetitem20 = self.effortDistribution_TableWidget.item(3, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Main", u"15.0", None));
        ___qtablewidgetitem21 = self.effortDistribution_TableWidget.item(3, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem22 = self.effortDistribution_TableWidget.item(4, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Main", u"Overloading", None));
        ___qtablewidgetitem23 = self.effortDistribution_TableWidget.item(4, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Main", u"15.0", None));
        ___qtablewidgetitem24 = self.effortDistribution_TableWidget.item(4, 2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Main", u"0", None));
        self.effortDistribution_TableWidget.setSortingEnabled(__sortingEnabled1)

        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("Main", u"Effort Distribution", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"Actors", None))
        ___qtablewidgetitem25 = self.actors_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Main", u"ACTOR_ID", None));
        ___qtablewidgetitem26 = self.actors_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Main", u"#", None));
        ___qtablewidgetitem27 = self.actors_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Main", u"Code", None));
        ___qtablewidgetitem28 = self.actors_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Main", u"Name", None));
        ___qtablewidgetitem29 = self.actors_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Main", u"Complexity", None));
        ___qtablewidgetitem30 = self.actors_TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Main", u"Comment", None));
        self.actorsSearch_LineEdit.setPlaceholderText(QCoreApplication.translate("Main", u" Search...", None))
        self.label_76.setText("")
        self.label_77.setText(QCoreApplication.translate("Main", u"Options", None))
        self.newActor_Button.setText(QCoreApplication.translate("Main", u"    New Actor", None))
        self.editActor_Button.setText(QCoreApplication.translate("Main", u"    Edit Actor", None))
        self.deleteActor_Button.setText(QCoreApplication.translate("Main", u"    Delete Actors", None))
        ___qtablewidgetitem31 = self.actorsSummary_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Main", u"Actor Type", None));
        ___qtablewidgetitem32 = self.actorsSummary_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Main", u"Description", None));
        ___qtablewidgetitem33 = self.actorsSummary_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Main", u"Weight Factor", None));
        ___qtablewidgetitem34 = self.actorsSummary_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Main", u"Actors", None));
        ___qtablewidgetitem35 = self.actorsSummary_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Main", u"UAW", None));

        __sortingEnabled2 = self.actorsSummary_TableWidget.isSortingEnabled()
        self.actorsSummary_TableWidget.setSortingEnabled(False)
        ___qtablewidgetitem36 = self.actorsSummary_TableWidget.item(0, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Main", u"Simple", None));
        ___qtablewidgetitem37 = self.actorsSummary_TableWidget.item(0, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Main", u"Another system that interacts with the system to be developed through\n"
"an application programming interface (API)", None));
        ___qtablewidgetitem38 = self.actorsSummary_TableWidget.item(0, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem39 = self.actorsSummary_TableWidget.item(0, 3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem40 = self.actorsSummary_TableWidget.item(0, 4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem41 = self.actorsSummary_TableWidget.item(1, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Main", u"Average", None));
        ___qtablewidgetitem42 = self.actorsSummary_TableWidget.item(1, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Main", u"Another system interacting through a protocol (e.g. TCP/IP) or\n"
"a person interacting through a text-mode interface.", None));
        ___qtablewidgetitem43 = self.actorsSummary_TableWidget.item(1, 2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Main", u"2", None));
        ___qtablewidgetitem44 = self.actorsSummary_TableWidget.item(1, 3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem45 = self.actorsSummary_TableWidget.item(1, 4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem46 = self.actorsSummary_TableWidget.item(2, 0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Main", u"Complex", None));
        ___qtablewidgetitem47 = self.actorsSummary_TableWidget.item(2, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Main", u"A person who interacts with the system through an interface\n"
"graphics (GUI)", None));
        ___qtablewidgetitem48 = self.actorsSummary_TableWidget.item(2, 2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Main", u"3", None));
        ___qtablewidgetitem49 = self.actorsSummary_TableWidget.item(2, 3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem50 = self.actorsSummary_TableWidget.item(2, 4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem51 = self.actorsSummary_TableWidget.item(3, 0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Main", u"TOTAL", None));
        ___qtablewidgetitem52 = self.actorsSummary_TableWidget.item(3, 3)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem53 = self.actorsSummary_TableWidget.item(3, 4)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Main", u"0", None));
        self.actorsSummary_TableWidget.setSortingEnabled(__sortingEnabled2)

        self.label_39.setText("")
        self.label_40.setText(QCoreApplication.translate("Main", u"Summary", None))
        self.useCasesSearch_LineEdit.setPlaceholderText(QCoreApplication.translate("Main", u" Search...", None))
        ___qtablewidgetitem54 = self.useCases_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("Main", u"UC_ID", None));
        ___qtablewidgetitem55 = self.useCases_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("Main", u"#", None));
        ___qtablewidgetitem56 = self.useCases_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("Main", u"Code", None));
        ___qtablewidgetitem57 = self.useCases_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("Main", u"Name", None));
        ___qtablewidgetitem58 = self.useCases_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("Main", u"Complexity", None));
        ___qtablewidgetitem59 = self.useCases_TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("Main", u"Transactions", None));
        ___qtablewidgetitem60 = self.useCases_TableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("Main", u"Comment", None));
        self.label_61.setText("")
        self.label_62.setText(QCoreApplication.translate("Main", u"Options", None))
        self.newUseCase_Button.setText(QCoreApplication.translate("Main", u"    New Use Case", None))
        self.editUseCase_Button.setText(QCoreApplication.translate("Main", u"    Edit Use Case", None))
        self.deleteUseCase_Button.setText(QCoreApplication.translate("Main", u"    Delete Use Cases", None))
        self.label_5.setText(QCoreApplication.translate("Main", u"Use Cases", None))
        self.label_41.setText("")
        self.label_42.setText(QCoreApplication.translate("Main", u"Summary", None))
        ___qtablewidgetitem61 = self.useCasesSummary_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("Main", u"Use Case Type", None));
        ___qtablewidgetitem62 = self.useCasesSummary_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("Main", u"Description", None));
        ___qtablewidgetitem63 = self.useCasesSummary_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("Main", u"Weight Factor", None));
        ___qtablewidgetitem64 = self.useCasesSummary_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("Main", u"Use Cases", None));
        ___qtablewidgetitem65 = self.useCasesSummary_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("Main", u"UUCW", None));

        __sortingEnabled3 = self.useCasesSummary_TableWidget.isSortingEnabled()
        self.useCasesSummary_TableWidget.setSortingEnabled(False)
        ___qtablewidgetitem66 = self.useCasesSummary_TableWidget.item(0, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("Main", u"Simple", None));
        ___qtablewidgetitem67 = self.useCasesSummary_TableWidget.item(0, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("Main", u"Number of Transactions: from 1 to 3", None));
        ___qtablewidgetitem68 = self.useCasesSummary_TableWidget.item(0, 2)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem69 = self.useCasesSummary_TableWidget.item(0, 3)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem70 = self.useCasesSummary_TableWidget.item(0, 4)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem71 = self.useCasesSummary_TableWidget.item(1, 0)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("Main", u"Average", None));
        ___qtablewidgetitem72 = self.useCasesSummary_TableWidget.item(1, 1)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("Main", u"Number of Transactions: from 4 to 7", None));
        ___qtablewidgetitem73 = self.useCasesSummary_TableWidget.item(1, 2)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("Main", u"2", None));
        ___qtablewidgetitem74 = self.useCasesSummary_TableWidget.item(1, 3)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem75 = self.useCasesSummary_TableWidget.item(1, 4)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem76 = self.useCasesSummary_TableWidget.item(2, 0)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("Main", u"Complex", None));
        ___qtablewidgetitem77 = self.useCasesSummary_TableWidget.item(2, 1)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("Main", u"Numer of Transactions: more than 7", None));
        ___qtablewidgetitem78 = self.useCasesSummary_TableWidget.item(2, 2)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("Main", u"3", None));
        ___qtablewidgetitem79 = self.useCasesSummary_TableWidget.item(2, 3)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem80 = self.useCasesSummary_TableWidget.item(2, 4)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem81 = self.useCasesSummary_TableWidget.item(3, 0)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("Main", u"TOTAL", None));
        ___qtablewidgetitem82 = self.useCasesSummary_TableWidget.item(3, 3)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem83 = self.useCasesSummary_TableWidget.item(3, 4)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("Main", u"0", None));
        self.useCasesSummary_TableWidget.setSortingEnabled(__sortingEnabled3)

        self.label_4.setText(QCoreApplication.translate("Main", u"Technical Factors", None))
        ___qtablewidgetitem84 = self.technicalFactors_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("Main", u"Total", None));
        ___qtablewidgetitem85 = self.technicalFactors_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("Main", u"Factor", None));
        ___qtablewidgetitem86 = self.technicalFactors_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("Main", u"Description", None));
        ___qtablewidgetitem87 = self.technicalFactors_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("Main", u"Weight", None));
        ___qtablewidgetitem88 = self.technicalFactors_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("Main", u"Influence", None));
        ___qtablewidgetitem89 = self.technicalFactors_TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("Main", u"Result", None));
        ___qtablewidgetitem90 = self.technicalFactors_TableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("Main", u"Comment", None));

        __sortingEnabled4 = self.technicalFactors_TableWidget.isSortingEnabled()
        self.technicalFactors_TableWidget.setSortingEnabled(False)
        ___qtablewidgetitem91 = self.technicalFactors_TableWidget.item(0, 1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("Main", u"T01", None));
        ___qtablewidgetitem92 = self.technicalFactors_TableWidget.item(0, 2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("Main", u"Distributed system", None));
        ___qtablewidgetitem93 = self.technicalFactors_TableWidget.item(0, 3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("Main", u"2", None));
        ___qtablewidgetitem94 = self.technicalFactors_TableWidget.item(0, 4)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem95 = self.technicalFactors_TableWidget.item(0, 5)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem96 = self.technicalFactors_TableWidget.item(1, 1)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("Main", u"T02", None));
        ___qtablewidgetitem97 = self.technicalFactors_TableWidget.item(1, 2)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("Main", u"Performance or response time", None));
        ___qtablewidgetitem98 = self.technicalFactors_TableWidget.item(1, 3)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("Main", u"2", None));
        ___qtablewidgetitem99 = self.technicalFactors_TableWidget.item(1, 4)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem100 = self.technicalFactors_TableWidget.item(1, 5)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem101 = self.technicalFactors_TableWidget.item(2, 1)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("Main", u"T03", None));
        ___qtablewidgetitem102 = self.technicalFactors_TableWidget.item(2, 2)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("Main", u"End user efficiency", None));
        ___qtablewidgetitem103 = self.technicalFactors_TableWidget.item(2, 3)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem104 = self.technicalFactors_TableWidget.item(2, 4)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem105 = self.technicalFactors_TableWidget.item(2, 5)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem106 = self.technicalFactors_TableWidget.item(3, 1)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("Main", u"T04", None));
        ___qtablewidgetitem107 = self.technicalFactors_TableWidget.item(3, 2)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("Main", u"Complex internal processing", None));
        ___qtablewidgetitem108 = self.technicalFactors_TableWidget.item(3, 3)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem109 = self.technicalFactors_TableWidget.item(3, 4)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem110 = self.technicalFactors_TableWidget.item(3, 5)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem111 = self.technicalFactors_TableWidget.item(4, 1)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("Main", u"T05", None));
        ___qtablewidgetitem112 = self.technicalFactors_TableWidget.item(4, 2)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("Main", u"The code must be reusable (reusability)", None));
        ___qtablewidgetitem113 = self.technicalFactors_TableWidget.item(4, 3)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem114 = self.technicalFactors_TableWidget.item(4, 4)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem115 = self.technicalFactors_TableWidget.item(4, 5)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem116 = self.technicalFactors_TableWidget.item(5, 1)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("Main", u"T06", None));
        ___qtablewidgetitem117 = self.technicalFactors_TableWidget.item(5, 2)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("Main", u"Ease of installation", None));
        ___qtablewidgetitem118 = self.technicalFactors_TableWidget.item(5, 3)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("Main", u"0.5", None));
        ___qtablewidgetitem119 = self.technicalFactors_TableWidget.item(5, 4)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem120 = self.technicalFactors_TableWidget.item(5, 5)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem121 = self.technicalFactors_TableWidget.item(6, 1)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("Main", u"T07", None));
        ___qtablewidgetitem122 = self.technicalFactors_TableWidget.item(6, 2)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("Main", u"Easy to use", None));
        ___qtablewidgetitem123 = self.technicalFactors_TableWidget.item(6, 3)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("Main", u"0.5", None));
        ___qtablewidgetitem124 = self.technicalFactors_TableWidget.item(6, 4)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem125 = self.technicalFactors_TableWidget.item(6, 5)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem126 = self.technicalFactors_TableWidget.item(7, 1)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("Main", u"T08", None));
        ___qtablewidgetitem127 = self.technicalFactors_TableWidget.item(7, 2)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("Main", u"Portability", None));
        ___qtablewidgetitem128 = self.technicalFactors_TableWidget.item(7, 3)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("Main", u"2", None));
        ___qtablewidgetitem129 = self.technicalFactors_TableWidget.item(7, 4)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem130 = self.technicalFactors_TableWidget.item(7, 5)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem131 = self.technicalFactors_TableWidget.item(8, 1)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("Main", u"T09", None));
        ___qtablewidgetitem132 = self.technicalFactors_TableWidget.item(8, 2)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("Main", u"Ease of change", None));
        ___qtablewidgetitem133 = self.technicalFactors_TableWidget.item(8, 3)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem134 = self.technicalFactors_TableWidget.item(8, 4)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem135 = self.technicalFactors_TableWidget.item(8, 5)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem136 = self.technicalFactors_TableWidget.item(9, 1)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("Main", u"T10", None));
        ___qtablewidgetitem137 = self.technicalFactors_TableWidget.item(9, 2)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("Main", u"Concurrence", None));
        ___qtablewidgetitem138 = self.technicalFactors_TableWidget.item(9, 3)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem139 = self.technicalFactors_TableWidget.item(9, 4)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem140 = self.technicalFactors_TableWidget.item(9, 5)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem141 = self.technicalFactors_TableWidget.item(10, 1)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("Main", u"T11", None));
        ___qtablewidgetitem142 = self.technicalFactors_TableWidget.item(10, 2)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("Main", u"Special security features", None));
        ___qtablewidgetitem143 = self.technicalFactors_TableWidget.item(10, 3)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem144 = self.technicalFactors_TableWidget.item(10, 4)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem145 = self.technicalFactors_TableWidget.item(10, 5)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem146 = self.technicalFactors_TableWidget.item(11, 1)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("Main", u"T12", None));
        ___qtablewidgetitem147 = self.technicalFactors_TableWidget.item(11, 2)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("Main", u"Provides direct access to third parties", None));
        ___qtablewidgetitem148 = self.technicalFactors_TableWidget.item(11, 3)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem149 = self.technicalFactors_TableWidget.item(11, 4)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem150 = self.technicalFactors_TableWidget.item(11, 5)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem151 = self.technicalFactors_TableWidget.item(12, 1)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("Main", u"T13", None));
        ___qtablewidgetitem152 = self.technicalFactors_TableWidget.item(12, 2)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("Main", u"Special user training required", None));
        ___qtablewidgetitem153 = self.technicalFactors_TableWidget.item(12, 3)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem154 = self.technicalFactors_TableWidget.item(12, 4)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem155 = self.technicalFactors_TableWidget.item(12, 5)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem156 = self.technicalFactors_TableWidget.item(13, 0)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("Main", u"TFactor: 0", None));
        self.technicalFactors_TableWidget.setSortingEnabled(__sortingEnabled4)

        self.cancelTechnicalFactor_Button.setText(QCoreApplication.translate("Main", u"  Cancel", None))
        self.saveTechnicalFactor_Button.setText(QCoreApplication.translate("Main", u"  Save", None))
        self.label_6.setText(QCoreApplication.translate("Main", u"Factor", None))
        self.technicalFactorsFactor_ComboBox.setItemText(0, QCoreApplication.translate("Main", u"T01 \u2013 Distributed system", None))
        self.technicalFactorsFactor_ComboBox.setItemText(1, QCoreApplication.translate("Main", u"T02 \u2013 Performance or response time", None))
        self.technicalFactorsFactor_ComboBox.setItemText(2, QCoreApplication.translate("Main", u"T03 \u2013 End user efficiency", None))
        self.technicalFactorsFactor_ComboBox.setItemText(3, QCoreApplication.translate("Main", u"T04 \u2013 Complex internal processing", None))
        self.technicalFactorsFactor_ComboBox.setItemText(4, QCoreApplication.translate("Main", u"T05 \u2013 The code must be reusable", None))
        self.technicalFactorsFactor_ComboBox.setItemText(5, QCoreApplication.translate("Main", u"T06 \u2013 Easy of installation", None))
        self.technicalFactorsFactor_ComboBox.setItemText(6, QCoreApplication.translate("Main", u"T07 \u2013 Easy to use", None))
        self.technicalFactorsFactor_ComboBox.setItemText(7, QCoreApplication.translate("Main", u"T08 \u2013 Portability", None))
        self.technicalFactorsFactor_ComboBox.setItemText(8, QCoreApplication.translate("Main", u"T09 \u2013 Easy of change", None))
        self.technicalFactorsFactor_ComboBox.setItemText(9, QCoreApplication.translate("Main", u"T10 \u2013 Concurrence", None))
        self.technicalFactorsFactor_ComboBox.setItemText(10, QCoreApplication.translate("Main", u"T11 \u2013 Special security features", None))
        self.technicalFactorsFactor_ComboBox.setItemText(11, QCoreApplication.translate("Main", u"T12 \u2013 Provides direct access to third parties", None))
        self.technicalFactorsFactor_ComboBox.setItemText(12, QCoreApplication.translate("Main", u"T13 \u2013 Special user training required", None))

        self.technicalFactorsFactor_ComboBox.setPlaceholderText(QCoreApplication.translate("Main", u" Select Technical Factor", None))
        self.label_8.setText(QCoreApplication.translate("Main", u"Influence", None))
        self.technicalFactors_RadioButton_0.setText(QCoreApplication.translate("Main", u"0", None))
        self.technicalFactors_RadioButton_1.setText(QCoreApplication.translate("Main", u"1", None))
        self.technicalFactors_RadioButton_2.setText(QCoreApplication.translate("Main", u"2", None))
        self.technicalFactors_RadioButton_3.setText(QCoreApplication.translate("Main", u"3", None))
        self.technicalFactors_RadioButton_4.setText(QCoreApplication.translate("Main", u"4", None))
        self.technicalFactors_RadioButton_5.setText(QCoreApplication.translate("Main", u"5", None))
#if QT_CONFIG(tooltip)
        self.technicalFactorsInfo_Label.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.technicalFactorsInfo_Label.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.technicalFactorsInfo_Label.setText("")
        self.label_9.setText(QCoreApplication.translate("Main", u"Comment", None))
        self.technicalFactorsCommentCounter_Label.setText(QCoreApplication.translate("Main", u"0/300", None))
        self.label_64.setText(QCoreApplication.translate("Main", u"Manage Technical Factors", None))
        self.label_63.setText("")
        self.label_7.setText(QCoreApplication.translate("Main", u"Weight", None))
        self.warning_TF_label.setText("")
        ___qtablewidgetitem157 = self.technicalFactorsSummary_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("Main", u"Factor Type", None));
        ___qtablewidgetitem158 = self.technicalFactorsSummary_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("Main", u"Description", None));
        ___qtablewidgetitem159 = self.technicalFactorsSummary_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("Main", u"Factors", None));

        __sortingEnabled5 = self.technicalFactorsSummary_TableWidget.isSortingEnabled()
        self.technicalFactorsSummary_TableWidget.setSortingEnabled(False)
        ___qtablewidgetitem160 = self.technicalFactorsSummary_TableWidget.item(0, 0)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("Main", u"Irrelevant", None));
        ___qtablewidgetitem161 = self.technicalFactorsSummary_TableWidget.item(0, 1)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("Main", u"Influence: from 0 to 2", None));
        ___qtablewidgetitem162 = self.technicalFactorsSummary_TableWidget.item(0, 2)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("Main", u"13", None));
        ___qtablewidgetitem163 = self.technicalFactorsSummary_TableWidget.item(1, 0)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("Main", u"Medium", None));
        ___qtablewidgetitem164 = self.technicalFactorsSummary_TableWidget.item(1, 1)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("Main", u"Influence: from 3 to 4", None));
        ___qtablewidgetitem165 = self.technicalFactorsSummary_TableWidget.item(1, 2)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem166 = self.technicalFactorsSummary_TableWidget.item(2, 0)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("Main", u"Essential", None));
        ___qtablewidgetitem167 = self.technicalFactorsSummary_TableWidget.item(2, 1)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("Main", u"Influence: 5", None));
        ___qtablewidgetitem168 = self.technicalFactorsSummary_TableWidget.item(2, 2)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem169 = self.technicalFactorsSummary_TableWidget.item(3, 0)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("Main", u"TOTAL", None));
        ___qtablewidgetitem170 = self.technicalFactorsSummary_TableWidget.item(3, 2)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("Main", u"13", None));
        self.technicalFactorsSummary_TableWidget.setSortingEnabled(__sortingEnabled5)

        self.label_65.setText(QCoreApplication.translate("Main", u"Summary", None))
        self.label_73.setText("")
        ___qtablewidgetitem171 = self.environmentalFactorsSummary_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("Main", u"Factor Type", None));
        ___qtablewidgetitem172 = self.environmentalFactorsSummary_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("Main", u"Description", None));
        ___qtablewidgetitem173 = self.environmentalFactorsSummary_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("Main", u"Factors", None));

        __sortingEnabled6 = self.environmentalFactorsSummary_TableWidget.isSortingEnabled()
        self.environmentalFactorsSummary_TableWidget.setSortingEnabled(False)
        ___qtablewidgetitem174 = self.environmentalFactorsSummary_TableWidget.item(0, 0)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("Main", u"Irrelevant", None));
        ___qtablewidgetitem175 = self.environmentalFactorsSummary_TableWidget.item(0, 1)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("Main", u"Influence: from 0 to 2", None));
        ___qtablewidgetitem176 = self.environmentalFactorsSummary_TableWidget.item(0, 2)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("Main", u"8", None));
        ___qtablewidgetitem177 = self.environmentalFactorsSummary_TableWidget.item(1, 0)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("Main", u"Medium", None));
        ___qtablewidgetitem178 = self.environmentalFactorsSummary_TableWidget.item(1, 1)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("Main", u"Influence: from 3 to 4", None));
        ___qtablewidgetitem179 = self.environmentalFactorsSummary_TableWidget.item(1, 2)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem180 = self.environmentalFactorsSummary_TableWidget.item(2, 0)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("Main", u"Essential", None));
        ___qtablewidgetitem181 = self.environmentalFactorsSummary_TableWidget.item(2, 1)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("Main", u"Influence: 5", None));
        ___qtablewidgetitem182 = self.environmentalFactorsSummary_TableWidget.item(2, 2)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem183 = self.environmentalFactorsSummary_TableWidget.item(3, 0)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("Main", u"TOTAL", None));
        ___qtablewidgetitem184 = self.environmentalFactorsSummary_TableWidget.item(3, 2)
        ___qtablewidgetitem184.setText(QCoreApplication.translate("Main", u"8", None));
        self.environmentalFactorsSummary_TableWidget.setSortingEnabled(__sortingEnabled6)

        self.label_57.setText(QCoreApplication.translate("Main", u"Summary", None))
        self.label_58.setText("")
        ___qtablewidgetitem185 = self.environmentalFactors_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("Main", u"Total", None));
        ___qtablewidgetitem186 = self.environmentalFactors_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem186.setText(QCoreApplication.translate("Main", u"Factor", None));
        ___qtablewidgetitem187 = self.environmentalFactors_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("Main", u"Description", None));
        ___qtablewidgetitem188 = self.environmentalFactors_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("Main", u"Weight", None));
        ___qtablewidgetitem189 = self.environmentalFactors_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("Main", u"Influence", None));
        ___qtablewidgetitem190 = self.environmentalFactors_TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem190.setText(QCoreApplication.translate("Main", u"Result", None));
        ___qtablewidgetitem191 = self.environmentalFactors_TableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem191.setText(QCoreApplication.translate("Main", u"Comment", None));

        __sortingEnabled7 = self.environmentalFactors_TableWidget.isSortingEnabled()
        self.environmentalFactors_TableWidget.setSortingEnabled(False)
        ___qtablewidgetitem192 = self.environmentalFactors_TableWidget.item(0, 1)
        ___qtablewidgetitem192.setText(QCoreApplication.translate("Main", u"E1", None));
        ___qtablewidgetitem193 = self.environmentalFactors_TableWidget.item(0, 2)
        ___qtablewidgetitem193.setText(QCoreApplication.translate("Main", u"Familiarity with UML", None));
        ___qtablewidgetitem194 = self.environmentalFactors_TableWidget.item(0, 3)
        ___qtablewidgetitem194.setText(QCoreApplication.translate("Main", u"1.5", None));
        ___qtablewidgetitem195 = self.environmentalFactors_TableWidget.item(0, 4)
        ___qtablewidgetitem195.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem196 = self.environmentalFactors_TableWidget.item(0, 5)
        ___qtablewidgetitem196.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem197 = self.environmentalFactors_TableWidget.item(1, 1)
        ___qtablewidgetitem197.setText(QCoreApplication.translate("Main", u"E2", None));
        ___qtablewidgetitem198 = self.environmentalFactors_TableWidget.item(1, 2)
        ___qtablewidgetitem198.setText(QCoreApplication.translate("Main", u"Application experience", None));
        ___qtablewidgetitem199 = self.environmentalFactors_TableWidget.item(1, 3)
        ___qtablewidgetitem199.setText(QCoreApplication.translate("Main", u"0.5", None));
        ___qtablewidgetitem200 = self.environmentalFactors_TableWidget.item(1, 4)
        ___qtablewidgetitem200.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem201 = self.environmentalFactors_TableWidget.item(1, 5)
        ___qtablewidgetitem201.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem202 = self.environmentalFactors_TableWidget.item(2, 1)
        ___qtablewidgetitem202.setText(QCoreApplication.translate("Main", u"E3", None));
        ___qtablewidgetitem203 = self.environmentalFactors_TableWidget.item(2, 2)
        ___qtablewidgetitem203.setText(QCoreApplication.translate("Main", u"Experience in Object Orientation", None));
        ___qtablewidgetitem204 = self.environmentalFactors_TableWidget.item(2, 3)
        ___qtablewidgetitem204.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem205 = self.environmentalFactors_TableWidget.item(2, 4)
        ___qtablewidgetitem205.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem206 = self.environmentalFactors_TableWidget.item(2, 5)
        ___qtablewidgetitem206.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem207 = self.environmentalFactors_TableWidget.item(3, 1)
        ___qtablewidgetitem207.setText(QCoreApplication.translate("Main", u"E4", None));
        ___qtablewidgetitem208 = self.environmentalFactors_TableWidget.item(3, 2)
        ___qtablewidgetitem208.setText(QCoreApplication.translate("Main", u"Lead Analyst Capability", None));
        ___qtablewidgetitem209 = self.environmentalFactors_TableWidget.item(3, 3)
        ___qtablewidgetitem209.setText(QCoreApplication.translate("Main", u"0.5", None));
        ___qtablewidgetitem210 = self.environmentalFactors_TableWidget.item(3, 4)
        ___qtablewidgetitem210.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem211 = self.environmentalFactors_TableWidget.item(3, 5)
        ___qtablewidgetitem211.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem212 = self.environmentalFactors_TableWidget.item(4, 1)
        ___qtablewidgetitem212.setText(QCoreApplication.translate("Main", u"E5", None));
        ___qtablewidgetitem213 = self.environmentalFactors_TableWidget.item(4, 2)
        ___qtablewidgetitem213.setText(QCoreApplication.translate("Main", u"Motivation", None));
        ___qtablewidgetitem214 = self.environmentalFactors_TableWidget.item(4, 3)
        ___qtablewidgetitem214.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem215 = self.environmentalFactors_TableWidget.item(4, 4)
        ___qtablewidgetitem215.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem216 = self.environmentalFactors_TableWidget.item(4, 5)
        ___qtablewidgetitem216.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem217 = self.environmentalFactors_TableWidget.item(5, 1)
        ___qtablewidgetitem217.setText(QCoreApplication.translate("Main", u"E6", None));
        ___qtablewidgetitem218 = self.environmentalFactors_TableWidget.item(5, 2)
        ___qtablewidgetitem218.setText(QCoreApplication.translate("Main", u"Stability of requirements", None));
        ___qtablewidgetitem219 = self.environmentalFactors_TableWidget.item(5, 3)
        ___qtablewidgetitem219.setText(QCoreApplication.translate("Main", u"2", None));
        ___qtablewidgetitem220 = self.environmentalFactors_TableWidget.item(5, 4)
        ___qtablewidgetitem220.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem221 = self.environmentalFactors_TableWidget.item(5, 5)
        ___qtablewidgetitem221.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem222 = self.environmentalFactors_TableWidget.item(6, 1)
        ___qtablewidgetitem222.setText(QCoreApplication.translate("Main", u"E7", None));
        ___qtablewidgetitem223 = self.environmentalFactors_TableWidget.item(6, 2)
        ___qtablewidgetitem223.setText(QCoreApplication.translate("Main", u"Part-time workers", None));
        ___qtablewidgetitem224 = self.environmentalFactors_TableWidget.item(6, 3)
        ___qtablewidgetitem224.setText(QCoreApplication.translate("Main", u"-1", None));
        ___qtablewidgetitem225 = self.environmentalFactors_TableWidget.item(6, 4)
        ___qtablewidgetitem225.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem226 = self.environmentalFactors_TableWidget.item(6, 5)
        ___qtablewidgetitem226.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem227 = self.environmentalFactors_TableWidget.item(7, 1)
        ___qtablewidgetitem227.setText(QCoreApplication.translate("Main", u"E8", None));
        ___qtablewidgetitem228 = self.environmentalFactors_TableWidget.item(7, 2)
        ___qtablewidgetitem228.setText(QCoreApplication.translate("Main", u"Programming language difficulty", None));
        ___qtablewidgetitem229 = self.environmentalFactors_TableWidget.item(7, 3)
        ___qtablewidgetitem229.setText(QCoreApplication.translate("Main", u"-1", None));
        ___qtablewidgetitem230 = self.environmentalFactors_TableWidget.item(7, 4)
        ___qtablewidgetitem230.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem231 = self.environmentalFactors_TableWidget.item(7, 5)
        ___qtablewidgetitem231.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem232 = self.environmentalFactors_TableWidget.item(8, 0)
        ___qtablewidgetitem232.setText(QCoreApplication.translate("Main", u"EFactor: 0", None));
        self.environmentalFactors_TableWidget.setSortingEnabled(__sortingEnabled7)

        self.label_3.setText(QCoreApplication.translate("Main", u"Environmental Factors", None))
        self.cancelEnvironmentalFactor_Button.setText(QCoreApplication.translate("Main", u"  Cancel", None))
        self.saveEnvironmentalFactor_Button.setText(QCoreApplication.translate("Main", u"  Save", None))
        self.label_23.setText(QCoreApplication.translate("Main", u"Factor", None))
        self.environmentalFactorsFactor_ComboBox.setItemText(0, QCoreApplication.translate("Main", u"E1 \u2013 Familiarity with the project model used", None))
        self.environmentalFactorsFactor_ComboBox.setItemText(1, QCoreApplication.translate("Main", u"E2 \u2013 Application experience", None))
        self.environmentalFactorsFactor_ComboBox.setItemText(2, QCoreApplication.translate("Main", u"E3 \u2013 Object oriented experience", None))
        self.environmentalFactorsFactor_ComboBox.setItemText(3, QCoreApplication.translate("Main", u"E4 \u2013 Lead analyst capability", None))
        self.environmentalFactorsFactor_ComboBox.setItemText(4, QCoreApplication.translate("Main", u"E5 \u2013 Motivation", None))
        self.environmentalFactorsFactor_ComboBox.setItemText(5, QCoreApplication.translate("Main", u"E6 \u2013 Stability of requirements", None))
        self.environmentalFactorsFactor_ComboBox.setItemText(6, QCoreApplication.translate("Main", u"E7 \u2013 Part time workers", None))
        self.environmentalFactorsFactor_ComboBox.setItemText(7, QCoreApplication.translate("Main", u"E8 \u2013 Programming language difficulty", None))

        self.environmentalFactorsFactor_ComboBox.setPlaceholderText(QCoreApplication.translate("Main", u" Select Environmental Factor", None))
        self.label_24.setText(QCoreApplication.translate("Main", u"Influence", None))
        self.environmentalFactors_RadioButton_0.setText(QCoreApplication.translate("Main", u"0", None))
        self.environmentalFactors_RadioButton_1.setText(QCoreApplication.translate("Main", u"1", None))
        self.environmentalFactors_RadioButton_2.setText(QCoreApplication.translate("Main", u"2", None))
        self.environmentalFactors_RadioButton_3.setText(QCoreApplication.translate("Main", u"3", None))
        self.environmentalFactors_RadioButton_4.setText(QCoreApplication.translate("Main", u"4", None))
        self.environmentalFactors_RadioButton_5.setText(QCoreApplication.translate("Main", u"5", None))
#if QT_CONFIG(tooltip)
        self.environmentalFactorsInfo_Label.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.environmentalFactorsInfo_Label.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.environmentalFactorsInfo_Label.setText("")
        self.label_25.setText(QCoreApplication.translate("Main", u"Comment", None))
        self.environmentalFactorsCommentCounter_Label.setText(QCoreApplication.translate("Main", u"0/300", None))
        self.label_71.setText(QCoreApplication.translate("Main", u"Manage Environmental Factors", None))
        self.label_72.setText("")
        self.label_32.setText(QCoreApplication.translate("Main", u"Weight", None))
        self.warning_EF_label.setText("")
    # retranslateUi

