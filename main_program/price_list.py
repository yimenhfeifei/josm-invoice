#!/usr/bin/python3
try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtSql import *
    
    from gui_interface_designs import price_list_window_generated
    from shared_modules.sql_statements import createMaterialsTable
    from shared_modules.sql_statements import insertMaterialsRecord
    from shared_modules.sql_statements import selectPrices
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
        
        self.databaseName = "test.db"
        
        
        self.prices = [("Gold", "90.00"),
                       ("Steel", "10.00"),
                       ("Copper", "60.00")]
        
        self.openDatabase(self.databaseName)
        
        self.query = QSqlQuery()
        
        with SqlQueryErrorCheck(self.query) as query:
            query.exec_("REPLACE INTO materials VALUES ('Wire', '6.00', 'false')")
        
        self.populateTable(self.nonFerrousTable, "false")
        
        self.query.prepare(createMaterialsTable)
        
        self.query.exec_()
        
        self.query.prepare(insertMaterialsRecord)
        
        self.query.bindValue(":material", "Iron")
        self.query.bindValue(":price", "2.00")
        self.query.bindValue(":ferrous", "true")
        
        self.query.exec_()
        
    def openDatabase(self, name):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(name)
        if not db.open():
            QMessageBox.warning(None, "Test", db.lastError().text())
            sys.exit(1)
        
    def populateTable(self, table, ferrousBool):
        priceValidator = QRegExpValidator(QRegExp(r"^\d{1,5}(\.\d{1,2})?$"), self)
        
        fields = ["material", "price"]
        
        self.query.prepare(selectPrices)
        
        self.query.bindValue(":ferrousBool", ferrousBool)
        
        self.query.exec_()
        
        if not self.query.isActive():
            QMessageBox.warning(None, "Failed select", self.query.lastError().text())
        
        table.clearContents()
        
        while self.query.next():
            table.addRow()
            
            row = table.currentRow()
            
            for field, value in enumerate(fields):
                item = QTableWidgetItem(str(self.query.value(field)))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                table.setItem(row, field, item)
                
            table.setValidatedCell(row, table.getHeaderIndex("New Price"), priceValidator)
            
            table.addDeleteButton(row, table.getHeaderIndex("Delete"))
            
        table.selectRow(0)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = PriceListWindow()
    application.setOrganizationName("John Orchard & Company")
    application.setOrganizationDomain("orchard.com")
    application.setApplicationName("Orchard Price List")
    application.setApplicationVersion(__VERSION__)
    mainWindow.show()
    sys.exit(application.exec_())
