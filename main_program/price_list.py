#!/usr/bin/python3
try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import price_list_window_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

__VERSION__ = "0.0"
__QT__ = "4.7.0"
__SIP__ = "4.12.4"
__PYQT__ = "4.8.5"
__PYTHON__ = "3.2.2"

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
        
        
        self.prices = [("Gold", "90.00"),
                       ("Steel", "10.00"),
                       ("Copper", "60.00")]
        
        self.populateNonFerrousTable()
        
    def populateNonFerrousTable(self):
        self.nonFerrousTable.setHorizontalHeaderLabels(["Current Price", "New Price"])
        validator = QRegExpValidator(QRegExp("\d"), self)
        
        for material, price in self.prices:
            self.nonFerrousTable.setCurrentToEmptyRow()
        
            row = self.nonFerrousTable.currentRow()
        
            self.nonFerrousTable.setVerticalHeaderItem(row, QTableWidgetItem(material))
            
            item = QTableWidgetItem(price)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.nonFerrousTable.setItem(row, 0, item)
        
            edit = QLineEdit(self.nonFerrousTable.viewport())
        
            edit.setValidator(validator)
        
            edit.setFrame(False)
        
            edit.setAlignment(Qt.AlignHCenter)
        
            self.nonFerrousTable.setCellWidget(row, 1, edit)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = PriceListWindow()
    application.setOrganizationName("John Orchard & Company")
    application.setOrganizationDomain("orchard.com")
    application.setApplicationName("Orchard Price List")
    application.setApplicationVersion(__VERSION__)
    mainWindow.show()
    sys.exit(application.exec_())
