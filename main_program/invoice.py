#!/usr/bin/python3
try:
    import sys
    from decimal import Decimal
    from datetime import datetime
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import invoice_window_generated
    from custom_widgets.invoiceReviewDialog import InvoiceReviewDialog
    from business_customers import customers
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

__VERSION__ = "0.1"
__QT__ = "4.7.0"
__SIP__ = "4.12.4"
__PYQT__ = "4.8.5"
__PYTHON__ = "3.2.2"

class InvoiceWindow(QMainWindow, invoice_window_generated.Ui_invoiceWindow):

    def __init__(self, parent=None):
        super(InvoiceWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Invoice")
        
        self.screenRect = QDesktopWidget().geometry()
        
        self.move((self.screenRect.width() - self.width()) / 2,
                  (self.screenRect.height() - self.height()) / 2)
        
        self.populateCustomerBox(customers)
        
        self.number = self.getInvoiceNumber()
        
        self.validating = [self.descriptionEdit,
                           self.weightEdit,
                           self.pricePerTonneEdit,
                           self.valueEdit,
                           self.vatEdit]
        
        self.payloadTableWidget.setHorizontalHeaderLabels(["Description",
                                                           "Weight",
                                                           "Price Per Tonne",
                                                           "Value",
                                                           "Delete"])
        
        self.deleteColumn = 4
        
        for widget in self.validating:
            self.connect(widget, SIGNAL("textChanged(QString)"),
                         self.changed)
            
        self.connect(self.addButton, SIGNAL("clicked()"),
                     self.addPayload)
        
        self.connect(self.payloadTableWidget, SIGNAL("cellClicked(int, int)"),
                     self.payloadTableClicked)
        
        self.connect(self.reviewButton, SIGNAL("clicked()"),
                     self.createInvoiceReview)
        
        self.connect(self.pricePerTonneEdit, SIGNAL("returnPressed()"),
                     self.addPayload)
        
        self.changed()
        
        self.descriptionEdit.setFocus()
        
    def getInvoiceNumber(self):
        return [line for line in open("invoice_number.txt", "r")][0]
    
    def getInvoiceVatRate(self):
        return self.vatEdit.text()
        
    def populateCustomerBox(self, customers):
        for index, name in enumerate(customers.keys()):
            self.customerCombobox.insertItem(index, name)
        
    def payloadTableClicked(self, row, column):
        if column == self.deleteColumn:
            self.payloadTableWidget.selectRow(row)
            self.payloadTableWidget.removeRow(row)
        
    def changed(self):
        for widget in self.validating:
            widget.validate()
            
        if self.weightEdit.isValid() and self.pricePerTonneEdit.isValid():
            self.calculateValue()
        else:
            self.valueEdit.clear()
    
    def calculateValue(self):
        weight = Decimal(self.weightEdit.text()) / Decimal("1000.00")
        pricePerUnit = Decimal(self.pricePerTonneEdit.text())
        self.valueEdit.setText("{:.2f}".format(weight * pricePerUnit))
        
    def allValid(self):
        for widget in self.validating:
            if not widget.isValid():
                return False
        return True
        
    def addPayload(self):
        if self.allValid(): 
            self.addRow(self.descriptionEdit.text(),
                        "{:.2f}".format(Decimal(self.weightEdit.text())),
                        "{:.2f}".format(Decimal(self.pricePerTonneEdit.text())),
                        self.valueEdit.text())
            
            self.resetForm()
        else:
            QMessageBox.warning(self, "Attention", "All fields must be valid!")
            
    def addRow(self, *args):
        self.payloadTableWidget.setCurrentToEmptyRow()
        
        row = self.payloadTableWidget.currentRow()
        
        for column, value in enumerate(args):
            item = QTableWidgetItem(value)
        
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
            self.payloadTableWidget.setItem(row, column, item)
            
        self.addDeleteButton(row)
            
    def addDeleteButton(self, row):
        deleteItem = QTableWidgetItem("Delete")
        deleteItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        deleteItem.setTextColor(Qt.red)
        deleteItem.setFont(QFont("Monospace", weight=QFont.Bold))
        
        self.payloadTableWidget.setItem(row, self.deleteColumn, deleteItem)
        
    def getInvoiceDetails(self):
        return {"number": self.number,
                "date": datetime.now().strftime("%Y/%m/%d"),
                "name": self.customerCombobox.currentText(),
                "vatRate": self.getInvoiceVatRate(),
                "payloadTotal": str(self.getPayloadTotal()),
                "vatTotal": "{:.2f}".format(self.getVatTotal()),
                "grandTotal": "{:.2f}".format(self.getGrandTotal())}
    
    def getPayloadTotal(self):
        values = []
        for row in range(self.payloadTableWidget.rowCount()):
            values.append(Decimal(self.payloadTableWidget.item(row, self.deleteColumn-1).text()))
            
        return sum(values)
    
    def getVatTotal(self):
        print(self.getInvoiceVatRate())
        return self.getPayloadTotal() * (Decimal(self.getInvoiceVatRate()) / 100)
    
    def getGrandTotal(self):
        return self.getPayloadTotal() + self.getVatTotal()
        
    def getPayloads(self):
        payloads = {}
        table = self.payloadTableWidget
        
        for row in range(table.rowCount()):
            fields = []
            for column in range(table.columnCount() - 1):
                fields.append(table.item(row, column).text())
                
            payloads["payload {}".format(row)] = {"description": fields[0],
                                                  "weight": fields[1],
                                                  "ppu": fields[2],
                                                  "value": fields[3]}
        return payloads
    
    def createInvoiceReview(self):
        if self.payloadTableWidget.isValid():
            self.generateInvoice()
        else:
            QMessageBox.warning(self, "Attention", "No payloads to review!")
            
    def generateInvoice(self):
        #if InvoiceReviewDialog(self.getInvoiceDetails(),
                               #self.getPayloads()).exec_():
            #f = open("invoice_number.txt", "w")
            #f.seek(0)
            #self.number = str(int(self.number) + 1)
            
            #f.write(self.number)
            
        #self.descriptionEdit.setFocus()
        
        p = QPrinter(QPrinter.HighResolution)
        p.setPaperSize(QPrinter.A5)
        
        pp = QPrintPreviewDialog(p, self)
        self.connect(pp, SIGNAL("paintRequested(QPrinter*)"),
                     self.printIt)
        pp.exec_()
        
    def printIt(self, printer):
        painter = QPainter(printer)
        
        inv = InvoiceReviewDialog(self.getInvoiceDetails(), self.getPayloads())
        
        image = QPixmap.grabWidget(inv, inv.rect())
        
        inv.reject()
        
        image = image.scaled(printer.pageRect().width(),
                             printer.pageRect().height(),
                             Qt.KeepAspectRatio)
        
        painter.begin(self)
        painter.drawPixmap(0, 0, image)
        painter.end()
        printer.newPage()
            
    def resetForm(self):
        value = self.vatEdit.text()
        for widget in self.validating:
            widget.clear()
        self.vatEdit.setText(value)
        self.descriptionEdit.setFocus()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = InvoiceWindow()
    application.setOrganizationName("John Orchard & Company")
    application.setOrganizationDomain("orchard.com")
    application.setApplicationName("Orchard Suite")
    application.setApplicationVersion(__VERSION__)
    mainWindow.show()
    application.exec_()
    