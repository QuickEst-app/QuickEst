# This Python file uses the following encoding: utf-8
# model/environmentalFactors_model.py

import config
import pandas as pd
from PySide6.QtSql import QSqlQuery

class EnvironmentalFactorsModel:
    """
    Model for managing environmental factor data in the application.

    This class handles all database operations related to environmental factors, including updating and retrieving environmental factor data. It calculates and maintains the influence and results of some operations of this factors.

    Methods
    -------
    """

    def __init__(self):
        """
        Initialize the EnvironmentalFactorsModel.
        """
        self.factor_results = {f"E{i}": 0 for i in range(1, 9)}
        self.factor_counts = {'irrelevant': 0, 'medium': 0, 'essential': 0}
        self.environmentalFactors = []

    def update_environmental_factor(self, factor_data, project_id):
        """
        Update an environmental factor in the database.

        Parameters
        ----------
        factor_data : dict
            Dictionary containing environmental factor data.
        project_id : int
            The ID of the project.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        factor = factor_data.get('factor')
        weight = factor_data.get('weight')
        influence = factor_data.get('influence')
        comment = factor_data.get('comment')
        q_select = QSqlQuery()
        q_select.prepare("SELECT influence FROM environmental_factors WHERE factor = ? AND project_id = ?")
        q_select.addBindValue(factor)
        q_select.addBindValue(project_id)
        old_influence = None
        if q_select.exec() and q_select.first():
            old_influence = q_select.value(0)
        else:
            return config.FAILURE

        q_update = QSqlQuery()
        q_update.prepare(
            """
            UPDATE environmental_factors
            SET weight = ?, influence = ?, comment = ?
            WHERE factor = ? AND project_id = ?
            """
        )
        q_update.addBindValue(weight)
        q_update.addBindValue(influence)
        q_update.addBindValue(comment)
        q_update.addBindValue(factor)
        q_update.addBindValue(project_id)

        if q_update.exec():
            if q_update.numRowsAffected() == 1:
                old_category = self.categorize_influence(old_influence)
                new_category = self.categorize_influence(influence)
                if old_category != new_category:
                    if old_category in self.factor_counts:
                        self.factor_counts[old_category] -= 1
                    if new_category in self.factor_counts:
                        self.factor_counts[new_category] += 1
                result = weight * influence
                self.factor_results[factor] = result
                return config.SUCCESS
            elif q_update.numRowsAffected() == 0:
                return config.NOT_EXIST
            else:
                return config.FAILURE
        else:
            return config.FAILURE

    def categorize_influence(self, influence):
        """
        Categorize the influence value into 'irrelevant', 'medium', or 'essential'.

        Parameters
        ----------
        influence : int
            The influence value to categorize.

        Returns
        -------
        str
            The category of the influence value.
        """
        if 0 <= influence <= 2:
            return 'irrelevant'
        elif 3 <= influence <= 4:
            return 'medium'
        elif influence == 5:
            return 'essential'
        return 'undefined'

    def get_EF_results(self):
        """
        Get the results of environmental factors.

        Returns
        -------
        tuple
            A dictionary of factor results, the total environmental factor and the count of factors by category.
        """
        EFactor = sum(self.factor_results.values())
        return self.factor_results, EFactor, self.factor_counts

    def load_environmental_factors_data(self, project_id):
        """
        Load environmental factors data for the given project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        self.factor_results = {f"E{i}": 0 for i in range(1, 9)}
        self.factor_counts = {'irrelevant': 0, 'medium': 0, 'essential': 0}

        q = QSqlQuery()
        query = "SELECT factor, description, weight, influence, comment FROM environmental_factors WHERE project_id = ?"
        q.prepare(query)
        q.addBindValue(project_id)

        if not q.exec():
            return config.FAILURE

        self.environmentalFactors = []
        while q.next():
            environmentalFactor_data = {
                'factor': q.value(0),
                'description': q.value(1),
                'weight': q.value(2),
                'influence': q.value(3),
                'comment': q.value(4)
            }
            self.environmentalFactors.append(environmentalFactor_data)
            category = self.categorize_influence(environmentalFactor_data['influence'])
            self.factor_counts[category] += 1
            self.factor_results[environmentalFactor_data['factor']] = environmentalFactor_data['weight'] * environmentalFactor_data['influence']
        return config.SUCCESS

    def get_data(self, project_id):
        """
        Get environmental factors data and summary for the given project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        dict or int
            Dictionary containing environmental factors data and summary, or failure code.
        """
        query = QSqlQuery()
        sql = "SELECT factor, description, weight, influence, comment FROM environmental_factors WHERE project_id = ?"
        if not query.prepare(sql):
            return config.FAILURE

        query.addBindValue(project_id)
        if not query.exec():
            return config.FAILURE

        results = []
        while query.next():
            result = round(query.value(2) * query.value(3), 4)
            results.append({
                'Factor': query.value(0),
                'Description': query.value(1),
                'Weight': query.value(2),
                'Influence': query.value(3),
                'Result': result,
                'Comment': query.value(4)
            })

        data = pd.DataFrame(results)
        total_result = data['Result'].sum()
        EFactor_row = pd.DataFrame([{
            'Factor': '',
            'Description': '',
            'Weight': '',
            'Influence': 'EFactor',
            'Result': total_result,
            'Comment': ''
        }])
        data = pd.concat([data, EFactor_row], ignore_index=True)

        summary_data = {
            "Factor Type": ["Irrelevant", "Medium", "Essential"],
            "Description": [
                "Influence: from 0 to 2",
                "Influence: from 3 to 4",
                "Influence: 5"
            ],
            "Factors": [
                self.factor_counts['irrelevant'],
                self.factor_counts['medium'],
                self.factor_counts['essential']
            ]
        }
        summary = pd.DataFrame(summary_data)
        total_factors = summary['Factors'].sum()
        total_row = pd.DataFrame([{
            'Factor Type': '',
            'Description': 'Total',
            'Factors': total_factors
        }])
        summary = pd.concat([summary, total_row], ignore_index=True)

        return {'environmentalFactors_data': data, 'environmentalFactors_summary': summary}

    def insert_environmental_factors_default(self, project_id):
        """
        Insert default environmental factors for a new project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        factors = [
            ('E1','Familiarity with the project model used',1.5,0,''),
            ('E2','Application experience',0.5,0,''),
            ('E3','Object oriented experience',1.0,0,''),
            ('E4','Lead analyst capability',0.5,0,''),
            ('E5','Motivation',1.0,0,''),
            ('E6','Stability of requirements',2.0,0,''),
            ('E7','Part time workers',-1.0,0,''),
            ('E8','Programming language difficulty',-1.0,0,'')
        ]
        query = QSqlQuery()
        for factor in factors:
            sql = "INSERT INTO environmental_factors (factor, description, weight, influence, comment, project_id) VALUES (?, ?, ?, ?, ?, ?)"
            query.prepare(sql)
            if not query.prepare(sql):
                return config.FAILURE
            for value in factor:
                query.addBindValue(value)
            query.addBindValue(project_id)
            if not query.exec():
                return config.FAILURE
        return config.SUCCESS

    def export_environmental_factors_data(self, project_id):
        """
        Export environmental factors data for the given project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        list or int
            List of environmental factors data or failure code.
        """
        data = []
        query = "SELECT * FROM environmental_factors WHERE project_id = ?"
        q = QSqlQuery()
        if not q.prepare(query):
            return config.FAILURE
        q.addBindValue(project_id)

        if not q.exec():
            return config.FAILURE

        while q.next():
            row = [q.value(i) for i in range(q.record().count())]
            data.append(row)

        return data

    def get_environmental_factors_data(self):
        """
        Retrieve the environmental factors data.

        Returns
        -------
        list
            A list containing the environmental factors data.
        """
        return self.environmentalFactors
