try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class PayloadTableWidget(QTableWidget):
    
    calculateTotalValue = pyqtSignal(list)
    
    def __init__(self, parent=None):
        super(PayloadTableWidget, self).__init__(parent)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setSelectionMode(QTableWidget.SingleSelection)
        
        self.weightColumn = 0
        self.materialColumn = 1
        self.valueColumn = 2
        self.deleteColumn = 3
        
    def getWeightColumn(self):
        return self.weightColumn
    
    def getMaterialColumn(self):
        return self.materialColumn
    
    def getValueColumn(self):
        return self.valueColumn
    
    def getDeleteColumn(self):
        return self.deleteColumn
        
    @pyqtSlot()
    def onChange(self, cellRow, cellColumn):
        if cellColumn == (self.columnCount() - 2):
            cellValues = [self.item(row, (self.columnCount() - 2)).text() 
                      for row in range(self.rowCount())]
            self.calculateTotalValue.emit(cellValues)
        
    def setCurrentToEmptyRow(self):
        self.setCurrentCell(0, 0)
        startingColumn = 0
        
        for row in range(self.rowCount()):
            if self.item(row, startingColumn) == None:
                self.setCurrentCell(row, startingColumn)
                return
            
        self.insertRow(self.rowCount())
        self.setCurrentCell((self.rowCount() - 1), startingColumn)
        
    def getValidatedStatus(self):
        if self.item(0, 0) == None:
            return False
        else:
            return True
