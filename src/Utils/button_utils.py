# This Python file uses the following encoding: utf-8
# Utils/button_utils.py

from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QObject

class ButtonUtils(QObject):
    """
    Utility class for configuring buttons.

    Methods
    -------
    """
    def __init__(self):
        """
        Initialize the ButtonUtils class.
        """
        super().__init__()

    @staticmethod
    def check_selection(table_widget, edit_button, delete_button, edit_icon, edit_disabled_icon, delete_icon, delete_disabled_icon,
        edit_enabled_color='#48F4FF', edit_disabled_color='#22577A', delete_enabled_color='#FF0000', delete_disabled_color='#FFFFFF'):
        """
        Updates the state of edit and delete buttons based on table selection.

        Parameters
        ----------
        table_widget : QTableWidget
            The table widget.
        edit_button : QPushButton
            The edit button.
        delete_button : QPushButton
            The delete button.
        edit_icon : str
            The icon path for the enabled edit button.
        edit_disabled_icon : str
            The icon path for the disabled edit button.
        delete_icon : str
            The icon path for the enabled delete button.
        delete_disabled_icon : str
            The icon path for the disabled delete button.
        edit_enabled_color : str, optional
            The background color for the enabled edit button (default is '#48F4FF').
        edit_disabled_color : str, optional
            The background color for the disabled edit button (default is '#22577A').
        delete_enabled_color : str, optional
            The background color for the enabled delete button (default is '#FF0000').
        delete_disabled_color : str, optional
            The background color for the disabled delete button (default is '#FFFFFF').
        """
        selectedRows = len(table_widget.selectionModel().selectedRows())
        isEditEnabled = selectedRows == 1
        isDeleteEnabled = selectedRows >= 1

        edit_button.setEnabled(isEditEnabled)
        ButtonUtils.set_styles_button(edit_button, edit_enabled_color, edit_disabled_color, edit_icon, edit_disabled_icon, isEditEnabled)

        delete_button.setEnabled(isDeleteEnabled)
        ButtonUtils.set_styles_button(delete_button, delete_enabled_color, delete_disabled_color, delete_icon, delete_disabled_icon, isDeleteEnabled)

    @staticmethod
    def set_styles_button(button, background_color_enabled, color_enabled, image_enabled, image_disabled, is_enabled, padding='6px 0px 6px 6px', background_color_disabled='#545454', color_disabled='#9D9D9D', icon_size=30):
        """
        Sets the style and icon for a button.

        Parameters
        ----------
        button : QPushButton
            The button to style.
        background_color_enabled : str
            The background color when enabled.
        color_enabled : str
            The text color when enabled.
        image_enabled : str
            The icon path when enabled.
        image_disabled : str
            The icon path when disabled.
        is_enabled : bool
            Whether the button is enabled.
        padding : str, optional
            The padding for the button (default is '6px 0px 6px 6px').
        background_color_disabled : str, optional
            The background color when disabled (default is '#545454').
        color_disabled : str, optional
            The text color when disabled (default is '#9D9D9D').
        icon_size : int, optional
            The icon size (default is 30).
        """
        button_style = f"background-color: {background_color_enabled if is_enabled else background_color_disabled}; color: {color_enabled if is_enabled else color_disabled}; padding: {padding};"
        image_path = image_enabled if is_enabled else image_disabled
        button.setStyleSheet(button_style)
        button.setIcon(QIcon(image_path))
        button.setIconSize(QSize(icon_size, icon_size))
