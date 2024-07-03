# This Python file uses the following encoding: utf-8
# view/technical_factors_view.py

import config
from Utils.table_utils import TableUtils
from Utils.button_utils import ButtonUtils
from Utils.widget_config import WidgetConfig
from PySide6.QtWidgets import QHeaderView, QWidget, QAbstractItemView, QTableWidgetItem
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QTextCursor

class TechnicalFactorsView(QWidget):
    """
    Class implementing the view for managing technical factors.

    It handles the user interface related to technical factors management, providing functionalities to view and update this factors. It includes the setup of tables and action buttons, facilitating efficient information management.

    Attributes
    ----------
    factor_saved : Signal
        Signal emitted when a technical factor is saved.

    Methods
    -------
    """

    factor_saved = Signal(dict)

    def __init__(self, parent=None):
        """
        Initialize the view with the given parent.

        Parameters
        ----------
        parent : QWidget, optional
            Parent widget.
        """
        super().__init__(parent)
        self.main = parent  # Main as parent class
        self.ui = self.main.ui  # Use the UI initialized in Main
        self.technicalFactors_table = self.ui.technicalFactors_TableWidget
        self.technicalFactors_summary_table = self.ui.technicalFactorsSummary_TableWidget
        self.setup_technical_factors_ui()

    def setup_technical_factors_ui(self):
        """
        Setup the user interface elements for the technical factors view.
        """
        # Summary table
        self.technicalFactors_summary_table.setCornerWidget(QWidget())
        self.technicalFactors_summary_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.technicalFactors_summary_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.technicalFactors_summary_table.setSpan(3, 0, 1, 2)

        # Technical Factors table
        self.technicalFactors_table.setCornerWidget(QWidget())
        technicalFactors_headerTable = self.technicalFactors_table.horizontalHeader()
        technicalFactors_headerTable.sectionClicked.connect(lambda index: TableUtils.on_header_clicked(index, self.technicalFactors_table, []))

        self.technicalFactors_table.setColumnHidden(0, True)
        for column in range(self.technicalFactors_table.columnCount()):
            self.technicalFactors_table.horizontalHeader().setSectionResizeMode(column, QHeaderView.Stretch)
        self.technicalFactors_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.technicalFactors_table.setSpan(13, 0, 1, 7)

        # Manage Technical Factors
        self.ui.technicalFactorsFactor_ComboBox.currentIndexChanged.connect(self.update_technical_factors_tooltip)

        self.technicalFactors_radioButtons = [
            self.ui.technicalFactors_RadioButton_0,
            self.ui.technicalFactors_RadioButton_1,
            self.ui.technicalFactors_RadioButton_2,
            self.ui.technicalFactors_RadioButton_3,
            self.ui.technicalFactors_RadioButton_4,
            self.ui.technicalFactors_RadioButton_5
        ]

        self.ui.saveTechnicalFactor_Button.setEnabled(False)
        ButtonUtils.set_styles_button(self.ui.saveTechnicalFactor_Button, '#5AFFA6', '#094646', config.SAVE_FACTORS_IMG, config.SAVE_DISABLED_IMG, False, icon_size=22)
        self.ui.cancelTechnicalFactor_Button.setEnabled(False)
        ButtonUtils.set_styles_button(self.ui.cancelTechnicalFactor_Button, '#FF0000', '#FFFFFF', config.CANCEL_FACTORS_IMG, config.CANCEL_DISABLED_IMG, False, icon_size=22)

        self.ui.saveTechnicalFactor_Button.clicked.connect(self.save_technical_factor)
        self.ui.cancelTechnicalFactor_Button.clicked.connect(lambda: self.ui.technicalFactorsFactor_ComboBox.setCurrentIndex(-1))

        self.ui.technicalFactorsFactor_ComboBox.currentIndexChanged.connect(self.update_weights_limits)
        self.ui.technicalFactorsFactor_ComboBox.currentIndexChanged.connect(self.check_enable_buttons)
        self.ui.technicalFactorsInfo_Label.setVisible(False)
        self.ui.warning_TF_label.setVisible(False)

        self.ui.technicalFactorsComment_PlainTextEdit.textChanged.connect(lambda: WidgetConfig.limit_comment_length(self.ui.technicalFactorsComment_PlainTextEdit, self.ui.technicalFactorsCommentCounter_Label))

        WidgetConfig.configure_widgets(False, self.technicalFactors_radioButtons, self.ui.technicalFactorsWeight_DoubleSpinBox, self.ui.technicalFactorsComment_PlainTextEdit)

        self.setTabOrder(self.ui.technicalFactorsFactor_ComboBox, self.ui.technicalFactors_RadioButton_0)
        self.setTabOrder(self.ui.technicalFactors_RadioButton_0, self.ui.technicalFactorsWeight_DoubleSpinBox)
        self.setTabOrder(self.ui.technicalFactorsWeight_DoubleSpinBox,  self.ui.technicalFactorsComment_PlainTextEdit)

        original_focus_in_event = self.ui.technicalFactorsComment_PlainTextEdit.focusInEvent
        original_focus_out_event = self.ui.technicalFactorsComment_PlainTextEdit.focusOutEvent

        self.ui.technicalFactorsComment_PlainTextEdit.focusInEvent = lambda event: (
            self.ui.technicalFactorsComment_PlainTextEdit.selectAll() if event.reason() in (Qt.TabFocusReason, Qt.BacktabFocusReason) else None,
            original_focus_in_event(event)
        )
        self.ui.technicalFactorsComment_PlainTextEdit.focusOutEvent = lambda event: (
            self.ui.technicalFactorsComment_PlainTextEdit.setTextCursor(QTextCursor(self.ui.technicalFactorsComment_PlainTextEdit.document().end())),
            original_focus_out_event(event)
        )

    def save_technical_factor(self):
        """
        Emit the factor_saved signal with the current technical factor data.
        """
        factor_data = {
            'factor': self.ui.technicalFactorsFactor_ComboBox.currentText().split(" – ")[0],  # Factor
            'weight': self.ui.technicalFactorsWeight_DoubleSpinBox.value(),  # Weight
            'influence': next((i for i, rb in enumerate(self.technicalFactors_radioButtons) if rb.isChecked()), 0),  # Influence
            'comment': self.ui.technicalFactorsComment_PlainTextEdit.toPlainText().strip()  # Comment
        }
        self.factor_saved.emit(factor_data)

    def display_message(self, title, message, icon_path, dialog_type='simple_message'):
        """
        Display a message dialog.

        Parameters
        ----------
        title : str
            Title of the message dialog.
        message : str
            Message content.
        icon_path : str
            Path to the icon for the dialog.
        dialog_type : str, optional
            Type of dialog, default is 'simple_message'.

        Returns
        -------
        QDialog
            The message dialog.
        """
        return WidgetConfig.show_message_dialog(title, message, icon_path, dialog_type)

    def update_technical_factors_tooltip(self):
        """
        Update tooltips for the technical factors based on the selected factor.
        """
        helpToolTips = {
            'T01': """Architecture can be centralized as well as distributed.\n
        0: The application does not assist in the transfer of data or processes between CPUs.
        1: The application prepares data for the end user to process on another CPU.
            Example: spreadsheets or database managers.
        2: Data are prepared to be transferred and processed on another CPU.
        3: Distributed processing and data transfer online in one direction.
        4: Distributed processing and data transfer online in both directions.
        5: Processing functions are executed dynamically on the most appropriate CPU.""",
            'T02': """Identify the application performance objectives, established and approved by the user.\n
        0: No special performance demands were established by the user.
        1: Performance requirements were established and reviewed by the user, but no special action was necessary.
        2: Response time is critical during peak hours. The processing deadline is always for the next business day.
            No special consideration for CPU usage was required.
        3: Response time is critical at all times the application is in use. Processing deadline requirements with
            other systems are limited.No special CPU usage procedures were necessary.
        4: The performance requirements set by the user are rigorous enough to require performance analysis tasks
            during the application's analysis and design phase.
        5: In addition to what is described in item 4, performance analysis tools were used in the design, development,
            and/or implementation phases to deliver the performance established by the user.""",
            'T03': """The provided functions emphasize an application for the end-user's efficiency. Examples include: menu, online help documentation,
automatic cursor movement, vertical and horizontal screen scrolling, predefined function keys, easy navigation between screens,
a minimum number of screens to perform a business function, remote printing, multilingual support (more than two languages),
among others.\n
        0: The application does not present any of the items mentioned above.
        1: Presents 1 to 3 of the items mentioned above.
        2: Presents 4 to 5 of the items mentioned above.
        3: Presents 6 or more of the items mentioned above, but there are no requirements related to efficiency.
        4: Presents 6 or more of the items mentioned above, and the requirements established for efficiency are rigorous and sufficient for
            the application design phase to include factors to minimize typing, maximize defaults, use templates, among others.
        5: Presents 6 or more of the items mentioned above, and the requirements established for user efficiency are rigorous or sufficient
            enough that the use of special tools and processes is necessary to demonstrate that the efficiency objectives have been achieved.""",
            'T04': """The processing complexity influences the system sizing, and therefore, the degree of influence must be quantified\n based on the following categories:\n
        - Special auditing processing and/or special security processing.
        - Extensive logical processing.
        - Extensive mathematical processing.
        - A large amount of processing execution, resulting from incomplete transactions that require reprocessing.
           For example, incomplete ATM transactions caused by communication interruptions, missing data values,
           or error validations.
        - Complex processing to handle multiple input/output possibilities. For example, multiple media and device
           independence.\n
        0: Does not present any item mentioned above.
        1: Presents one of the items above.
        2: Presents two of the items above.
        3: Presents three of the items above.
        4: Presents four of the items above.
        5: Presents all the items mentioned in the paragraph above.""",
            'T05': """The application and its source code were specifically designed, developed, and supported to be\nreusable in other applications.\n
        0: Does not present reusable code.
        1: Reusable code is used only within the application.
        2: Less than 10% of the application was made with its use in other applications in mind.
        3: 10% or more of the application was made with its use in other applications in mind.
        4: The application was designed and documented to facilitate the reuse of code, and the
            application is customized by the user at the source code level.
        5: The application was designed and documented to facilitate the reuse of the source code.""",
            'T06': """Indicate the level of preparedness of procedures and tools for the system installation.\n
        0: No consideration has been taken into account by the user, and no special procedure was required for installation.
        1: No special consideration has been taken into account by the user, but a special procedure was required for installation.
        2: Installation requirements were established by the user.
        3: Installation requirements were set by the user, and installation scripts were prepared and tested.
        4: In addition to what is described in item 2, automated installation tools were prepared and tested.
        5: In addition to what is described in item 3, automated installation tools were prepared and tested.""",
            'T07': """Effective installation, backup, and recovery procedures were developed and tested. The application minimizes the need for manual activities.\n
        0: No special consideration regarding operational ease, beyond standard backup procedures, was taken into account by the user.
        1: Efficient initialization, backup, and recovery procedures were prepared, but operator intervention is necessary.
        2: Efficient initialization, backup, and recovery procedures were prepared, and no operator intervention is necessary.
        3: The application minimizes the operation of mounting magnetic tapes.
        4: The application minimizes the need for handling forms.
        5: The application was designed in such a way that no operator intervention is required in normal operation.""",
            'T08': """The application was specifically designed, developed, and supported to be installed on multiple platforms (Windows, Unix, Linux, etc.).\n
        0: The user has not requested consideration for the need to install the application on more than one platform.
        1: The need for installation on multiple platforms was considered in the project, and the application was designed to operate only in
            identical hardware and software environments.
        2: The need for installation on multiple platforms was considered in the project, and the application was designed to operate only in
            similar hardware and software environments.
        3: The need for installation on multiple platforms was considered in the project, and the application was designed to operate in different
            environments.
        4: A documentation and maintenance plan was developed and tested to support the application on multiple platforms, and the application
            meets items 1 and 2.
        5: A documentation and maintenance plan was developed and tested to support the application on multiple platforms if the application
            meets item 3.""",
            'T09': """The application was specifically designed and developed to support maintenance, ensuring ease of changes.\n
        0: No special requirement to design the application to minimize or facilitate changes was considered by the user.
        1: Flexible query/reporting features are provided, so it is capable of handling simple query requests.
            Example: and/or logic applied only to a single Internal Logical File (count as one item).
        2: Flexible query/reporting features are provided, so it is capable of handling medium complexity query requests.
            Example: and/or logic applied to more than one Internal Logical File (count as two items).
        3: Flexible query/reporting features are provided, so it is capable of handling complex query requests.
            Example: Combinations of and/or logic applied to one or more Internal Logical Files (count as three items).
        4: Control data are maintained in tables that are updated by the user through online and iterative processes,
            but the changes are only updated by the user through online and iterative processes, with modifications becoming
            effective on the next business day.
        5: Control data are maintained in tables that can be updated by the user through online and iterative processes, with
            modifications becoming effective immediately (count as two items).""",
            'T10': """Indicate the concurrent access volume to the application.\n
        0: Concurrent access is not expected.
        1: Concurrent accesses are expected sporadically.
        2: Concurrent accesses are expected.
        3: Concurrent accesses are expected daily.
        4: Many concurrent accesses were specified by the user for the application,
            necessitating the performance of performance analysis tasks during the
            application's design phase.
        5: Requires the use of tools to control access in the development and
            implementation phases, in addition to the previous considerations.""",
            'T11': """Indicate the level of security required by the application.\n
        0: No requirement was requested by the user to consider the need for security control in the application.
        1: The need for security control was considered in the system design.
        2: The need for security control was considered in the system design, and the application was designed so
            that only authorized users can access.
        3: The need for security control was considered in the system design, and the application was designed so
            that only authorized users can access. Access will be controlled and audited.
        4: In addition to what is described in item 3, specific security features or mechanisms are implemented,
            ensuring comprehensive security coverage.
        5: A security plan was developed and tested to support access control to the application and an audit.""",
            'T12': """Indicate the level of direct access to third-party services or systems required by the application.\n
        0: No access to third-party services or systems is necessary for the application.
        1: The application requires basic access to third-party services to obtain information or services, but without deep integration.
        2: The application must integrate with third-party services to perform specific operations and receive data regularly.
        3: The application is designed to frequently interact with multiple third-party services, including real-time data synchronization.
        5: The application has a complex, bidirectional integration with multiple third-party services, with requirements for high availability, security, and access auditing.""",
            'T13': """Indicate the level of ease of providing training to users to use the software.\n
        0: No request by the user to consider the need for special training.
        1: The need for special training was considered in the system design.
        2: The need for training was considered in the system design, and an application was designed
            for users to easily access.
        3: The need for special training was considered in the system design, and an application was
            designed for users to use at various levels.
        4-5: A training plan was developed and tested to facilitate the use of the application.""",
        }

        warning_header = """
        <b>Warning: Modifying Weights of Technical Factors.</b><br><br>Modifying the weights of technical factors can significantly affect the accuracy of your project effort estimates.Adjust these values only if you have adequate knowledge.<br><br>
        The allowed ranges have been set to provide flexibility in adapting the methodology to the specific needs of the project while maintaining the integrity of the original UCP methodology. These ranges ensure that the adjusted values accurately reflect the complexity and characteristics of the project without significantly skewing the estimates.<br><br>
        """
        warningToolTips = {
                'T01': f"""{warning_header}
    <b>Distributed System</b>: Allowed range from 1.0 to 3.0 (Default: 2.0).""",
                'T02': f"""{warning_header}
    <b>Performance or response time</b>: Allowed range from 0.5 to 2.0 (Default: 1.0).""",
                'T03': f"""{warning_header}
    <b>End user efficiency</b>: Allowed range from 0.5 to 2.0 (Default: 1.0).""",
                'T04': f"""{warning_header}
    <b>Complex internal processing</b>: Allowed range from 0.5 to 2.0 (Default: 1.0).""",
                'T05': f"""{warning_header}
    <b>The code must be reusable</b>: Allowed range from 0.5 to 2.0 (Default: 1.0).""",
                'T06': f"""{warning_header}
    <b>Ease of installation</b>: Allowed range from 0.2 to 1.0 (Default: 0.5).""",
                'T07': f"""{warning_header}
    <b>Ease to use</b>: Allowed range from 0.2 to 1.0 (Default: 0.5).""",
                'T08': f"""{warning_header}
    <b>Portability</b>: Allowed range from 1.0 to 3.0 (Default: 2.0).""",
                'T09': f"""{warning_header}
    <b>Easy of change</b>: Allowed range from 0.5 to 2.0 (Default: 1.0).""",
                'T10': f"""{warning_header}
    <b>Concurrence</b>: Allowed range from 0.5 to 2.0 (Default: 1.0).""",
                'T11': f"""{warning_header}
    <b>Special security features</b>: Allowed range from 0.5 to 2.0 (Default: 1.0).""",
                'T12': f"""{warning_header}
    <b>Provides direct access to third parties</b>: Allowed range from 0.5 to 2.0 (Default: 1.0).""",
                'T13': f"""{warning_header}
    <b>Special user training required</b>: Allowed range from 0.5 to 2.0 (Default: 1.0)."""
            }


        selectedFactor = self.ui.technicalFactorsFactor_ComboBox.currentText().split(" – ")[0]
        help_tooltip = helpToolTips.get(selectedFactor)
        self.ui.technicalFactorsInfo_Label.setToolTip(help_tooltip)
        warning_tooltip = warningToolTips.get(selectedFactor)
        self.ui.warning_TF_label.setToolTip(warning_tooltip)

    def check_enable_buttons(self):
        """
        Enable or disable the save button based on the validity of the input.
        """
        factor = self.ui.technicalFactorsFactor_ComboBox.currentText().split(" – ")[0]
        if factor != '':
            self.ui.technicalFactorsInfo_Label.setVisible(True)
            self.ui.warning_TF_label.setVisible(True)
            self.ui.saveTechnicalFactor_Button.setEnabled(True)
            ButtonUtils.set_styles_button(self.ui.saveTechnicalFactor_Button, '#5AFFA6', '#094646', config.SAVE_FACTORS_IMG, config.SAVE_DISABLED_IMG, True, icon_size=22)
            self.ui.cancelTechnicalFactor_Button.setEnabled(True)
            ButtonUtils.set_styles_button(self.ui.cancelTechnicalFactor_Button, '#FF0000', '#FFFFFF', config.CANCEL_FACTORS_IMG, config.CANCEL_DISABLED_IMG, True, icon_size=22)
            for row in range(self.technicalFactors_table.rowCount()-1):
                if self.technicalFactors_table.item(row, 1).text() == factor:
                    weight = float(self.technicalFactors_table.item(row, 3).text())
                    influence = int(self.technicalFactors_table.item(row, 4).text())
                    comment = self.technicalFactors_table.cellWidget(row, 6).toolTip() if self.technicalFactors_table.cellWidget(row, 6) else ""
                    self.ui.technicalFactorsWeight_DoubleSpinBox.setValue(weight)
                    self.technicalFactors_radioButtons[influence].setChecked(True)
                    self.ui.technicalFactorsComment_PlainTextEdit.setPlainText(comment)
                    break
            WidgetConfig.configure_widgets(True, self.technicalFactors_radioButtons, self.ui.technicalFactorsWeight_DoubleSpinBox, self.ui.technicalFactorsComment_PlainTextEdit)
        else:
            self.ui.technicalFactorsInfo_Label.setVisible(False)
            self.ui.warning_TF_label.setVisible(False)
            self.ui.saveTechnicalFactor_Button.setEnabled(False)
            ButtonUtils.set_styles_button(self.ui.saveTechnicalFactor_Button, '#5AFFA6', '#094646', config.SAVE_FACTORS_IMG, config.SAVE_DISABLED_IMG, False, icon_size=22)
            self.ui.cancelTechnicalFactor_Button.setEnabled(False)
            ButtonUtils.set_styles_button(self.ui.cancelTechnicalFactor_Button, '#FF0000', '#FFFFFF', config.CANCEL_FACTORS_IMG, config.CANCEL_DISABLED_IMG, False, icon_size=22)
            WidgetConfig.configure_widgets(False, self.technicalFactors_radioButtons, self.ui.technicalFactorsWeight_DoubleSpinBox, self.ui.technicalFactorsComment_PlainTextEdit)

    def update_technical_factors_table(self, data_saved, TFactor):
        """
        Update the technical factors table with the provided data.

        Parameters
        ----------
        data_saved : dict
            Dictionary containing the saved data for a technical factor.
        TFactor : float
            The updated technical factor value.
        """
        self.technicalFactors_table.setSortingEnabled(False)
        self.technicalFactors_table.horizontalHeader().setSortIndicatorShown(True)

        for i in range(self.technicalFactors_table.rowCount()-1):
            if self.technicalFactors_table.item(i, 1).text() == data_saved['factor']:
                row_index = i
                break

        self.technicalFactors_table.item(self.technicalFactors_table.rowCount()-1, 0).setText(f"TFactor: {TFactor}")

        if 'description' in data_saved:
            self.technicalFactors_table.item(row_index, 2).setText(data_saved['description'])

        items_values = [data_saved['weight'], data_saved['influence'], data_saved['result']]
        for i, item_value in enumerate(items_values):
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, item_value)
            item.setBackground(QColor(222, 255, 250))
            item.setTextAlignment(Qt.AlignCenter)
            self.technicalFactors_table.setItem(row_index, 3 + i, item)
        if data_saved['comment'] != '':
            comment_item = QTableWidgetItem("")
            comment_item.setBackground(QColor(222, 255, 250))
            WidgetConfig.create_comment(data_saved['comment'], row_index, self.technicalFactors_table, config.COMMENT_IMG_GREEN)
            self.technicalFactors_table.setItem(row_index, 6, comment_item)
        else:
            comment_item = QTableWidgetItem(" ")
            comment_item.setBackground(QColor(222, 255, 250))
            self.technicalFactors_table.removeCellWidget(row_index, self.technicalFactors_table.columnCount() - 1)
            self.technicalFactors_table.setItem(row_index, 6, comment_item)

        self.ui.technicalFactorsFactor_ComboBox.setCurrentIndex(-1)
        self.technicalFactors_table.setSortingEnabled(True)
        self.technicalFactors_table.scrollToItem(self.technicalFactors_table.currentItem(), QAbstractItemView.PositionAtCenter)

    def update_technical_factors_summary(self, factors_count):
        """
        Update the technical factors summary table with the provided data.

        Parameters
        ----------
        factors_count : dict
            Dictionary containing the count of factors for each category.
        """
        self.technicalFactors_summary_table.item(0, 2).setText(str(factors_count['irrelevant']))
        self.technicalFactors_summary_table.item(1, 2).setText(str(factors_count['medium']))
        self.technicalFactors_summary_table.item(2, 2).setText(str(factors_count['essential']))

    def update_weights_limits(self, index):
        """
        Update the minimum and maximum limits of factor weights based on the selected factor in the QComboBox.

        Parameters
        ----------
        index : int
            The index of the selected item in the QComboBox.
        """
        limits = {
            0: (1.0, 3.0),
            1: (0.5, 2.0),
            2: (0.5, 2.0),
            3: (0.5, 2.0),
            4: (0.5, 2.0),
            5: (0.2, 1.0),
            6: (0.2, 1.0),
            7: (1.0, 3.0),
            8: (0.5, 2.0),
            9: (0.5, 2.0),
            10: (0.5, 2.0),
            11: (0.5, 2.0),
            12: (0.5, 2.0)
        }
        min_val, max_val = limits.get(index, (0.0, 0.0))
        self.ui.technicalFactorsWeight_DoubleSpinBox.setRange(min_val, max_val)
