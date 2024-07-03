# This Python file uses the following encoding: utf-8
# Utils/base_dialog.py

from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class BaseDialog(QDialog):
    """
    A custom dialog class with an icon and text content.

    This class creates a dialog with a title, content, and an icon.

    Methods
    -------
    """

    def __init__(self, title, content, icon_path, parent=None):
        """
        Initialize the dialog.

        Parameters
        ----------
        title : str
            The title text for the dialog.
        content : str
            The content text for the dialog.
        icon_path : str
            The file path to the icon image.
        parent : QWidget, optional
            The parent widget of the dialog.
        """
        super().__init__(parent)
        self.setModal(False)
        self.setStyleSheet("""
            QDialog {
                background-color: white;
                color: black;
            }
            QLabel {
                background-color: white;
                color: black;
            }
            QPushButton {
                background-color: white;
                color: black;
            }
        """)

        main_layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        icon_layout = QVBoxLayout()
        icon_layout.setAlignment(Qt.AlignTop)

        icon_label = QLabel()
        icon = QIcon(icon_path)
        icon_pixmap = icon.pixmap(100, 100, QIcon.Mode.Normal, QIcon.State.Off)
        icon_label.setPixmap(icon_pixmap)
        icon_layout.addWidget(icon_label)
        header_layout.addLayout(icon_layout)

        text_layout = QVBoxLayout()
        text_layout.setContentsMargins(10, 0, 10, 10)

        title_label = QLabel(f"<h3>{title}</h3>")
        text_layout.addWidget(title_label)

        content_label = QLabel(content)
        content_label.setWordWrap(True)
        content_label.setOpenExternalLinks(True)
        text_layout.addWidget(content_label)

        header_layout.addLayout(text_layout)
        main_layout.addLayout(header_layout)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        button_layout.addWidget(ok_button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def showEvent(self, event):
        """
        Raises the dialog when shown.

        Parameters
        ----------
        event : QShowEvent
            The show event.
        """
        super().showEvent(event)
        self.raise_()

    def closeEvent(self, event):
        """
        Clears the instance reference when the dialog is closed.

        Parameters
        ----------
        event : QCloseEvent
            The close event.
        """
        self._instance = None
        super().closeEvent(event)
