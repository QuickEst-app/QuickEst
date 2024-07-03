# This Python file uses the following encoding: utf-8
# Utils/pdf_viewer.py

from PySide6.QtWidgets import QMessageBox, QPushButton, QSpinBox, QToolBar, QWidget, QVBoxLayout
from PySide6.QtCore import QUrl, Slot, QPointF
from PySide6.QtPdf import QPdfDocument, QPdfBookmarkModel
from PySide6.QtPdfWidgets import QPdfView

class PDFViewer(QWidget):
    """
    Widget for viewing PDF documents.

    Parameters
    ----------
    parent : QWidget, optional
        The parent widget (default is None).

    Methods
    -------
    """
    def __init__(self, parent=None):
        """
        Initialize the PDFViewer.

        Parameters
        ----------
        parent : QWidget, optional
            The parent widget (default is None).
        """
        super().__init__(parent)
        self.setWindowTitle("PDF Viewer")

        self.pdf_document = QPdfDocument(self)
        self.pdf_view = QPdfView(self)
        self.pdf_view.setDocument(self.pdf_document)
        self.page_navigator = self.pdf_view.pageNavigator()
        self.bookmark_model = QPdfBookmarkModel(self)
        self.bookmark_model.setDocument(self.pdf_document)

        self.next_button = QPushButton("Next")
        self.prev_button = QPushButton("Previous")
        self.page_spinbox = QSpinBox()
        self.page_spinbox.setMinimum(1)
        self.page_spinbox.setMaximum(1)

        self.next_button.clicked.connect(self.next_page)
        self.prev_button.clicked.connect(self.previous_page)
        self.page_spinbox.valueChanged.connect(self.go_to_page)

        toolbar = QToolBar()
        toolbar.addWidget(self.prev_button)
        toolbar.addWidget(self.next_button)
        toolbar.addWidget(self.page_spinbox)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.pdf_view)
        self.setLayout(layout)

        self.current_page = 0

    def closeEvent(self, event):
        """
        Closes the PDF document when the widget is closed.

        Parameters
        ----------
        event : QCloseEvent
            The close event.
        """
        self.pdf_document.close()
        event.accept()

    def load_pdf(self, file_path):
        """
        Loads a PDF document from the specified file path.

        Parameters
        ----------
        file_path : str
            The path to the PDF file.
        """
        self.pdf_document.close()
        self.pdf_document.load(file_path)
        if self.pdf_document.status() != QPdfDocument.Status.Ready:
            QMessageBox.critical(self, "Error", "Failed to load PDF")
        else:
            self.setWindowTitle("QuickEst – Methodology and manual")
            self.page_spinbox.setMaximum(self.pdf_document.pageCount())
            self.pdf_view.setZoomMode(QPdfView.ZoomMode.FitToWidth)
            self.go_to_page(1)

    def next_page(self):
        """Advances to the next page."""
        if self.current_page < self.pdf_document.pageCount():
            self.current_page += 1
            self.page_spinbox.setValue(self.current_page)
            self.page_navigator.jump(self.current_page - 1, QPointF(0, 0))

    def previous_page(self):
        """Returns to the previous page."""
        if self.current_page > 1:
            self.current_page -= 1
            self.page_spinbox.setValue(self.current_page)
            self.page_navigator.jump(self.current_page - 1, QPointF(0, 0))

    def go_to_page(self, page):
        """
        Jumps to the specified page.

        Parameters
        ----------
        page : int
            The page number to jump to.
        """
        self.current_page = page
        self.page_navigator.jump(self.current_page - 1, QPointF(0, 0))

    @Slot(QUrl)
    def open(self, doc_location):
        """
        Opens a PDF document from a URL.

        Parameters
        ----------
        doc_location : QUrl
            The URL of the document to open.
        """
        if doc_location.isLocalFile():
            self.load_pdf(doc_location.toLocalFile())
        else:
            QMessageBox.critical(self, "Failed to open", f"{doc_location} is not a valid local file")
