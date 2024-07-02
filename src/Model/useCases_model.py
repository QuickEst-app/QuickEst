# This Python file uses the following encoding: utf-8
# model/useCases_model.py

import config
import pandas as pd
from PySide6.QtSql import QSqlQuery

class UseCasesModel:
    """
    Model for managing use case data in the application.

    This class is responsible for all database operations related to use cases, including adding, updating, deleting, and retrieving use case data. It also calculates and maintains use case weights and counts for the project.

    Methods
    -------
    """

    def __init__(self):
        """
        Initializes the UseCasesModel with default values.
        """
        self.useCases_count = {"Simple": 0, "Average": 0, "Complex": 0}
        self.useCases_weights = {"Simple": 5.0, "Average": 10.0, "Complex": 15.0}
        self.useCases_UUCW = {"Simple": 0.0, "Average": 0.0, "Complex": 0.0}
        self.useCases = []

    def create_use_case(self, use_case_data, project_id):
        """
        Creates a new use case and inserts it into the database.

        Parameters
        ----------
        useCase_data : dict
            Dictionary containing use case data.
        project_id : int
            The ID of the project to which the use case belongs.

        Returns
        -------
        tuple
            A tuple containing a status code indicating the result of the operation, and the ID of the new use case or None.
        """
        code = use_case_data.get('code')
        name = use_case_data.get('name')
        complexity = use_case_data.get('complexity')
        transactions = use_case_data.get('transactions')
        comment = use_case_data.get('comment')

        q_insert = QSqlQuery()
        q_insert.prepare(
            """
            INSERT INTO use_cases (code, name, complexity, transactions, comment, project_id)
            VALUES (?,?,?,?,?,?)
            """
        )
        q_insert.addBindValue(code)
        q_insert.addBindValue(name)
        q_insert.addBindValue(complexity)
        q_insert.addBindValue(transactions)
        q_insert.addBindValue(comment)
        q_insert.addBindValue(project_id)

        if q_insert.exec():
            new_useCase_id = q_insert.lastInsertId()
            self.update_counts_and_UUCW(complexity, increment=True)
            return config.SUCCESS, new_useCase_id
        else:
            lastError = q_insert.lastError().text().lower()
            if "unique constraint" in lastError or "duplicate" in lastError:
                return config.ALREADY_EXIST, None
            else:
                return config.FAILURE, None

    def update_use_case(self, old_data, new_data):
        """
        Updates an existing use case in the database.

        Parameters
        ----------
        old_data : dict
            Dictionary containing old use case data.
        new_data : dict
            Dictionary containing new use case data.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        useCase_id = old_data.get('id')
        old_complexity = old_data.get('complexity')
        code = new_data.get('code')
        name = new_data.get('name')
        new_complexity = new_data.get('complexity')
        transactions = new_data.get('transactions')
        comment = new_data.get('comment')

        q_update = QSqlQuery()
        q_update.prepare(
            """
            UPDATE use_cases
            SET code = ?, name = ?, complexity = ?, transactions = ?, comment = ?
            WHERE id = ?
            """
        )
        q_update.addBindValue(code)
        q_update.addBindValue(name)
        q_update.addBindValue(new_complexity)
        q_update.addBindValue(transactions)
        q_update.addBindValue(comment)
        q_update.addBindValue(useCase_id)

        if q_update.exec():
            if q_update.numRowsAffected() == 1:
                if old_complexity != new_complexity:
                    self.update_counts_and_UUCW(old_complexity, increment=False)
                    self.update_counts_and_UUCW(new_complexity, increment=True)
                return config.SUCCESS
            elif q_update.numRowsAffected() == 0:
                return config.NOT_EXIST
            else:
                return config.FAILURE
        else:
            lastError = q_update.lastError()
            if "unique constraint" in lastError.text().lower():
                return config.ALREADY_EXIST
            else:
                return config.FAILURE

    def delete_use_cases(self, use_cases_data):
        """
        Deletes specified use cases from the database.

        Parameters
        ----------
        use_cases_data : dict
            A dictionary containing the details of the use cases to be deleted.

        Returns
        -------
        tuple
            A tuple containing a status code indicating the result of the operation, and a list of missing IDs or None.
        """
        missing_ids = []
        successful_ids = []

        for useCase_id, details in use_cases_data.items():
            complexity = details['complexity']
            query = QSqlQuery()
            query.prepare("DELETE FROM use_cases WHERE id = ?")
            query.addBindValue(useCase_id)

            if not query.exec():
                return config.FAILURE, None

            if query.numRowsAffected() == 0:
                missing_ids.append(useCase_id)

            if query.numRowsAffected() > 0:
                successful_ids.append(useCase_id)
                self.update_counts_and_UUCW(complexity, increment=False)

        if missing_ids:
            return config.NOT_EXIST, missing_ids
        elif len(successful_ids) == len(use_cases_data):
            return config.SUCCESS, None
        else:
            return config.FAILURE, None

    def update_use_cases_weights(self, weights, project_id):
        """
        Updates the weights for use cases and recalculates the UUCW.

        Parameters
        ----------
        weights : dict
            Dictionary containing the use cases weights.
        project_id : int
            The ID of the project to which the weights belong.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        simple_weight = weights['simple_weight']
        average_weight = weights['average_weight']
        complex_weight = weights['complex_weight']
        set_clauses = ["useCases_simple_weight = ?", "useCases_average_weight = ?", "useCases_complex_weight = ?"]
        values = [simple_weight, average_weight, complex_weight, project_id]
        query_str = "UPDATE parameters SET " + ", ".join(set_clauses) + " WHERE project_id = ?"
        q_update = QSqlQuery()

        if not q_update.prepare(query_str):
            return config.FAILURE

        for value in values:
            q_update.addBindValue(value)

        if q_update.exec():
            self.useCases_weights['Simple'] = simple_weight
            self.useCases_weights['Average'] = average_weight
            self.useCases_weights['Complex'] = complex_weight
            for complexity in self.useCases_count:
                self.useCases_UUCW[complexity] = self.useCases_count[complexity] * self.useCases_weights[complexity]
            return config.SUCCESS
        else:
            return config.FAILURE

    def update_counts_and_UUCW(self, complexity, increment=True):
        """
        Updates the counts and UUCW based on the complexity.

        Parameters
        ----------
        complexity : str
            The complexity of the use case (Simple, Average, Complex).
        increment : bool, optional
            Whether to increment or decrement the count (default is True).
        """
        if increment:
            self.useCases_count[complexity] += 1
        else:
            self.useCases_count[complexity] -= 1

        self.useCases_UUCW[complexity] = self.useCases_count[complexity] * self.useCases_weights[complexity]

    def get_summary_data(self):
        """
        Returns a summary of the use cases data.

        Returns
        -------
        tuple
            A tuple containing the use cases count, total use cases, UUCW, total UUCW, and weights.
        """
        total_useCases = sum(self.useCases_count.values())
        total_UUCW = sum(self.useCases_UUCW.values())
        return self.useCases_count.copy(), total_useCases, self.useCases_UUCW.copy(), total_UUCW, self.useCases_weights.copy()

    def load_use_cases_data(self, project_id):
        """
        Loads use case data for a specific project.

        Parameters
        ----------
        project_id : int
            The ID of the project for which to load use cases.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        return_value = self.load_use_cases_weights(project_id)
        if return_value == config.FAILURE:
            return config.FAILURE

        q = QSqlQuery()
        query = "SELECT id, code, name, complexity, transactions, comment FROM use_cases WHERE project_id = ?"
        q.prepare(query)
        q.addBindValue(project_id)

        if not q.exec():
            return config.FAILURE

        for key in self.useCases_count:
            self.useCases_count[key] = 0
            self.useCases_UUCW[key] = 0.0

        self.useCases = []
        while q.next():
            useCases_data = {
                'id': q.value(0),
                'code': q.value(1),
                'name': q.value(2),
                'complexity': q.value(3),
                'transactions': q.value(4),
                'comment': q.value(5)
            }
            self.useCases.append(useCases_data)
            self.update_counts_and_UUCW(useCases_data['complexity'])
        return config.SUCCESS

    def load_use_cases_weights(self, project_id):
        """
        Loads the use case weights for a specific project.

        Parameters
        ----------
        project_id : int
            The ID of the project for which to load use case weights.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        q = QSqlQuery()
        if not q.prepare("SELECT useCases_simple_weight, useCases_average_weight, useCases_complex_weight FROM parameters WHERE project_id = ?"):
            return config.FAILURE

        q.addBindValue(project_id)
        if not q.exec():
            return config.FAILURE

        if q.next():
            self.useCases_weights['Simple'] = q.value(0)
            self.useCases_weights['Average'] = q.value(1)
            self.useCases_weights['Complex'] = q.value(2)
            return config.SUCCESS
        else:
            return config.FAILURE

    def get_data(self, project_id):
        """
        Retrieves use case data and summary for a specific project.

        Parameters
        ----------
        project_id : int
            The ID of the project for which to retrieve data.

        Returns
        -------
        dict or int
            A dictionary containing the use cases data and summary or failure code.
        """
        query = QSqlQuery()
        sql = "SELECT code, name, complexity, transactions, comment FROM use_cases WHERE project_id = ?"
        if not query.prepare(sql):
            return config.FAILURE

        query.addBindValue(project_id)
        if not query.exec():
            return config.FAILURE

        results = []
        while query.next():
            results.append({
                'Code': query.value(0),
                'Name': query.value(1),
                'Complexity': query.value(2),
                'Transactions': query.value(3),
                'Comment': query.value(4)
            })

        if results:
            data = pd.DataFrame(results)
        else:
            data = pd.DataFrame(columns=['Code', 'Name', 'Complexity', 'Transactions', 'Comment'])

        summary_data = {
            "Use Case Type": ["Simple", "Average", "Complex"],
            "Description": [
                "Number of Transactions: from 1 to 3",
                "Number of Transactions: from 4 to 7",
                "Numer of Transactions: more than 7"
            ],
            "Weight Factor": [
                self.useCases_weights['Simple'],
                self.useCases_weights['Average'],
                self.useCases_weights['Complex']
            ],
            "Use Cases": [
                self.useCases_count['Simple'],
                self.useCases_count['Average'],
                self.useCases_count['Complex']
            ],
            "UUCW": [
                self.useCases_UUCW['Simple'],
                self.useCases_UUCW['Average'],
                self.useCases_UUCW['Complex']
            ]
        }
        summary = pd.DataFrame(summary_data)
        total_useCases = summary['Use Cases'].sum()
        total_UUCW = summary['UUCW'].sum()
        total_row = pd.DataFrame([{
            'Use Case Type': '',
            'Description': '',
            'Weight Factor': 'Total',
            'Use Cases': total_useCases,
            'UUCW': total_UUCW,
        }])

        summary = pd.concat([summary, total_row], ignore_index=True)

        return {'useCases_data': data, 'useCases_summary': summary}

    def export_use_cases_data(self, project_id):
        """
        Exports use case data for a specific project.

        Parameters
        ----------
        project_id : int
            The ID of the project for which to export data.

        Returns
        -------
        list or int
            A list of use case data or failure code.
        """
        data = []
        query = "SELECT * FROM use_cases WHERE project_id = ?"
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

    def get_use_cases_data(self):
        """
        Retrieve the use cases data.

        Returns
        -------
        list
            A list containing the use cases data.
        """
        return self.useCases
