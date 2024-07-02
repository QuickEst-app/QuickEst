# This Python file uses the following encoding: utf-8
# Utils/widget_config.py

from PySide6.QtWidgets import QMessageBox, QPushButton
from PySide6.QtGui import QPixmap, QIcon, QTextCursor
from PySide6.QtCore import Qt, QSize, QObject

class WidgetConfig(QObject):
    """
    Utility class for configuring widgets.

    Methods
    -------
    """
    def __init__(self):
        """
        Initialize the WidgetConfig class.
        """
        super().__init__()

    @staticmethod
    def configure_widgets(enabled, radio_buttons, weight_spinbox, comment_plain_text_edit):
        """
        Configures the state of multiple widgets.

        Parameters
        ----------
        enabled : bool
            Whether the widgets should be enabled.
        radio_buttons : list of QRadioButton
            The list of radio buttons to configure.
        weight_spinbox : QSpinBox
            The spinbox to configure.
        comment_plain_text : QPlainTextEdit
            The plain text edit to configure.
        """
        for rb in radio_buttons:
            rb.setEnabled(enabled)
        weight_spinbox.setEnabled(enabled)
        comment_plain_text_edit.setEnabled(enabled)

        if not enabled:
            for rb in radio_buttons:
                rb.setAutoExclusive(False)
                rb.setChecked(False)
                rb.setAutoExclusive(True)
            comment_plain_text_edit.setPlainText("")

    @staticmethod
    def create_comment(comment, row, table_widget, comment_icon, column=None):
        """
        Creates a comment button in a table cell.

        Parameters
        ----------
        comment : str
            The comment text.
        row : int
            The row index.
        table_widget : QTableWidget
            The table widget.
        comment_icon:
            The comment icon
        column : int, optional
            The column index (default is the last column).
        """
        comment_button = QPushButton()
        comment_button.setToolTip(comment)
        comment_button.setFocusPolicy(Qt.NoFocus)

        comment_button.setIcon(QIcon(comment_icon))
        comment_button.setIconSize(QSize(35, 35))

        comment_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
            QPushButton:hover {
                background-color: transparent;
            }
            QToolTip {
                background-color: white;
                color: black; font-family: 'Arial';
                font-size: 12px;
                padding: 2px;
                border: 2px solid black;
            }
        """)

        if column is None:
            column = table_widget.columnCount() - 1
        table_widget.setCellWidget(row, column, comment_button)

    @staticmethod
    def show_message_dialog(title, message, icon_path, dialog_type='simple_message', ok_callback=None):
        """
        Displays a message dialog.

        Parameters
        ----------
        title : str
            The dialog title.
        message : str
            The dialog message.
        icon_path : str
            The path to the custom icon.
        dialog_type : str, optional
            The type of dialog ('simple_message' or 'confirmation_message') (default is 'simple_message').
        ok_callback : callable, optional
            Callback function to call when OK is clicked (default is None).

        Returns
        -------
        bool
            True if the user confirms the action, False otherwise or None for simple messages.
        """
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.NoIcon)

        # Load the original pixmap
        original_pixmap = QPixmap(icon_path)

        # Ensure high DPI support
        device_pixel_ratio = 2.0 if hasattr(Qt, 'AA_EnableHighDpiScaling') else 1.0
        original_pixmap.setDevicePixelRatio(device_pixel_ratio)

        # Scale the pixmap maintaining aspect ratio and smooth transformation
        scaled_pixmap = original_pixmap.scaled(64 * device_pixel_ratio, 64 * device_pixel_ratio, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        scaled_pixmap.setDevicePixelRatio(device_pixel_ratio)

        msg_box.setIconPixmap(scaled_pixmap)

        if dialog_type == 'confirmation_message':
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec()
            return reply == QMessageBox.Yes
        else:
            msg_box.setStandardButtons(QMessageBox.Ok)
            ok_button = msg_box.button(QMessageBox.Ok)
            if ok_callback is not None:
                ok_button.clicked.connect(ok_callback)
            msg_box.exec()
            return None

    @staticmethod
    def print_name_length(name_line_edit, name_counter_label, check_enable_save_button_callback, max_name_length=20):
        """
        Updates the name length counter and checks if the save button should be enabled.

        Parameters
        ----------
        name_line_edit : QLineEdit
            The line edit for the name input.
        name_counter_label : QLabel
            The label to display the name length.
        check_enable_save_button_callback : callable
            Callback function to check if the save button should be enabled.
        max_name_length : int, optional
            The maximum length for the name (default is 20).
        """
        text = name_line_edit.text()
        name_counter_label.setText(f"{len(text)}/{max_name_length}")
        check_enable_save_button_callback()

    @staticmethod
    def limit_comment_length(comment_plain_text_edit, comment_counter_label, max_comment_length=300):
        """
        Limits the comment length and updates the length counter.

        Parameters
        ----------
        comment_plain_text_edit : QPlainTextEdit
            The plain text edit for the comment input.
        comment_counter_label : QLabel
            The label to display the comment length.
        max_comment_length : int, optional
            The maximum length for the comment (default is 300).
        """
        text = comment_plain_text_edit.toPlainText()
        comment_counter_label.setText(f"{len(text)}/{max_comment_length}")

        if len(text) > max_comment_length:
            comment_plain_text_edit.setPlainText(text[:max_comment_length])
            cursor = QTextCursor(comment_plain_text_edit.document())
            cursor.movePosition(QTextCursor.End)
            comment_plain_text_edit.setTextCursor(cursor)

