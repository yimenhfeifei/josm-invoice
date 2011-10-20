try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class ExtendedTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(ExtendedTableWidget, self).__init__(parent)

        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setSelectionMode(QTableWidget.SingleSelection)
        
        self.connect(self, SIGNAL("cellChanged(int, int)"),
                     self.changed)
        
        self.connect(self, SIGNAL("cellClicked(int, int)"),
                     self.tableClicked)
        
    def addDeleteButton(self, row, column):
        deleteItem = QTableWidgetItem("Delete")
        deleteItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        deleteItem.setTextColor(Qt.red)
        deleteItem.setFont(QFont("Monospace", weight=QFont.Bold))
        
        self.setItem(row, column, deleteItem)
        
    def getHeaderIndex(self, name):
        for columnIndex in range(self.columnCount()):
            if self.horizontalHeaderItem(columnIndex).text() == name:
                return columnIndex
        print("Couldn't find header.")
        
    def changed(self, cellRow, cellColumn):
        pass
    
    def deleteRow(self, row):
        self.selectRow(row)
        self.removeRow(row)
    
    def tableClicked(self, row, column):
        if column == self.getHeaderIndex("Delete"):
            self.deleteRow(row)
            
    def setValidatedCell(self, row, column, validator):
        edit = QLineEdit(self.viewport())
        
        edit.setValidator(validator)
        
        edit.setFrame(False)
        
        edit.setAlignment(Qt.AlignHCenter)
        
        self.setCellWidget(row, column, edit)
        
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
