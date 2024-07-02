# This Python file uses the following encoding: utf-8
# controller/environmentalFactors_controller.py

import config
from PySide6.QtCore import QObject, Signal

class EnvironmentalFactorsController(QObject):
    """
    Controller for managing environmental factor operations in the application.

    This class acts as the intermediary between the view and the environmental factor model. It handles user interactions, business logic, and updates the view based on changes in the model.

    Attributes
    ----------
    environmentalFactors_data : Signal
        Signal to update the dashboard with environmental factors data.

    Methods
    -------
    """
    environmentalFactors_data = Signal(dict, float)

    def __init__(self, view, model):
        """
        Initialize the EnvironmentalFactorsController.

        Parameters
        ----------
        view : EnvironmentalFactorsView
            The view that this controller will interact with.
        model : EnvironmentalFactorsModel
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

    def load_environmental_factors(self, project_data):
        """
        Load environmental factors for the given project.

        Parameters
        ----------
        project_data : dict
            Dictionary containing project data including the project ID.
        """
        self.project_id = int(project_data['id'])
        environmentalFactors = self.model.get_environmental_factors_data()
        for environmentalFactor in environmentalFactors:
            factors_results, EFactor, factors_count = self.model.get_EF_results()
            environmentalFactor['result'] = factors_results[environmentalFactor['factor']]
            if EFactor.is_integer(): EFactor = int(EFactor)
            self.view.update_environmental_factors_table(environmentalFactor, EFactor)
        self.view.update_environmental_factors_summary(factors_count)
        self.environmentalFactors_data.emit(factors_count, EFactor)


    def save_data_factor(self, data_saved):
        """
        Save the data for an environmental factor.

        Parameters
        ----------
        data_saved : dict
            Dictionary containing the saved data for the environmental factor.
        """
        result = self.model.update_environmental_factor(data_saved, self.project_id)
        if result == config.SUCCESS:
            factors_results, EFactor, factors_count = self.model.get_EF_results()
            data_saved['result'] = factors_results[data_saved['factor']]
            if EFactor.is_integer(): EFactor = int(EFactor)
            self.view.update_environmental_factors_table(data_saved, EFactor)
            self.view.update_environmental_factors_summary(factors_count)
            self.environmentalFactors_data.emit(factors_count, EFactor)
            self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
        elif result == config.NOT_EXIST:
            self.view.display_message("Warning", "The factor to be modified does not exist.", config.WARNING_IMG)
        elif result == config.FAILURE:
            self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)
