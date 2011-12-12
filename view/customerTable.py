#!/usr/bin/python3
try:
    import traceback
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *    

    from shared_modules.extendedTableWidget import ExtendedTableWidget
except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)

class CustomerTable(ExtendedTableWidget):
    
    def __init__(self, parent=None):
        super(ExtendedTableWidget, self).__init__(parent)
        
        self.dirty = False
        
        self.setColumnCount(4)
                
        self.setHorizontalHeaderLabels(["Name",
                                        "Address",
                                        "Vat Reg",
                                        "Delete"])
        
        self.connect(self, SIGNAL("cellClicked(int, int)"),
                     self.onCellClicked)
        
    def onCellClicked(self, row, column):
        if column == self.getHeaderIndex("Delete"):
            self.removeRow(row)

