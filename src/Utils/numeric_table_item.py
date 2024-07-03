# This Python file uses the following encoding: utf-8
# Utils/numeric_table_item.py

from PySide6.QtWidgets import QTableWidgetItem

class NumericTableWidgetItem(QTableWidgetItem):
    """
    Custom QTableWidgetItem for numeric sorting.

    Methods
    -------
    """
    def __lt__(self, other):
        """
        Compares this item with another item for sorting.

        Parameters
        ----------
        other : QTableWidgetItem
            The other item to compare with.

        Returns
        -------
        bool
            True if this item's number is less than the other item's number, otherwise False.
        """
        self_number = int(self.text().split('-')[1])
        other_number = int(other.text().split('-')[1])
        return self_number < other_number
