# This Python file uses the following encoding: utf-8
# main_window.py
"""
This module implements the main window class for QuickEst application.
It initializes the GUI, sets up the MVC architecture, and handles user interactions.
"""

import config
import os

from Utils.widget_config import WidgetConfig
from Utils.pdf_viewer import PDFViewer
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu
from PySide6.QtGui import QFontDatabase, QFont

from Dialog.info_dialog import QuickestInfoDialog
from Dialog.license_dialog import QuickestLicenseDialog
from UI.ui_main import Ui_Main

# Importing MVC components
from View.dashboard_view import DashboardView
from Controller.dashboard_controller import DashboardController
from Model.dashboard_model import DashboardModel

from View.projects_view import ProjectsView
from Controller.projects_controller import ProjectsController
from Model.projects_model import ProjectsModel

from View.actors_view import ActorsView
from Controller.actors_controller import ActorsController
from Model.actors_model import ActorsModel

from View.useCases_view import UseCasesView
from Controller.useCases_controller import UseCasesController
from Model.useCases_model import UseCasesModel

from View.technicalFactors_view import TechnicalFactorsView
from Controller.technicalFactors_controller import TechnicalFactorsController
from Model.technicalFactors_model import TechnicalFactorsModel

from View.environmentalFactors_view import EnvironmentalFactorsView
from Controller.environmentalFactors_controller import EnvironmentalFactorsController
from Model.environmentalFactors_model import EnvironmentalFactorsModel

os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"

class MainWindow(QMainWindow):
    """
    The main window class for the QuickEst application.

    Parameters
    ----------
    parent : QWidget, optional
        The parent widget (default is None).

    Methods
    -------
    """

    def __init__(self, parent=None):
        """
        Initialize the Main window.

        Parameters
        ----------
        parent : QWidget, optional
            The parent widget (default is None).
        """
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.setWindowTitle("QuickEst")
        self.load_fonts()
        self.set_app_menus()
        self.setup_navigation()
        self.setup_mvc()
        self.connect_signals()
        self.current_project_data = None

    def switch_to_hub(self):
        """Switch the view to the main hub."""
        self.current_project_data = None
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.dashboard_Button.setChecked(True)
        self.ui.dashboard_Button_2.setChecked(True)

    def load_fonts(self):
        """Load and set application fonts."""
        fontId = QFontDatabase.addApplicationFont(config.TITLE_FONT)
        if fontId != -1:
            fontFamilies = QFontDatabase.applicationFontFamilies(fontId)
            if fontFamilies:
                self.ui.quickestName_Label.setFont(QFont(fontFamilies[0], 16))
                self.ui.quickestHubName_Label.setFont(QFont(fontFamilies[0], 16))

    def set_app_menus(self):
        """Create and set up application menus."""
        self.menuFile = QMenu()
        self.menuFile.addAction("New project").triggered.connect(self.new_project)
        self.menuFile.addAction("Import project").triggered.connect(self.open_project)
        self.menuFile.addSeparator()
        self.menuFile.addAction("Export project").triggered.connect(self.download_project)
        self.menuFile.addAction("Edit project").triggered.connect(self.edit_project)
        self.menuFile.addAction("Delete project").triggered.connect(self.delete_project)
        self.menuFile.addSeparator()
        self.menuFile.addAction("Close project").triggered.connect(self.close_project)
        self.ui.file_ToolButton.setMenu(self.menuFile)

        self.menuHelp = QMenu()
        self.menuHelp.addAction("Contents").triggered.connect(self.show_contents)
        self.menuHelp.addAction("License info").triggered.connect(self.show_license_info)
        about_menu = QMenu("About...")
        about_menu.addAction("QuickEst").triggered.connect(self.show_quickest_info)
        about_menu.addAction("Qt").triggered.connect(self.show_qt_info)
        self.menuHelp.addMenu(about_menu)
        self.ui.help_ToolButton.setMenu(self.menuHelp)

    def new_project(self):
        """Create a new project."""
        self.projects_controller.open_management_project_dialog("new", None, None)

    def open_project(self):
        """Open an existing project."""
        self.projects_controller.import_project()

    def download_project(self):
        """Download the current project."""
        self.projects_controller.download_project(self.current_project_data['id'], self.current_project_data['name'])

    def edit_project(self):
        """Edit the current project."""
        self.projects_controller.open_management_project_dialog("edit", self.current_project_data, self.current_project_data['row'])

    def delete_project(self):
        """Delete the current project."""
        self.projects_controller.delete_project(self.current_project_data['id'], self.current_project_data['row'])

    def close_project(self):
        """Close the current project."""
        self.projects_controller.close_project()

    def show_contents(self):
        """Show the contents help dialog."""
        self.pdf_viewer = PDFViewer()
        pdf_path = config.CONTENTS_FILE
        self.pdf_viewer.load_pdf(pdf_path)
        self.pdf_viewer.show()

    def show_license_info(self):
        """Show the license information dialog."""
        dialog = QuickestLicenseDialog(self)
        if not dialog.isVisible():
            dialog.show()
        else:
            dialog.raise_()

    def show_quickest_info(self):
        """Show information about QuickEst."""
        dialog = QuickestInfoDialog(self)
        if not dialog.isVisible():
            dialog.show()
        else:
            dialog.raise_()

    def show_qt_info(self):
        """Show information about Qt."""
        QApplication.aboutQt()

    def save_project_data(self, project_data):
        """Save the project data.

        Parameters
        ----------
        project_data : dict
            The data of the project to save.
        """
        self.current_project_data = project_data
        self.ui.projectName_Label.setText("Project Name: " + self.current_project_data['name'])
        if self.current_project_data['description'] != '':
            WidgetConfig.create_comment(self.current_project_data['description'], 0, self.ui.comment_tableWidget, config.COMMENT_IMG_YELLOW)
            self.ui.comment_tableWidget.setVisible(True)
        else:
            self.ui.comment_tableWidget.removeCellWidget(0, 0)
            self.ui.comment_tableWidget.setVisible(False)

    def setup_navigation(self):
        """Set up the navigation for the application."""
        self.ui.iconMenu_Widget.setHidden(True)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        navigation_map = {
            (self.ui.dashboard_Button, self.ui.dashboard_Button_2): self.switch_to_dashboard_page,
            (self.ui.actors_Button, self.ui.actors_Button_2): self.switch_to_actors_page,
            (self.ui.useCases_Button, self.ui.useCases_Button_2): self.switch_to_use_cases_page,
            (self.ui.technicalFactors_Button, self.ui.technicalFactors_Button_2): self.switch_to_technical_factors_page,
            (self.ui.environmentalFactors_Button, self.ui.environmentalFactors_Button_2): self.switch_to_environmental_factors_page,
            (self.ui.close_Button, self.ui.close_Button_2): self.close_project
        }
        for buttons, function in navigation_map.items():
            for button in buttons:
                button.clicked.connect(function)

    def switch_to_dashboard_page(self):
        """Switch to the dashboard page."""
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def switch_to_actors_page(self):
        """Switch to the actors page."""
        self.ui.stackedWidget_2.setCurrentIndex(1)

    def switch_to_use_cases_page(self):
        """Switch to the use cases page."""
        self.ui.stackedWidget_2.setCurrentIndex(2)

    def switch_to_technical_factors_page(self):
        """Switch to the technical factors page."""
        self.ui.stackedWidget_2.setCurrentIndex(3)

    def switch_to_environmental_factors_page(self):
        """Switch to the environmental factors page."""
        self.ui.stackedWidget_2.setCurrentIndex(4)

    def setup_mvc(self):
        """
        Set up the Model-View-Controller architecture for the application.
        """
        self.dashboard_view = DashboardView(self)
        self.dashboard_model = DashboardModel()
        self.dashboard_controller = DashboardController(self.dashboard_view, self.dashboard_model)

        self.actors_view = ActorsView(self)
        self.actors_model = ActorsModel()
        self.actors_controller = ActorsController(self.actors_view, self.actors_model)

        self.useCases_view = UseCasesView(self)
        self.useCases_model = UseCasesModel()
        self.useCases_controller = UseCasesController(self.useCases_view, self.useCases_model)

        self.technicalFactors_view = TechnicalFactorsView(self)
        self.technicalFactors_model = TechnicalFactorsModel()
        self.technicalFactors_controller = TechnicalFactorsController(self.technicalFactors_view, self.technicalFactors_model)

        self.environmentalFactors_view = EnvironmentalFactorsView(self)
        self.environmentalFactors_model = EnvironmentalFactorsModel()
        self.environmentalFactors_controller = EnvironmentalFactorsController(self.environmentalFactors_view, self.environmentalFactors_model)

        self.projects_view = ProjectsView(self)
        self.projects_model = ProjectsModel()
        self.projects_controller = ProjectsController(
            self.projects_view,
            self.projects_model,
            self.actors_model,
            self.useCases_model,
            self.technicalFactors_model,
            self.environmentalFactors_model,
            self.dashboard_model
        )

    def on_project_opened(self, project_data):
        """
        Handle the event when a project is opened.

        Parameters
        ----------
        project_data : dict
            The data of the project being opened.
        """
        self.dashboard_controller.load_dashboard(project_data),
        self.actors_controller.load_actors(project_data),
        self.useCases_controller.load_use_cases(project_data),
        self.technicalFactors_controller.load_technical_factors(project_data),
        self.environmentalFactors_controller.load_environmental_factors(project_data)

        self.save_project_data(project_data)
        if project_data['change_view']:
            self.ui.stackedWidget.setCurrentIndex(1)

    def connect_signals(self):
        """
        Connect signals from controllers to the appropriate handler methods.
        """
        self.projects_controller.project_opened.connect(self.on_project_opened)
        self.actors_controller.actors_data.connect(self.dashboard_controller.set_actors_data)
        self.useCases_controller.useCases_data.connect(self.dashboard_controller.set_use_cases_data)
        self.technicalFactors_controller.technicalFactors_data.connect(self.dashboard_controller.set_technical_factors_data)
        self.environmentalFactors_controller.environmentalFactors_data.connect(self.dashboard_controller.set_environmental_factors_data)
        self.dashboard_controller.report_generation_request.connect(self.handle_report_generation_request)
        self.projects_controller.project_saved.connect(self.save_project_data)
        self.projects_controller.project_closed.connect(self.switch_to_hub)

    def handle_report_generation_request(self, project_id):
        """
        Handle the report generation request.

        Parameters
        ----------
        project_id : int
            The ID of the project for which to generate the report.
        """
        self.projects_controller.generate_excel_report(project_id)
