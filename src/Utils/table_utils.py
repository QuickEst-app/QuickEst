# This Python file uses the following encoding: utf-8
# Utils/table_utils.py

from PySide6.QtWidgets import QTableWidgetItem, QPushButton, QCheckBox, QToolTip
from PySide6.QtGui import QColor, QMouseEvent
from PySide6.QtCore import Qt, QEvent, QObject, QRect

class TableUtils(QObject):
    """
    Utility class for table operations and row highlighting.

    Attributes
    ----------
    currentRow : int
        The currently highlighted row.
    currentTableWidget : QTableWidget
        The currently highlighted table widget.
    tables : list of QTableWidget
        List of table widgets being managed.

    Methods
    -------
    """
    currentRow = -1
    currentTableWidget = None
    tables = []

    def __init__(self):
        """
        Initialize the TableUtils class.
        """
        super().__init__()

    def add_table(self, table):
        """
        Adds a table to the managed list and sets up event filters.

        Parameters
        ----------
        table : QTableWidget
            The table widget to add.
        """
        self.__class__.tables.append(table)
        table.setMouseTracking(True)
        table.cellEntered.connect(lambda row, column, table=table: self.on_cell_entered(table, row))
        table.viewport().installEventFilter(self)

    def on_cell_entered(self, table_widget, row):
        """
        Handles cell entered events to highlight the row.

        Parameters
        ----------
        table_widget : QTableWidget
            The table widget.
        row : int
            The row index entered.
        """
        if self.__class__.currentRow != row:
            self.reset_table_background(self.__class__.currentTableWidget, self.__class__.currentRow)
        self.__class__.currentRow = row
        self.__class__.currentTableWidget = table_widget
        self.highlight(table_widget, row, QColor(0, 0, 0, 64))

    def highlight(self, table_widget, row, color):
        """
        Highlights a specified row with a color.

        Parameters
        ----------
        tableWidget : QTableWidget
            The table widget.
        row : int
            The row index to highlight.
        color : QColor
            The color to use for highlighting.
        """
        for i in range(table_widget.columnCount()):
            item = table_widget.item(row, i)
            if item is None:
                item = QTableWidgetItem()
                table_widget.setItem(row, i, item)
            item.setBackground(color)

    def eventFilter(self, source, event):
        """
        Handles mouse move and leave events to manage row highlighting.

        Parameters
        ----------
        source : QObject
            The source of the event.
        event : QEvent
            The event to handle.

        Returns
        -------
        bool
            Whether the event was handled.
        """
        if event.type() == QEvent.MouseMove:
            if isinstance(event, QMouseEvent):
                for table in self.__class__.tables:
                    if source == table.viewport():
                        index = table.indexAt(event.position().toPoint())
                        if index.isValid():
                            table.setCursor(Qt.PointingHandCursor)
                            if (self.__class__.currentTableWidget != table) or (self.__class__.currentRow != index.row()):
                                self.reset_table_background(self.__class__.currentTableWidget, self.__class__.currentRow)
                            self.__class__.currentRow, self.__class__.currentTableWidget = index.row(), table
                        else:
                            table.unsetCursor()
                            self.reset_table_background(self.__class__.currentTableWidget, self.__class__.currentRow)
                            self.__class__.currentRow, self.__class__.currentTableWidget = -1, None
                        break
        elif event.type() == QEvent.Leave:
            if self.__class__.currentTableWidget:
                self.__class__.currentTableWidget.unsetCursor()
                self.reset_table_background(self.__class__.currentTableWidget, self.__class__.currentRow)
                self.__class__.currentRow, self.__class__.currentTableWidget = -1, None
        return super().eventFilter(source, event)

    def reset_table_background(self, table_widget, row):
        """Resets the background color of a specified row.

        Parameters
        ----------
        tableWidget : QTableWidget
            The table widget.
        row : int
            The row index to reset.
        """
        if row != -1 and table_widget is not None:
            for column in range(table_widget.columnCount()):
                item = table_widget.item(row, column)
                if item:
                    item.setBackground(Qt.transparent)
        self.__class__.currentRow = -1
        self.__class__.currentTableWidget = None

    @staticmethod
    def on_header_clicked(logical_index, table_widget, not_sorting_index, update=False):
        """
        Handles table header click events for sorting.

        Parameters
        ----------
        logical_index : int
            The index of the clicked header.
        table_widget : QTableWidget
            The table widget.
        not_sorting_index : list of int
            List of column indices that should not be sorted.
        update : bool, optional
            Whether to update row numbers (default is False).
        """
        if logical_index in not_sorting_index:
            table_widget.setSortingEnabled(False)
        else:
            table_widget.setSortingEnabled(True)
            if update:
                TableUtils.update_row_numbers(table_widget, 0)

    @staticmethod
    def update_row_numbers(table_widget, starting_row=0, column=1):
        """
        Updates row numbers in a table.

        Parameters
        ----------
        table_widget : QTableWidget
            The table widget.
        starting_row : int, optional
            The starting row for updating (default is 0).
        column : int, optional
            The column index for row numbers (default is 1).
        """
        sort_column = table_widget.horizontalHeader().sortIndicatorSection()
        if sort_column != column:
            table_widget.setSortingEnabled(True)
        else:
            table_widget.setSortingEnabled(False)

        for rowIndex in range(starting_row, table_widget.rowCount()):
            currentRowNumberItem = table_widget.item(rowIndex, column)
            if currentRowNumberItem:
                currentRowNumberItem.setData(Qt.EditRole, rowIndex + 1)
            else:
                item = QTableWidgetItem()
                item.setData(Qt.EditRole, rowIndex + 1)
                table_widget.setItem(rowIndex, column, item)
            table_widget.item(rowIndex, column).setTextAlignment(Qt.AlignCenter)

    @staticmethod
    def adjust_header_widget(header, widget, columns, x=None, y=None, w=None, h=None):
        """
        Adjusts a widget to span over specified columns in the header of a table.

        Parameters
        ----------
        header : QHeaderView
            The header view of the table.
        widget : QWidget
            The widget to adjust.
        columns : list of int
            The columns that the widget should span.
        x : int, optional
            The x-coordinate for the widget (default is calculated).
        y : int, optional
            The y-coordinate for the widget (default is 0).
        w : int, optional
            The width of the widget (default is calculated).
        h : int, optional
            The height of the widget (default is header height).
        """
        if columns:
            first_section_pos = header.sectionViewportPosition(columns[0]) - 1
            last_section_pos = header.sectionViewportPosition(columns[-1]) + header.sectionSize(columns[-1])
            section_width = last_section_pos - first_section_pos
            header_height = header.height()
            widget_width = w if w is not None else section_width
            widget_height = h if h is not None else header_height
            widget_x = x if x is not None else first_section_pos
            widget_y = y if y is not None else 0
            widget.setGeometry(QRect(widget_x, widget_y, widget_width, widget_height))

    @staticmethod
    def setup_header_checkbox(table_widget, header, columns_to_span):
        """
        Sets up a checkbox in the header of a table to span specified columns.

        Parameters
        ----------
        table_widget : QTableWidget
            The table widget.
        header : QHeaderView
            The header view of the table.
        columns_to_span : list of int
            The columns that the checkbox should span.

        Returns
        -------
        QCheckBox
            The created checkbox.
        """
        checkbox = QCheckBox()
        checkbox.setFocusPolicy(Qt.NoFocus)
        checkbox.setCursor(Qt.PointingHandCursor)
        checkbox.setStyleSheet("""
            QCheckBox{
                border: 1px solid black;
                background-color: transparent;
                border-radius: 3px;
            }
            QToolTip {
                background-color: white;
                border: 2px solid black;
                padding: 2px;
            }
        """)
        checkbox.setParent(header)
        checkbox.setToolTip("Select all rows in the table")

        TableUtils.adjust_header_widget(header, checkbox, columns_to_span, 9, 10, 18, 18)
        header.sectionResized.connect(lambda: TableUtils.adjust_header_widget(header, checkbox, columns_to_span, 9, 10, 18, 18))
        header.geometriesChanged.connect(lambda: TableUtils.adjust_header_widget(header, checkbox, columns_to_span, 9, 10, 18, 18))

        checkbox.stateChanged.connect(lambda state: TableUtils.toggle_select_all(state, table_widget, checkbox))
        return checkbox

    @staticmethod
    def toggle_select_all(state, table_widget, checkbox):
        """
        Toggles the selection of all rows in a table based on the checkbox state.

        Parameters
        ----------
        state : int
            The state of the checkbox (checked or unchecked).
        table_widget : QTableWidget
            The table widget.
        checkbox : QCheckBox
            The checkbox controlling the selection.
        """
        if state == Qt.Checked.value:
            table_widget.selectAll()
        else:
            table_widget.clearSelection()

    @staticmethod
    def check_column_visibility(table, widget, column=1):
        """
        Checks if a specified column in a QTableWidget is visible and sets the visibility of a widget accordingly.

        Parameters
        ----------
        table : QTableWidget
            The table widget containing the column to check.
        widget : QWidget
            The widget whose visibility will be set based on the column's visibility.
        column : int, optional
            The index of the column to check (default is 1).
        """
        header = table.horizontalHeader()
        column_start = header.sectionViewportPosition(column)
        viewport_width = table.viewport().width()
        is_column_visible = column_start >= 0 and column_start < viewport_width
        widget.setVisible(is_column_visible)
