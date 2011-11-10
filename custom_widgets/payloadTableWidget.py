try:
    import sys
    import decimal
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class PayloadTableWidget(QTableWidget):
    
    updateTicketTotal = pyqtSignal()

    def __init__(self, parent=None):
        super(PayloadTableWidget, self).__init__(parent)

        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setSelectionMode(QTableWidget.SingleSelection)
        
        self.weightColumn = 0
        self.materialColumn = 1
        self.valueColumn = 2
        self.deleteColumn = 3
        
        self.connect(self, SIGNAL("cellChanged(int, int)"),
                     self.changed)
        
        decimal.getcontext().rounding = decimal.ROUND_HALF_UP
        
    def getWeightColumn(self):
        return self.weightColumn
    
    def getMaterialColumn(self):
        return self.materialColumn
    
    def getValueColumn(self):
        return self.valueColumn
    
    def getDeleteColumn(self):
        return self.deleteColumn
    
    def getTotal(self):
        cellValues = [Decimal(self.item(row, self.valueColumn).text()) 
                      for row in range(self.rowCount())]
        
        total = sum(cellValues)
        total = total.to_integral() + Decimal(".00")
        
        return total
        
    def changed(self, cellRow, cellColumn):
        if cellColumn == (self.valueColumn):
            self.updateTicketTotal.emit()
        
    def setCurrentToEmptyRow(self):
        self.setCurrentCell(0, 0)
        startingColumn = 0
        
        for row in range(self.rowCount()):
            if self.item(row, startingColumn) == None:
                self.setCurrentCell(row, startingColumn)
                return
            
        self.insertRow(self.rowCount())
        self.setCurrentCell((self.rowCount() - 1), startingColumn)
        
    def isValid(self):
        if self.item(0, 0) == None:
            return False
        else:
            return True
        
    def reset(self):
        for row in [i for i in range(self.rowCount())][::-1]:
            self.removeRow(row)
