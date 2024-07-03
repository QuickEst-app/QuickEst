# This Python file uses the following encoding: utf-8
# controller/technicalFactors_controller.py

import config
from PySide6.QtCore import QObject, Signal

class TechnicalFactorsController(QObject):
    """
    Controller for managing technical factor operations in the application.

    This class acts as the intermediary between the view and the technical factor model. It handles user interactions, business logic, and updates the view based on changes in the model.

    Attributes
    ----------
    technicalFactors_data : Signal
        Signal to update the dashboard with technical factors data.

    Methods
    -------
    """
    technicalFactors_data = Signal(dict, float)

    def __init__(self, view, model):
        """
        Initialize the TechnicalFactorsController.

        Parameters
        ----------
        view : TechnicalFactorsView
            The view that this controller will interact with.
        model : TechnicalFactorsModel
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
        self.view.factor_saved.connect(self.save_data_factor)

    def load_technical_factors(self, project_data):
        """
        Load technical factors for the given project.

        Parameters
        ----------
        project_data : dict
            Dictionary containing project data including the project ID.
        """
        self.project_id = int(project_data['id'])
        technicalFactors = self.model.get_technical_factors_data()
        for technicalFactor in technicalFactors:
            factors_results, TFactor, factors_count = self.model.get_TF_results()
            technicalFactor['result'] = factors_results[technicalFactor['factor']]
            if TFactor.is_integer(): TFactor = int(TFactor)
            self.view.update_technical_factors_table(technicalFactor, TFactor)
        self.view.update_technical_factors_summary(factors_count)
        self.technicalFactors_data.emit(factors_count, TFactor)

    def save_data_factor(self, data_saved):
        """
        Save the data for a technical factor.

        Parameters
        ----------
        data_saved : dict
            Dictionary containing the saved data for the technical factor.
        """
        result = self.model.update_technical_factor(data_saved,self.project_id)
        if result == config.SUCCESS:
            factors_results, TFactor, factors_count = self.model.get_TF_results()
            data_saved['result'] = factors_results[data_saved['factor']]
            if TFactor.is_integer(): TFactor = int(TFactor)
            self.view.update_technical_factors_table(data_saved, TFactor)
            self.view.update_technical_factors_summary(factors_count)
            self.technicalFactors_data.emit(factors_count, TFactor)
            self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
        elif result == config.NOT_EXIST:
            self.view.display_message("Warning", "The factor to be modified doesn't exist.", config.WARNING_IMG)
        elif result == config.FAILURE:
            self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)
