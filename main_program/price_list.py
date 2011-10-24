#!/usr/bin/python3
try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtSql import *
    
    from gui_interface_designs import price_list_window_generated
    from shared_modules.sql_statements import createMaterialsTable
    from shared_modules.sql_statements import insertMaterialsRecord
    from shared_modules.sql_statements import selectPrices
    from shared_modules.sql_statements import replaceMaterialsRecord
    from custom_widgets.addMaterialDialog import AddMaterialDialog
    from shared_modules.regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

__VERSION__ = "0.0"
__QT__ = "4.7.0"
__SIP__ = "4.12.4"
__PYQT__ = "4.8.5"
__PYTHON__ = "3.2.2"

class SqlQueryErrorCheck(object):
    def __init__(self, query):
        self.query = query
        
    def __enter__(self):
        return self.query
    
    def __exit__(self, eType, eValue, eTraceback):
        if eType == None:
            if not self.query.isActive():
                QMessageBox.warning(None, "Failed query",
                                    self.query.lastError().text())
        else:
            pass
    
class PopulateTableDirtyUpdate(object):
    def __init__(self, table):
        self.table = table
        
    def __enter__(self):
        return self.table
    
    def __exit__(self, eType, eValue, eTraceback):
        if eType == None:
            
        else:
            pass

class PriceListWindow(QMainWindow, price_list_window_generated.Ui_priceListWindow):

    def __init__(self, parent=None):
        super(PriceListWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Price List")
        
        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setPaperSize(QPrinter.A4)
        self.printer.setResolution(300)
        self.printer.setPageMargins(10.0, 10.0, 10.0, 10.0, QPrinter.Millimeter)
        
        self.screenRect = QDesktopWidget().geometry()
        
        self.move((self.screenRect.width() - self.width()) / 2,
                  (self.screenRect.height() - self.height()) / 2)
        
        self.connect(self.newMaterialButton, SIGNAL("clicked()"),
                     self.showAddMaterialDialog)
        
        self.connect(self.updateMaterialsButton, SIGNAL("clicked()"),
                     self.updateDatabase)
        
        self.tables = {"nonFerrous": self.nonFerrousTable,
                       "ferrous": self.ferrousTable}
        
        self.fields = ["material", "price"]
        
        self.databaseName = "test.db"
        
        self.openDatabase(self.databaseName)
        
        self.query = QSqlQuery()
        
        #self.createDatabase()
        
        self.query.prepare(replaceMaterialsRecord)
        
        self.query.bindValue(":material", "Iron")
        self.query.bindValue(":price", "2.00")
        self.query.bindValue(":ferrousFlag", "ferrous")
        
        with SqlQueryErrorCheck(self.query) as query:
            query.exec_()
        
        self.populateTable("nonFerrous")
        self.nonFerrousTable.dirty = False
        print(self.nonFerrousTable.isDirty())
    
    def populateTables(self):
        self.populateTable("nonFerrous")
        self.populateTable("ferrous")
        
    def openDatabase(self, name):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(name)
        if not db.open():
            QMessageBox.warning(None, "Test", db.lastError().text())
            sys.exit(1)
            
    def createDatabase(self):
        self.query.prepare(createMaterialsTable)
        
        with SqlQueryErrorCheck(self.query) as query:
            query.exec_()
            
    def showAddMaterialDialog(self):
        dialog = AddMaterialDialog()
        if dialog.exec_():
            if dialog.isValid():
                self.addMaterial(dialog.ferrousBox.itemData(dialog.ferrousBox.currentIndex()), "new",
                                 dialog.materialEdit.text(), "{:.2f}".format(Decimal(dialog.priceEdit.text())))
            else:
                QMessageBox.warning(None, "Attention",
                                    "Form was not vaild.")
        else:
            pass
            
    def addMaterial(self, ferrousFlag, newFlag, *immutables):
        table = self.tables[ferrousFlag]
        
        table.addRow()
            
        row = table.rowCount()-1
        
        table.setSortingEnabled(False)
        
        for field, value in enumerate(immutables):
            item = QTableWidgetItem(value)
            item.setData(Qt.UserRole, newFlag)
            item.setData(33, ferrousFlag)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            
            table.setItem(row, field, item)
        
        table.setValidatedCell(row, table.getHeaderIndex("New Price"),
                               regexObjects["qPrice"])
        
        if item.data(Qt.UserRole) == "new":
            table.cellWidget(row, table.getHeaderIndex("New Price")).setText(item.text())
            
        table.addDeleteButton(row, table.getHeaderIndex("Delete"))
        
        self.nonFerrousTable.resizeColumnToContents(table.getHeaderIndex("Material"))
        
        table.setSortingEnabled(True)
        
    def populateTable(self, ferrousFlag):
        table = self.tables[ferrousFlag]
        
        self.query.prepare(selectPrices)
        
        self.query.bindValue(":ferrousFlag", ferrousFlag)
        
        with SqlQueryErrorCheck(self.query) as query:
            query.exec_()
        
        table.clearContents()
        
        while self.query.next():
            values = []
            for field, value in enumerate(self.fields):
                values.append(str(self.query.value(field)))
                
            self.addMaterial(ferrousFlag, False, *values)
            
        self.nonFerrousTable.dirty = False
        self.ferrousTable.dirty = False
            
    def insertOrUpdate(self, material, price, ferrousFlag):
        self.query.prepare(replaceMaterialsRecord)
        
        self.query.bindValue(":material", material)
        self.query.bindValue(":price", price)
        self.query.bindValue(":ferrousFlag", ferrousFlag)
        
        with SqlQueryErrorCheck(self.query) as query:
            query.exec_()
            
    def updateDatabase(self):
        # need to check both tables
        table = self.tables["nonFerrous"]
        for row in range(table.rowCount()):
            widget = table.cellWidget(row, table.getHeaderIndex("New Price"))
            status = widget.validator().validate(widget.text(), 0)
            if table.item(row, 0).data(Qt.UserRole) == "new" or status[0] == 2:
                self.insertOrUpdate(table.item(row, table.getHeaderIndex("Material")).text(),
                                    table.cellWidget(row, table.getHeaderIndex("New Price")).text(),
                                    table.item(row, 0).data(33))
                
        self.populateTable("nonFerrous")
        self.nonFerrousTable.dirty = False

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = PriceListWindow()
    application.setOrganizationName("John Orchard & Company")
    application.setOrganizationDomain("orchard.com")
    application.setApplicationName("Orchard Price List")
    application.setApplicationVersion(__VERSION__)
    mainWindow.show()
    sys.exit(application.exec_())
