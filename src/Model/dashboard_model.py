# This Python file uses the following encoding: utf-8
# model/dashboard_model.py

import config
import pandas as pd
from PySide6.QtSql import QSqlQuery

class DashboardModel:
    """
    Model for managing the dashboard data in the application.

    This class is responsible for all calculations and data operations related to the project dashboard. It's is responsible for calculating and obtaining key metrics related to project effort estimation.

    Methods
    -------
    """

    def __init__(self):
        """
        Initialize the DashboardModel.
        """
        self.UAW = 0.0
        self.UUCW = 0.0
        self.UUCP = 0.0
        self.TFactor = 0.0
        self.TCF = 0.0
        self.EFactor = 0.0
        self.ECF = 0.0
        self.UCP = 0.0
        self.CF = 20.0
        self.E = 0.0
        self.total_E = 0.0
        self.percentages = {}
        self.person_hours = {}
        self.total_hours = 0.0

    def update_percentages(self, percentages, project_id):
        """
        Update the percentages for different phases of the project.

        Parameters
        ----------
        percentages : dict
            Dictionary containing the effort distribution percentages.
        project_id : int
            The ID of the project to update.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        analysis = percentages.get('analysis')
        design = percentages.get('design')
        programming = percentages.get('programming')
        testing = percentages.get('testing')
        overloading = percentages.get('overloading')
        query_str = """
        UPDATE parameters SET analysis_percentage = ?, design_percentage = ?,
        programming_percentage = ?, testing_percentage = ?, overloading_percentage = ?
        WHERE project_id = ?
        """
        q_update = QSqlQuery()
        if not q_update.prepare(query_str):
            return config.FAILURE
        q_update.addBindValue(analysis)
        q_update.addBindValue(design)
        q_update.addBindValue(programming)
        q_update.addBindValue(testing)
        q_update.addBindValue(overloading)
        q_update.addBindValue(project_id)

        if q_update.exec():
            self.percentages = {
                'analysis': analysis,
                'design': design,
                'programming': programming,
                'testing': testing,
                'overloading': overloading
            }
            return config.SUCCESS
        else:
            return config.FAILURE

    def update_cf(self, cf, project_id):
        """
        Update the conversion factor (CF) for the project.

        Parameters
        ----------
        cf : float
            The new conversion factor.
        project_id : int
            The ID of the project to update.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        query_str = "UPDATE parameters SET cf = ? WHERE project_id = ?"
        q_update = QSqlQuery()
        if not q_update.prepare(query_str):
            return config.FAILURE
        q_update.addBindValue(cf)
        q_update.addBindValue(project_id)

        if q_update.exec():
            self.CF = cf
            return config.SUCCESS
        else:
            return config.FAILURE

    def load_dashboard_data(self, project_id):
        """
        Load the dashboard data for the given project.

        Parameters
        ----------
        project_id : int
            The ID of the project to load data for.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        q = QSqlQuery()
        query_str = """
        SELECT cf, analysis_percentage, design_percentage, programming_percentage,
        testing_percentage, overloading_percentage FROM parameters WHERE project_id = ?
        """
        if not q.prepare(query_str):
            return config.FAILURE
        q.addBindValue(project_id)
        if not q.exec():
            return config.FAILURE

        if q.next():
            cf = q.value(0)
            percentages = {
                'analysis': q.value(1),
                'design': q.value(2),
                'programming': q.value(3),
                'testing': q.value(4),
                'overloading': q.value(5)
            }
            self.percentages = percentages
            self.CF = cf
            return config.SUCCESS
        else:
            return config.FAILURE

    def calculate_UUCP(self, UAW, UUCW):
        """
        Calculate the Unadjusted Use Case Points (UUCP).

        Parameters
        ----------
        UAW : float
            Unadjusted Actor Weight.
        UUCW : float
            Unadjusted Use Case Weight.

        Returns
        -------
        float
            The calculated UUCP.
        """
        self.UAW = UAW
        self.UUCW = UUCW
        self.UUCP = round(UAW + UUCW, 4)
        return self.UUCP

    def calculate_TCF(self, TFactor):
        """
        Calculate the Technical Complexity Factor (TCF).

        Parameters
        ----------
        TFactor : float
            Technical Factor.

        Returns
        -------
        float
            The calculated TCF.
        """
        self.TFactor = TFactor
        self.TCF = round(0.6 + (0.01 * TFactor), 4)
        return self.TCF

    def calculate_ECF(self, EFactor):
        """
        Calculate the Environmental Complexity Factor (ECF).

        Parameters
        ----------
        EFactor : float
            Environmental Factor.

        Returns
        -------
        float
            The calculated ECF.
        """
        self.EFactor = EFactor
        self.ECF = round(1.4 + (-0.03 * EFactor), 4)
        return self.ECF

    def calculate_UCP(self):
        """
        Calculate the Adjusted Use Case Points (UCP).

        Returns
        -------
        float
            The calculated UCP.
        """
        self.UCP = round(self.UUCP * self.ECF * self.TCF, 4)
        return self.UCP

    def calculate_E(self):
        """
        Calculate the Estimated Effort (E).

        Returns
        -------
        float
            The calculated Estimated Effort.
        """
        self.E = round(self.UCP * self.CF, 4)
        return self.E

    def calculate_effort(self):
        """
        Calculate the effort distribution based on the percentages and estimated effort.

        Returns
        -------
        tuple
            Dictionary of person-hours per activity and total_hours
        """
        self.total_hours = 0.0
        programming_percentage = self.percentages.get('programming', 0)
        person_hours = {}
        for activity, percentage in self.percentages.items():
            if programming_percentage != 0:
                hours = round((self.E * percentage) / programming_percentage, 4)
                person_hours[activity] = hours
                self.total_hours += hours
            else:
                person_hours[activity] = 0.0

        total_hours = round(self.total_hours, 4)
        self.person_hours = person_hours

        return person_hours, total_hours

    def get_effort_distribution_data(self, project_id):
        """
        Get the effort distribution data for the project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        DataFrame
            DataFrame containing effort distribution data.
        """
        activities_data = {
            "Activity": ["Analysis", "Design", "Programming", "Testing", "Overloading"],
            "%": [
                self.percentages['analysis'],
                self.percentages['design'],
                self.percentages['programming'],
                self.percentages['testing'],
                self.percentages['overloading']
            ],
            "Person-Hours": [
                self.person_hours['analysis'],
                self.person_hours['design'],
                self.person_hours['programming'],
                self.person_hours['testing'],
                self.person_hours['overloading']
            ]
        }
        data = pd.DataFrame(activities_data)
        total_effort = data['Person-Hours'].sum()
        total_row = pd.DataFrame([{
            'Activity': '',
            '%': 'Total Effort',
            'Person-Hours': total_effort
        }])
        data = pd.concat([data, total_row], ignore_index=True)
        return data

    def get_metrics_data(self, project_id):
        """
        Get the metrics data for the project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        dict
            Dictionary containing metrics data and total effort.
        """
        metrics_data = {
            "Metric": [
                "Unadjusted Actor Weight  [UAW]",
                "Unadjusted Use Case Weight [UUCW]",
                "Unadjusted Use Case Points [UUCP]",
                "Technical Factor [TFactor]",
                "Technical Complexity Factor [TCF]",
                "Environmental Factor [EFactor]",
                "Environmental Complexity Factor [ECF]",
                "Adjusted Use Case Point [UCP]",
                "Conversion Factor [CF]",
                "Estimated Effort [E]"
            ],
            "Value": [
                self.UAW,
                self.UUCW,
                self.UUCP,
                self.TFactor,
                self.TCF,
                self.EFactor,
                self.ECF,
                self.UCP,
                self.CF,
                self.E
            ]
        }
        data = pd.DataFrame(metrics_data)
        total_effort_data = {"Total Development Time": f"{self.total_hours} Hours"}
        total_effort = pd.DataFrame(total_effort_data, index=[0])
        return {'metrics_data': data, 'total_effort': total_effort}

    def get_dashboard_data(self):
        """
        Retrieve the dashboard data.

        Returns
        -------
        list
            A list containing the dashboard data.
        """
        return self.CF, self.percentages
