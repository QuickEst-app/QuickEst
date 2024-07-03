# This Python file uses the following encoding: utf-8

import config
from Utils.widget_config import WidgetConfig
from Utils.button_utils import ButtonUtils
from datetime import datetime
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QPixmap, QTextCursor
from UI.ui_project_dialog import Ui_ProjectDialog

class ProjectDialog(QDialog, Ui_ProjectDialog):
    """
    Class for managing the project dialog in the application.

    This class implements the dialog for creating and editing projects. It includes fields for project details and emits signals when actions are performed.

    Attributes
    ----------
    data_saved : Signal
        Signal emitted when data is saved.

    Methods
    -------
    """

    data_saved = Signal(dict)

    def __init__(self, action, data=None, parent=None):
        """
        Initialize the dialog with given action and data.

        Parameters
        ----------
        action : str
            Action type (e.g., "edit").
        data : dict, optional
            Dictionary containing initial data for the dialog.
        parent : QWidget, optional
            Parent widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.action = action
        self.initialize_ui()
        if action == "edit" and data:
            self.load_data(data)

    def initialize_ui(self):
        """
        Initialize the user interface elements.
        """
        self.setWindowTitle("Management Project")
        self.setFixedSize(self.size())
        self.cancel_Button.clicked.connect(self.reject)
        self.save_Button.clicked.connect(self.save_data)
        self.save_Button.setEnabled(False)
        self.set_save_button_style(False)
        title_prefix = "New" if self.action == "new" else "Edit"
        if self.action == "edit":
            image_path = config.EDIT_PROJECT_IMG
            pixmap = QPixmap(image_path)
            self.icono_Label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        self.setWindowTitle(f"{title_prefix} Project")
        self.titulo_Label.setText(f"{title_prefix} Project")

        self.name_LineEdit.textChanged.connect(self.on_name_text_changed)
        self.description_PlainTextEdit.textChanged.connect(self.on_description_text_changed)

        original_focus_in_event = self.description_PlainTextEdit.focusInEvent
        original_focus_out_event = self.description_PlainTextEdit.focusOutEvent

        self.description_PlainTextEdit.focusInEvent = lambda event: (
            self.description_PlainTextEdit.selectAll() if event.reason() in (Qt.TabFocusReason, Qt.BacktabFocusReason) else None,
            original_focus_in_event(event)
        )
        self.description_PlainTextEdit.focusOutEvent = lambda event: (
            self.description_PlainTextEdit.setTextCursor(QTextCursor(self.description_PlainTextEdit.document().end())),
            original_focus_out_event(event)
        )

    def load_data(self, data):
        """
        Load existing data into the dialog.

        Parameters
        ----------
        data : dict
            Dictionary containing the data to load.
        """
        name = data["name"]
        self.name_LineEdit.setText(name)
        self.nameCounter_Label.setText(f"{len(name)}/20")

        description = data["description"]
        self.description_PlainTextEdit.setPlainText(description)
        self.descriptionCounter_Label.setText(f"{len(description)}/300")

    def on_name_text_changed(self):
        """
        Update the name length counter and check if the save button should be enabled.
        """
        WidgetConfig.print_name_length(
            name_line_edit=self.name_LineEdit,
            name_counter_label=self.nameCounter_Label,
            check_enable_save_button_callback=self.check_enable_save_button,
            max_name_length=20
        )

    def on_description_text_changed(self):
        """
        Limit the description length and update the length counter.
        """
        WidgetConfig.limit_comment_length(
            comment_plain_text_edit=self.description_PlainTextEdit,
            comment_counter_label=self.descriptionCounter_Label,
            max_comment_length=300
        )

    def check_enable_save_button(self):
        """
        Enable or disable the save button based on the validity of the input.
        """
        name_text = self.name_LineEdit.text().strip()
        is_enabled = len(name_text) > 0
        self.save_Button.setEnabled(is_enabled)
        self.set_save_button_style(is_enabled)

    def set_save_button_style(self, isEnabled):
        """
        Set the style of the save button based on its enabled state.

        Parameters
        ----------
        isEnabled : bool
            Boolean indicating if the save button is enabled.
        """
        ButtonUtils.set_styles_button(
            self.save_Button,
            "#1B5E5E",
            "white",
            config.SAVE_IMG,
            config.SAVE_DISABLED_IMG,
            isEnabled,
            padding='8px 0px 8px 0px',
            background_color_disabled='#545454',
            color_disabled='#9D9D9D',
            icon_size=20
        )

    def save_data(self):
        """
        Collect data from the dialog and emit the data_saved signal.
        """
        now = datetime.now()
        formatted_now = now.strftime("%Y/%m/%d %H:%M:%S")

        input_values = {
            'favorite': 0,
            'name': self.name_LineEdit.text().strip(),
            'description': self.description_PlainTextEdit.toPlainText().strip(),
            'created_at': formatted_now,
            'last_access': "––"
        }
        self.data_saved.emit(input_values)
