# This Python file uses the following encoding: utf-8

import config
from Utils.button_utils import ButtonUtils

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from UI.ui_percentage_dialog import Ui_PercentageDialog

class PercentageDialog(QDialog, Ui_PercentageDialog):
    """
    Class for managing the dialog that handles percentage inputs.

    This class provides the interface and functionalities to manage the percentages used in the application. It includes fields for inputting percentages and emits signals when actions are performed.

    Attributes
    ----------
    data_saved : Signal
        Signal emitted when data is saved.

    Methods
    -------
    """

    data_saved = Signal(dict)

    def __init__(self, percentages, parent=None):
        """
        Initialize the dialog with given percentages.

        Parameters
        ----------
        percentages : dict
            Dictionary containing initial percentages for the spin boxes.
        parent : QWidget, optional
            Parent widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.initialize_ui()
        self.load_data(percentages)
        self.update_total_percentage()

    def initialize_ui(self):
        """
        Initialize the user interface elements.
        """
        self.setWindowTitle("Percentage Settings")
        self.setFixedSize(self.size())
        self.cancel_Button.clicked.connect(self.reject)
        self.save_Button.clicked.connect(self.save_data)

        self.spin_boxes = {
            'analysis': self.analysis_SpinBox,
            'design': self.design_SpinBox,
            'programming': self.programming_SpinBox,
            'testing': self.testing_SpinBox,
            'overloading': self.overloading_SpinBox
        }
        self.setTabOrder(self.analysis_SpinBox, self.design_SpinBox)
        self.setTabOrder(self.design_SpinBox, self.programming_SpinBox)
        self.setTabOrder(self.programming_SpinBox, self.testing_SpinBox)
        self.setTabOrder(self.testing_SpinBox, self.overloading_SpinBox)

    def load_data(self, percentages):
        """
        Load percentages values for the spin boxes.

        Parameters
        ----------
        percentages : dict
            Dictionary containing initial percentages for the spin boxes.
        """
        for key, spin_box in self.spin_boxes.items():
            spin_box.setValue(float(percentages[key]))
            spin_box.valueChanged.connect(self.update_total_percentage)
            spin_box.lineEdit().textChanged.connect(lambda _, spinbox=spin_box: self.check_spinbox_values(spinbox))
            line_edit = spin_box.lineEdit()
            line_edit.setCursorPosition(len(line_edit.text()))

    def check_spinbox_values(self, spin_box):
        """
        Check if the spin box value is within the allowed range and not empty.

        Parameters
        ----------
        spin_box : QSpinBox
            Spinbox of which we want to check the value.
        """
        try:
            value = float(spin_box.lineEdit().text())
            min_value = spin_box.minimum()
            max_value = spin_box.maximum()
            if value < min_value or value > max_value:
                raise ValueError
        except ValueError:
            spin_box.clearFocus()
            spin_box.setFocus()
            line_edit = spin_box.lineEdit()
            line_edit.setCursorPosition(len(line_edit.text()))

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

    def update_total_percentage(self):
        """
        Update the total percentage displayed in the progress bar and adjust spin boxes' maximum values.
        """
        total = sum(spin_box.value() for spin_box in self.spin_boxes.values())
        self.totalPercentage_ProgressBar.setValue(total)

        progress_bar_format = f"{total:.0f}%" if total.is_integer() else f"{total:.2f}%"
        self.totalPercentage_ProgressBar.setFormat(progress_bar_format)

        for spin_box in self.spin_boxes.values():
            max_possible_value = 100 - (total - spin_box.value())
            spin_box.setMaximum(max_possible_value)

        self.save_Button.setEnabled(total == 100)
        self.set_save_button_style(total == 100)

    def save_data(self):
        """
        Collect data from the spin boxes and emit the data_saved signal.
        """
        spin_box_values = {key: spin_box.value() for key, spin_box in self.spin_boxes.items()}
        self.data_saved.emit(spin_box_values)
