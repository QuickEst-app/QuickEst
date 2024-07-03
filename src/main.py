# This Python file uses the following encoding: utf-8
# main.py
"""
This file run the main application for QuickEst.
"""

import sys
import config
import DataSource.database as db
from Utils.widget_config import WidgetConfig
from Utils.dialog_event_filter import DialogEventFilter
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLocale
from PySide6.QtGui import QIcon
from Main.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    qt_locale = QLocale(QLocale.English, QLocale.UnitedStates)
    QLocale.setDefault(qt_locale)

    app.setStyle("fusion")
    app.setApplicationName("QuickEst")
    app.setWindowIcon(QIcon(config.QUICKEST_IMG))
    event_filter = DialogEventFilter()

    app.installEventFilter(event_filter)

    db_result = db.DataBase.get_instance()
    if isinstance(db_result, str):
        WidgetConfig.show_message_dialog("Failed Operation", f"Error initializing database: {db_result}", config.CRITICAL_IMG)
        sys.exit()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
