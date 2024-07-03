# This Python file uses the following encoding: utf-8
# model/projects_model.py

import config
import pandas as pd
import DataSource.database as db
from datetime import datetime
from PySide6.QtCore import QDir, QFile, QDataStream, QIODevice, QCryptographicHash, QFileInfo, QJsonDocument, QTextStream
from PySide6.QtSql import QSqlQuery

class ProjectsModel:
    """
    Model for managing project data in the application.

    This class handles all database operations related to projects, including creation, deletion, updating, export, import and retrieval project data. It also manages database transactions to ensure data integrity.

    Methods
    -------
    """

    def __init__(self):
        """
        Initialize the ProjectsModel.
        """
        self.db_instance = db.DataBase.get_instance()

    def start_transaction(self):
        """
        Start a new database transaction.

        Returns
        -------
        bool
            True if the transaction was started successfully, False otherwise.
        """
        return self.db_instance.transaction()

    def commit(self):
        """
        Commit the current database transaction.

        Returns
        -------
        bool
            True if the transaction was committed successfully, False otherwise.
        """
        return self.db_instance.commit()

    def rollback(self):
        """
        Roll back the current database transaction.

        Returns
        -------
        bool
            True if the transaction was rolled back successfully, False otherwise.
        """
        return self.db_instance.rollback()

    def add_project(self, project_data):
        """
        Add a new project to the database.

        Parameters
        ----------
        project_data : dict
            Dictionary containing project data.

        Returns
        -------
        tuple
            Status code indicating the result of the operation, and the new project ID if successful, None otherwise.
        """

        # Check the number of existing projects
        q_count = QSqlQuery()
        q_count.prepare("SELECT COUNT(*) FROM projects")

        if not q_count.exec():
            return config.FAILURE, None

        q_count.next()
        project_count = q_count.value(0)

        if project_count >= config.PROJECT_LIMIT:
            return config.TOO_MANY_PROJECTS, None

        favorite = project_data.get('favorite')
        name = project_data.get('name')
        description = project_data.get('description')
        created_at = project_data.get('created_at')
        last_access = project_data.get('last_access')
        q_insert = QSqlQuery()
        q_insert.prepare(
            """
            INSERT INTO projects (favorite, name, description, created_at, last_access)
            VALUES (?,?,?,?,?)
            """
        )
        q_insert.addBindValue(favorite)
        q_insert.addBindValue(name)
        q_insert.addBindValue(description)
        q_insert.addBindValue(created_at)
        q_insert.addBindValue(last_access)

        if q_insert.exec():
            new_project_id = q_insert.lastInsertId()
            return config.SUCCESS, new_project_id
        else:
            lastError = q_insert.lastError().text().lower()
            if "unique constraint" in lastError or "duplicate" in lastError:
                return config.ALREADY_EXIST, None
            else:
                return config.FAILURE, None

    def delete_project(self, project_id):
        """
        Delete a project from the database.

        Parameters
        ----------
        project_id : int
            The ID of the project to delete.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        q_delete = QSqlQuery()
        q_delete.prepare("DELETE FROM projects WHERE id = ?")
        q_delete.addBindValue(project_id)

        if q_delete.exec():
            if q_delete.numRowsAffected() > 0:
                return config.SUCCESS
            else:
                return config.NOT_EXIST
        else:
            return config.FAILURE

    def update_favorite_project(self, project_id, favorite):
        """
        Update the favorite status of a project.

        Parameters
        ----------
        project_id : int
            The ID of the project to update.
        favorite : bool
            The new favorite status.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        q_update = QSqlQuery()
        q_update.prepare(
            """
            UPDATE projects
            SET favorite = ?
            WHERE id = ?
            """
        )
        q_update.addBindValue(favorite)
        q_update.addBindValue(project_id)

        if q_update.exec():
            if q_update.numRowsAffected() > 0:
                return config.SUCCESS
            else:
                return config.NOT_EXIST
        else:
            return config.FAILURE

    def update_last_access(self, project_id, last_access):
        """
        Update the last access date of a project.

        Parameters
        ----------
        project_id : int
            The ID of the project to update.
        last_access : str
            The new last access date.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        q_update = QSqlQuery()
        q_update.prepare(
            """
            UPDATE projects
            SET last_access = ?
            WHERE id = ?
            """
        )
        q_update.addBindValue(last_access)
        q_update.addBindValue(project_id)

        if q_update.exec():
            if q_update.numRowsAffected() > 0:
                return config.SUCCESS
            else:
                return config.NOT_EXIST
        else:
            return config.FAILURE

    def update_project(self, project_id, project_data):
        """
        Update the details of a project.

        Parameters
        ----------
        project_id : int
            The ID of the project to update.
        project_data : dict
            Dictionary containing project data.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        name = project_data.get('name')
        description = project_data.get('description')
        q_update = QSqlQuery()
        q_update.prepare(
            """
            UPDATE projects
            SET name = ?, description = ?
            WHERE id = ?
            """
        )
        q_update.addBindValue(name)
        q_update.addBindValue(description)
        q_update.addBindValue(project_id)

        if q_update.exec():
            if q_update.numRowsAffected() > 0:
                return config.SUCCESS
            else:
                return config.NOT_EXIST
        else:
            lastError = q_update.lastError().text().lower()
            if "unique constraint" in lastError or "duplicate" in lastError:
                return config.ALREADY_EXIST
            else:
                return config.FAILURE

    def insert_parameters(self, project_id):
        """
        Insert default parameters for a new project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        query = QSqlQuery()
        if not query.prepare("INSERT INTO parameters (project_id) VALUES (?)"):
            return config.FAILURE

        query.addBindValue(project_id)

        if not query.exec():
            return config.FAILURE
        return config.SUCCESS

    def find_manifest(self, directory):
        """
        Find the project manifest file in the specified directory.

        Parameters
        ----------
        directory : str
            The directory to search for the manifest file.

        Returns
        -------
        str or int
            The path to the manifest file if found, or failure code.
        """
        dir = QDir(directory)
        project_files = dir.entryList([f"*{config.PROJECT_FILE_EXTENSION}"], QDir.Files)

        if not project_files:
            return config.FAILURE

        manifest_file_path = QDir.cleanPath(dir.filePath(project_files[0]))

        if not manifest_file_path:
            return config.FAILURE

        return manifest_file_path

    def load_json(self, manifest_file):
        """
        Load a JSON manifest file.

        Parameters
        ----------
        manifest_file : str
            The path to the manifest file.

        Returns
        -------
        dict or int
            The loaded JSON object as a dictionary if successful, or failure code.
        """
        try:
            file = QFile(manifest_file)
            if file.open(QFile.ReadOnly | QFile.Text):
                content = file.readAll()
                file.close()
                json_document = QJsonDocument.fromJson(content)
                project_manifest = json_document.object()
            else:
                return config.FAILURE
        except Exception:
            return config.FAILURE
        return project_manifest

    def load_project_data(self, project_manifest, directory):
        """
        Load project data based on the manifest.

        Parameters
        ----------
        project_manifest : dict
            The project manifest dictionary.
        directory : str
            The directory containing the project files.

        Returns
        -------
        dict or int
            Dictionary containing the loaded project data if successful, or failure code.
        """
        loaded_data = {}
        for table, info in project_manifest.items():
            try:
                file_path = QDir(directory).filePath(info["file_name"])
                if not QFile.exists(file_path):
                    return config.FAILURE
            except KeyError:
                return config.FAILURE
            try:
                expected_hash = info["hash"]
                actual_hash = self.calculate_file_hash(file_path)
                if expected_hash != actual_hash:
                    return config.FAILURE
            except KeyError:
                return config.FAILURE

            return_value = self.read_data_from_binary_file(file_path)
            if return_value == config.FAILURE:
                return config.FAILURE
            else:
                loaded_data[table] = return_value

        try:
            required_keys = ["project", "parameters", "actors", "use_cases", "technical_factors", "environmental_factors"]
            for key in required_keys:
                if key not in loaded_data:
                    raise KeyError()
        except KeyError:
            return config.FAILURE

        return loaded_data

    def calculate_file_hash(self, file_path):
        """
        Calculate the SHA-256 hash of a file.

        Parameters
        ----------
        file_path : str
            The path to the file.

        Returns
        -------
        str or None
            The SHA-256 hash of the file, None otherwise.
        """
        file = QFile(file_path)
        if file.open(QFile.ReadOnly):
            hash = QCryptographicHash(QCryptographicHash.Sha256)
            while not file.atEnd():
                line = file.read(4096)
                hash.addData(line)
            file.close()
            return hash.result().toHex().data().decode("utf-8")
        else:
            return None

    def read_data_from_binary_file(self, file_path):
        """
        Read data from a binary file.

        Parameters
        ----------
        file_path : str
            The path to the binary file.

        Returns
        -------
        list or int
            List of data read from the file if successful, or failure code.
        """
        data = []
        file_type = self.determine_file_type(file_path)
        if file_type is None:
            return config.FAILURE
        file = QFile(file_path)
        if not file.open(QIODevice.ReadOnly):
            return config.FAILURE

        stream = QDataStream(file)

        while not stream.atEnd():
            if file_type == "project":
                data.append(self.read_project(stream))
            elif file_type == "parameters":
                data.append(self.read_parameter(stream))
            elif file_type == "actors":
                data.append(self.read_actor(stream))
            elif file_type == "use_cases":
                data.append(self.read_use_case(stream))
            elif file_type == "technical_factors" or file_type == "environmental_factors":
                data.append(self.read_factor(stream))
            else:
                return config.FAILURE
        file.close()
        return data

    def determine_file_type(self, file_path):
        """
        Determine the type of file based on its name.

        Parameters
        ----------
        file_path : str
            The path to the file.

        Returns
        -------
        str or None
            The file type if recognized, None otherwise.
        """
        file_name = QFileInfo(file_path).fileName()
        if file_name == config.PROJECT_FILE:
            return "project"
        elif file_name == config.PARAMETERS_FILE:
            return "parameters"
        elif file_name == config.ACTORS_FILE:
            return "actors"
        elif file_name == config.USE_CASES_FILE:
            return "use_cases"
        elif file_name == config.TECHNICAL_FACTORS_FILE:
            return "technical_factors"
        elif file_name == config.ENVIRONMENTAL_FACTORS_FILE:
            return "environmental_factors"
        else:
            return None

    def read_project(self, stream):
        """
        Read project data from a stream.

        Parameters
        ----------
        stream : QDataStream
            The data stream.

        Returns
        -------
        dict
            The project data.
        """
        project = {}
        project['id'] = stream.readInt32()
        project['favorite'] = stream.readInt32()
        project['name'] = stream.readString()
        project['description'] = stream.readString()
        project['created_at'] = stream.readString()
        project['last_access'] = stream.readString()
        return project

    def read_parameter(self, stream):
        """
        Read parameter data from a stream.

        Parameters
        ----------
        stream : QDataStream
            The data stream.

        Returns
        -------
        dict
            The parameter data.
        """
        parameter = {}
        parameter['id'] = stream.readInt32()
        parameter['cf'] = stream.readDouble()
        parameter['analysis_percentage'] = stream.readDouble()
        parameter['design_percentage'] = stream.readDouble()
        parameter['programming_percentage'] = stream.readDouble()
        parameter['testing_percentage'] = stream.readDouble()
        parameter['overloading_percentage'] = stream.readDouble()
        parameter['actors_simple_weight'] = stream.readDouble()
        parameter['actors_average_weight'] = stream.readDouble()
        parameter['actors_complex_weight'] = stream.readDouble()
        parameter['use_cases_simple_weight'] = stream.readDouble()
        parameter['use_cases_average_weight'] = stream.readDouble()
        parameter['use_cases_complex_weight'] = stream.readDouble()
        parameter['project_id'] = stream.readInt32()
        return parameter

    def read_actor(self, stream):
        """
        Read actor data from a stream.

        Parameters
        ----------
        stream : QDataStream
            The data stream.

        Returns
        -------
        dict
            The actor data.
        """
        actor = {}
        actor['id'] = stream.readInt32()
        actor['code'] = stream.readString()
        actor['name'] = stream.readString()
        actor['complexity'] = stream.readString()
        actor['comment'] = stream.readString()
        actor['project_id'] = stream.readInt32()
        return actor

    def read_use_case(self, stream):
        """
        Read use case data from a stream.

        Parameters
        ----------
        stream : QDataStream
            The data stream.

        Returns
        -------
        dict
            The use case data.
        """
        use_case = {}
        use_case['id'] = stream.readInt32()
        use_case['code'] = stream.readString()
        use_case['name'] = stream.readString()
        use_case['complexity'] = stream.readString()
        use_case['transactions'] = stream.readInt32()
        use_case['comment'] = stream.readString()
        use_case['project_id'] = stream.readInt32()
        return use_case

    def read_factor(self, stream):
        """
        Read factor data from a stream.

        Parameters
        ----------
        stream : QDataStream
            The data stream.

        Returns
        -------
        dict
            The factor data.
        """
        factor = {}
        factor['id'] = stream.readInt32()
        factor['factor'] = stream.readString()
        factor['description'] = stream.readString()
        factor['weight'] = stream.readDouble()
        factor['influence'] = stream.readInt32()
        factor['comment'] = stream.readString()
        factor['project_id'] = stream.readInt32()
        return factor

    def get_projects(self):
        """
        Get all projects from the database.

        Returns
        -------
        tuple
            Status code and a list of projects.
        """
        q = QSqlQuery()
        if not q.exec("SELECT * FROM projects"):
            return config.FAILURE, []

        projects = []
        while q.next():
            project_data = {
                'id': q.value(0),
                'favorite': q.value(1),
                'name': q.value(2),
                'description': q.value(3),
                'created_at': q.value(4),
                'last_access': q.value(5)
            }
            projects.append(project_data)

        return config.SUCCESS, projects

    def get_project_data(self, project_id):
        """
        Get data for a specific project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        dict or int
            Dictionary containing project data and report date if successful, or failure code.
        """
        query = QSqlQuery()
        sql = "SELECT name, description FROM projects WHERE id = ?"
        if not query.prepare(sql):
            return config.FAILURE

        query.addBindValue(project_id)
        if not query.exec():
            return config.FAILURE

        results = []
        while query.next():
            results.append({
                'Project Name': query.value(0),
                'Project Description': query.value(1)
            })

        data = pd.DataFrame(results)
        now = datetime.now()
        formatted_now = now.strftime("%d/%m/%Y %H:%M:%S")
        date_data = {"QuickEst Report Date": formatted_now}
        date = pd.DataFrame(date_data, index=[0])

        return {'project_data': data, 'report_date': date}

    def export_parameters_data(self, project_id):
        """
        Export parameters data for a project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        list or int
            List of parameters data or failure code.
        """
        data = []
        query = "SELECT * FROM parameters WHERE project_id = ?"
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

    def export_project_data(self, project_id):
        """
        Export data for a specific project.

        Parameters
        ----------
        project_id : int
            The ID of the project.

        Returns
        -------
        list or int
            List of project data or failure code.
        """
        data = []
        query = "SELECT * FROM projects WHERE id = ?"
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

    def write_data_to_binary_file(self, data, destination_file):
        """
        Write data to a binary file.

        Parameters
        ----------
        data : list
            The data to write.
        destination_file : str
            The path to the destination file.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        file = QFile(destination_file)
        if not file.open(QIODevice.WriteOnly):
            return config.FAILURE

        stream = QDataStream(file)
        for row in data:
            for value in row:
                if isinstance(value, int):
                    stream.writeInt32(value)
                elif isinstance(value, float):
                    stream.writeDouble(value)
                elif isinstance(value, str):
                    stream.writeString(value)
                else:
                    stream.writeString(str(value))
        file.close()
        return config.SUCCESS

    def write_project_manifest(self, file_path, project_directory, project_manifest):
        """
        Write the project manifest to a file.

        Parameters
        ----------
        file_path : str
            The path to the manifest file.
        project_directory : str
            The directory containing the project files.
        project_manifest : dict
            The project manifest data.

        Returns
        -------
        int
            Status code indicating the result of the operation.
        """
        manifest_file_path = QDir(project_directory).filePath(file_path)
        json_document = QJsonDocument(project_manifest)
        file = QFile(manifest_file_path)
        if file.open(QFile.WriteOnly | QFile.Text):
            stream = QTextStream(file)
            stream << json_document.toJson()
            file.close()
            return config.SUCCESS
        else:
            return config.FAILURE

