# This Python file uses the following encoding: utf-8
# view/environmentalFactors_view.py

import config
from Utils.table_utils import TableUtils
from Utils.button_utils import ButtonUtils
from Utils.widget_config import WidgetConfig
from PySide6.QtWidgets import QHeaderView, QWidget, QAbstractItemView, QTableWidgetItem
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QTextCursor

class EnvironmentalFactorsView(QWidget):
    """
    Class implementing the view for managing environmental factors.

    It handles the user interface related to environmental factors management, providing functionalities to view and update this factors. It includes the setup of tables and action buttons, facilitating efficient information management.

    Attributes
    ----------
    factor_saved : Signal
        Signal emitted when an environmental factor is saved.

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
        self.environmentalFactors_table = self.ui.environmentalFactors_TableWidget
        self.environmentalFactors_summary_table = self.ui.environmentalFactorsSummary_TableWidget
        self.setup_environmental_factors_ui()

    def setup_environmental_factors_ui(self):
        """
        Setup the user interface elements for the environmental factors view.
        """
        # Summary table
        self.environmentalFactors_summary_table.setCornerWidget(QWidget())
        self.environmentalFactors_summary_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.environmentalFactors_summary_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.environmentalFactors_summary_table.setSpan(3, 0, 1, 2)

        # Environmental Factors table
        self.environmentalFactors_table.setCornerWidget(QWidget())
        environmentalFactors_headerTable = self.environmentalFactors_table.horizontalHeader()
        environmentalFactors_headerTable.sectionClicked.connect(lambda index: TableUtils.on_header_clicked(index, self.environmentalFactors_table, []))

        self.environmentalFactors_table.setColumnHidden(0, True)
        for column in range(self.environmentalFactors_table.columnCount()):
            self.environmentalFactors_table.horizontalHeader().setSectionResizeMode(column, QHeaderView.Stretch)
        self.environmentalFactors_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.environmentalFactors_table.setSpan(8, 0, 1, 7)

        # Manage Environmental Factors
        self.ui.environmentalFactorsFactor_ComboBox.currentIndexChanged.connect(self.update_environmental_factors_tooltip)

        self.environmentalFactors_radioButtons = [
            self.ui.environmentalFactors_RadioButton_0,
            self.ui.environmentalFactors_RadioButton_1,
            self.ui.environmentalFactors_RadioButton_2,
            self.ui.environmentalFactors_RadioButton_3,
            self.ui.environmentalFactors_RadioButton_4,
            self.ui.environmentalFactors_RadioButton_5
        ]

        self.ui.saveEnvironmentalFactor_Button.setEnabled(False)
        ButtonUtils.set_styles_button(self.ui.saveEnvironmentalFactor_Button, '#5AFFA6', '#094646', config.SAVE_FACTORS_IMG, config.SAVE_DISABLED_IMG, False, icon_size=22)
        self.ui.cancelEnvironmentalFactor_Button.setEnabled(False)
        ButtonUtils.set_styles_button(self.ui.cancelEnvironmentalFactor_Button, '#FF0000', '#FFFFFF', config.CANCEL_FACTORS_IMG, config.CANCEL_DISABLED_IMG, False, icon_size=22)
        self.ui.saveEnvironmentalFactor_Button.clicked.connect(self.save_environmental_factor)
        self.ui.cancelEnvironmentalFactor_Button.clicked.connect(lambda: self.ui.environmentalFactorsFactor_ComboBox.setCurrentIndex(-1))

        self.ui.environmentalFactorsFactor_ComboBox.currentIndexChanged.connect(self.update_weights_limits)
        self.ui.environmentalFactorsFactor_ComboBox.currentIndexChanged.connect(self.check_enable_buttons)
        self.ui.warning_EF_label.setVisible(False)
        self.ui.environmentalFactorsInfo_Label.setVisible(False)

        self.ui.environmentalFactorsComment_PlainTextEdit.textChanged.connect(lambda: WidgetConfig.limit_comment_length(self.ui.environmentalFactorsComment_PlainTextEdit, self.ui.environmentalFactorsCommentCounter_Label))

        WidgetConfig.configure_widgets(False, self.environmentalFactors_radioButtons, self.ui.environmentalFactorsWeight_DoubleSpinBox, self.ui.environmentalFactorsComment_PlainTextEdit)

        self.setTabOrder(self.ui.environmentalFactorsFactor_ComboBox, self.ui.environmentalFactors_RadioButton_0)
        self.setTabOrder(self.ui.environmentalFactors_RadioButton_0, self.ui.environmentalFactorsWeight_DoubleSpinBox)
        self.setTabOrder(self.ui.environmentalFactorsWeight_DoubleSpinBox,  self.ui.environmentalFactorsComment_PlainTextEdit)

        original_focus_in_event = self.ui.environmentalFactorsComment_PlainTextEdit.focusInEvent
        original_focus_out_event = self.ui.environmentalFactorsComment_PlainTextEdit.focusOutEvent

        self.ui.environmentalFactorsComment_PlainTextEdit.focusInEvent = lambda event: (
            self.ui.environmentalFactorsComment_PlainTextEdit.selectAll() if event.reason() in (Qt.TabFocusReason, Qt.BacktabFocusReason) else None,
            original_focus_in_event(event)
        )
        self.ui.environmentalFactorsComment_PlainTextEdit.focusOutEvent = lambda event: (
            self.ui.environmentalFactorsComment_PlainTextEdit.setTextCursor(QTextCursor(self.ui.environmentalFactorsComment_PlainTextEdit.document().end())),
            original_focus_out_event(event)
        )

    def save_environmental_factor(self):
        """
        Emit the factor_saved signal with the current environmental factor data.
        """
        factor_data = {
            'factor': self.ui.environmentalFactorsFactor_ComboBox.currentText().split(" – ")[0],  # Factor
            'weight': self.ui.environmentalFactorsWeight_DoubleSpinBox.value(),  # Weight
            'influence': next((i for i, rb in enumerate(self.environmentalFactors_radioButtons) if rb.isChecked()), 0),  # Influence
            'comment': self.ui.environmentalFactorsComment_PlainTextEdit.toPlainText().strip()  # Comment
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

    def update_environmental_factors_tooltip(self):
        """
        Update the tooltip for the environmental factors based on the selected factor.
        """
        toolTip_E1E4 = "0: No experience.\n3: Average experience.\n5: Extensive experience (expert)."
        helpToolTips = {
            'E1': toolTip_E1E4,
            'E2': toolTip_E1E4,
            'E3': toolTip_E1E4,
            'E4': toolTip_E1E4,
            'E5': """0: No motivation for the project.\n3: Average motivation.\n5: High motivation.""",
            'E6': """0: Extremely unstable requirements.\n3: Average stability.\n5: Stable requirements with no possibility of changes.""",
            'E7': """0: There is no part-time staff (i.e., everyone is full-time).\n3: A half and half (i.e., the company has staff working part-time and others full-time).\n5: All the staff works part-time (no one full-time).""",
            'E8': """0: The programming language is easy to use.\n3: Medium.\n5: The programming language is extremely difficult.""",
        }

        warning_header = """
        <b>Warning: Modifying Weights of Environmental Factors.</b><br><br>Modifying the weights of environmental factors can significantly affect the accuracy of your project effort estimates.Adjust these values only if you have adequate knowledge.<br><br>
        The allowed ranges have been set to provide flexibility in adapting the methodology to the specific needs of the project while maintaining the integrity of the original UCP methodology. These ranges ensure that the adjusted values accurately reflect the complexity and characteristics of the project without significantly skewing the estimates.<br><br>
        """
        warningToolTips = {
            'E1': f"{warning_header}<b>Familiarity with the project model used</b>: Allowed range from 1.0 to 2.0 (Default: 1.5).",
            'E2': f"{warning_header}<b>Application experience</b>: Allowed range from 0.2 to 0.8 (Default: 0.5).",
            'E3': f"{warning_header}<b>Object oriented experience</b>: Allowed range from 0.5 to 1.5 (Default: 1.0).",
            'E4': f"{warning_header}<b>Lead analyst capability</b>: Allowed range from 0.2 to 0.8 (Default: 0.5).",
            'E5': f"{warning_header}<b>Motivation</b>: Allowed range from 0.5 to 1.5 (Default: 1.0).",
            'E6': f"{warning_header}<b>Stability of requirements</b>: Allowed range from 1.0 to 2.5 (Default: 2.0).",
            'E7': f"{warning_header}<b>Part time workers</b>: Allowed range from -1.5 to -0.5 (Default: -1.0).",
            'E8': f"{warning_header}<b>Programming language difficulty</b>: Allowed range from -1.5 to -0.5 (Default: -1.0)."
        }

        selectedFactor = self.ui.environmentalFactorsFactor_ComboBox.currentText().split(" – ")[0]
        help_tooltip = helpToolTips.get(selectedFactor)
        self.ui.environmentalFactorsInfo_Label.setToolTip(help_tooltip)
        warning_tooltip = warningToolTips.get(selectedFactor)
        self.ui.warning_EF_label.setToolTip(warning_tooltip)

    def check_enable_buttons(self):
        """
        Enable or disable the save button based on the current input values.
        """
        factor = self.ui.environmentalFactorsFactor_ComboBox.currentText().split(" – ")[0]
        if factor != '':
            self.ui.environmentalFactorsInfo_Label.setVisible(True)
            self.ui.saveEnvironmentalFactor_Button.setEnabled(True)
            ButtonUtils.set_styles_button(self.ui.saveEnvironmentalFactor_Button, '#5AFFA6', '#094646', config.SAVE_FACTORS_IMG, config.SAVE_DISABLED_IMG, True, icon_size=22)
            self.ui.cancelEnvironmentalFactor_Button.setEnabled(True)
            ButtonUtils.set_styles_button(self.ui.cancelEnvironmentalFactor_Button, '#FF0000', '#FFFFFF', config.CANCEL_FACTORS_IMG, config.CANCEL_DISABLED_IMG, True, icon_size=22)
            self.ui.warning_EF_label.setVisible(True)
            for row in range(self.environmentalFactors_table.rowCount() - 1):
                if self.environmentalFactors_table.item(row, 1).text() == factor:
                    weight = float(self.environmentalFactors_table.item(row, 3).text())
                    influence = int(self.environmentalFactors_table.item(row, 4).text())
                    comment = self.environmentalFactors_table.cellWidget(row, 6).toolTip() if self.environmentalFactors_table.cellWidget(row, 6) else ""
                    self.ui.environmentalFactorsWeight_DoubleSpinBox.setValue(weight)
                    self.environmentalFactors_radioButtons[influence].setChecked(True)
                    self.ui.environmentalFactorsComment_PlainTextEdit.setPlainText(comment)
                    break
            WidgetConfig.configure_widgets(True, self.environmentalFactors_radioButtons, self.ui.environmentalFactorsWeight_DoubleSpinBox, self.ui.environmentalFactorsComment_PlainTextEdit)
        else:
            self.ui.environmentalFactorsInfo_Label.setVisible(False)
            self.ui.warning_EF_label.setVisible(False)
            self.ui.saveEnvironmentalFactor_Button.setEnabled(False)
            ButtonUtils.set_styles_button(self.ui.saveEnvironmentalFactor_Button, '#5AFFA6', '#094646', config.SAVE_FACTORS_IMG, config.SAVE_DISABLED_IMG, False, icon_size=22)
            self.ui.cancelEnvironmentalFactor_Button.setEnabled(False)
            ButtonUtils.set_styles_button(self.ui.cancelEnvironmentalFactor_Button, '#FF0000', '#FFFFFF', config.CANCEL_FACTORS_IMG, config.CANCEL_DISABLED_IMG, False, icon_size=22)
            WidgetConfig.configure_widgets(False, self.environmentalFactors_radioButtons, self.ui.environmentalFactorsWeight_DoubleSpinBox, self.ui.environmentalFactorsComment_PlainTextEdit)

    def update_environmental_factors_table(self, data_saved, EFactor):
        """
        Update the environmental factors table with the saved data.

        Parameters
        ----------
        data_saved : dict
            Dictionary containing the saved data for the environmental factor.
        EFactor : float
            The updated environmental factor value.
        """
        self.environmentalFactors_table.setSortingEnabled(False)
        self.environmentalFactors_table.horizontalHeader().setSortIndicatorShown(True)
        for i in range(self.environmentalFactors_table.rowCount() - 1):
            if self.environmentalFactors_table.item(i, 1).text() == data_saved['factor']:
                row_index = i
                break

        self.environmentalFactors_table.item(self.environmentalFactors_table.rowCount() - 1, 0).setText(f"EFactor: {EFactor}")

        if 'description' in data_saved:
            self.environmentalFactors_table.item(row_index, 2).setText(data_saved['description'])

        items_values = [data_saved['weight'], data_saved['influence'], data_saved['result']]
        for i, item_value in enumerate(items_values):
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, item_value)
            item.setBackground(QColor(222, 255, 250))
            item.setTextAlignment(Qt.AlignCenter)
            self.environmentalFactors_table.setItem(row_index, 3 + i, item)
        if data_saved['comment'] != '':
            WidgetConfig.create_comment(data_saved['comment'], row_index, self.environmentalFactors_table, config.COMMENT_IMG_GREEN)
            comment_item = QTableWidgetItem("")
            comment_item.setBackground(QColor(222, 255, 250))
            self.environmentalFactors_table.setItem(row_index, 6, comment_item)
        else:
            comment_item = QTableWidgetItem(" ")
            comment_item.setBackground(QColor(222, 255, 250))
            self.environmentalFactors_table.removeCellWidget(row_index, self.environmentalFactors_table.columnCount() - 1)
            self.environmentalFactors_table.setItem(row_index, 6, comment_item)

        self.ui.environmentalFactorsFactor_ComboBox.setCurrentIndex(-1)
        self.environmentalFactors_table.setSortingEnabled(True)
        self.environmentalFactors_table.scrollToItem(self.environmentalFactors_table.currentItem(), QAbstractItemView.PositionAtCenter)

    def update_environmental_factors_summary(self, factors_count):
        """
        Update the summary table with the environmental factors counts.

        Parameters
        ----------
        factors_count : dict
            Dictionary containing counts of environmental factors by relevance.
        """
        self.environmentalFactors_summary_table.item(0, 2).setText(str(factors_count['irrelevant']))
        self.environmentalFactors_summary_table.item(1, 2).setText(str(factors_count['medium']))
        self.environmentalFactors_summary_table.item(2, 2).setText(str(factors_count['essential']))

    def update_weights_limits(self, index):
        """
        Update the minimum and maximum limits of factor weights based on the selected factor in the QComboBox.

        Parameters
        ----------
        index : int
            The index of the selected item in the QComboBox.
        """
        limits = {
            0: (1.0, 2.0),
            1: (0.2, 0.8),
            2: (0.5, 1.5),
            3: (0.2, 0.8),
            4: (0.5, 1.5),
            5: (1.0, 2.5),
            6: (-1.5, -0.5),
            7: (-1.5, -0.5)
        }
        min_val, max_val = limits.get(index, (0.0, 0.0))
        self.ui.environmentalFactorsWeight_DoubleSpinBox.setRange(min_val, max_val)
