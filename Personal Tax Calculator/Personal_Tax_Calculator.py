# ******************************************************************************************
# Description:
# Program calculates tax
# Usage limited to those aged below 65, no student loan, no marriage benefits, no savings
# or dividends benefits, not unique to any specific tax code, no child care vouchers
#
# To use, enter in basic salary and pick the frequency from the drop-down menu
# Click Calculate!
# Play around with additional tax-free allowances, pension, etc.
#
# GUI made using PyQt4
# exe made using PyInstaller
# ******************************************************************************************

# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'Tax Calculator.ui'
# Created by: PyQt4 UI code generator 4.11.4

import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_TaxCalculatorGUI(object):

    # Set up the main Gui
    def setupUi(self, TaxCalculatorGUI):

        TaxCalculatorGUI.setObjectName(_fromUtf8("TaxCalculatorGUI"))
        TaxCalculatorGUI.resize(380, 500)
        self.centralwidget = QtGui.QWidget(TaxCalculatorGUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.CheckApplicableBoxLabel = QtGui.QLabel(self.centralwidget)
        self.CheckApplicableBoxLabel.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.CheckApplicableBoxLabel.setObjectName(_fromUtf8("CheckApplicableBoxLabel"))

        self.AgeLabel = QtGui.QLabel(self.centralwidget)
        self.AgeLabel.setGeometry(QtCore.QRect(10, 40, 46, 20))
        self.AgeLabel.setObjectName(_fromUtf8("AgeLabel"))

        self.AllowancesDeductionsLabel = QtGui.QLabel(self.centralwidget)
        self.AllowancesDeductionsLabel.setGeometry(QtCore.QRect(10, 70, 120, 20))
        self.AllowancesDeductionsLabel.setObjectName(_fromUtf8("AllowancesDeductionsLabel"))

        self.AnnualPensionLabel = QtGui.QLabel(self.centralwidget)
        self.AnnualPensionLabel.setGeometry(QtCore.QRect(10, 100, 151, 20))
        self.AnnualPensionLabel.setObjectName(_fromUtf8("AnnualPensionLabel"))

        self.SalaryLabel = QtGui.QLabel(self.centralwidget)
        self.SalaryLabel.setGeometry(QtCore.QRect(10, 130, 91, 20))
        self.SalaryLabel.setObjectName(_fromUtf8("SalaryLabel"))

        self.SalaryGBPLabel = QtGui.QLabel(self.centralwidget)
        self.SalaryGBPLabel.setGeometry(QtCore.QRect(130, 130, 16, 20))
        self.SalaryGBPLabel.setObjectName(_fromUtf8("SalaryGBPLabel"))

        self.SalaryLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.SalaryLineEdit.setGeometry(QtCore.QRect(140, 130, 50, 20))
        self.SalaryLineEdit.setObjectName(_fromUtf8("SalaryLineEdit"))

        self.SalaryPerLabel = QtGui.QLabel(self.centralwidget)
        self.SalaryPerLabel.setGeometry(QtCore.QRect(200, 130, 20, 20))
        self.SalaryPerLabel.setObjectName(_fromUtf8("SalaryPerLabel"))

        self.SalaryComboBox = QtGui.QComboBox(self.centralwidget)
        self.SalaryComboBox.setGeometry(QtCore.QRect(230, 130, 140, 20))
        self.SalaryComboBox.setObjectName(_fromUtf8("SalaryComboBox"))
        self.SalaryComboBox.addItem(_fromUtf8(""))
        self.SalaryComboBox.addItem(_fromUtf8(""))
        self.SalaryComboBox.addItem(_fromUtf8(""))
        self.SalaryComboBox.addItem(_fromUtf8(""))
        self.SalaryComboBox.addItem(_fromUtf8(""))

        self.BlindCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.BlindCheckBox.setGeometry(QtCore.QRect(230, 10, 70, 20))
        self.BlindCheckBox.setObjectName(_fromUtf8("BlindCheckBox"))

        self.NoNICheckBox = QtGui.QCheckBox(self.centralwidget)
        self.NoNICheckBox.setGeometry(QtCore.QRect(290, 10, 81, 20))
        self.NoNICheckBox.setObjectName(_fromUtf8("NoNICheckBox"))

        self.AgeComboBox = QtGui.QComboBox(self.centralwidget)
        self.AgeComboBox.setGeometry(QtCore.QRect(230, 40, 140, 20))
        self.AgeComboBox.setObjectName(_fromUtf8("AgeComboBox"))
        self.AgeComboBox.addItem(_fromUtf8(""))

        self.AllowDeductLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.AllowDeductLineEdit.setGeometry(QtCore.QRect(230, 70, 140, 20))
        self.AllowDeductLineEdit.setObjectName(_fromUtf8("AllowDeductLineEdit"))
        self.AllowDeductLineEdit.setText(_fromUtf8("0"))

        self.PensionComboBox = QtGui.QComboBox(self.centralwidget)
        self.PensionComboBox.setGeometry(QtCore.QRect(230, 100, 40, 20))
        self.PensionComboBox.setObjectName(_fromUtf8("PensionComboBox"))
        self.PensionComboBox.addItem(_fromUtf8(""))
        self.PensionComboBox.addItem(_fromUtf8(""))

        self.PensionLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.PensionLineEdit.setGeometry(QtCore.QRect(280, 100, 90, 20))
        self.PensionLineEdit.setObjectName(_fromUtf8("PensionLineEdit"))
        self.PensionLineEdit.setText(_fromUtf8("0"))

        self.CalculateButton = QtGui.QPushButton(self.centralwidget)
        self.CalculateButton.setGeometry(QtCore.QRect(290, 160, 80, 20))
        self.CalculateButton.setObjectName(_fromUtf8("CalculateButton"))

        self.DisplayTaxTextBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.DisplayTaxTextBrowser.setGeometry(QtCore.QRect(10, 200, 360, 270))
        self.DisplayTaxTextBrowser.setObjectName(_fromUtf8("DisplayTaxTextBrowser"))

        TaxCalculatorGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TaxCalculatorGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        TaxCalculatorGUI.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(TaxCalculatorGUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TaxCalculatorGUI.setStatusBar(self.statusbar)

        self.retranslateUi(TaxCalculatorGUI)
        QtCore.QMetaObject.connectSlotsByName(TaxCalculatorGUI)

    # Define variables
    def retranslateUi(self, TaxCalculatorGUI):

        TaxCalculatorGUI.setWindowTitle(_translate("TaxCalculatorGUI", "Tax Calculator - 2018/2019", None))

        self.CheckApplicableBoxLabel.setText(_translate("TaxCalculatorGUI", "Check Applicable Box", None))

        self.AgeLabel.setText(_translate("TaxCalculatorGUI", "Age", None))

        self.AllowancesDeductionsLabel.setText(_translate("TaxCalculatorGUI", "Allowances/Deductions", None))

        self.AnnualPensionLabel.setText(_translate("TaxCalculatorGUI", "Annual Pension Contribution", None))

        self.SalaryLabel.setText(_translate("TaxCalculatorGUI", "Salary (Pre-Tax)", None))

        self.SalaryGBPLabel.setText(_translate("TaxCalculatorGUI", "£", None))

        self.SalaryPerLabel.setText(_translate("TaxCalculatorGUI", "per", None))

        self.SalaryComboBox.setItemText(0, _translate("TaxCalculatorGUI", "Year", None))
        self.SalaryComboBox.setItemText(1, _translate("TaxCalculatorGUI", "Month", None))
        self.SalaryComboBox.setItemText(2, _translate("TaxCalculatorGUI", "Week (52 Weeks/Year)", None))
        self.SalaryComboBox.setItemText(3, _translate("TaxCalculatorGUI", "Day (5 Days/Week)", None))
        self.SalaryComboBox.setItemText(4, _translate("TaxCalculatorGUI", "Hour (37.5 Hours/Week)", None))

        self.BlindCheckBox.setText(_translate("TaxCalculatorGUI", "Blind", None))
        self.NoNICheckBox.setText(_translate("TaxCalculatorGUI", "Don\'t Pay NI", None))

        self.AgeComboBox.setItemText(0, _translate("TaxCalculatorGUI", "Under 65", None))

        self.PensionComboBox.setItemText(0, _translate("TaxCalculatorGUI", "%", None))
        self.PensionComboBox.setItemText(1, _translate("TaxCalculatorGUI", "£", None))

        self.CalculateButton.setText(_translate("TaxCalculatorGUI", "Calculate!", None))
        self.CalculateButton.clicked.connect(self.CalculateTax)

    # Function to calculate tax on press of button
    def CalculateTax(self):

        # Initialise variables
        self.blindAllowance = 0
        self.NI = 0
        self.annualSalary = 0

        # Determine applicability of blind allowance
        if self.BlindCheckBox.checkState():
            self.blindAllowance = 2390

        # Interpret salary according to frequency of pay and convert to annual equivalent
        Frequency = str(self.SalaryComboBox.currentText())
        Amount = float(self.SalaryLineEdit.text())
        if Frequency == "Year":
            self.annualSalary = Amount
        elif Frequency == "Month":
            self.annualSalary = 12*Amount
        elif Frequency == "Week (52 Weeks/Year)":
            self.annualSalary = 52*Amount
        elif Frequency == "Day (5 Days/Week)":
            self.annualSalary = 260*Amount
        elif Frequency == "Hour (37.5 Hours/Week)":
            self.annualSalary = 260*7.5*Amount

        # Calculate National Insurance
        NILow = 8424
        NIHigh = 46384
        if self.NoNICheckBox.checkState():
            self.NI = 0
        elif self.annualSalary <= NILow:
            self.NI = 0
        elif self.annualSalary > NILow and self.annualSalary <= NIHigh:
            self.NI = 0.12*(self.annualSalary - NILow)
        elif self.annualSalary > NIHigh:
            self.NI = 0.12*(NIHigh-NILow) + 0.02*(self.annualSalary - NIHigh)

        # Interpret additional allowances/deductions
        taxFreeAllowance = float(self.AllowDeductLineEdit.text())

        # Determine if pension is taxable, and calculate
        if self.annualSalary > 40000:
            pensionLimit = 40000
        else:
            pensionLimit = self.annualSalary

        pensionType = str(self.PensionComboBox.currentText())
        if pensionType == "%":
            pension = float(self.PensionLineEdit.text())/100*self.annualSalary
        elif pensionType == "£":
            pension = float(self.PensionLineEdit.text())

        if pension > pensionLimit:
            pensionAllowance = pensionLimit
        if pension <= pensionLimit:
            pensionAllowance = pension

        # Adjust income to reflect pension contribution
        totalIncome = self.annualSalary
        adjustedIncome = totalIncome - pensionAllowance

        # Personal allowance
        standardPersonalAllowance = 11850
        if adjustedIncome <= 100000:
            standardPersonalAllowance = standardPersonalAllowance
        elif adjustedIncome > 100000 and adjustedIncome <= 123700:
            standardPersonalAllowance = standardPersonalAllowance - (adjustedIncome - 100000)/2
        elif adjustedIncome > 123700:
            standardPersonalAllowance = 0
        personalAllowance = standardPersonalAllowance + self.blindAllowance + taxFreeAllowance

        # Calculate taxable income
        taxableIncome = adjustedIncome - personalAllowance

        # Calculate PAYE tax
        tax = 0
        if taxableIncome > 150000:
            tax = 0.45 * (taxableIncome - 150000)
            taxableIncome = 150000
        if taxableIncome > 34500:
            tax = tax + 0.4 * (taxableIncome - 34500)
            taxableIncome = 34500
        if taxableIncome > 0:
            tax = tax + 0.2 * taxableIncome
        taxableIncome = adjustedIncome - personalAllowance

        if taxableIncome <= 0:
            tax = 0
            taxableIncome = 0

        totalTax = self.NI + tax
        netPay = self.annualSalary - totalTax - pension

        # Display results
        if self.blindAllowance != 0:
            self.DisplayTaxTextBrowser.append("Blind Allowance: £{:.2f}".format(self.blindAllowance))
        self.DisplayTaxTextBrowser.append("Annual Salary: £{:.2f}".format(self.annualSalary))
        self.DisplayTaxTextBrowser.append("Annual Tax Free Allowance: £{:.2f}".format(personalAllowance))
        self.DisplayTaxTextBrowser.append("Annual Total Taxable Income: £{:.2f}".format(taxableIncome))
        self.DisplayTaxTextBrowser.append("Annual PAYE Tax: £{:.2f}".format(tax))
        self.DisplayTaxTextBrowser.append("Annual National Insurance: £{:.2f}".format(self.NI))
        self.DisplayTaxTextBrowser.append("Annual Pension Contribution: £{:.2f}".format(pension))
        self.DisplayTaxTextBrowser.append("Total Annual Deductions: £{:.2f}".format(tax + self.NI + pension))
        self.DisplayTaxTextBrowser.append("Total Annual Net Pay: £{:.2f}".format(netPay))
        self.DisplayTaxTextBrowser.append("")
        if self.blindAllowance != 0:
            self.DisplayTaxTextBrowser.append("Monthly Blind Allowance: £{:.2f}".format(self.blindAllowance/12))
        self.DisplayTaxTextBrowser.append("Monthly Salary: £{:.2f}".format(self.annualSalary/12))
        self.DisplayTaxTextBrowser.append("Monthly Tax Free Allowance: £{:.2f}".format(personalAllowance/12))
        self.DisplayTaxTextBrowser.append("Monthly Taxable Income: £{:.2f}".format(taxableIncome/12))
        self.DisplayTaxTextBrowser.append("Monthly PAYE Tax: £{:.2f}".format(tax/12))
        self.DisplayTaxTextBrowser.append("Monthly National Insurance: £{:.2f}".format(self.NI/12))
        self.DisplayTaxTextBrowser.append("Monthly Pension Contribution: £{:.2f}".format(pension/12))
        self.DisplayTaxTextBrowser.append("Total Monthly Deductions: £{:.2f}".format((tax + self.NI + pension)/12))
        self.DisplayTaxTextBrowser.append("Total Monthly Net Pay: £{:.2f}".format(netPay/12))
        self.DisplayTaxTextBrowser.append("")

# Run GUI class
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TaxCalculatorGUI = QtGui.QMainWindow()
    ui = Ui_TaxCalculatorGUI()
    ui.setupUi(TaxCalculatorGUI)
    TaxCalculatorGUI.show()
    sys.exit(app.exec_())

