# This Python file uses the following encoding: utf-8
from Utils.base_dialog import BaseDialog
import config

class QuickestInfoDialog(BaseDialog):
    """
    Class for displaying information dialogs in the application.

    This class implements a dialog for showing information about QuickEst application to the user. It is customizable with a title, message, and icon.

    Attributes
    ----------
    _instance : QuickestInfoDialog or None
        Singleton instance of the dialog.
    _initialized : bool
        Indicates if the instance has been initialized.

    Methods
    -------
    """

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance if one doesn't exist, otherwise return the existing instance.

        Parameters
        ----------
        args : tuple
            Positional arguments.
        kwargs : dict
            Keyword arguments.

        Returns
        -------
        QuickestInfoDialog
            Instance of QuickestInfoDialog.
        """
        if cls._instance is None:
            cls._instance = super(QuickestInfoDialog, cls).__new__(cls)
        return cls._instance

    def __init__(self, parent=None):
        """
        Initialize the dialog with information about QuickEst.

        Parameters
        ----------
        parent : QWidget, optional
            Parent widget.
        """
        if QuickestInfoDialog._initialized:
            return
        super().__init__("About QuickEst", """
            <p>QuickEst is an application designed to make quick and accurate estimates of the development effort of software projects.</p>
            <p><strong>Version:</strong> 1.0.0</p>
            <p><strong>Developed by:</strong> Iván Vega Moreno</p>
            <p><strong>Contact:</strong> quickest.app.info@gmail.com</p>
            <p><small>QuickEst © 2024 Iván Vega Moreno. All Rights Reserved.</small></p>
            <p><small>This software is licensed under the LGPL license. For more details, see the license information.</small></p>
            """, config.QUICKEST_IMG, parent)
        self.setFixedSize(530, 300)
        QuickestInfoDialog._initialized = True
