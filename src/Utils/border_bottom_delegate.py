# This Python file uses the following encoding: utf-8
# Utils/border_bottom_delegate

from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtGui import QPen
from PySide6.QtCore import Qt

class BorderBottomDelegate(QStyledItemDelegate):
    """
    Custom delegate to draw a bottom border for table items.

    Methods
    -------
    """
    def paint(self, painter, option, index):
        """
        Paints the item with a custom bottom border.

        Parameters
        ----------
        painter : QPainter
            The painter used to draw the item.
        option : QStyleOptionViewItem
            The style options for the item.
        index : QModelIndex
            The model index of the item being painted.
        """
        super().paint(painter, option, index)
        painter.setPen(QPen(Qt.white, 2, Qt.SolidLine))
        bottom_left = option.rect.bottomLeft()
        bottom_right = option.rect.bottomRight()
        painter.drawLine(bottom_left, bottom_right)
