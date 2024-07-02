# This Python file uses the following encoding: utf-8
# view/projects_view.py

import config
from Utils.table_utils import TableUtils
from Utils.widget_config import WidgetConfig
from PySide6.QtWidgets import QHeaderView, QPushButton, QLineEdit, QTableWidgetItem, QAbstractItemView, QWidget, QMenu, QToolButton, QTableWidget
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt, QSize, Signal, QTimer

class ProjectsView(QWidget):
    """
    Class implementing the view for managing projects in the application.

    It provides functionalities to view, add, edit, delete, download, export and import projects, setting up tables, action buttons, and a search bar, facilitating efficient information management.

    Attributes
    ----------
    text_changed : Signal
        Signal emitted when the search text changes.
    project_managed : Signal
        Signal emitted when a project is managed (created or edited).
    project_imported : Signal
        Signal emitted when a project is imported.
    project_deleted : Signal
        Signal emitted when a project is deleted.
    project_favorite : Signal
        Signal emitted when a project's favorite status is changed.
    project_selected : Signal
        Signal emitted when a project is selected.
    project_downloaded : Signal
        Signal emitted when a project is downloaded.
    projects_exported : Signal
        Signal emitted when projects are exported.
    report_request : Signal
        Signal emitted to generate a project report.

    Methods
    -------
    """

    text_changed = Signal(str)
    project_managed = Signal(str, dict, int)
    project_imported = Signal()
    project_deleted = Signal(int, int)
    project_favorite = Signal(int, int, bool)
    project_selected = Signal(dict, int)
    project_downloaded = Signal(int, str)
    projects_exported = Signal()
    report_request = Signal(int)

    def __init__(self, parent=None):
        """
        Initialize the view with the given parent.

        Parameters
        ----------
        parent : QWidget, optional
            Parent widget.
        """
        super().__init__(parent)
        self.main = parent  # Main as parent class
        self.ui = self.main.ui  # Use the UI initialized in Main
        self.projects_table = self.ui.projects_TableWidget
        self.tableUtils = TableUtils()
        self.setup_projects_ui()

    def setup_projects_ui(self):
        """
        Setup the user interface elements for the projects view.
        """
        # Option buttons
        widgets_and_functions = [
            (self.ui.createProject_Widget, self.create_project),
            (self.ui.openProject_Widget, self.import_project),
            (self.ui.exportProjects_Widget, self.export_projects),
        ]
        for widget, function in widgets_and_functions:
            button = QPushButton(widget)
            button.setFocusPolicy(Qt.NoFocus)
            button.resize(self.main.size())
            button.setStyleSheet("background-color: transparent; border: none;")
            button.clicked.connect(function)

        # Projects table
        self.projects_table.setCornerWidget(QWidget())
        self.tableUtils.add_table(self.projects_table)

        self.projects_table.cellClicked.connect(lambda row, _: self.open_project(row=row))
        self.projects_table.setColumnHidden(0, True)

        self.projects_table.setSortingEnabled(False)
        projects_headerTable = self.projects_table.horizontalHeader()
        projects_headerTable.sectionClicked.connect(lambda index: TableUtils.on_header_clicked(index, self.projects_table, [self.projects_table.columnCount()-1]))

        favoriteHeader_Button = QPushButton(self.projects_table)
        favoriteHeader_Button.setFocusPolicy(Qt.NoFocus)
        favoriteHeader_Button.setIcon(QIcon(config.FAVORITE_IMG))
        favoriteHeader_Button.setIconSize(QSize(25, 25))
        favoriteHeader_Button.resize(self.projects_table.columnWidth(1), 46)
        favoriteHeader_Button.setStyleSheet("background-color: transparent; border: none;")
        favoriteHeader_Button.isDescending = False
        favoriteHeader_Button.clicked.connect(self.sort_favorites)

        search_action = QAction(QIcon(config.SEARCH_IMG), None, self)
        self.ui.projectsSearch_LineEdit.findChildren(QAction)[0].setIcon(QIcon(config.CLEAR_SEARCH_IMG))
        self.ui.projectsSearch_LineEdit.addAction(search_action, QLineEdit.LeadingPosition)
        self.ui.projectsSearch_LineEdit.textChanged.connect(self.search_project)

        self.projects_table.resizeEvent = self.on_table_resize
        self.projects_table.horizontalScrollBar().valueChanged.connect(lambda: TableUtils.check_column_visibility(self.projects_table, favoriteHeader_Button))

    def on_table_resize(self, event):
        """
        Handles the resize event for the projects table.

        This method adjusts the column widths and resize modes of the projects table
        based on the current width of the table.

        Parameters
        ----------
        event : QResizeEvent
            The resize event that triggered this handler.
        """
        if self.projects_table.width() <= 700:
            self.projects_table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        else:
            self.projects_table.setColumnWidth(1, 80)
            self.projects_table.setColumnWidth(3, 180)
            self.projects_table.setColumnWidth(6, 80)
            self.projects_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
            self.projects_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
            self.projects_table.horizontalHeader().setSectionResizeMode(6, QHeaderView.Fixed)
            for column in range(self.projects_table.columnCount()):
                if column not in [1, 3, 6]:
                    self.projects_table.horizontalHeader().setSectionResizeMode(column, QHeaderView.Stretch)

        horizontal_scrollbar_visible = self.projects_table.horizontalScrollBar().isVisible()

        common_styles = """
            QTableWidget {
                border: none;
            }
            QHeaderView::section {
                border: 1px solid white;
                background: rgba(0,0,0,0.25);
                color: white;
                height: 45px;
                padding-left: 15px;
                margin-bottom: 2px;
            }
            QTableWidget::Item {
                color: white;
            }
            QTableWidget::Item:selected {
                background: rgba(0,0,0,0.25);
            }
            QHeaderView::down-arrow {
                image: url(:/resources/images/whiteDownArrow.png);
            }
            QHeaderView::up-arrow {
                image: url(:/resources/images/whiteUpArrow.png);
            }
            QScrollBar:vertical {
                border: none;
                background: #3B4252;
                width: 20px;
                margin: 0px 3px 0px 3px;
                border-radius: 7px;
            }
            QScrollBar::handle:vertical {
                background: #9FF0FF;
                min-height: 20px;
                border-radius: 7px;
            }
            QScrollBar::add-line:vertical {
                background: none;
                height: 0px;
            }
            QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
            }
            QScrollBar:horizontal {
                border: none;
                background: #3B4252;
                height: 20px;
                margin: 3px 0px 3px 0px;
                border-radius: 7px;
            }
            QScrollBar::handle:horizontal {
                background: #9FF0FF;
                min-width: 20px;
                border-radius: 7px;
            }
            QScrollBar::add-line:horizontal {
                background: none;
                width: 0px;
            }
            QScrollBar::sub-line:horizontal {
                background: none;
                width: 0px;
            }
        """
        if horizontal_scrollbar_visible:
            self.projects_table.setStyleSheet(f"""
                {common_styles}
                QTableWidget {{
                    border-right: 1px solid white;
                    border-left: 1px solid white;
                }}
                QHeaderView::section {{
                    border-right: 1px solid white;
                    border-left: 1px solid white;
                }}
            """)
        else:
            self.projects_table.setStyleSheet(common_styles)

        if event:
            QTableWidget.resizeEvent(self.projects_table, event)

    def import_project(self):
        """
        Emit signal to import a project.
        """
        self.project_imported.emit()

    def sort_favorites(self):
        """
        Sort projects by favorite status.
        """
        btnFav = self.sender()
        isDescending = getattr(btnFav, 'isDescending', False)
        if isDescending:
            btnFav.isDescending = False
            self.projects_table.sortItems(4, Qt.DescendingOrder)
            self.projects_table.horizontalHeader().setSortIndicatorShown(False)
        else:
            btnFav.isDescending = True
            self.projects_table.sortItems(1, Qt.DescendingOrder)
            self.projects_table.horizontalHeader().setSortIndicatorShown(True)

    def search_project(self):
        """
        Emit signal when the search text changes.
        """
        self.text_changed.emit(self.ui.projectsSearch_LineEdit.text())

    def filter_table(self, search_text):
        """
        Filter the projects table based on the search text.

        Parameters
        ----------
        search_text : str
            Text to filter the projects table.

        Returns
        -------
        set
            Set of rows that match the search text.
        """
        matching_items = self.projects_table.findItems(search_text, Qt.MatchContains)
        matching_items = [item for item in matching_items if item is not None]
        matching_items_in_columns = [item for item in matching_items if item.column() == 2]
        rows_to_show = set(item.row() for item in matching_items_in_columns)
        return rows_to_show

    def update_table_visibility(self, rows_to_show):
        """
        Update the visibility of rows in the projects table.

        Parameters
        ----------
        rows_to_show : set
            Set of rows to show.
        """
        for i in range(self.projects_table.rowCount()):
            self.projects_table.setRowHidden(i, i not in rows_to_show)

    def display_message(self, title, message, icon_path, dialog_type='simple_message', ok_callback=None):
        """
        Display a message dialog.

        Parameters
        ----------
        title : str
            Title of the message dialog.
        message : str
            Message content.
        icon_path : str
            Path to the icon for the dialog.
        dialog_type : str, optional
            Type of dialog, default is 'simple_message'.
        ok_callback : callable, optional
            Callback function to be called when OK button is clicked.

        Returns
        -------
        QDialog
            The message dialog.
        """
        return WidgetConfig.show_message_dialog(title, message, icon_path, dialog_type, ok_callback)

    def update_last_access(self, row, last_access):
        """
        Update the last access time of a project in the table.

        Parameters
        ----------
        row : int
            Row index of the project.
        last_access : str
            Last access time to set.
        """
        self.projects_table.setItem(row, 5, QTableWidgetItem("   " + last_access))

    def update_projects_table(self, data, row_position=None):
        """
        Update the projects table with the provided data.

        Parameters
        ----------
        data : dict
            Project data to update.
        row_position : int, optional
            Row position to update, default is None.
        """
        self.projects_table.setSortingEnabled(False)
        self.projects_table.horizontalHeader().setSortIndicatorShown(True)

        if row_position is None:
            row_position = 0
            self.projects_table.insertRow(row_position)
            self.projects_table.setItem(row_position, 0, QTableWidgetItem(str(data['id'])))
            self.projects_table.setItem(row_position, 1, QTableWidgetItem(""))
            self.add_favorite_button(self.projects_table, row_position, 1, data['favorite'])
            self.projects_table.setItem(row_position, 2, QTableWidgetItem("   " + data['name']))
            self.projects_table.setItem(row_position, 4, QTableWidgetItem("   " + data['created_at']))
            self.projects_table.setItem(row_position, 5, QTableWidgetItem("   " + data['last_access']))
            self.add_options_button(self.projects_table, row_position, 6)
        else:
            self.projects_table.setItem(row_position, 2, QTableWidgetItem("   " + data['name']))

        if data['description'] != '':
            WidgetConfig.create_comment(data['description'],row_position, self.projects_table, config.COMMENT_IMG_BLUE, 3)
            self.projects_table.setItem(row_position, 3, QTableWidgetItem(""))
        else:
            self.projects_table.removeCellWidget(row_position, 3)
            self.projects_table.setItem(row_position, 3, QTableWidgetItem("––"))
            self.projects_table.item(row_position, 3).setTextAlignment(Qt.AlignCenter)

        self.projects_table.setSortingEnabled(True)
        self.projects_table.scrollToItem(self.projects_table.currentItem(), QAbstractItemView.PositionAtCenter)

    def add_favorite_button(self, table_widget, row, column, favorite):
        """
        Add a favorite button to the projects table.

        Parameters
        ----------
        table_widget : QTableWidget
            The projects table widget.
        row : int
            Row index to add the button.
        column : int
            Column index to add the button.
        favorite : bool
            Initial favorite status.
        """
        favorite_Button = QPushButton()
        favorite_Button.setFixedSize(table_widget.columnWidth(column), table_widget.rowHeight(row))
        if favorite:
            favorite_Button.setIcon(QIcon(config.FAVORITE_IMG))
            table_widget.item(row, column).setText("  ")  # 2 spaces = favorite
        else:
            favorite_Button.setIcon(QIcon(config.NOT_FAVORITE_IMG))
            table_widget.item(row, column).setText(" ")  # 1 space = not favorite
        favorite_Button.setIconSize(QSize(25, 25))
        favorite_Button.setFocusPolicy(Qt.NoFocus)
        favorite_Button.isFavorite = favorite
        favorite_Button.setStyleSheet("""
            QPushButton{ background-color: transparent; margin:7px 12px 7px 12px; border-radius: 5px;}
            QPushButton::hover{ background-color: #341D64; border: 1px solid #7000FF;}
        """)

        favorite_Button.setCursor(Qt.PointingHandCursor)
        table_widget.setCellWidget(row, column, favorite_Button)
        favorite_Button.clicked.connect(lambda: self.set_favorite(favorite_Button))

    def set_favorite(self, favorite_button):
        """
        Toggle the favorite status of a project.

        Parameters
        ----------
        favorite_button : QPushButton
            The favorite button to toggle.
        """
        index = self.projects_table.indexAt(favorite_button.pos())
        if index.isValid():
            table_row = index.row()
            project_id = self.projects_table.item(table_row, 0).text()
            is_favorite = getattr(favorite_button, 'isFavorite', False)
            self.project_favorite.emit(int(project_id), table_row, is_favorite)

    def update_favorite_button(self, row, is_favorite):
        """
        Update the favorite button in the projects table.

        Parameters
        ----------
        row : int
            Row index to update.
        is_favorite : bool
            New favorite status.
        """
        favorite_button = self.projects_table.cellWidget(row, 1)
        if is_favorite:
            favorite_button.setIcon(QIcon(config.NOT_FAVORITE_IMG))
            favorite_button.isFavorite = False
            self.projects_table.item(row, 1).setText(" ")  # 1 space = not favorite
        else:
            favorite_button.setIcon(QIcon(config.FAVORITE_IMG))
            favorite_button.isFavorite = True
            self.projects_table.item(row, 1).setText("  ")  # 2 spaces = favorite

    def add_options_button(self, table_widget, row, column):
        """
        Add an options button to the projects table.

        Parameters
        ----------
        table_widget : QTableWidget
            The projects table widget.
        row : int
            Row index to add the button.
        column : int
            Column index to add the button.
        """
        projectOptions_Menu = QMenu()
        projectOptions_Menu.addAction(QIcon(config.DOWNLOAD_PROJECT_IMG), "Download project").triggered.connect(lambda: self.download_project(projectOptions_ToolButton))
        projectOptions_Menu.addAction(QIcon(config.EXCEL_IMG), "Generate report").triggered.connect(lambda: self.generate_report(projectOptions_ToolButton))
        projectOptions_Menu.addAction(QIcon(config.EDIT_PROJECT_IMG), "Edit project").triggered.connect(lambda: self.edit_project(projectOptions_ToolButton))
        projectOptions_Menu.addAction(QIcon(config.DELETE_PROJECT_IMG), "Delete project").triggered.connect(lambda: self.delete_project(projectOptions_ToolButton))
        projectOptions_Menu.setStyleSheet("QMenu::item:selected {background-color: #9FF0FF; color:black;}")

        projectOptions_ToolButton = QToolButton()
        projectOptions_ToolButton.menu = projectOptions_Menu
        projectOptions_ToolButton.setMenu(projectOptions_Menu)
        projectOptions_ToolButton.setPopupMode(QToolButton.InstantPopup)
        projectOptions_ToolButton.setFixedSize(table_widget.columnWidth(6), table_widget.rowHeight(row))
        projectOptions_ToolButton.setIcon(QIcon(config.PROJECT_OPTIONS_IMG))
        projectOptions_ToolButton.setIconSize(QSize(30, 30))
        projectOptions_ToolButton.setFocusPolicy(Qt.NoFocus)
        projectOptions_ToolButton.setStyleSheet("""
            QToolButton{background-color: transparent; margin:7px 12px 7px 12px; border-radius: 5px;}
            QToolButton::menu-indicator {image: none;}
            QToolButton::hover{background-color: #341D64; border: 1px solid #7000FF;}
        """)
        projectOptions_ToolButton.setCursor(Qt.PointingHandCursor)
        table_widget.setCellWidget(row, column, projectOptions_ToolButton)

    def create_project(self):
        """
        Emit signal to create a new project.
        """
        self.project_managed.emit("new", None, None)

    def edit_project(self, button):
        """
        Emit signal to edit an existing project.

        Parameters
        ----------
        button : QToolButton
            The button to trigger the edit.
        """
        index = self.projects_table.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            project_data = {
                'id': self.projects_table.item(row, 0).text(),
                'name': self.projects_table.item(row, 2).text().strip(),
                'description': self.projects_table.cellWidget(row, 3).toolTip() if self.projects_table.cellWidget(row, 3) else ""
            }
            self.project_managed.emit("edit", project_data, row)

    def download_project(self, button):
        """
        Emit signal to download a project.

        Parameters
        ----------
        button : QToolButton
            The button to trigger the download.
        """
        index = self.projects_table.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            project_id = self.projects_table.item(row, 0).text()
            project_name = self.projects_table.item(row, 2).text().strip()
            self.project_downloaded.emit(int(project_id), project_name)

    def generate_report(self, button):
        """
        Emit signal to generate a project report.

        Parameters
        ----------
        button : QToolButton
            The button to trigger the download of reports.
        """
        index = self.projects_table.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            project_id = self.projects_table.item(row, 0).text()
            project_name = self.projects_table.item(row, 2).text().strip()
            project_description = self.projects_table.cellWidget(row, 3).toolTip() if self.projects_table.cellWidget(row, 3) else ""
            project_data ={
                'description': project_description,
                'id': project_id,
                'name': project_name,
                'change_view': False
            }
            self.project_selected.emit(project_data, row)
            QTimer.singleShot(0, lambda: self.report_request.emit(int(project_id)))

    def delete_project(self, button):
        """
        Emit signal to delete a project.

        Parameters
        ----------
        button : QToolButton
            The button to trigger the deletion.
        """
        index = self.projects_table.indexAt(button.pos())
        if index.isValid():
            table_row = index.row()
            project_id = self.projects_table.item(table_row, 0).text()
            self.project_deleted.emit(int(project_id), table_row)

    def remove_table_row(self, row):
        """
        Remove a row from the projects table.

        Parameters
        ----------
        row : int
            Row index to remove.
        """
        self.projects_table.removeRow(row)
        self.projects_table.selectionModel().clearSelection()

    def open_project(self, row=None, project_id=None):
        """
        Open the project based on the selected row or project ID.

        Parameters
        ----------
        row : int, optional
            Row index of the project in the table.
        project_id : int, optional
            ID of the project.
        """
        if row is not None:
            project_id = self.projects_table.item(row, 0).text()
        elif project_id is not None:
            for r in range(self.projects_table.rowCount()):
                item = self.projects_table.item(r, 0)
                if item.text() == str(project_id):
                    row = r
                    break

        project_name = self.projects_table.item(row, 2).text().strip()
        project_description = self.projects_table.cellWidget(row, 3).toolTip() if self.projects_table.cellWidget(row, 3) else ""

        project_data = {
            'id': project_id,
            'name': project_name,
            'description': project_description,
            'change_view': True
        }
        self.project_selected.emit(project_data, row)
        self.projects_table.selectionModel().clearSelection()

    def export_projects(self):
        """
        Emit signal to export projects.
        """
        self.projects_exported.emit()
