# This Python file uses the following encoding: utf-8
# view/dashboard_view.py

import config
from Utils.widget_config import WidgetConfig
from PySide6.QtWidgets import QHeaderView, QWidget, QLabel, QGraphicsScene
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtGui import QColor, QBrush, QPen, QPainter, QFont
from PySide6.QtCore import Qt, Signal, QRectF

class DashboardView(QWidget):
    """
    Class implementing the view for the dashboard in the application.

    It handles the visualization of project metrics and charts, providing a summary of the data. It sets up charts and tables displaying important metrics, buttons to update data, and options to export information, facilitating project monitoring and analysis.

    Attributes
    ----------
    percentages_data : Signal
        Signal emitted with effort distribution percentages data.
    UUCP_updated : Signal
        Signal emitted when UUCP values are updated.
    TCF_updated : Signal
        Signal emitted when TCF values are updated.
    ECF_updated : Signal
        Signal emitted when ECF values are updated.
    report_generation : Signal
        Signal emitted to trigger report generation.
    cf_data : Signal
        Signal emitted with conversion factor data.

    Methods
    -------
    """

    percentages_data = Signal(dict)
    UUCP_updated = Signal(float, float)
    TCF_updated = Signal(float)
    ECF_updated = Signal(float)
    report_generation = Signal()
    cf_data = Signal(float)

    def __init__(self, parent=None):
        """
        Initialize the DashboardView.

        Parameters
        ----------
        parent : QWidget, optional
            The parent widget of this view.
        """
        super().__init__(parent)
        self.main = parent  # Main as parent class
        self.ui = self.main.ui  # Use the UI initialized in Main
        self.effort_table = self.ui.effortDistribution_TableWidget
        self.init_donut_chart()
        self.update_donut_chart()
        self.setup_dashboard_ui()

    def setup_dashboard_ui(self):
        """
        Setup the user interface elements for the dashboard.
        """
        # Effort Distribution
        self.effort_table.setCornerWidget(QWidget())
        self.effort_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.effort_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.effort_table.horizontalHeader().sectionClicked.connect(lambda index: self.configure_effort_distribution() if index == 1 else None)

        # Conversion Factor
        self.ui.editCF_Button.clicked.connect(self.edit_cf)

        # Excel Report
        self.ui.generateReport_PushButton.clicked.connect(self.generate_report)

    def generate_report(self):
        """
        Emit signal to generate a report.
        """
        self.report_generation.emit()

    def display_message(self, title, message, icon_path, dialog_type='simple_message'):
        """
        Display a message dialog.

        Parameters
        ----------
        title : str
            Title of the message dialog.
        message : str
            Message content.
        icon_path : str
            Path to the icon for the dialog.
        dialog_type : str, optional
            Type of dialog, default is 'simple_message'.

        Returns
        -------
        QDialog
            The message dialog.
        """
        return WidgetConfig.show_message_dialog(title, message, icon_path, dialog_type)

    def edit_cf(self):
        """
        Emit signal to edit the conversion factor.
        """
        cf = self.ui.CF_LineEdit.text()
        self.cf_data.emit(float(cf))

    def update_cf(self, cf):
        """
        Update the conversion factor display.

        Parameters
        ----------
        cf : float
            The conversion factor.
        """
        self.ui.CF_LineEdit.setText(str(cf))

    def configure_effort_distribution(self):
        """
        Configure the effort distribution data and emit the percentages_data signal.
        """
        percentages = {
            "analysis": self.effort_table.item(0, 1).text(),
            "design": self.effort_table.item(1, 1).text(),
            "programming": self.effort_table.item(2, 1).text(),
            "testing": self.effort_table.item(3, 1).text(),
            "overloading": self.effort_table.item(4, 1).text()
        }
        self.percentages_data.emit(percentages)

    def update_effort_distribution(self, percentages=None, person_hours=None, total_effort=None):
        """
        Update the effort distribution table and donut chart.

        Parameters
        ----------
        percentages : dict, optional
            Dictionary of effort distribution percentages.
        person_hours : dict, optional
            Dictionary of effort distribution in person-hours.
        total_effort : float, optional
            Total effort in person-hours.
        """
        if percentages is not None:
            self.effort_table.item(0, 1).setText(str(percentages['analysis']))
            self.effort_table.item(1, 1).setText(str(percentages['design']))
            self.effort_table.item(2, 1).setText(str(percentages['programming']))
            self.effort_table.item(3, 1).setText(str(percentages['testing']))
            self.effort_table.item(4, 1).setText(str(percentages['overloading']))
            self.update_donut_chart()
        if person_hours is not None:
            self.effort_table.item(0, 2).setText(str(person_hours['analysis']))
            self.effort_table.item(1, 2).setText(str(person_hours['design']))
            self.effort_table.item(2, 2).setText(str(person_hours['programming']))
            self.effort_table.item(3, 2).setText(str(person_hours['testing']))
            self.effort_table.item(4, 2).setText(str(person_hours['overloading']))
            if total_effort is not None:
                if total_effort > config.TOTAL_EFFORT:
                    self.ui.warning_Button.setVisible(True)
                else:
                    self.ui.warning_Button.setVisible(False)
                self.totalEffort_Label.setText(f"Total Effort\n{total_effort}\nPerson-Hours")

    def init_donut_chart(self):
        """
        Initialize the donut chart for effort distribution.
        """
        self.chart = QChart()

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignRight)
        self.chart.legend().setLabelColor(Qt.white)

        self.chart.setGeometry(0, 0, 440, 440)
        self.chart.setBackgroundBrush(QBrush(Qt.transparent))
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setBackgroundBrush(QBrush(QColor('#22577A')))

        self.chartView.viewport().setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents, False)
        self.ui.graphicsView.viewport().setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents, False)

        self.totalEffort_Label = QLabel("Total Effort\n0\nHours-Person", self.chartView)
        self.totalEffort_Label.setAlignment(Qt.AlignCenter)
        self.totalEffort_Label.setStyleSheet("color: white; background-color: rgba(255, 255, 255, 0); font-family: Arial;")

        self.totalEffort_Label.setGeometry(QRectF(self.chartView.rect()).center().x() - 224, QRectF(self.chartView.rect()).center().y() - 50, 100, 50)

        scene = QGraphicsScene(165, 205, self.ui.graphicsView.width(), self.ui.graphicsView.height())
        scene.addWidget(self.chartView)

        self.ui.graphicsView.setScene(scene)

    def update_donut_chart(self):
        """
        Update the data in the donut chart.
        """
        analysisPercentage = float(self.effort_table.item(0, 1).text())
        designPercentage = float(self.effort_table.item(1, 1).text())
        programmingPercentage = float(self.effort_table.item(2, 1).text())
        testingPercentage = float(self.effort_table.item(3, 1).text())
        overloadingPercentage = float(self.effort_table.item(4, 1).text())

        series = QPieSeries()
        series.setHoleSize(0.5)
        series.setPieSize(0.80)

        series.append("Analysis", analysisPercentage).setColor(QColor("#FFA4A4"))
        series.append("Design", designPercentage).setColor(QColor("#FDDEA2"))
        series.append("Programming", programmingPercentage).setColor(QColor("#93F3E3"))
        series.append("Testing", testingPercentage).setColor(QColor("#FDFFAA"))
        series.append("Overloading", overloadingPercentage).setColor(QColor("#7CE0FF"))

        pen = QPen(Qt.black)
        pen.setWidth(2)

        for slice in series.slices():
            slice.setPen(pen)

        self.chart.removeAllSeries()
        self.chart.addSeries(series)

        markers = self.chart.legend().markers()
        for marker in markers:
            marker.setFont(QFont("Arial", 18))

    def set_actors_data(self, actors_count, total_actors, UAW):
        """
        Set actor data in the UI and update UUCP.

        Parameters
        ----------
        actors_count : dict
            Dictionary of actor counts by complexity.
        total_actors : int
            Total number of actors.
        UAW : float
            Unadjusted Actor Weight.
        """
        self.ui.count_simpleActors_Label.setText(str(actors_count['Simple']))
        self.ui.count_averageActors_Label.setText(str(actors_count['Average']))
        self.ui.count_complexActors_Label.setText(str(actors_count['Complex']))
        self.ui.totalActors_Label.setText(str(total_actors))
        self.ui.UAW_LineEdit.setText(str(UAW))

        UUCW = float(self.ui.UUCW_LineEdit.text())
        self.UUCP_updated.emit(UAW, UUCW)

    def set_use_cases_data(self, useCases_count, total_useCases, UUCW):
        """
        Set use case data in the UI and update UUCP.

        Parameters
        ----------
        useCases_count : dict
            Dictionary of use case counts by complexity.
        total_useCases : int
            Total number of use cases.
        UUCW : float
            Unadjusted Use Case Weight.
        """
        self.ui.count_simpleUC_Label.setText(str(useCases_count['Simple']))
        self.ui.count_averageUC_Label.setText(str(useCases_count['Average']))
        self.ui.count_complexUC_Label.setText(str(useCases_count['Complex']))
        self.ui.totalUC_Label.setText(str(total_useCases))
        self.ui.UUCW_LineEdit.setText(str(UUCW))

        UAW = float(self.ui.UAW_LineEdit.text())
        self.UUCP_updated.emit(UAW, UUCW)

    def set_technical_factors_data(self, technicalFactors_count, TFactor):
        """
        Set technical factors data in the UI and update TCF.

        Parameters
        ----------
        technicalFactors_count : dict
            Dictionary of technical factors counts by relevance.
        TFactor : float
            Technical Factor.
        """
        self.ui.count_irrelevantTF_Label.setText(str(technicalFactors_count['irrelevant']))
        self.ui.count_mediumTF_Label.setText(str(technicalFactors_count['medium']))
        self.ui.count_essentialTF_Label.setText(str(technicalFactors_count['essential']))
        self.ui.totalTF_Label.setText("13")

        self.ui.TFactor_LineEdit.setText(str(TFactor))

        self.TCF_updated.emit(TFactor)

    def set_environmental_factors_data(self, environmentalFactors_count, EFactor):
        """
        Set environmental factors data in the UI and update ECF.

        Parameters
        ----------
        environmentalFactors_count : dict
            Dictionary of environmental factors counts by relevance.
        EFactor : float
            Environmental Factor.
        """
        self.ui.count_irrelevantEF_Label.setText(str(environmentalFactors_count['irrelevant']))
        self.ui.count_mediumEF_Label.setText(str(environmentalFactors_count['medium']))
        self.ui.count_essentialEF_Label.setText(str(environmentalFactors_count['essential']))
        self.ui.totalEF_Label.setText("8")

        self.ui.EFactor_LineEdit.setText(str(EFactor))

        self.ECF_updated.emit(EFactor)

    def set_UUCP(self, UUCP):
        """
        Set the UUCP value in the UI.

        Parameters
        ----------
        UUCP : float
            Unadjusted Use Case Points.
        """
        self.ui.UUCP_LineEdit.setText(str(UUCP))

    def set_TCF(self, TCF):
        """
        Set the TCF value in the UI.

        Parameters
        ----------
        TCF : float
            Technical Complexity Factor.
        """
        self.ui.TCF_LineEdit.setText(str(TCF))

    def set_ECF(self, ECF):
        """
        Set the ECF value in the UI.

        Parameters
        ----------
        ECF : float
            Environmental Complexity Factor.
        """
        self.ui.ECF_LineEdit.setText(str(ECF))

    def set_UCP(self, UCP):
        """
        Set the UCP value in the UI.

        Parameters
        ----------
        UCP : float
            Use Case Points.
        """
        self.ui.UCP_LineEdit.setText(str(UCP))

    def set_E(self, E):
        """
        Set the E value in the UI.

        Parameters
        ----------
        E : float
            Effort in person-hours.
        """
        self.ui.E_LineEdit.setText(str(E))
