#!/usr/bin/python3
try:
    import traceback
    import sys
    from decimal import getcontext
    from decimal import Decimal
    from decimal import ROUND_HALF_UP
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

    from view.extendedTableWidget import ExtendedTableWidget
except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)

class InvoiceTable(ExtendedTableWidget):

    updateTicketTotal = pyqtSignal()

    def __init__(self, parent=None):
        super(InvoiceTable, self).__init__(parent)
        
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setSelectionMode(QTableWidget.SingleSelection)
        
        self.connect(self, SIGNAL("cellChanged(int, int)"),
                     self.changed)
        
        getcontext().rounding = ROUND_HALF_UP
        
        self.setColumnCount(4)
        
        self.setHorizontalHeaderLabels(["Description",
                                        "Weight",
                                        "Price Per Unit",
                                        "Value"])
        
    def getTotal(self):
        cellValues = [Decimal(self.item(row, self.valueColumn).text()) 
                      for row in range(self.rowCount())]
            
        total = sum(cellValues)
        total = total.to_integral() + Decimal(".00")
            
        return total
            
    def changed(self, cellRow, cellColumn):
        if cellColumn == (self.getHeaderIndex("Value")):
            self.updateTicketTotal.emit()

    def isValid(self):
        if self.item(0, 0) == None:
            return False
        else:
            return True
