# This Python file uses the following encoding: utf-8
# view/actors_view.py

import config

from Utils.table_utils import TableUtils
from Utils.border_bottom_delegate import BorderBottomDelegate
from Utils.button_utils import ButtonUtils
from Utils.widget_config import WidgetConfig
from Utils.numeric_table_item import NumericTableWidgetItem

from PySide6.QtWidgets import QHeaderView, QWidget, QTableWidgetItem, QAbstractItemView, QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QIcon

class ActorsView(QWidget):
    """
    Class implementing the view for managing actors in the application.

    It handles the user interface related to actor management, providing functionalities to view, add, edit, and delete actors. It includes the setup of tables, action buttons, and a search bar for filtering actors, facilitating efficient information management.

    Attributes
    ----------
    actor_managed : Signal
        Signal emitted when an actor is managed (created or edited).
    actors_deleted : Signal
        Signal emitted when actors are deleted.
    actors_weights_updated : Signal
        Signal emitted when actor weights are updated.
    text_changed : Signal
        Signal emitted when the text in the actor search bar changes.

    Methods
    -------
    """

    actor_managed = Signal(str, str, dict, int)
    actors_deleted = Signal(dict, list)
    actors_weights_updated = Signal(dict)
    text_changed = Signal(str)

    def __init__(self, parent=None):
        """
        Initialize the actors view.

        Parameters
        ----------
        parent : QWidget, optional
            The parent widget of this view, default is None.
        """
        super().__init__(parent)
        self.main = parent  # Main as parent class
        self.ui = self.main.ui  # Use the UI initialized in Main
        self.actors_table = self.ui.actors_TableWidget
        self.actors_summary_table = self.ui.actorsSummary_TableWidget
        self.tableUtils = TableUtils()
        self.setup_actors_ui()

    def setup_actors_ui(self):
        """
        Setup the user interface for the actors table and the actors summary table.
        """
        # Summary table
        self.actors_summary_table.setCornerWidget(QWidget())
        self.actors_summary_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.actors_summary_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.actors_summary_table.setColumnWidth(1, 480)
        self.actors_summary_table.setSpan(3, 0, 1, 3)
        self.actors_summary_table.horizontalHeader().sectionClicked.connect(lambda index: self.update_actors_weights() if index == 2 else None)
        self.actors_summary_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Actor table
        self.actors_table.setCornerWidget(QWidget())
        self.tableUtils.add_table(self.actors_table)
        self.actors_table.setColumnHidden(0, True)
        actors_headerTable = self.actors_table.horizontalHeader()
        actors_headerTable.sectionClicked.connect(lambda index: TableUtils.on_header_clicked(index, self.actors_table, [1], True))
        self.actors_table.setColumnWidth(1, 80)
        self.actors_table.setColumnWidth(5, 106)
        for column in range(self.actors_table.columnCount()):
            if column not in [1, 5]:
                self.actors_table.horizontalHeader().setSectionResizeMode(column, QHeaderView.Stretch)
            else:
                self.actors_table.horizontalHeader().setSectionResizeMode(column, QHeaderView.Fixed)

        actors_borderBottomDelegate = BorderBottomDelegate()
        for column in range(self.actors_table.columnCount()):
            self.actors_table.setItemDelegateForColumn(column, actors_borderBottomDelegate)

        actors_header = self.actors_table.horizontalHeader()
        self.table_checkbox = TableUtils.setup_header_checkbox(self.actors_table, actors_header, [1])
        self.actors_table.horizontalScrollBar().valueChanged.connect(lambda: TableUtils.check_column_visibility(self.actors_table, self.table_checkbox))

        # Options Buttons
        self.ui.editActor_Button.setEnabled(False)
        ButtonUtils.set_styles_button(self.ui.editActor_Button, '#48F4FF', '#22577A', config.EDIT_IMG, config.EDIT_DISABLED_IMG, False)
        self.ui.deleteActor_Button.setEnabled(False)
        ButtonUtils.set_styles_button(self.ui.deleteActor_Button, '#FF0000', '#FFFFFF', config.DELETE_IMG, config.DELETE_DISABLED_IMG, False)
        self.actors_table.itemSelectionChanged.connect(lambda: ButtonUtils.check_selection(
            self.actors_table,
            self.ui.editActor_Button,
            self.ui.deleteActor_Button,
            config.EDIT_IMG,
            config.EDIT_DISABLED_IMG,
            config.DELETE_IMG,
            config.DELETE_DISABLED_IMG,
        ))
        self.ui.newActor_Button.clicked.connect(self.create_actor)
        self.ui.editActor_Button.clicked.connect(self.edit_actor)
        self.ui.deleteActor_Button.clicked.connect(self.delete_actors)
        search_action = QAction(QIcon(config.SEARCH_IMG), None, self)
        self.ui.actorsSearch_LineEdit.findChildren(QAction)[0].setIcon(QIcon(config.CLEAR_SEARCH_IMG))
        self.ui.actorsSearch_LineEdit.addAction(search_action, QLineEdit.LeadingPosition)
        self.ui.actorsSearch_LineEdit.textChanged.connect(self.search_actor)

    def create_actor(self):
        """
        Emit a signal to create a new actor.
        """
        actor_codes = {
            f"ACT-{item.text().split('-')[1]}": int(item.text().split("-")[1])
            for row in range(self.actors_table.rowCount())
            if (item := self.actors_table.item(row, 2)) is not None and item.text().startswith("ACT-")
        }
        self.actor_managed.emit("new", "actor", actor_codes, None)

    def search_actor(self):
        """
        Emit a signal when the text in the actor search bar changes.
        """
        self.text_changed.emit(self.ui.actorsSearch_LineEdit.text())

    def display_message(self, title, message, icon_path, dialog_type='simple_message'):
        """
        Display a dialog with a message.

        Parameters
        ----------
        title : str
            The title of the message.
        message : str
            The content of the message.
        icon_path : str
            Path to the icon for the message.
        dialog_type : str, optional
            Type of dialog, default is 'simple_message'.

        Returns
        -------
        QDialog
            The displayed dialog.
        """
        return WidgetConfig.show_message_dialog(title, message, icon_path, dialog_type)

    def edit_actor(self):
        """
        Edit the selected actor.
        """
        selected_indexes = self.actors_table.selectedIndexes()
        unique_rows = set(index.row() for index in selected_indexes)
        if len(unique_rows) != 1:
            self.display_message("Failed Operation", "No row selected. Please, try again.", config.CRITICAL_IMG)
            return
        selected_row = unique_rows.pop()
        actor_codes = {
            f"ACT-{item.text().split('-')[1]}": int(item.text().split("-")[1])
            for row in range(self.actors_table.rowCount())
            if (item := self.actors_table.item(row, 2)) is not None and item.text().startswith("ACT-")
        }
        actor_data = {
            'id': self.actors_table.item(selected_row, 0).text(),
            'code': self.actors_table.item(selected_row, 2).text(),
            'name': self.actors_table.item(selected_row, 3).text(),
            'complexity': self.actors_table.item(selected_row, 4).text(),
            'comment': self.actors_table.cellWidget(selected_row, 5).toolTip() if self.actors_table.cellWidget(selected_row, 5) else "",
            'codes': actor_codes
        }
        actor_codes.pop(actor_data['code'])
        #self.actors_table.selectionModel().clearSelection()
        self.actor_managed.emit("edit", "actor", actor_data, selected_row)

    def update_actors_table(self, data_saved, selected_row=None, update_rows=True):
        """
        Update the actors table with the provided data.

        Parameters
        ----------
        data_saved : dict
            Saved actor data.
        selected_row : int, optional
            Selected row to update, default is None.
        update_rows : bool, optional
            Whether to update row numbers, default is True.
        """
        self.actors_table.setSortingEnabled(False)
        if selected_row is None:
            row = self.actors_table.rowCount()
            self.actors_table.insertRow(row)
            numbers_item = QTableWidgetItem()
            numbers_item.setData(Qt.EditRole, row + 1)
            self.actors_table.setItem(row, 0, QTableWidgetItem(str(data_saved['id'])))
            self.actors_table.setItem(row, 1, numbers_item)
            self.actors_table.item(row, 1).setTextAlignment(Qt.AlignCenter)
        else:
            row = selected_row
        self.actors_table.setItem(row, 2, NumericTableWidgetItem(data_saved['code']))
        self.actors_table.item(row, 2).setTextAlignment(Qt.AlignCenter)
        self.actors_table.setItem(row, 3, QTableWidgetItem(data_saved['name']))
        self.actors_table.item(row, 3).setTextAlignment(Qt.AlignCenter)
        self.actors_table.setItem(row, 4, QTableWidgetItem(data_saved['complexity']))
        self.actors_table.item(row, 4).setTextAlignment(Qt.AlignCenter)
        if data_saved['comment'] != '':
            WidgetConfig.create_comment(data_saved['comment'], row, self.actors_table, config.COMMENT_IMG_YELLOW)
            self.actors_table.setItem(row, 5, QTableWidgetItem(""))
        else:
            self.actors_table.removeCellWidget(row, self.actors_table.columnCount() - 1)
            self.actors_table.setItem(row, 5, QTableWidgetItem(" "))

        if update_rows:
            self.actors_table.selectRow(row)
            TableUtils.update_row_numbers(self.actors_table)
            self.actors_table.scrollToItem(self.actors_table.currentItem(), QAbstractItemView.PositionAtCenter)
            self.actors_table.selectionModel().clearSelection()

        self.table_checkbox.setCheckState(Qt.Unchecked)
        self.table_checkbox.setVisible(self.actors_table.rowCount() > 0)

        if self.actors_table.rowCount() == config.ACTOR_LIMIT:
            self.ui.newActor_Button.setEnabled(False)
            ButtonUtils.set_styles_button(self.ui.newActor_Button, '#48F4FF', '#22577A', config.NEW_IMG, config.NEW_DISABLED_IMG, False)
            self.ui.newActor_Button.setEnabled(False)

    def update_actors_summary(self, actors_count, total_actors, actors_UAW, total_UAW, weights):
        """
        Update the actors summary table with the provided data.

        Parameters
        ----------
        actors_count : dict
            Count of actors by complexity.
        total_actors : int
            Total number of actors.
        actors_UAW : dict
            Unadjusted Actor Weights (UAW) by complexity.
        total_UAW : float
            Total UAW.
        weights : dict
            Actor weights by complexity.
        """
        complexity_mapping = {"Simple": 0, "Average": 1, "Complex": 2}
        for complexity, row_index in complexity_mapping.items():
            self.actors_summary_table.item(row_index, 2).setText(str(weights[complexity]))
            self.actors_summary_table.item(row_index, 3).setText(str(actors_count[complexity]))
            self.actors_summary_table.item(row_index, 4).setText(str(actors_UAW[complexity]))
        self.actors_summary_table.item(3, 3).setText(str(total_actors))
        self.actors_summary_table.item(3, 4).setText(str(total_UAW))

    def delete_actors(self):
        """
        Delete the selected actors.
        """
        selected_rows = sorted([index.row() for index in self.actors_table.selectionModel().selectedRows()], reverse=True)
        if not selected_rows:
            self.display_message("Failed operation", "No actors selected. Please select at least one actor to delete.", config.WARNING_IMG)
            return
        actors_data = {
            self.actors_table.item(row, 0).text(): {
                'code': self.actors_table.item(row, 2).text(),
                'complexity': self.actors_table.item(row, 4).text()
            } for row in selected_rows
        }
        self.actors_deleted.emit(actors_data, selected_rows)

    def delete_rows(self, rows=None, clear_all=False):
        """
        Delete rows from the actors table.

        Parameters
        ----------
        rows : list of int, optional
            List of row indices to delete. Ignored if clear_all is True.
        clear_all : bool, optional
            If True, deletes all rows in the table.
        """
        if clear_all:
            self.actors_table.setRowCount(0)
        else:
            if rows is not None:
                for row in sorted(rows, reverse=True):
                    self.actors_table.removeRow(row)
                    TableUtils.update_row_numbers(self.actors_table, row)

        self.table_checkbox.setCheckState(Qt.Unchecked)
        self.table_checkbox.setVisible(self.actors_table.rowCount() > 0)

        self.ui.newActor_Button.setEnabled(True)
        ButtonUtils.set_styles_button(self.ui.newActor_Button, '#5AFFA6', '#094646', config.NEW_IMG, config.NEW_DISABLED_IMG, True)
        self.ui.newActor_Button.setEnabled(True)

    def update_actors_weights(self):
        """
        Update actor weights and emit the corresponding signal.
        """
        complexity_to_key = {
            'Simple': 'simple_weight',
            'Average': 'average_weight',
            'Complex': 'complex_weight'
        }
        weights = {key: 0 for key in complexity_to_key.values()}
        for row in range(self.actors_summary_table.rowCount() - 1):
            complexity = self.actors_summary_table.item(row, 0).text()
            weight = float(self.actors_summary_table.item(row, 2).text())
            if complexity in complexity_to_key:
                weights[complexity_to_key[complexity]] = weight
        self.actors_weights_updated.emit(weights)

    def filter_table(self, search_text):
        """
        Filter the actors table based on the search text.

        Parameters
        ----------
        search_text : str
            Text to filter the actors table.

        Returns
        -------
        set
            Set of rows that match the search text.
        """
        matching_items = self.actors_table.findItems(search_text, Qt.MatchContains)
        matching_items = [item for item in matching_items if item is not None]
        matching_items_in_columns = [item for item in matching_items if item.column() in [2, 3, 4]]
        rows_to_show = set(item.row() for item in matching_items_in_columns)
        return rows_to_show

    def update_table_visibility(self, rows_to_show):
        """
        Update the visibility of rows in the actors table.

        Parameters
        ----------
        rows_to_show : set
            Set of rows to show.
        """
        for i in range(self.actors_table.rowCount()):
            self.actors_table.setRowHidden(i, i not in rows_to_show)
