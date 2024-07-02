# This Python file uses the following encoding: utf-8
# view/use_cases_view.py

import config
from Utils.table_utils import TableUtils
from Utils.border_bottom_delegate import BorderBottomDelegate
from Utils.button_utils import ButtonUtils
from Utils.widget_config import WidgetConfig
from Utils.numeric_table_item import NumericTableWidgetItem
from PySide6.QtWidgets import QHeaderView, QWidget, QTableWidgetItem, QLineEdit, QAbstractItemView
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QIcon

class UseCasesView(QWidget):
    """
    Class implementing the view for managing use cases in the application.

    It handles the user interface related to use cases management, providing functionalities to view, add, edit, and delete use cases. It includes the setup of tables, action buttons, and a search bar for filtering use cases, facilitating efficient information management.

    Attributes
    ----------
    useCase_managed : Signal
        Signal emitted when a use case is managed.
    useCases_deleted : Signal
        Signal emitted when use cases are deleted.
    useCases_weights_updated : Signal
        Signal emitted when use cases weights are updated.
    text_changed : Signal
        Signal emitted when the search text changes.

    Methods
    -------
    """

    useCase_managed = Signal(str, str, dict, int)
    useCases_deleted = Signal(dict, list)
    useCases_weights_updated = Signal(dict)
    text_changed = Signal(str)

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
        self.useCases_table = self.ui.useCases_TableWidget
        self.useCases_summary_table = self.ui.useCasesSummary_TableWidget
        self.tableUtils = TableUtils()
        self.setup_use_cases_ui()

    def setup_use_cases_ui(self):
        """
        Setup the user interface elements for the use cases view.
        """
        # Summary table
        self.useCases_summary_table.setCornerWidget(QWidget())
        self.useCases_summary_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.useCases_summary_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.useCases_summary_table.setColumnWidth(1, 480)
        self.useCases_summary_table.setSpan(3, 0, 1, 3)
        self.useCases_summary_table.horizontalHeader().sectionClicked.connect(lambda index: self.update_use_cases_weights() if index == 2 else None)

        # Use Cases table
        self.useCases_table.setCornerWidget(QWidget())
        self.tableUtils.add_table(self.useCases_table)
        self.useCases_table.setColumnHidden(0, True)
        useCases_headerTable = self.useCases_table.horizontalHeader()
        useCases_headerTable.sectionClicked.connect(lambda index: TableUtils.on_header_clicked(index, self.useCases_table, [1], True))

        self.useCases_table.setColumnWidth(1, 80)
        self.useCases_table.setColumnWidth(6, 106)
        for column in range(self.useCases_table.columnCount()):
            if column not in [1, 6]:
                self.useCases_table.horizontalHeader().setSectionResizeMode(column, QHeaderView.Stretch)
            else:
                self.useCases_table.horizontalHeader().setSectionResizeMode(column, QHeaderView.Fixed)

        useCases_borderBottomDelegate = BorderBottomDelegate()
        for column in range(self.useCases_table.columnCount()):
            self.useCases_table.setItemDelegateForColumn(column, useCases_borderBottomDelegate)

        useCases_header = self.useCases_table.horizontalHeader()
        self.table_checkbox = TableUtils.setup_header_checkbox(self.useCases_table, useCases_header, [1])
        self.useCases_table.horizontalScrollBar().valueChanged.connect(lambda: TableUtils.check_column_visibility(self.useCases_table, self.table_checkbox))

        # Options Buttons
        self.ui.editUseCase_Button.setEnabled(False)
        ButtonUtils.set_styles_button(self.ui.editUseCase_Button, '#48F4FF', '#22577A', config.EDIT_IMG, config.EDIT_DISABLED_IMG, False)
        self.ui.deleteUseCase_Button.setEnabled(False)
        ButtonUtils.set_styles_button(self.ui.deleteUseCase_Button, '#FF0000', '#FFFFFF', config.DELETE_IMG, config.DELETE_DISABLED_IMG, False)
        self.useCases_table.itemSelectionChanged.connect(lambda: ButtonUtils.check_selection(
            self.useCases_table,
            self.ui.editUseCase_Button,
            self.ui.deleteUseCase_Button,
            config.EDIT_IMG,
            config.EDIT_DISABLED_IMG,
            config.DELETE_IMG,
            config.DELETE_DISABLED_IMG,
        ))

        self.ui.newUseCase_Button.clicked.connect(self.create_use_case)
        self.ui.editUseCase_Button.clicked.connect(self.edit_use_case)
        self.ui.deleteUseCase_Button.clicked.connect(self.delete_use_cases)

        # Use cases search
        search_action = QAction(QIcon(config.SEARCH_IMG), None, self)
        self.ui.useCasesSearch_LineEdit.findChildren(QAction)[0].setIcon(QIcon(config.CLEAR_SEARCH_IMG))
        self.ui.useCasesSearch_LineEdit.addAction(search_action, QLineEdit.LeadingPosition)
        self.ui.useCasesSearch_LineEdit.textChanged.connect(self.search_use_case)

    def create_use_case(self):
        """
        Emit signal to create a new use case.
        """
        useCases_codes = {
            f"UC-{item.text().split('-')[1]}": int(item.text().split("-")[1])
            for row in range(self.useCases_table.rowCount())
            if (item := self.useCases_table.item(row, 2)) is not None and item.text().startswith("UC-")
        }
        self.useCase_managed.emit("new", "useCase", useCases_codes, None)

    def search_use_case(self):
        """
        Emit signal when the search text changes.
        """
        self.text_changed.emit(self.ui.useCasesSearch_LineEdit.text())

    def display_message(self, title, message, icon_path, dialog_type='simple_message'):
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

        Returns
        -------
        QDialog
            The message dialog.
        """
        return WidgetConfig.show_message_dialog(title, message, icon_path, dialog_type)

    def edit_use_case(self):
        """
        Emit signal to edit the selected use case.
        """
        selected_indexes = self.useCases_table.selectedIndexes()
        unique_rows = set(index.row() for index in selected_indexes)
        if len(unique_rows) != 1:
            self.display_message("Failed Operation", "No row selected. Please, try again.", config.CRITICAL_IMG)
            return
        selected_row = unique_rows.pop()
        useCases_codes = {
            f"UC-{item.text().split('-')[1]}": int(item.text().split("-")[1])
            for row in range(self.useCases_table.rowCount())
            if (item := self.useCases_table.item(row, 2)) is not None and item.text().startswith("UC-")
        }
        useCase_data = {
            'id': self.useCases_table.item(selected_row, 0).text(),
            'code': self.useCases_table.item(selected_row, 2).text(),
            'name': self.useCases_table.item(selected_row, 3).text(),
            'complexity': self.useCases_table.item(selected_row, 4).text(),
            'transactions': self.useCases_table.item(selected_row, 5).text(),
            'comment': self.useCases_table.cellWidget(selected_row, 6).toolTip() if self.useCases_table.cellWidget(selected_row, 6) else "",
            'codes': useCases_codes
        }
        useCases_codes.pop(useCase_data['code'])
        self.useCase_managed.emit("edit", "useCase", useCase_data, selected_row)

    def update_use_cases_table(self, data_saved, selected_row=None, update_rows=True):
        """
        Update the use cases table with the provided data.

        Parameters
        ----------
        data_saved : dict
            Dictionary containing the saved data for a use case.
        selected_row : int, optional
            Row index to update, by default None.
        update_rows : bool, optional
            Whether to update row numbers, default is True.
        """
        self.useCases_table.setSortingEnabled(False)

        if selected_row is None:
            row = self.useCases_table.rowCount()
            self.useCases_table.insertRow(row)
            numbers_item = QTableWidgetItem()
            numbers_item.setData(Qt.EditRole, row + 1)
            self.useCases_table.setItem(row, 0, QTableWidgetItem(str(data_saved['id'])))
            self.useCases_table.setItem(row, 1, numbers_item)
            self.useCases_table.item(row, 1).setTextAlignment(Qt.AlignCenter)
        else:
            row = selected_row

        self.useCases_table.setItem(row, 2, NumericTableWidgetItem(data_saved['code']))
        self.useCases_table.item(row, 2).setTextAlignment(Qt.AlignCenter)
        self.useCases_table.setItem(row, 3, QTableWidgetItem(data_saved['name']))
        self.useCases_table.item(row, 3).setTextAlignment(Qt.AlignCenter)
        self.useCases_table.setItem(row, 4, QTableWidgetItem(data_saved['complexity']))
        self.useCases_table.item(row, 4).setTextAlignment(Qt.AlignCenter)
        transactions_item = QTableWidgetItem()
        transactions_item.setData(Qt.EditRole, data_saved['transactions'])
        self.useCases_table.setItem(row, 5, transactions_item)
        self.useCases_table.item(row, 5).setTextAlignment(Qt.AlignCenter)
        if data_saved['comment'] != '':
            WidgetConfig.create_comment(data_saved['comment'], row, self.useCases_table, config.COMMENT_IMG_YELLOW)
            self.useCases_table.setItem(row, 6, QTableWidgetItem(""))
        else:
            self.useCases_table.removeCellWidget(row, self.useCases_table.columnCount() - 1)
            self.useCases_table.setItem(row, 6, QTableWidgetItem(" "))

        if update_rows:
            self.useCases_table.selectRow(row)
            TableUtils.update_row_numbers(self.useCases_table)
            self.useCases_table.scrollToItem(self.useCases_table.currentItem(), QAbstractItemView.PositionAtCenter)
            self.useCases_table.selectionModel().clearSelection()

        self.table_checkbox.setCheckState(Qt.Unchecked)
        self.table_checkbox.setVisible(self.useCases_table.rowCount() > 0)

        if self.useCases_table.rowCount() == config.USE_CASE_LIMIT:
            self.ui.newUseCase_Button.setEnabled(False)
            ButtonUtils.set_styles_button(self.ui.newUseCase_Button, '#48F4FF', '#22577A', config.NEW_IMG, config.NEW_DISABLED_IMG, False)
            self.ui.newUseCase_Button.setEnabled(False)

    def update_use_cases_summary(self, useCases_count, total_useCases, useCases_UUCW, total_UUCW, weights):
        """
        Update the use cases summary table with the provided data.

        Parameters
        ----------
        useCases_count : dict
            Dictionary containing the count of use cases for each complexity.
        total_useCases : int
            Total number of use cases.
        useCases_UUCW : dict
            Dictionary containing the UUCW for each complexity.
        total_UUCW : int
            Total UUCW.
        weights : dict
            Dictionary containing the weights for each complexity.
        """
        complexity_mapping = {"Simple": 0, "Average": 1, "Complex": 2}
        for complexity, row_index in complexity_mapping.items():
            self.useCases_summary_table.item(row_index, 2).setText(str(weights[complexity]))
            self.useCases_summary_table.item(row_index, 3).setText(str(useCases_count[complexity]))
            self.useCases_summary_table.item(row_index, 4).setText(str(useCases_UUCW[complexity]))

        self.useCases_summary_table.item(3, 3).setText(str(total_useCases))
        self.useCases_summary_table.item(3, 4).setText(str(total_UUCW))

    def delete_use_cases(self):
        """
        Emit signal to delete the selected use case(s).
        """
        selected_rows = sorted([index.row() for index in self.useCases_table.selectionModel().selectedRows()], reverse=True)
        if not selected_rows:
            self.display_message("Failed operation", "No use cases selected. Please select at least one use case to delete.", config.WARNING_IMG)
            return

        useCases_data = {
            self.useCases_table.item(row, 0).text(): {
                'code': self.useCases_table.item(row, 2).text(),
                'complexity': self.useCases_table.item(row, 4).text()
            } for row in selected_rows
        }
        self.useCases_deleted.emit(useCases_data, selected_rows)

    def delete_rows(self, rows=None, clear_all=False):
        """
        Delete rows from the use cases table.

        Parameters
        ----------
        rows : list of int, optional
            List of row indices to delete. Ignored if clear_all is True.
        clear_all : bool, optional
            If True, deletes all rows in the table.
        """
        if clear_all:
            self.useCases_table.setRowCount(0)
        else:
            if rows is not None:
                for row in sorted(rows, reverse=True):
                    self.useCases_table.removeRow(row)
                    TableUtils.update_row_numbers(self.useCases_table, row)

        self.table_checkbox.setCheckState(Qt.Unchecked)
        self.table_checkbox.setVisible(self.useCases_table.rowCount() > 0)

        self.ui.newUseCase_Button.setEnabled(True)
        ButtonUtils.set_styles_button(self.ui.newUseCase_Button, '#5AFFA6', '#094646', config.NEW_IMG, config.NEW_DISABLED_IMG, True)
        self.ui.newUseCase_Button.setEnabled(True)

    def update_use_cases_weights(self):
        """
        Update the use cases weights based on the summary table data.
        """
        complexity_to_key = {
            'Simple': 'simple_weight',
            'Average': 'average_weight',
            'Complex': 'complex_weight'
        }

        weights = {key: 0 for key in complexity_to_key.values()}

        for row in range(self.useCases_summary_table.rowCount() - 1):
            complexity = self.useCases_summary_table.item(row, 0).text()
            weight = float(self.useCases_summary_table.item(row, 2).text())

            if complexity in complexity_to_key:
                weights[complexity_to_key[complexity]] = weight

        self.useCases_weights_updated.emit(weights)

    def filter_table(self, search_text):
        """
        Filter the use cases table based on the search text.

        Parameters
        ----------
        search_text : str
            The text to search for in the table.

        Returns
        -------
        set of int
            Set of row indices that match the search text.
        """
        matching_items = self.useCases_table.findItems(search_text, Qt.MatchContains)
        matching_items = [item for item in matching_items if item is not None]
        matching_items_in_columns = [item for item in matching_items if item.column() in [2, 3, 4, 5]]
        rows_to_show = set(item.row() for item in matching_items_in_columns)
        return rows_to_show

    def update_table_visibility(self, rows_to_show):
        """
        Update the visibility of rows in the use cases table.

        Parameters
        ----------
        rows_to_show : set of int
            Set of row indices to show.
        """
        for i in range(self.useCases_table.rowCount()):
            self.useCases_table.setRowHidden(i, i not in rows_to_show)
