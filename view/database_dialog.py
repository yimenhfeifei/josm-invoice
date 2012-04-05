#!/usr/bin/python3
try:
    import traceback
    import sys

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

    from view.customerTable import CustomerTable
    from database_mapper import Database

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)


class DatabaseDialog(QDialog):

    def __init__(self, parent=None):
        super(DatabaseDialog, self).__init__(parent)

        self.resize(550, 500)

        self.table = CustomerTable()
        self.table.setSortingEnabled(False)
        self.table.setWordWrap(True)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.horizontalHeader().setSortIndicatorShown(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setDefaultSectionSize(120)
        self.table.horizontalHeader().setMinimumSectionSize(100)
        self.table.verticalHeader().setMinimumSectionSize(50)

        self.addButton = QPushButton("Add Customer")

        self.database = Database("customers.csv")

        self.mainLayout = QVBoxLayout()

        self.widgetLayout = QVBoxLayout()

        self.widgetLayout.addWidget(self.addButton)

        self.widgetLayout.addWidget(self.table)

        self.mainLayout.addLayout(self.widgetLayout)

        self.setLayout(self.mainLayout)

        self.populateTable()

        self.connect(self.addButton, SIGNAL("clicked()"),
                     self.addRecord)

        self.connect(self.table, SIGNAL("cellClicked(int, int)"),
                     self.onCellClicked)

        self.connect(self.table, SIGNAL("cellChanged(int, int)"),
                     self.onCellChanged)

    def addRecord(self):
        self.table.appendRow()
        row = self.table.rowCount() - 1
        self.table.setCurrentCell(row, 0)

    def onCellClicked(self, row, column):
        if column == self.table.getHeaderIndex("Delete"):
            self.table.removeRow(row)

    def onCellChanged(self, row, column):
        self.table.setDirty()

    def saveRecords(self):
        self.database.saveRecords(self.table.getRows(3))

    def promptToSave(self):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setWindowTitle("The database has been changed")
        messageBox.setText("Do you want to save the changes?")
        messageBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard |
                                      QMessageBox.Cancel)

        ret = messageBox.exec_()

        if ret == QMessageBox.Cancel:
            return False
        elif ret == QMessageBox.Save:
            self.saveRecords()

        return True

    def isTableModified(self):
        return self.table.isDirty()

    def reject(self):
        if self.isTableModified():
            if self.promptToSave():
                self.accept()
        else:
            self.accept()

    def populateTable(self):
        self.table.removeAllRows()

        for record in self.database.loadRecords():
            self.table.appendRow()
            row = self.table.rowCount() - 1

            for i, column in enumerate(record):
                self.table.setItem(row, i, QTableWidgetItem(column))

            self.table.addDeleteCell(row, 3)

        self.table.resizeRowsToContents()
        self.table.setClean()
