# This Python file uses the following encoding: utf-8
# model/technicalFactors_model.py

import config
import pandas as pd

from PySide6.QtSql import QSqlQuery

class TechnicalFactorsModel:
    """
    Model for managing technical factor data in the application.

    This class handles all database operations related to technical factors, including updating and retrieving technical factor data. It calculates and maintains the influence and results of some operations of this factors.

    Methods
    -------
    """

    def __init__(self):
        """
        Initialize the TechnicalFactorsModel with default values.
        """
        self.factor_results = {f"T{i:02}": 0 for i in range(1, 14)}
        self.factor_counts = {'irrelevant': 0, 'medium': 0, 'essential': 0}
        self.technicalFactors = []

    def update_technical_factor(self, factor_data, project_id):
        """
        Update a technical factor in the database.

        Parameters
        ----------
        factor_data : dcit
            Dictionary containing technical factor data.
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
        # Consultar la influencia anterior antes de la actualización
        q_select = QSqlQuery()
        q_select.prepare("SELECT influence FROM technical_factors WHERE factor = ? AND project_id = ?")
        q_select.addBindValue(factor)
        q_select.addBindValue(project_id)
        old_influence = None
        if q_select.exec() and q_select.first():
            old_influence = q_select.value(0)
        else:
            return config.FAILURE

        # Preparar y ejecutar la actualización después de obtener la influencia anterior
        q_update = QSqlQuery()
        q_update.prepare(
            """
            UPDATE technical_factors
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

                # Categorizar influencias viejas y nuevas
                old_category = self.categorize_influence(old_influence)
                new_category = self.categorize_influence(influence)

                # Actualizar los contadores solo si la categoría ha cambiado
                if old_category != new_category:
                    if old_category in self.factor_counts:
                        self.factor_counts[old_category] -= 1
                    if new_category in self.factor_counts:
                        self.factor_counts[new_category] += 1

                # Actualizar los resultados de los factores
                result = weight * influence
                self.factor_results[factor] = result

                return config.SUCCESS
            elif q_update.numRowsAffected() == 0:
                return config.NOT_EXIST
            else:
                return config.FAILURE # No debería suceder si 'factor' es único
        else:
            return config.FAILURE

    def categorize_influence(self, influence):
        """
        Categorize the influence based on its value.

        Parameters
        ----------
        influence : int
            The influence value to categorize.

        Returns
        -------
        str
            The category of the influence: 'irrelevant', 'medium', 'essential', or 'undefined'.
        """
        if 0 <= influence <= 2:
            return 'irrelevant'
        elif 3 <= influence <= 4:
            return 'medium'
        elif influence == 5:
            return 'essential'
        return 'undefined'  # Si el valor está fuera de rango

    def get_TF_results(self):
        """
        Calculate and return the results of the technical factors.

        Returns
        -------
        tuple
            A tuple containing the factor results, total TFactor, and factor counts.
        """
        TFactor = sum(self.factor_results.values())
        return self.factor_results, TFactor, self.factor_counts

    def load_technical_factors_data(self, project_id):
        """
        Load technical factors data from the database for a given project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        # Resetear contadores y resultados antes de cargar nuevos datos
        self.factor_results = {f"T{i:02}": 0 for i in range(1, 14)}
        self.factor_counts = {'irrelevant': 0, 'medium': 0, 'essential': 0}

        # Obtener factores técnicos de la base de datos
        q = QSqlQuery()
        query = "SELECT factor, description, weight, influence, comment FROM technical_factors WHERE project_id = ?"
        q.prepare(query)
        q.addBindValue(project_id)

        if not q.exec():
            return config.FAILURE

        self.technicalFactors = []
        while q.next():
            technicalFactor_data = {
                'factor': q.value(0),
                'description': q.value(1),
                'weight': q.value(2),
                'influence': q.value(3),
                'comment': q.value(4)
            }
            self.technicalFactors.append(technicalFactor_data)
            # Actualizar los contadores y resultados con los datos cargados
            category = self.categorize_influence(technicalFactor_data['influence'])
            self.factor_counts[category] += 1
            self.factor_results[technicalFactor_data['factor']] = technicalFactor_data['weight'] * technicalFactor_data['influence']
        return config.SUCCESS

    def get_data(self, project_id):
        """
        Get detailed data for all technical factors in a project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        dict or int
            Dictionary containing technical factors data and summary, or failure code.
        """
        query = QSqlQuery()
        sql = "SELECT factor, description, weight, influence, comment FROM technical_factors WHERE project_id = ?"
        if not query.prepare(sql):
            return config.FAILURE

        query.addBindValue(project_id)
        if not query.exec():
            return config.FAILURE

        results = []
        while query.next():
            result = round(query.value(2) * query.value(3), 4)  # Cálculo de Result
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
        TFactor_row = pd.DataFrame([{
            'Factor': '',
            'Description': '',
            'Weight': '',
            'Influence': 'TFactor',
            'Result': total_result,
            'Comment': ''
        }])
        data = pd.concat([data, TFactor_row], ignore_index=True)

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
            'Description': 'TOTAL',
            'Factors': total_factors
        }])
        summary = pd.concat([summary, total_row], ignore_index=True)

        return {'technicalFactors_data': data, 'technicalFactors_summary': summary}

    def insert_technical_factors_default(self, project_id):
        """
        Insert default technical factors for a new project.

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
            ('T01', 'Distributed system', 2.0, 0, ''),
            ('T02','Performance or response time', 1.0, 0, ''),
            ('T03','End user efficiency',1.0, 0, ''),
            ('T04','Complex internal processing',1.0, 0, ''),
            ('T05','The code must be reusable (reusability)',1.0, 0, ''),
            ('T06','Ease of installation',0.5, 0, ''),
            ('T07','Easy to use',0.5, 0, ''),
            ('T08','Portability',2.0, 0, ''),
            ('T09','Ease of change',1.0, 0, ''),
            ('T10','Concurrence',1.0, 0, ''),
            ('T11','Special security features',1.0, 0, ''),
            ('T12','Provides direct access to third parties',1.0, 0, ''),
            ('T13','Special user training required',1.0, 0, '')
        ]
        query = QSqlQuery()
        for factor in factors:
            sql = "INSERT INTO technical_factors (factor, description, weight, influence, comment, project_id) VALUES (?, ?, ?, ?, ?, ?)"
            query.prepare(sql)
            if not query.prepare(sql):
                return config.FAILURE
            for value in factor:
                query.addBindValue(value)
            query.addBindValue(project_id)
            if not query.exec():
                return config.FAILURE
        return config.SUCCESS

    def export_technical_factors_data(self, project_id):
        """
        Export technical factors data for a project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        list or int
            List of technical factors data, or failure code.
        """
        data = []
        query = "SELECT * FROM technical_factors WHERE project_id = ?"

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

    def get_technical_factors_data(self):
        """
        Retrieve the technical factors data.

        Returns
        -------
        list
            A list containing the technical factors data.
        """
        return self.technicalFactors
