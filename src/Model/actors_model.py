# This Python file uses the following encoding: utf-8
# model/actors_model.py

import config
import pandas as pd
from PySide6.QtSql import QSqlQuery

class ActorsModel:
    """
    Model for managing actor data in the application.

    This class is responsible for all database operations related to actors, including adding, updating, deleting, and retrieving actor data. It also calculates and maintains actor weights and counts for the project.

    Methods
    -------
    """

    def __init__(self):
        """
        Initialize the ActorsModel.
        """
        self.actors_count = {"Simple": 0, "Average": 0, "Complex": 0}
        self.actors_weights = {"Simple": 1.0, "Average": 2.0, "Complex": 3.0}
        self.actors_UAW = {"Simple": 0.0, "Average": 0.0, "Complex": 0.0}  # Simple actors count * Simple weight
        self.actors = []

    def create_actor(self, actor_data, project_id):
        """
        Create a new actor in the database.

        Parameters
        ----------
        actor_data : dict
            Dictionary containing the actor data:
        project_id : int
            The ID of the project to which the actor belongs.

        Returns
        -------
        tuple
            Status code indicating the result of the operation, and the new actor ID if successful.
        """
        code = actor_data.get('code')
        name = actor_data.get('name')
        complexity = actor_data.get('complexity')
        comment = actor_data.get('comment')

        q_insert = QSqlQuery()
        if not q_insert.prepare("INSERT INTO actors (code, name, complexity, comment, project_id) VALUES (?,?,?,?,?)"):
            return config.FAILURE, None
        q_insert.addBindValue(code)
        q_insert.addBindValue(name)
        q_insert.addBindValue(complexity)
        q_insert.addBindValue(comment)
        q_insert.addBindValue(project_id)

        if q_insert.exec():
            new_actor_id = q_insert.lastInsertId()
            self.update_counts_and_UAW(complexity)  # Incrementar contadores
            return config.SUCCESS, new_actor_id
        else:
            lastError = q_insert.lastError().text().lower()
            if "unique constraint" in lastError or "duplicate" in lastError:
                return config.ALREADY_EXIST, None
            else:
                return config.FAILURE, None

    def update_actor(self, old_data, new_data):
        """
        Update an existing actor in the database.

        Parameters
        ----------
        olda_data : dict
            Dictionary containing the current actor data.
        new_data : dict
            Dictionary containing the new actor data including.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        actor_id = old_data.get('id')
        old_complexity = old_data.get('complexity')
        code = new_data.get('code')
        name = new_data.get('name')
        new_complexity = new_data.get('complexity')
        comment = new_data.get('comment')

        q_update = QSqlQuery()
        if not q_update.prepare("UPDATE actors SET code = ?, name = ?, complexity = ?, comment = ? WHERE id = ?"):
            return config.FAILURE
        q_update.addBindValue(code)
        q_update.addBindValue(name)
        q_update.addBindValue(new_complexity)
        q_update.addBindValue(comment)
        q_update.addBindValue(actor_id)

        if q_update.exec():
            if q_update.numRowsAffected() == 1:
                if old_complexity != new_complexity:
                    self.update_counts_and_UAW(old_complexity, increment=False)
                    self.update_counts_and_UAW(new_complexity)
                return config.SUCCESS
            elif q_update.numRowsAffected() == 0:
                return config.NOT_EXIST
            else:
                return config.FAILURE
        else:
            lastError = q_update.lastError().text().lower()
            if "unique constraint" in lastError:
                return config.ALREADY_EXIST
            else:
                return config.FAILURE

    def delete_actors(self, actors_data):
        """
        Delete actors from the database.

        Parameters
        ----------
        actors_data : dict
            Dictionary containing details of the actors to be deleted.

        Returns
        -------
        tuple
            Status code indicating the result of the operation, and a list of missing IDs if any.
        """
        missing_ids = []
        successful_ids = []

        for actor_id, details in actors_data.items():
            complexity = details['complexity']
            query = QSqlQuery()
            if not query.prepare("DELETE FROM actors WHERE id = ?"):
                return config.FAILURE, None
            query.addBindValue(actor_id)

            if not query.exec():
                return config.FAILURE, None

            if query.numRowsAffected() == 0:
                missing_ids.append(actor_id)

            if query.numRowsAffected() > 0:
                successful_ids.append(actor_id)
                self.update_counts_and_UAW(complexity, increment=False)

        if missing_ids:
            return config.NOT_EXIST, missing_ids
        elif len(successful_ids) == len(actors_data):
            return config.SUCCESS, None
        else:
            return config.FAILURE, None

    def update_actors_weights(self, weights, project_id):
        """
        Update the weights of the actors.

        Parameters
        ----------
        weights : dict
            Dictionary containing the actors weights.
        project_id : int
            The ID of the project to which the actors belong.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        simple_weight = weights['simple_weight']
        average_weight = weights['average_weight']
        complex_weight = weights['complex_weight']

        set_clauses = ["actors_simple_weight = ?", "actors_average_weight = ?", "actors_complex_weight = ?"]
        values = [simple_weight, average_weight, complex_weight, project_id]
        query_str = "UPDATE parameters SET " + ", ".join(set_clauses) + " WHERE project_id = ?"
        q_update = QSqlQuery()
        if not q_update.prepare(query_str):
            return config.FAILURE
        for value in values:
            q_update.addBindValue(value)

        if q_update.exec():
            self.actors_weights['Simple'] = simple_weight
            self.actors_weights['Average'] = average_weight
            self.actors_weights['Complex'] = complex_weight
            for complexity in self.actors_count:
                self.actors_UAW[complexity] = self.actors_count[complexity] * self.actors_weights[complexity]
            return config.SUCCESS
        else:
            return config.FAILURE

    def update_counts_and_UAW(self, complexity, increment=True):
        """
        Update the actor counts and unadjusted actor weights (UAW).

        Parameters
        ----------
        complexity : str
            The complexity of the actor.
        increment : bool, optional
            Value to increment or decrement the count, by default True.
        """
        if increment:
            self.actors_count[complexity] += 1
        else:
            self.actors_count[complexity] -= 1
        self.actors_UAW[complexity] = self.actors_count[complexity] * self.actors_weights[complexity]

    def get_summary_data(self):
        """
        Get summary data for the actors.

        Returns
        -------
        tuple
            A tuple containing the actors count, total actors, actors UAW, total UAW, and actors weights.
        """
        total_actors = sum(self.actors_count.values())
        total_UAW = sum(self.actors_UAW.values())
        return self.actors_count.copy(), total_actors, self.actors_UAW.copy(), total_UAW, self.actors_weights.copy()

    def load_actors_data(self, project_id):
        """
        Load actors data for the given project.

        Parameters
        ----------
        project_id : int
            The ID of the project to load actors for.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        return_value = self.load_actors_weights(project_id)
        if return_value == config.FAILURE:
            return config.FAILURE

        q = QSqlQuery()
        query = "SELECT id, code, name, complexity, comment FROM actors WHERE project_id = ?"
        if not q.prepare(query):
            return config.FAILURE
        q.addBindValue(project_id)

        if not q.exec():
            return config.FAILURE

        for key in self.actors_count:
            self.actors_count[key] = 0
            self.actors_UAW[key] = 0.0

        self.actors = []
        while q.next():
            actor_data = {
                'id': q.value(0),
                'code': q.value(1),
                'name': q.value(2),
                'complexity': q.value(3),
                'comment': q.value(4)
            }
            self.actors.append(actor_data)
            self.update_counts_and_UAW(actor_data['complexity'])
        return config.SUCCESS

    def load_actors_weights(self, project_id):
        """
        Load the weights of the actors for the given project.

        Parameters
        ----------
        project_id : int
            The ID of the project to load weights for.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        q = QSqlQuery()
        if not q.prepare("SELECT actors_simple_weight, actors_average_weight, actors_complex_weight FROM parameters WHERE project_id = ?"):
            return config.FAILURE

        q.addBindValue(project_id)
        if not q.exec():
            return config.FAILURE

        if q.next():
            self.actors_weights['Simple'] = q.value(0)
            self.actors_weights['Average'] = q.value(1)
            self.actors_weights['Complex'] = q.value(2)
            return config.SUCCESS
        else:
            return config.FAILURE

    def get_data(self, project_id):
        """
        Get actors data and summary for the given project.

        Parameters
        ----------
        project_id : int
            The ID of the project to get data for.

        Returns
        -------
        dict or int
            Dictionary containing actors data and actors summary or failure code.
        """
        query = QSqlQuery()
        sql = "SELECT code, name, complexity, comment FROM actors WHERE project_id = ?"
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
                'Comment': query.value(3)
            })

        if results:
            data = pd.DataFrame(results)
        else:
            data = pd.DataFrame(columns=['Code', 'Name', 'Complexity', 'Comment'])

        summary_data = {
            "Actor Type": ["Simple", "Average", "Complex"],
            "Description": [
                "Another system that interacts with the system to be developed through an application programming interface (API)",
                "Another system interacting through a protocol (e.g. TCP/IP) or a person interacting through a text-mode interface.",
                "A person who interacts with the system through an interface graphics (GUI)"
            ],
            "Weight Factor": [
                self.actors_weights['Simple'],
                self.actors_weights['Average'],
                self.actors_weights['Complex']
            ],
            "Actors": [
                self.actors_count['Simple'],
                self.actors_count['Average'],
                self.actors_count['Complex']
            ],
            "UAW": [
                self.actors_UAW['Simple'],
                self.actors_UAW['Average'],
                self.actors_UAW['Complex']
            ]
        }
        summary = pd.DataFrame(summary_data)
        total_actors = summary['Actors'].sum()
        total_UAW = summary['UAW'].sum()
        total_row = pd.DataFrame([{
            'Actor Type': '',
            'Description': '',
            'Weight Factor': 'Total',
            'Actors': total_actors,
            'UAW': total_UAW,
        }])
        summary = pd.concat([summary, total_row], ignore_index=True)

        return {'actors_data': data, 'actors_summary': summary}

    def export_actors_data(self, project_id):
        """
        Export actors data for the given project.

        Parameters
        ----------
        project_id : int
            The ID of the project to export actors data for.

        Returns
        -------
        list or int
            List of actors data or failure code.
        """
        data = []
        query = "SELECT * FROM actors WHERE project_id = ?"
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

    def get_actors_data(self):
        """
        Retrieve the actors data.

        Returns
        -------
        list
            A list containing the actors data.
        """
        return self.actors
