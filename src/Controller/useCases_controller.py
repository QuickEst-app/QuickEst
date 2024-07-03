# This Python file uses the following encoding: utf-8
# controller/useCases_controller.py

import config
from PySide6.QtCore import QObject, Signal
from Dialog.actors_useCases_dialog import ActorsUCDialog
from Dialog.weight_dialog import WeightDialog

class UseCasesController(QObject):
    """
    Controller for managing use case operations in the application.

    This class acts as the intermediary between the view and the use case model. It handles user interactions, business logic, and updates the view based on changes in the model.

    Attributes
    ----------
    useCases_data : Signal
        Signal to update the dashboard with use cases data.

    Methods
    -------
    """
    useCases_data = Signal(dict, int, float)

    def __init__(self, view, model):
        """
        Initialize the UseCasesController.

        Parameters
        ----------
        view : UseCasesView
            The view that this controller will interact with.
        model : UseCasesModel
            The model that this controller will interact with.
        """
        super().__init__()
        self.view = view
        self.model = model
        self.project_id = None  # Id of the selected project
        self.connect_signals()

    def connect_signals(self):
        """
        Connect signals from the view to the appropriate handler methods.
        """
        self.view.useCase_managed.connect(self.open_management_dialog)  # Create/Edit use case
        self.view.useCases_deleted.connect(self.delete_use_cases)  # Delete use case
        self.view.useCases_weights_updated.connect(self.open_weights_dialog)  # Update use case weights
        self.view.text_changed.connect(self.filter_use_cases_table)  # Search use cases

    def filter_use_cases_table(self, search_text):
        """
        Filter the use cases table based on search text.

        Parameters
        ----------
        search_text : str
            The text to search for in the use cases table.
        """
        rows_to_show = self.view.filter_table(search_text)
        self.view.update_table_visibility(rows_to_show)

    def load_use_cases(self, project_data):
        """
        Load use cases for the given project.

        Parameters
        ----------
        project_data : dict
            Dictionary containing project data including the project ID.
        """
        self.project_id = int(project_data['id'])
        self.view.delete_rows(clear_all=True)
        useCases = self.model.get_use_cases_data()
        for useCase in useCases:
            self.view.update_use_cases_table(useCase, update_rows=False)
        useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights = self.model.get_summary_data()

        useCases_UUCW = {key: (int(value) if value.is_integer() else value) for key, value in useCases_UUCW.items()}
        if total_UUCW.is_integer(): total_UUCW = int(total_UUCW)
        weights = {key: (int(value) if value.is_integer() else value) for key, value in weights.items()}

        self.view.update_use_cases_summary(useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights)
        self.useCases_data.emit(useCases_count, total_useCases, total_UUCW)

    def open_management_dialog(self, action, option, data_send, selected_row):
        """
        Open the management dialog for creating or editing a use case.

        Parameters
        ----------
        action : str
            The action to perform ("new" or "edit").
        option : str
            Additional options for the action.
        data_send : dict
            Data to be sent to the dialog.
        selected_row : int
            The selected row in the table.
        """
        self.management_Dialog = ActorsUCDialog(action, option, data_send)
        if action == "new":
            self.management_Dialog.data_saved.connect(lambda data_saved: self.create_use_case(data_saved))
        else:
            self.management_Dialog.data_saved.connect(lambda data_saved: self.update_use_case(data_send, data_saved, selected_row))
        self.management_Dialog.exec()

    def create_use_case(self, data_saved):
        """
        Create a new use case in the database.

        Parameters
        ----------
        data_saved : dict
            Data for the new use case.
        """
        result, useCase_id = self.model.create_use_case(data_saved, self.project_id)
        if result == config.SUCCESS:
            self.management_Dialog.accept()
            data_saved['id'] = str(useCase_id)
            self.view.update_use_cases_table(data_saved)
            useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights = self.model.get_summary_data()

            useCases_UUCW = {key: (int(value) if value.is_integer() else value) for key, value in useCases_UUCW.items()}
            if total_UUCW.is_integer(): total_UUCW = int(total_UUCW)
            weights = {key: (int(value) if value.is_integer() else value) for key, value in weights.items()}

            self.view.update_use_cases_summary(useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights)
            self.useCases_data.emit(useCases_count, total_useCases, total_UUCW)
            self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
        elif result == config.ALREADY_EXIST:
            self.view.display_message("Warning", "There is already a use case with that code. Please, try again.", config.WARNING_IMG)
        elif result == config.FAILURE:
            self.management_Dialog.accept()
            self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)

    def update_use_case(self, data_send, data_saved, selected_row):
        """
        Update an existing use case in the database.

        Parameters
        ----------
        data_send : dict
            Original data of the use case to be updated.
        data_saved : dict
            New data for the use case.
        selected_row : int
            The selected row in the table.
        """
        result = self.model.update_use_case(data_send, data_saved)
        if result == config.SUCCESS:
            self.management_Dialog.accept()
            self.view.update_use_cases_table(data_saved, selected_row)
            if data_send['complexity'] != data_saved['complexity']:
                useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights = self.model.get_summary_data()

                useCases_UUCW = {key: (int(value) if value.is_integer() else value) for key, value in useCases_UUCW.items()}
                if total_UUCW.is_integer(): total_UUCW = int(total_UUCW)
                weights = {key: (int(value) if value.is_integer() else value) for key, value in weights.items()}

                self.view.update_use_cases_summary(useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights)
                self.useCases_data.emit(useCases_count, total_useCases, total_UUCW)
            self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
        elif result == config.ALREADY_EXIST:
            self.view.display_message("Warning", "There is already a use case with that code. Please, try again.", config.WARNING_IMG)
        elif result == config.NOT_EXIST:
            self.management_Dialog.accept()
            self.view.display_message("Warning", "The use case to be modified does not exist.", config.WARNING_IMG)
        elif result == config.FAILURE:
            self.management_Dialog.accept()
            self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)

    def delete_use_cases(self, useCases_data, selected_rows):
        """
        Delete selected use cases from the database.

        Parameters
        ----------
        useCases_info : list of dict
            Information of the use cases to be deleted.
        selected_rows : list of int
            Rows selected in the table.
        """
        reply = self.view.display_message("Confirmation Message", "Are you sure you want to delete the selected use cases?", config.CONFIRMATION_IMG, "confirmation_message")
        if reply:
            result, missing_ids = self.model.delete_use_cases(useCases_data)
            if result == config.SUCCESS:
                self.view.delete_rows(selected_rows)
                useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights = self.model.get_summary_data()

                useCases_UUCW = {key: (int(value) if value.is_integer() else value) for key, value in useCases_UUCW.items()}
                if total_UUCW.is_integer(): total_UUCW = int(total_UUCW)
                weights = {key: (int(value) if value.is_integer() else value) for key, value in weights.items()}

                self.view.update_use_cases_summary(useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights)
                self.useCases_data.emit(useCases_count, total_useCases, total_UUCW)
                self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
            elif result == config.NOT_EXIST:
                missing_codes = [useCases_data[id]['code'] for id in missing_ids if id in useCases_data]
                missing_codes_str = ", ".join(missing_codes)
                self.view.display_message("Warning", f"The following use cases do not exist and could not be deleted: {missing_codes_str}", config.WARNING_IMG)
            elif result == config.FAILURE:
                self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)

    def open_weights_dialog(self, weights):
        """
        Open the dialog to update use case weights.

        Parameters
        ----------
        weights : dict
            Dictionary containing the current weights of the use cases.
        """
        self.weight_Dialog = WeightDialog(weights, "useCases")
        self.weight_Dialog.data_saved.connect(self.update_use_cases_weights)
        self.weight_Dialog.exec()

    def update_use_cases_weights(self, weights_saved):
        """
        Update the weights of the use cases.

        Parameters
        ----------
        weights_saved : dict
            Dictionary containing the new weights of the use cases.
        """
        result = self.model.update_use_cases_weights(weights_saved, self.project_id)
        if result == config.SUCCESS:
            self.weight_Dialog.accept()
            useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights = self.model.get_summary_data()

            useCases_UUCW = {key: (int(value) if value.is_integer() else value) for key, value in useCases_UUCW.items()}
            if total_UUCW.is_integer(): total_UUCW = int(total_UUCW)
            weights = {key: (int(value) if value.is_integer() else value) for key, value in weights.items()}

            self.view.update_use_cases_summary(useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights)
            self.useCases_data.emit(useCases_count, total_useCases, total_UUCW)
            self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
        elif result == config.FAILURE:
            self.weight_Dialog.accept()
            self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)
