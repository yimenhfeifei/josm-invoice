#!/usr/bin/python3
try:
    import traceback
    import sys

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from view.customerTable import CustomerTable
    from database_mapper import Database
    from database_mapper import PurchaseCustomer
    from database_mapper import SalesCustomer
    from shared_modules.extendedCombobox import ExtendedComboBox

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
        
        self.database = Database("invoice_data.db", "sqlite")
        
        self.customerCombobox = ExtendedComboBox(self)
        
        self.recordTypes = {"Purchase Customers": PurchaseCustomer,
                            "Sales Customers": SalesCustomer}
        
        self.customerCombobox.populate(list(self.recordTypes.keys()))
        
        self.mainLayout = QVBoxLayout()
        
        self.widgetLayout = QVBoxLayout()
        
        self.widgetLayout.addWidget(self.customerCombobox)
        
        self.widgetLayout.addWidget(self.table)
        
        self.mainLayout.addLayout(self.widgetLayout)
        
        self.setLayout(self.mainLayout)
        
        self.populateTable()
        
        self.connect(self.customerCombobox, SIGNAL("currentIndexChanged(QString)"),
                     self.populateTable)
        
        self.connect(self.table, SIGNAL("cellChanged(int, int)"),
                     self.table.setDirty)
        
        self.connect(self.table, SIGNAL("cellChanged(int, int)"),
                     self.onCellChanged)
        
        self.connect(self.table, SIGNAL("cellClicked(int, int)"),
                     self.onCellClicked)
        
    def getRowId(self, row):
        return self.table.item(row, 0).data(Qt.UserRole)

    def onCellClicked(self, row, column):
        if column == self.table.getHeaderIndex("Delete"):
            rowId = self.getRowId(row)
            self.table.removeRow(row)
       
    def onCellChanged(self, row, column):
        cId = self.getRowId(row)
        
        if cId == None:
            return
        
        cType = self.recordTypes[self.customerCombobox.currentText()]
        customer = self.database.session.query(cType).filter_by(id=cId).first()
        
        if column == self.table.getHeaderIndex("Name"):
            customer.name = self.table.item(row, column).text()
        elif column == self.table.getHeaderIndex("Address"):
            customer.address = self.table.item(row, column).text()
        elif column == self.table.getHeaderIndex("Vat Reg"):
            customer.vatReg = self.table.item(row, column).text()
        
        print(self.database.session.dirty)

    def promptToSave(self):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setWindowTitle("The database has been changed")
        messageBox.setText("Do you want to save the changes?")
        messageBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
                    
        if messageBox.exec_() == QMessageBox.Save:
            self.database.persist()
        else:
            for obj in self.database.session.dirty:
                self.database.session.expire(obj)
        
    def reject(self):
        if self.table.isDirty():
            self.promptToSave()

        self.accept()

    def populateTable(self):
        if self.table.isDirty():
            self.promptToSave()
        
        self.table.removeAllRows()
        
        currentType = self.customerCombobox.currentText()
        
        customers = self.database.session.query(self.recordTypes[currentType]).all()
        
        for customer in customers:
            self.table.appendRow()
            row = self.table.rowCount() - 1
            self.table.setItem(row, 0, QTableWidgetItem(customer.name))
            self.table.item(row, 0).setData(Qt.UserRole, customer.id)
            self.table.setItem(row, 1, QTableWidgetItem(customer.address))
            self.table.setItem(row, 2, QTableWidgetItem(customer.vatReg))
                        
            self.table.addDeleteCell(row, 3)

        self.table.resizeRowsToContents()
        self.table.setClean()
