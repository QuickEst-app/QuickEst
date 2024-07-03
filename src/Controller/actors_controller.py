# This Python file uses the following encoding: utf-8
# controller/actors_controller.py

import config
from PySide6.QtCore import QObject, Signal
from Dialog.actors_useCases_dialog import ActorsUCDialog
from Dialog.weight_dialog import WeightDialog

class ActorsController(QObject):
    """
    Controller for managing actor operations in the application.

    This class acts as the intermediary between the view and the actor model. It handles user interactions, business logic, and updates the view based on changes in the model.

    Attributes
    ----------
    actors_data : Signal
        Signal to update the dashboard with actors data.

    Methods
    -------
    """
    actors_data = Signal(dict, int, float)

    def __init__(self, view, model):
        """
        Initialize the ActorsController.

        Parameters
        ----------
        view : ActorsView
            The view that this controller will interact with.
        model : ActorsModel
            The model that this controller will interact with.
        """
        super().__init__()
        self.view = view
        self.model = model
        self.project_id = None
        self.connect_signals()

    def connect_signals(self):
        """
        Connect signals from the view to the appropriate handler methods.
        """
        self.view.actor_managed.connect(self.open_management_dialog)
        self.view.actors_deleted.connect(self.delete_actors)
        self.view.actors_weights_updated.connect(self.open_weights_dialog)
        self.view.text_changed.connect(self.filter_actors_table)

    def filter_actors_table(self, search_text):
        """
        Filter the actors table based on search text.

        Parameters
        ----------
        search_text : str
            The text to search for in the actors table.
        """
        rows_to_show = self.view.filter_table(search_text)
        self.view.update_table_visibility(rows_to_show)

    def load_actors(self, project_data):
        """
        Load actors for the given project.

        Parameters
        ----------
        project_data : dict
            Dictionary containing project data including the project ID.
        """
        self.project_id = int(project_data['id'])
        self.view.delete_rows(clear_all=True)
        actors = self.model.get_actors_data()
        for actor in actors:
            self.view.update_actors_table(actor, update_rows=False)
        actors_count, total_actors, actors_UAW, total_UAW, weights = self.model.get_summary_data()

        actors_UAW = {key: (int(value) if value.is_integer() else value) for key, value in actors_UAW.items()}
        if total_UAW.is_integer(): total_UAW = int(total_UAW)
        weights = {key: (int(value) if value.is_integer() else value) for key, value in weights.items()}

        self.view.update_actors_summary(actors_count, total_actors, actors_UAW, total_UAW, weights)
        self.actors_data.emit(actors_count, total_actors, total_UAW)

    def open_management_dialog(self, action, option, data_send, selected_row):
        """
        Open the management dialog for creating or editing an actor.

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
            self.management_Dialog.data_saved.connect(lambda data_saved: self.create_actor(data_saved))
        else:
            self.management_Dialog.data_saved.connect(lambda data_saved: self.update_actor(data_send, data_saved, selected_row))
        self.management_Dialog.exec()

    def create_actor(self, data_saved):
        """
        Create a new actor in the database.

        Parameters
        ----------
        data_saved : dict
            Data for the new actor.
        """
        result, actor_id = self.model.create_actor(data_saved, self.project_id)
        if result == config.SUCCESS:
            self.management_Dialog.accept()
            data_saved['id'] = str(actor_id)
            self.view.update_actors_table(data_saved)
            actors_count, total_actors, actors_UAW, total_UAW, weights = self.model.get_summary_data()

            actors_UAW = {key: (int(value) if value.is_integer() else value) for key, value in actors_UAW.items()}
            if total_UAW.is_integer(): total_UAW = int(total_UAW)
            weights = {key: (int(value) if value.is_integer() else value) for key, value in weights.items()}

            self.view.update_actors_summary(actors_count, total_actors, actors_UAW, total_UAW, weights)
            self.actors_data.emit(actors_count, total_actors, total_UAW)
            self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
        elif result == config.ALREADY_EXIST:
            self.view.display_message("Warning", "There is already an actor with that code. Please, try again.", config.WARNING_IMG)
        elif result == config.FAILURE:
            self.management_Dialog.accept()
            self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)

    def update_actor(self, data_send, data_saved, selected_row):
        """
        Update an existing actor in the database.

        Parameters
        ----------
        data_send : dict
            Original data of the actor to be updated.
        data_saved : dict
            New data for the actor.
        selected_row : int
            The selected row in the table.
        """
        result = self.model.update_actor(data_send, data_saved)
        if result == config.SUCCESS:
            self.management_Dialog.accept()
            self.view.update_actors_table(data_saved, selected_row)
            if data_send['complexity'] != data_saved['complexity']:
                actors_count, total_actors, actors_UAW, total_UAW, weights = self.model.get_summary_data()

                actors_UAW = {key: (int(value) if value.is_integer() else value) for key, value in actors_UAW.items()}
                if total_UAW.is_integer(): total_UAW = int(total_UAW)
                weights = {key: (int(value) if value.is_integer() else value) for key, value in weights.items()}

                self.view.update_actors_summary(actors_count, total_actors, actors_UAW, total_UAW, weights)
                self.actors_data.emit(actors_count, total_actors, total_UAW)
            self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
        elif result == config.ALREADY_EXIST:
            self.view.display_message("Warning", "There is already an actor with that code. Please, try again.", config.WARNING_IMG)
        elif result == config.NOT_EXIST:
            self.management_Dialog.accept()
            self.view.display_message("Warning", "The actor to be modified doesn't exist.", config.WARNING_IMG)
        elif result == config.FAILURE:
            self.management_Dialog.accept()
            self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)

    def delete_actors(self, actors_data, selected_rows):
        """
        Delete selected actors from the database.

        Parameters
        ----------
        actors_data : list of dict
            Information of the actors to be deleted.
        selected_rows : list of int
            Rows selected in the table.
        """
        reply = self.view.display_message("Confirmation Message", "Are you sure you want to delete the selected actors?", config.CONFIRMATION_IMG, "confirmation_message")
        if reply:
            result, missing_ids = self.model.delete_actors(actors_data)
            if result == config.SUCCESS:
                self.view.delete_rows(selected_rows)
                actors_count, total_actors, actors_UAW, total_UAW, weights = self.model.get_summary_data()

                actors_UAW = {key: (int(value) if value.is_integer() else value) for key, value in actors_UAW.items()}
                if total_UAW.is_integer(): total_UAW = int(total_UAW)
                weights = {key: (int(value) if value.is_integer() else value) for key, value in weights.items()}

                self.view.update_actors_summary(actors_count, total_actors, actors_UAW, total_UAW, weights)
                self.actors_data.emit(actors_count, total_actors, total_UAW)
                self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
            elif result == config.NOT_EXIST:
                missing_codes = [actors_data[id]['code'] for id in missing_ids if id in actors_data]
                missing_codes_str = ", ".join(missing_codes)
                self.view.display_message("Warning", f"The following actors don't exist and could not be deleted: {missing_codes_str}", config.WARNING_IMG)
            elif result == config.FAILURE:
                self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)

    def open_weights_dialog(self, weights):
        """
        Open the dialog to update actors' weights.

        Parameters
        ----------
        weights : dict
            Dictionary containing the current weights of the actors.
        """
        self.weight_Dialog = WeightDialog(weights, "actors")
        self.weight_Dialog.data_saved.connect(self.update_actors_weights)
        self.weight_Dialog.exec()

    def update_actors_weights(self, weights_saved):
        """
        Update the weights of the actors.

        Parameters
        ----------
        weights_saved : dict
            Dictionary containing the new weights of the actors.
        """
        result = self.model.update_actors_weights(weights_saved, self.project_id)
        if result == config.SUCCESS:
            self.weight_Dialog.accept()
            actors_count, total_actors, actors_UAW, total_UAW, weights = self.model.get_summary_data()

            actors_UAW = {key: (int(value) if value.is_integer() else value) for key, value in actors_UAW.items()}
            if total_UAW.is_integer(): total_UAW = int(total_UAW)
            weights = {key: (int(value) if value.is_integer() else value) for key, value in weights.items()}

            self.view.update_actors_summary(actors_count, total_actors, actors_UAW, total_UAW, weights)
            self.actors_data.emit(actors_count, total_actors, total_UAW)
            self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
        elif result == config.FAILURE:
            self.weight_Dialog.accept()
            self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)
