# This Python file uses the following encoding: utf-8
from Utils.base_dialog import BaseDialog
import config

class QuickestLicenseDialog(BaseDialog):
    """
    Class for displaying the license agreement dialog in the application.

    This class implements a dialog for showing the license agreement to the user. It includes functionality to display and navigate through the license text.

    Attributes
    ----------
    _instance : QuickestLicenseDialog or None
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
        QuickestLicenseDialog
            Instance of QuickestLicenseDialog.
        """
        if cls._instance is None:
            cls._instance = super(QuickestLicenseDialog, cls).__new__(cls)
        return cls._instance

    def __init__(self, parent=None):
        """
        Initialize the dialog with license information.

        Parameters
        ----------
        parent : QWidget, optional
            Parent widget.
        """
        if QuickestLicenseDialog._initialized:
            return
        super().__init__("License Information", """
            <h4>GNU Lesser General Public License v3.0</h4>
            <p><small>This program is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.</small></p>
            <p><small>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.</small></p>
            <p><small>You should have received a copy of the GNU Lesser General Public License along with this program. If not, see <a href='http://www.gnu.org/licenses/'>http://www.gnu.org/licenses/</a>.</small></p>
            <p><small>QuickEst © 2024 Iván Vega Moreno. All Rights Reserved.</small></p>
            """, config.LICENSE_IMG, parent)
        self.setFixedSize(550, 320)
        QuickestLicenseDialog._initialized = True
