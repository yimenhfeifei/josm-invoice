#!/usr/bin/python3
try:
    import traceback
    import sys

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from view.customerTable import CustomerTable
    from database_mapper import Database
    from shared_modules.extendedCombobox import ExtendedComboBox

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)


class DatabaseDialog(QDialog):

    def __init__(self, parent=None):
        super(DatabaseDialog, self).__init__(parent)
        
        self.resize(600, 700)
        
        self.table = CustomerTable()
        self.table.setSortingEnabled(True)
        self.table.setWordWrap(True)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setMinimumSectionSize(45)
        
        self.database = Database("invoice_data.db", "sqlite")
        
        self.customerCombobox = ExtendedComboBox(self)
        
        self.customerTypes = {"Purchase Customers": self.database.getPurchaseCustomersDict,
                              "Sales Customers": self.database.getSalesCustomersDict}
        
        self.customerCombobox.populate(list(self.customerTypes.keys()))
        
        self.mainLayout = QVBoxLayout()
        
        self.widgetLayout = QVBoxLayout()
        
        self.widgetLayout.addWidget(self.customerCombobox)
        
        self.widgetLayout.addWidget(self.table)
        
        self.mainLayout.addLayout(self.widgetLayout)
        
        self.setLayout(self.mainLayout)
        
        self.populateTable()
        
        self.table.resizeColumnsToContents()
        
        self.connect(self.customerCombobox, SIGNAL("currentIndexChanged(QString)"),
                     self.populateTable)
        
        self.connect(self.table, SIGNAL("cellChanged(int,int)"),
                     self.table.setDirty)
    def promptToSave(self):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setWindowTitle("The database has been changed")
        messageBox.setText("Do you want to save the changes?")
        messageBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
                    
        if messageBox.exec_() == QMessageBox.Save:
            return True
        else:
            return False      

    def populateTable(self):
        if self.table.isDirty():
            if self.promptToSave():
                print("saving")
            else:
                print("discarding")

        # Sorting is disabled temporarily to avoid row mixups when sorting.
        self.table.setSortingEnabled(False)
        
        self.table.removeAllRows()
        customers = self.customerTypes[self.customerCombobox.currentText()]()
        for name, dictionary in customers.items():
            self.table.appendRow()
            row = self.table.rowCount() - 1
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(dictionary["address"]))
            self.table.setItem(row, 2, QTableWidgetItem(dictionary["vatReg"]))
            
            self.table.addDeleteCell(row, 3)
        
        self.table.setSortingEnabled(True)
        self.table.setClean()
