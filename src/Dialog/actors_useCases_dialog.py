# This Python file uses the following encoding: utf-8

import config
from Utils.widget_config import WidgetConfig
from Utils.button_utils import ButtonUtils
from PySide6.QtWidgets import QDialog, QSpinBox, QLabel
from PySide6.QtGui import QPixmap, QTextCursor
from PySide6.QtCore import Qt, Signal
from UI.ui_actors_useCases_dialog import Ui_ActorsUCDialog

class ActorsUCDialog(QDialog, Ui_ActorsUCDialog):
    """
    Class for managing the dialog that handles actors and use cases.

    This class provides the interface and functionalities to manage the actors and use cases within the application. It includes fields for relevant data and emits signals when actions are performed.

    Attributes
    ----------
    data_saved : Signal
        Signal emitted when data is saved.

    Methods
    -------
    """

    data_saved = Signal(dict)

    def __init__(self, action, option, data=None, parent=None):
        """
        Initialize the dialog with the given action and option.

        Parameters
        ----------
        action : str
            Action type (e.g., "new", "edit").
        option : str
            Option type (e.g., "actor", "useCase").
        data : dict, optional
            Dictionary containing initial data for the dialog.
        parent : QWidget, optional
            Parent widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.action = action
        self.option = option
        if self.action == "edit":
            self.data = data.get('codes')
            self.single_data = data
        else:
            self.data = data
        self.initialize_ui()
        if action == "edit":
            self.load_data(data)

    def initialize_ui(self):
        """
        Initialize the user interface elements and connect signals.
        """
        self.setFixedSize(self.size())
        self.set_window_style(self.action, self.option)
        self.configure_code_spinbox(self.option)
        self.code_SpinBox.setButtonSymbols(QSpinBox.NoButtons)
        if self.option == "actor":
            label = QLabel(f"  (Allowed range: [1, {config.ACTOR_LIMIT}])")
        else:
            label = QLabel(f"  (Allowed range: [1, {config.USE_CASE_LIMIT}])")
        self.code_HorizontalLayout.insertWidget((self.code_HorizontalLayout.indexOf(self.code_SpinBox))+1, label)

        self.save_Button.setEnabled(False)
        self.set_save_button_style(False, self.action)

        self.name_LineEdit.textChanged.connect(self.on_name_text_changed)
        self.complexity_ComboBox.currentIndexChanged.connect(self.on_complexity_changed)
        self.comment_PlainTextEdit.textChanged.connect(self.on_comment_text_changed)
        self.cancel_Button.clicked.connect(self.reject)
        self.save_Button.clicked.connect(self.save_data)

        if self.action == "new":
            self.on_complexity_changed(-1)

        if self.option == "useCase":
            if self.action == "new":
                icon_path = config.INFO_IMG_GREEN
            else:
                icon_path = config.INFO_IMG_BLUE

            pixmap = QPixmap(icon_path)
            self.info_label.setPixmap(pixmap)

        line_edit = self.code_SpinBox.lineEdit()
        line_edit.setCursorPosition(len(line_edit.text()))

        self.setTabOrder(self.code_SpinBox, self.name_LineEdit)
        self.setTabOrder(self.name_LineEdit, self.complexity_ComboBox)
        self.setTabOrder(self.complexity_ComboBox, self.transactions_SpinBox)
        self.setTabOrder(self.transactions_SpinBox, self.comment_PlainTextEdit)

        original_focus_in_event = self.comment_PlainTextEdit.focusInEvent
        original_focus_out_event = self.comment_PlainTextEdit.focusOutEvent

        self.comment_PlainTextEdit.focusInEvent = lambda event: (
            self.comment_PlainTextEdit.selectAll() if event.reason() in (Qt.TabFocusReason, Qt.BacktabFocusReason) else None,
            original_focus_in_event(event)
        )
        self.comment_PlainTextEdit.focusOutEvent = lambda event: (
            self.comment_PlainTextEdit.setTextCursor(QTextCursor(self.comment_PlainTextEdit.document().end())),
            original_focus_out_event(event)
        )

    def configure_code_spinbox(self, option):
        """
        Configure the code spinbox based on the option type and ensure it does not allow values present in the data dictionary.

        Parameters
        ----------
        option : str
            Option type (e.g., "actor", "useCase").
        """
        self.code_prefix = "ACT-" if option == "actor" else "UC-"
        self.code_SpinBox.setMaximum(config.ACTOR_LIMIT if option == "actor" else config.USE_CASE_LIMIT)

        self.existing_codes = set(self.data.values()) if self.data else set()

        if self.action == "new":
            self.available_value = self.code_SpinBox.minimum()
            while self.available_value in self.existing_codes and self.available_value <= self.code_SpinBox.maximum():
                self.available_value += 1
            self.code_SpinBox.setValue(self.available_value)
        else:
            self.available_value = int(self.single_data["code"].split("-")[1])

        self.code_SpinBox.valueChanged.connect(self.check_enable_save_button)
        self.code_SpinBox.editingFinished.connect(self.validate_spinbox_value)
        self.code_SpinBox.lineEdit().textChanged.connect(self.check_enable_save_button)

    def validate_spinbox_value(self):
        """
        Validate the current value of the spinbox to ensure it is not in the list of existing codes.
        """
        value = self.code_SpinBox.value()
        if value in self.existing_codes or value == self.available_value:
            self.code_SpinBox.setValue(self.available_value)
            self.check_enable_save_button()

    def load_data(self, data):
        """
        Load existing data into the dialog.

        Parameters
        ----------
        data : dict
            Dictionary containing the data to load.
        """
        code_number = data["code"].split("-")[1]
        self.code_SpinBox.setValue(int(code_number))

        name = data["name"]
        self.name_LineEdit.setText(name)
        self.nameCounter_Label.setText(f"{len(name)}/20")

        complexity = data["complexity"]
        index = self.complexity_ComboBox.findText(complexity)
        self.complexity_ComboBox.setCurrentIndex(index)

        if self.option == "useCase":
            self.transactions_SpinBox.setValue(int(data['transactions']))
            self.on_complexity_changed(index, int(data['transactions']))

        comment = data["comment"]
        self.comment_PlainTextEdit.setPlainText(comment)
        self.commentCounter_Label.setText(f"{len(comment)}/300")

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

    def on_comment_text_changed(self):
        """
        Limit the comment length and update the length counter.
        """
        WidgetConfig.limit_comment_length(
            comment_plain_text_edit=self.comment_PlainTextEdit,
            comment_counter_label=self.commentCounter_Label,
            max_comment_length=300
        )

    def on_complexity_changed(self, index, value=-1):
        """
        Update transactions spinbox range based on complexity selection.

        Parameters
        ----------
        index : int
            Index of the selected complexity.
        value : int, optional
            Value to set, default is -1 to use the default initial value.
        """
        if self.option == "useCase":
            self.transactions_Widget.setVisible(index != -1)
        complexity_ranges = {
            0: (1, 3, 1),
            1: (4, 7, 4),
            2: (8, 100, 8)
        }
        min_val, max_val, init_val = complexity_ranges.get(index, (0, 0, 0))
        self.transactions_SpinBox.setMinimum(min_val)
        self.transactions_SpinBox.setMaximum(max_val)
        final_val = value if value != -1 else init_val
        self.transactions_SpinBox.setValue(final_val)
        self.check_enable_save_button()

    def check_enable_save_button(self):
        """
        Enable or disable the save button based on the validity of the input.
        """
        name_text = self.name_LineEdit.text().strip()
        complexity_index = self.complexity_ComboBox.currentIndex()
        try:
            code_value = int(self.code_SpinBox.lineEdit().text())
        except ValueError:
            code_value = ""

        if len(name_text) > 0 and complexity_index >= 0 and ((code_value not in self.existing_codes) and (code_value!=0) and (code_value!="")):
            self.save_Button.setEnabled(True)
            self.set_save_button_style(True, self.action)
        else:
            self.save_Button.setEnabled(False)
            self.set_save_button_style(False, self.action)

    def set_window_style(self, action, option):
        """
        Set the styles of the window based on action and option.

        Parameters
        ----------
        action : str
            Action type (e.g., "new", "edit").
        option : str
            Option type (e.g., "actor", "useCase").
        """
        title_prefix = "New" if action == "new" else "Edit"
        background_color = "#98FAC5" if action == "new" else "#A6FFF4"
        color = "#094646" if action == "new" else "#22577A"
        image_path = config.NEW_IMG if action == "new" else config.EDIT_IMG

        if option == "actor":
            option_title = "Actor"
            code_label = "ACT-"
            self.transactions_Widget.setVisible(False)
        elif option == "useCase":
            option_title = "Use Case"
            code_label = "UC-"
            self.transactions_Widget.setVisible(True)

        self.setWindowTitle(f"{title_prefix} {option_title}")
        self.titulo_Label.setText(f"{title_prefix} {option_title}")
        self.code_Label.setText(code_label)
        pixmap = QPixmap(image_path)
        self.icono_Label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        self.setStyleSheet(f"background-color: {background_color};color:{color};")

    def set_save_button_style(self, isEnabled, action):
        """
        Set the style of the save button based on its enabled state and action.

        Parameters
        ----------
        isEnabled : bool
            Boolean indicating if the save button is enabled.
        action : str
            Action type (e.g., "new", "edit").
        """
        ButtonUtils.set_styles_button(
            self.save_Button,
            "#1B5E5E" if isEnabled and action == "new" else "#22577A" if isEnabled else "#545454",  # background_color_enabled
            "white" if isEnabled else "#9D9D9D",
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
        input_values = {
            'code': f"{self.code_prefix}{self.code_SpinBox.value()}",
            'name': self.name_LineEdit.text().strip(),
            'complexity': self.complexity_ComboBox.currentText(),
            'comment': self.comment_PlainTextEdit.toPlainText().strip()
        }
        if self.option == "useCase":
            input_values['transactions'] = self.transactions_SpinBox.value()
        self.data_saved.emit(input_values)
