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
        
        self.customerCombobox = ExtendedComboBox()
        
        self.purchaseTable = CustomerTable()
        
        self.salesTable = CustomerTable()
        
        self.mainLayout = QVBoxLayout()
        
        self.mainLayout.addWidget(self.customerCombobox)
        
        self.setLayout(self.mainLayout)

    def populateTable(self):
        pass
