# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from UI.ui_cf_dialog import Ui_CFDialog

class CFDialog(QDialog, Ui_CFDialog):
    """
    Class for managing the conversion factor dialog in the application.

    This class provides the interface and functionalities to manage the conversion factor used in project calculations. It includes fields for inputting the conversion factor and emits signals when actions are performed.

    Attributes
    ----------
    data_saved : Signal
        Signal emitted when data is saved.

    Methods
    -------
    """

    data_saved = Signal(float)

    def __init__(self, cf, parent=None):
        """
        Initialize the dialog with the given conversion factor.

        Parameters
        ----------
        cf : float
            Initial value for the conversion factor.
        parent : QWidget, optional
            Parent widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.initialize_ui()
        self.cf = cf
        self.load_data(self.cf)
        self.setup_signals()

    def initialize_ui(self):
        """
        Initialize the user interface elements.
        """
        self.setWindowTitle("Conversion Factor Settings")
        self.setFixedSize(self.size())
        self.cancel_Button.clicked.connect(self.reject)
        self.save_Button.clicked.connect(self.save_data)

    def setup_signals(self):
        """
        Set up signals for the spin box and buttons.
        """
        self.cf_DoubleSpinBox.valueChanged.connect(self.check_spinbox_value)
        self.cf_DoubleSpinBox.lineEdit().textChanged.connect(self.check_spinbox_value)

    def check_spinbox_value(self):
        """
        Check if the conversion factor value is within the allowed range and enable/disable the save button.
        """
        try:
            cf_value = float(self.cf_DoubleSpinBox.lineEdit().text())
            min_value = self.cf_DoubleSpinBox.minimum()
            max_value = self.cf_DoubleSpinBox.maximum()
            if cf_value < min_value or cf_value > max_value:
                raise ValueError
        except ValueError:
            self.cf_DoubleSpinBox.clearFocus()
            self.cf_DoubleSpinBox.setFocus()
            line_edit = self.cf_DoubleSpinBox.lineEdit()
            line_edit.setCursorPosition(len(line_edit.text()))

    def load_data(self, cf):
        """
        Load cf value for the conversion factor spin box.

        Parameters
        ----------
        cf : float
            Initial value for the conversion factor.
        """
        self.cf_DoubleSpinBox.setValue(cf)
        line_edit = self.cf_DoubleSpinBox.lineEdit()
        line_edit.setCursorPosition(len(line_edit.text()))

    def save_data(self):
        """
        Collect the conversion factor value and emit the data_saved signal.
        """
        cf = self.cf_DoubleSpinBox.value()
        self.data_saved.emit(cf)
