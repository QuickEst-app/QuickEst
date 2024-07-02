# This Python file uses the following encoding: utf-8
# Utils/dialog_event_filter.py

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QEvent, QObject

class DialogEventFilter(QObject):
    """
    Event filter to apply custom styling to QMessageBox instances.

    Methods
    -------
    """
    def eventFilter(self, obj, event):
        """
        Filters events to apply custom styling to QMessageBox instances.

        Parameters
        ----------
        obj : QObject
            The object that is being filtered.
        event : QEvent
            The event that is being filtered.

        Returns
        -------
        bool
            True if the event should be filtered out, otherwise False.
        """
        if event.type() == QEvent.Show and isinstance(obj, QMessageBox):
            if "About Qt" in obj.text():
                obj.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;
                    }
                    QMessageBox QLabel {
                        background-color: white;
                        color: black;
                    }
                    QMessageBox QPushButton {
                        background-color: white;
                        color: black;
                    }
                """)
        return super().eventFilter(obj, event)
