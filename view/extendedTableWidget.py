#!/usr/bin/python3
try:
    import traceback
    import sys

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)

class ExtendedTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(ExtendedTableWidget, self).__init__(parent)

        self.dirty = False
        self.columnDirtyCheck = []      

    def isDirty(self):
        return self.dirty

    def setDirty(self):
        self.dirty = True
        
    def setClean(self):
        self.dirty = False

    def setColumnDirtyCheck(self, column):
        self.columnDirtyCheck.append(column)

    def addDeleteCell(self, row, column, text="Delete", colour=Qt.red,
                        font=QFont("Monospace", weight=QFont.Bold),
                        alignment=Qt.AlignHCenter | Qt.AlignVCenter):

        deleteItem = QTableWidgetItem(text)
        deleteItem.setTextAlignment(alignment)

        deleteItem.setTextColor(colour)
        deleteItem.setFont(font)

        self.setItem(row, column, deleteItem)

        self.setHorizontalHeaderItem(column, QTableWidgetItem(text))
        
    def getHorizontalHeaders(self):
        return [self.horizontalHeaderItem(index).text()
                for index in range(self.columnCount())]

    def getHeaderIndex(self, name):
        headers = self.getHorizontalHeaders()

        try:
            return headers.index(name)
        except ValueError:
            print("Coun't find {} in table column headers.".format(name))
            
    def getHeaderName(self, index):
        headers = self.getHorizontalHeaders()
        
        try:
            return headers[index]
        except IndexError:
            print("Couldn't find {} in table column headers.".format(index))

    def appendRow(self):
        self.insertRow(self.rowCount())
        self.setDirty()

    def removeRow(self, row):
        super(ExtendedTableWidget, self).removeRow(row)
        self.setDirty()

    def removeAllRows(self):
        for row in [i for i in range(self.rowCount())][::-1]:
            self.removeRow(row)
        self.setDirty()

    def setValidatedCell(self, row, column, validator,
                         alignment=Qt.AlignHCenter):

        edit = QLineEdit(self.viewport())

        edit.setValidator(validator)

        edit.setFrame(False)

        edit.setAlignment(alignment)

        self.setCellWidget(row, column, edit)

        if column in self.columnDirtyCheck:
            self.setDirty()
            
    def getRows(self, colEnd, ColStart=0):
        return [[self.item(row, column).text()
                 for column in range(ColStart, colEnd)
                 if self.item(row, column) != None]
                for row in range(self.rowCount())]

    def getContents(self):
        rows = {}
        for row in range(self.rowCount()):
            columnValues = {}
            for column in range(self.columnCount()):
                columnValues[self.horizontalHeaderItem(column).text()] = self.item(row, column).text()
            rows["row {}".format(row)] = columnValues
        return rows
