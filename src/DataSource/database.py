# This Python file uses the following encoding: utf-8
# model/database.py

import sys
import os
from PySide6.QtSql import QSqlDatabase, QSqlQuery

class DataBase:
    """
    Singleton class for managing the database connection and setup.

    This class ensures that only one instance of the database connection is created and used throughout the application. It also initializes the database and creates necessary tables if they don't exist.

    Attributes
    ----------
    _instance : QSqlDatabase
        The singleton instance of the database connection.

    Methods
    -------
    """

    _instance = None  # Class attribute to store the Singleton instance

    @classmethod
    def get_instance(cls):
        """
        Return the singleton instance of the database. If the instance doesn't exist, create it.

        Returns
        -------
        QSqlDatabase
            The singleton instance of the database connection.
        """
        if cls._instance is None:
            result = cls._init_db()
            if isinstance(result, str):
                return result
            cls._instance = result
        return cls._instance

    @staticmethod
    def _init_db():
        """
        Initialize the database and create tables if they don't exist.

        Returns
        -------
        QSqlDatabase or str
            The initialized database connection or an error message if the connection fails.
        """
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        db_path = os.path.join(script_dir, "QuickEst.db")
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(db_path)

        if not db.open():
            return "Cannot connect to database."

        # Enable foreign key support and prepare the database
        query = QSqlQuery(db)
        if not query.exec("PRAGMA foreign_keys = ON"):
            return f"Failed to enable foreign keys: {query.lastError().text()}"

        # Check if tables exist before creating them
        existing_tables = db.tables()
        if not existing_tables:
            # Tables do not exist, create them
            result = DataBase._setup_database(db)
            if result is not None:
                return result
        return db

    @staticmethod
    def _setup_database(db):
        """
        Create necessary tables if they do not exist.

        Parameters
        ----------
        db : QSqlDatabase
            The database connection to use.

        Returns
        -------
        None or str
            None if tables are created successfully, or an error message if any table creation query fails.
        """
        queries = [
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                favorite BOOLEAN NOT NULL DEFAULT False,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                created_at TEXT NOT NULL,
                last_access TEXT NOT NULL
            )""",
            """
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                code TEXT NOT NULL,
                name TEXT NOT NULL,
                complexity TEXT NOT NULL,
                comment TEXT,
                project_id INTEGER NOT NULL,
                FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE ON UPDATE NO ACTION,
                UNIQUE(code, project_id)
            )""",
            """
            CREATE TABLE IF NOT EXISTS use_cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                code TEXT NOT NULL,
                name TEXT NOT NULL,
                complexity TEXT NOT NULL,
                transactions INTEGER NOT NULL,
                comment TEXT,
                project_id INTEGER NOT NULL,
                FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE ON UPDATE NO ACTION,
                UNIQUE(code, project_id)
            )""",
            """CREATE TABLE IF NOT EXISTS technical_factors (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                factor TEXT NOT NULL,
                description TEXT NOT NULL,
                weight REAL NOT NULL,
                influence INTEGER NOT NULL DEFAULT 0,
                comment TEXT,
                project_id INTEGER NOT NULL,
                FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE ON UPDATE NO ACTION,
                UNIQUE(factor, project_id)
            )""",
            """CREATE TABLE IF NOT EXISTS environmental_factors (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                factor TEXT NOT NULL,
                description TEXT NOT NULL,
                weight REAL NOT NULL,
                influence INTEGER NOT NULL DEFAULT 0,
                comment TEXT,
                project_id INTEGER NOT NULL,
                FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE ON UPDATE NO ACTION,
                UNIQUE(factor, project_id)
            )""",
            """CREATE TABLE IF NOT EXISTS parameters (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                cf REAL NOT NULL DEFAULT 20.0,
                analysis_percentage REAL NOT NULL DEFAULT 10.0,
                design_percentage REAL NOT NULL DEFAULT 20.0,
                programming_percentage REAL NOT NULL DEFAULT 40.0,
                testing_percentage REAL NOT NULL DEFAULT 15.0,
                overloading_percentage REAL NOT NULL DEFAULT 15.0,
                actors_simple_weight REAL NOT NULL DEFAULT 1.0,
                actors_average_weight REAL NOT NULL DEFAULT 2.0,
                actors_complex_weight REAL NOT NULL DEFAULT 3.0,
                useCases_simple_weight REAL NOT NULL DEFAULT 5.0,
                useCases_average_weight REAL NOT NULL DEFAULT 10.0,
                useCases_complex_weight REAL NOT NULL DEFAULT 15.0,
                project_id INTEGER NOT NULL UNIQUE,
                FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE ON UPDATE NO ACTION
            )"""
        ]

        for query_text in queries:
            q = QSqlQuery(db)
            if not q.prepare(query_text):
                return f"Failed to prepare query: {q.lastError().text()}"
            if not q.exec():
                return f"Failed to execute query: {query_text} - {q.lastError().text()}"
        return None
