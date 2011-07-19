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
        
    @pyqtSlot()
    def onChange(self, x, y):
        if y ==2:
            values = [self.item(row, 2).text() for row in range(self.rowCount())]
            self.calculateTotalValue.emit(values)
        
    def setCurrentToEmptyRow(self):
        self.setCurrentCell(0, 0)
        startingColumn = 0
        
        for row in range(self.rowCount()):
            if self.item(row, startingColumn) == None:
                self.setCurrentCell(row, startingColumn)
                return
            
        self.insertRow(self.rowCount())
        self.setCurrentCell(self.rowCount()-1, startingColumn)