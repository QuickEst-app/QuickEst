# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from UI.ui_weight_dialog import Ui_WeightDialog

class WeightDialog(QDialog, Ui_WeightDialog):
    """
    Class for managing the weight input dialog in the application.

    This class provides the interface and functionalities to manage the weights used in calculations within the application. It includes fields for inputting weights and emits signals when actions are performed.

    Attributes
    ----------
    data_saved : Signal
        Signal emitted when data is saved.

    Methods
    -------
    """

    data_saved = Signal(dict)

    def __init__(self, weights, option, parent=None):
        """
        Initialize the dialog with given weights.

        Parameters
        ----------
        weights : dict
            Dictionary containing initial weights for the spin boxes.
        option: str
            Option type (e.g., "actors", "useCases").
        parent : QWidget, optional
            Parent widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.option = option
        self.initialize_ui()
        self.load_data(weights)
        self.setup_signals()

    def initialize_ui(self):
        """
        Initialize the user interface elements.
        """
        self.setWindowTitle("Weight Settings")
        self.setFixedSize(self.size())

        self.title_Label.setText("Actors Weights" if self.option == "actors" else "Use Cases Weights")
        if self.option == 'actors':
            self.simpleRange_Label.setText("Allowed range: [0.5, 2]\n(Default: 1)")
            self.averageRange_Label.setText("Allowed range: [1, 3]\n(Default: 2)")
            self.complexRange_Label.setText("Allowed range: [2, 5]\n(Default: 3)")
        elif self.option == 'useCases':
            self.simpleRange_Label.setText("Allowed range: [3, 7]\n(Default: 5)")
            self.averageRange_Label.setText("Allowed range: [7, 13]\n(Default: 10)")
            self.complexRange_Label.setText("Allowed range: [10, 20]\n(Default: 15)")

    def load_data(self, weights):
        """
        Load weights values for the spin boxes.

        Parameters
        ----------
        weights : dict
            Dictionary containing initial weights for the spin boxes.
        """
        self.simple_DoubleSpinBox.setValue(weights['simple_weight'])
        self.simple_DoubleSpinBox.lineEdit().setCursorPosition(len(self.simple_DoubleSpinBox.lineEdit().text()))
        self.average_DoubleSpinBox.setValue(weights['average_weight'])
        self.average_DoubleSpinBox.lineEdit().setCursorPosition(len(self.average_DoubleSpinBox.lineEdit().text()))
        self.complex_DoubleSpinBox.setValue(weights['complex_weight'])
        self.complex_DoubleSpinBox.lineEdit().setCursorPosition(len(self.complex_DoubleSpinBox.lineEdit().text()))
        self.update_spinbox_limits()

    def setup_signals(self):
        """
        Set up signals for buttons and value changes.
        """
        self.cancel_Button.clicked.connect(self.reject)
        self.save_Button.clicked.connect(self.save_data)
        self.simple_DoubleSpinBox.valueChanged.connect(self.update_spinbox_limits)
        self.average_DoubleSpinBox.valueChanged.connect(self.update_spinbox_limits)
        self.complex_DoubleSpinBox.valueChanged.connect(self.update_spinbox_limits)
        self.simple_DoubleSpinBox.lineEdit().textChanged.connect(lambda: self.check_spinbox_values(self.simple_DoubleSpinBox))
        self.average_DoubleSpinBox.lineEdit().textChanged.connect(lambda: self.check_spinbox_values(self.average_DoubleSpinBox))
        self.complex_DoubleSpinBox.lineEdit().textChanged.connect(lambda: self.check_spinbox_values(self.complex_DoubleSpinBox))

    def update_spinbox_limits(self):
        """
        Update the limits of the spin boxes to ensure valid values.
        """
        simple_weight = self.simple_DoubleSpinBox.value()
        average_weight = self.average_DoubleSpinBox.value()
        complex_weight = self.complex_DoubleSpinBox.value()

        if self.option == 'actors':
            self.simple_DoubleSpinBox.setRange(0.5, min(2, average_weight - 0.5))
            self.average_DoubleSpinBox.setRange(max(1, simple_weight + 0.5), min(3, complex_weight - 0.5))
            self.complex_DoubleSpinBox.setRange(max(2, average_weight + 0.5), 5)
        elif self.option == 'useCases':
            self.simple_DoubleSpinBox.setRange(3, min(7, average_weight - 0.5))
            self.average_DoubleSpinBox.setRange(max(7, simple_weight + 0.5), min(13, complex_weight - 0.5))
            self.complex_DoubleSpinBox.setRange(max(10, average_weight + 0.5), 20)

    def check_spinbox_values(self, spinbox):
        """
        Check if the spin box value is within the allowed range and not empty.

        Parameters
        ----------
        spinbox : QSpinBox
            Spinbox of which we want to check the value.
        """
        try:
            weight = float(spinbox.lineEdit().text())
            min_value = spinbox.minimum()
            max_value = spinbox.maximum()
            if weight < min_value or weight > max_value:
                raise ValueError
        except ValueError:
            spinbox.clearFocus()
            spinbox.setFocus()
            line_edit = spinbox.lineEdit()
            line_edit.setCursorPosition(len(spinbox.text()))

    def save_data(self):
        """
        Collect data from the spin boxes and emit the data_saved signal.
        """
        spin_box_values = {
            'simple_weight': self.simple_DoubleSpinBox.value(),
            'average_weight': self.average_DoubleSpinBox.value(),
            'complex_weight': self.complex_DoubleSpinBox.value()
        }
        self.data_saved.emit(spin_box_values)
