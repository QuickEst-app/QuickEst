# This Python file uses the following encoding: utf-8
# controller/dashboard_controller.py

import config
from PySide6.QtCore import QObject, Signal
from Dialog.percentage_dialog import PercentageDialog
from Dialog.cf_dialog import CFDialog

class DashboardController(QObject):
    """
    Controller for managing dashboard operations in the application.

    This class acts as the intermediary between the view and the dashboard model. It handles user interactions, business logic, and updates the view based on changes in the model.

    Attributes
    ----------
    report_generation_request : Signal
        Signal to request report generation from the main application.

    Methods
    -------
    """
    report_generation_request = Signal(int)

    def __init__(self, view, model):
        """
        Initialize the DashboardController.

        Parameters
        ----------
        view : DashboardView
            The view that this controller will interact with.
        model : DashboardModel
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
        self.view.percentages_data.connect(self.open_percentage_dialog)
        self.view.cf_data.connect(self.open_cf_dialog)
        self.view.UUCP_updated.connect(self.update_UUCP)
        self.view.TCF_updated.connect(self.update_TCF)
        self.view.ECF_updated.connect(self.update_ECF)
        self.view.report_generation.connect(self.report_request)

    def open_cf_dialog(self, cf):
        """
        Open the CF (Conversion Factor) dialog.

        Parameters
        ----------
        cf : float
            Conversion Factor value.
        """
        self.cf_Dialog = CFDialog(cf)
        self.cf_Dialog.data_saved.connect(self.handle_cf_data_saved)
        self.cf_Dialog.exec()

    def handle_cf_data_saved(self, cf_saved):
        """
        Handle the data saved from the CF dialog.

        Parameters
        ----------
        cf_saved : float
            Conversion Factor data.
        """
        result = self.model.update_cf(cf_saved, self.project_id)
        if result == config.SUCCESS:
            self.cf_Dialog.accept()
            if cf_saved.is_integer(): cf_saved = int(cf_saved)
            self.view.update_cf(cf_saved)
            self.update_E()
            self.update_effort()
            self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
        elif result == config.FAILURE:
            self.cf_Dialog.accept()
            self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)

    def load_dashboard(self, project_data):
        """
        Load the dashboard data for the given project.

        Parameters
        ----------
        project_data : dict
            Dictionary containing project data including the project ID.
        """
        self.project_id = int(project_data['id'])
        cf, percentages = self.model.get_dashboard_data()
        if cf.is_integer(): cf = int(cf)
        adjusted_percentages = {key: (int(value) if value.is_integer() else value) for key, value in percentages.items()}
        self.view.update_effort_distribution(percentages=adjusted_percentages)
        self.view.update_cf(cf)

    def open_percentage_dialog(self, percentages):
        """
        Open the percentage dialog.

        Parameters
        ----------
        percentages : dict
            Dictionary containing percentage data.
        """
        self.percentage_Dialog = PercentageDialog(percentages)
        self.percentage_Dialog.data_saved.connect(self.handle_percentage_data_saved)
        self.percentage_Dialog.exec()

    def handle_percentage_data_saved(self, percentages_saved):
        """
        Handle the data saved from the percentage dialog.

        Parameters
        ----------
        percentages_saved : dict
            Dictionary containing percentage data.
        """
        result = self.model.update_percentages(percentages_saved, self.project_id)
        if result == config.SUCCESS:
            self.percentage_Dialog.accept()
            adjusted_percentages = {key: (int(value) if value.is_integer() else value) for key, value in percentages_saved.items()}
            self.view.update_effort_distribution(percentages=adjusted_percentages)
            self.update_effort()
            self.view.display_message("Successful Operation", "The operation was completed successfully.", config.INFORMATION_IMG)
        elif result == config.FAILURE:
            self.percentage_Dialog.accept()
            self.view.display_message("Failed Operation", "The operation could not be completed.", config.CRITICAL_IMG)

    def update_UUCP(self, UAW, UUCW):
        """
        Update the UUCP (Unadjusted Use Case Points).

        Parameters
        ----------
        UAW : float
            Unadjusted Actor Weight.
        UUCW : float
            Unadjusted Use Case Weight.
        """
        UUCP = self.model.calculate_UUCP(UAW, UUCW)
        if UUCP.is_integer(): UUCP = int(UUCP)
        self.view.set_UUCP(str(UUCP))
        self.update_UCP()
        self.update_E()
        self.update_effort()

    def update_TCF(self, TFactor):
        """
        Update the TCF (Technical Complexity Factor).

        Parameters
        ----------
        TFactor : float
            The TFactor value.
        """
        TCF = self.model.calculate_TCF(TFactor)
        if TCF.is_integer(): TCF = int(TCF)
        self.view.set_TCF(str(TCF))
        self.update_UCP()
        self.update_E()
        self.update_effort()

    def update_ECF(self, EFactor):
        """
        Update the ECF (Environmental Complexity Factor).

        Parameters
        ----------
        EFactor : float
            The EFactor value.
        """
        ECF = self.model.calculate_ECF(EFactor)
        if ECF.is_integer(): ECF = int(ECF)
        self.view.set_ECF(str(ECF))
        self.update_UCP()
        self.update_E()
        self.update_effort()

    def update_UCP(self):
        """
        Update the UCP (Use Case Points).
        """
        UCP = self.model.calculate_UCP()
        if UCP.is_integer(): UCP = int(UCP)
        self.view.set_UCP(str(UCP))

    def update_E(self):
        """
        Update the E (Effort) value.
        """
        E = self.model.calculate_E()
        if E.is_integer(): E = int(E)
        self.view.set_E(str(E))

    def update_effort(self):
        """
        Update the effort distribution and total effort.
        """
        person_hours, total_hours = self.model.calculate_effort()
        if total_hours.is_integer(): total_hours = int(total_hours)
        adjusted_person_hours = {key: (int(value) if value.is_integer() else value) for key, value in person_hours.items()}
        self.view.update_effort_distribution(person_hours=adjusted_person_hours, total_effort=total_hours)

    def report_request(self):
        """
        Request the generation of a report.
        """
        self.report_generation_request.emit(self.project_id)

    def set_actors_data(self, actors_count, total_actors, UAW):
        """
        Update the actors data in the view.

        actors_count : dict
            Dictionary of actor counts by complexity.
        total_actors : int
            Total number of actors.
        UAW : float
            Unadjusted Actor Weight.
        """
        if UAW.is_integer(): UAW = int(UAW)
        self.view.set_actors_data(actors_count, total_actors, UAW)

    def set_use_cases_data(self, useCases_count, total_useCases, UUCW):
        """
        Update the use cases data in the UI.

        Parameters
        ----------
        useCases_count : dict
            Dictionary of use case counts by complexity.
        total_useCases : int
            Total number of use cases.
        UUCW : float
            Unadjusted Use Case Weight.
        """
        if UUCW.is_integer(): UUCW = int(UUCW)
        self.view.set_use_cases_data(useCases_count, total_useCases, UUCW)

    def set_technical_factors_data(self, technicalFactors_count, TFactor):
        """
        Update the technical factors data in the UI.

        Parameters
        ----------
        technicalFactors_count : dict
            Dictionary of technical factors counts by relevance.
        TFactor : float
            Technical Factor.
        """
        if TFactor.is_integer(): TFactor = int(TFactor)
        self.view.set_technical_factors_data(technicalFactors_count, TFactor)

    def set_environmental_factors_data(self, environmentalFactors_count, EFactor):
        """
        Update the environmental factors data in the UI.

        Parameters
        ----------
        environmentalFactors_count : dict
            Dictionary of environmental factors counts by relevance.
        EFactor : float
            Environmental Factor.
        """
        if EFactor.is_integer(): EFactor = int(EFactor)
        self.view.set_environmental_factors_data(environmentalFactors_count, EFactor)
