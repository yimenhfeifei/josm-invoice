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
        
        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setPaperSize(QPrinter.A4)
        self.printer.setResolution(300)
        
        self.fontScale = self.printer.resolution() / 96
        
        self.screenRect = QDesktopWidget().geometry()
        
        self.move((self.screenRect.width() - self.width()) / 2,
                  (self.screenRect.height() - self.height()) / 2)
        
        self.populateCustomerBox(customers)
        
        self.populateTypeBox("Purchase", "Sales")
        
        self.startingNumber = self.getInvoiceNumber()
        
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
                     self.printPreview)
        
        self.connect(self.pricePerTonneEdit, SIGNAL("returnPressed()"),
                     self.addPayload)
        
        self.changed()
        
        self.descriptionEdit.setFocus()
        
    def getInvoiceNumber(self):
        return [line for line in open("invoice_number.txt", "r")][0]
    
    def getInvoiceVatRate(self):
        return self.vatEdit.text()
    
    def populateTypeBox(self, *types):
        for index, name in enumerate(types):
            self.typeCombobox.insertItem(index, name + " Invoice")
        
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
        return {"number": self.startingNumber,
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
    
    def getVatTotal(self, amount):
        return amount * (Decimal(self.getInvoiceVatRate()) / 100)
    
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
    
        
    def generateStatements(self):
        statements = {}
        
        payloads = []
        payloadGroups = list(self.getPayloads().values())
        groupSize = 15
        payloads = [payloadGroups[n:n+groupSize] for n, i in enumerate(payloadGroups) if n % groupSize == 0]
        
        for num, batch in enumerate(payloads):
            payloadTotal = sum([Decimal(i["value"]) for i in batch])
            vatTotal = self.getVatTotal(payloadTotal)
            grandTotal = "{:.2f}".format(payloadTotal + vatTotal)
    
            statements["statement {}".format(num)] = {"number": str(int(self.startingNumber) + num),
                                                      "payloadTotal": "{:.2f}".format(payloadTotal),
                                                      "vatTotal": "{:.2f}".format(vatTotal),
                                                      "grandTotal": grandTotal,
                                                      "batch": batch}
        
        
            
        return statements
            
    def printPreview(self):
        previewDialog = QPrintPreviewDialog(self.printer, self)
        
        self.connect(previewDialog, SIGNAL("paintRequested(QPrinter*)"),
                     self.paintInvoice)
        
        previewDialog.exec_()
        
    def paintLetterHead(self, painter, pageRect):
        letterHead = [("John Orchard and Company", QFont("Helvetica", 14, weight=QFont.Bold)),
                      ("Scrap Metal Merchants", QFont("Helvetica", 10, weight=QFont.Bold)),
                      ("Chosen View, United Road, St Day, TR16 5HT", QFont("Helvetica", 12, weight=QFont.Bold)),
                      ("WML: 20659 TEL.: (01209)820313 FAX: (01209)822512 WCL: 169171", QFont("Helvetica", 10, weight=QFont.Bold)),
                      ("VAT Registration number: 1319249 76", QFont("Helvetica", 10))]
        
        for num, (line, font) in enumerate(letterHead):
                painter.setFont(font)
                if num == 3:
                    self.x = 0
                    space = (pageRect.width() - painter.fontMetrics().width(line))
                    space /= 3
                    for pair in list(zip(line.split()[::2], line.split()[1::2])):
                        painter.drawText(self.x, self.y, pair[0] + " " + pair[1])
                        self.x += (painter.fontMetrics().width(pair[0] + pair[1]) + space)
                        
                    self.y += painter.fontMetrics().height()
                else:
                    self.x = (pageRect.width() - painter.fontMetrics().width(line)) / 2
                    painter.drawText(self.x, self.y, line)
                    self.y += painter.fontMetrics().height()
                    
        return (self.x, self.y)
    
    def paintPayloads(self, painter, pageRect, statement):
        payloadHeaders = [("Description", 300),
                              ("Weight (Kg)", 50),
                              ("Price Per Tonne", 50),
                              ("Value (GBP)", 50)]
            
        length = 0
        for item, space in payloadHeaders:
            length += painter.fontMetrics().width(item) + space
        
        self.x = (pageRect.width() - length) / 2
        painter.setFont(QFont("Helvetica", 10, weight=QFont.Bold))
        headerPos = []
        for item, space in payloadHeaders:
            headerLength = (painter.fontMetrics().width(item) + space)
            offset = (headerLength - painter.fontMetrics().width(item)) / 2
            headerPos.append((self.x+offset, painter.fontMetrics().width(item)))
            painter.drawText(self.x+offset, self.y, item)
            self.x += headerLength
            
        self.y += painter.fontMetrics().height()
        
        painter.setFont(QFont("Helvetica", 10))
        for payload in statement["batch"]:                
            values = [payload["description"], payload["weight"],
                      payload["ppu"], payload["value"]]
            
            for num, item in enumerate(values):
                pair = headerPos[num]
                self.x = pair[0]
                self.x += ((pair[1] - painter.fontMetrics().width(item)) / 2)
                
                painter.drawText(self.x, self.y, item)
                
            self.y += painter.fontMetrics().height()
    
    def paintTotals(self, painter, pageRect, statement):
        totalLabels = ["Total: ",
                           "VAT ({}%): ".format(self.getInvoiceVatRate()),
                           "Invoice total: "]
            
        totalDetails = [statement["payloadTotal"],
                        statement["vatTotal"],
                        " £ {}".format(statement["grandTotal"])]
        
        labelLengths = []
        lineLengths = []
        for label, detail in zip(totalLabels, totalDetails):
            painter.setFont(QFont("Helvetica", 12, weight=QFont.Bold))
            labelLength = painter.fontMetrics().width(label)
            labelLengths.append(labelLength)
            painter.setFont(QFont("Helvetica", 12, weight=QFont.Bold))
            detailLength = painter.fontMetrics().width(detail)
            lineLengths.append(labelLength + detailLength)
            
        longestLabel = max(labelLengths)
        longestLine = max(lineLengths)
        
        self.x = 0
        self.x += (pageRect.width() - longestLine) / 2
        for label, detail in zip(totalLabels, totalDetails):
            painter.setFont(QFont("Helvetica", 12, weight=QFont.Bold))
            painter.drawText(self.x, self.y, label)
            painter.setFont(QFont("Helvetica", 12, weight=QFont.Bold))
            painter.drawText(self.x+longestLabel, self.y, detail)
            self.y += painter.fontMetrics().height()
    
    def paintFooter(self, painter, pageRect):
        footer = "N.B.: The VAT shown on this document is your output tax, and must be accounted for accordingly."
        painter.setFont(QFont("Helvetica", 12, QFont.Bold))
        footerWidth = painter.fontMetrics().width(footer)
        
        if footerWidth > pageRect.width():
            splitNumber =  footerWidth // pageRect.width()
            
            strings = footer.split(",", splitNumber)
        else:
            strings = [footer]

        self.x = 0
        offset = 0
        self.x += (pageRect.width() - painter.fontMetrics().width(strings[0])) / 2
        for num, string in enumerate(strings):
            if num > 0:
                offset = painter.fontMetrics().width(strings[0][:6])
            painter.drawText(self.x+offset, self.y, string)
            self.paintVerticalSpace(painter.fontMetrics().height())
        
    def paintDetails(self, painter, pageRect, statement):
        invoiceLabels = ["Invoice number: ",
                             "Date: ",
                             "Name: ",
                             "Address: ",
                             "Vat Reg. Number: "]
            
        invoiceDetails = [statement["number"],
                          datetime.now().strftime("%d/%m/%Y"),
                          self.customerCombobox.currentText(),
                          customers[self.customerCombobox.currentText()]["address"],
                          customers[self.customerCombobox.currentText()]["vatReg"]]
            
        lengths = []
        labels = []
        for pair in zip(invoiceLabels, invoiceDetails):
            painter.setFont(QFont("Helvetica", 10))
            labelWidth = painter.fontMetrics().width(pair[0])
            painter.setFont(QFont("Helvetica", 10, weight=QFont.Bold))
            valueWidth = painter.fontMetrics().width(pair[1])
            lengths.append(labelWidth + valueWidth)
            labels.append(painter.fontMetrics().width(pair[0]))
        longestLine = max(lengths)
        longestLabel = max(labels)
        
        self.x = 0
        self.x += (pageRect.width() - longestLine) / 2
        for pair in zip(invoiceLabels, invoiceDetails):
            painter.setFont(QFont("Helvetica", 10, weight=QFont.Bold))
            painter.drawText(self.x, self.y, pair[0])
            painter.setFont(QFont("Helvetica", 10))
            painter.drawText(self.x+longestLabel, self.y, pair[1])
            self.y += painter.fontMetrics().height()
        
    def paintVerticalSpace(self, size):
        self.y += size
        
    def paintPageLine(self, painter, pageRect):
        painter.drawLine(0, self.y, pageRect.width(), self.y)
        
    def paintInvoiceType(self, painter, pageRect):
        invoiceType = self.typeCombobox.currentText()
        painter.setFont(QFont("Helvetica", 12, QFont.Bold))
        self.x = (pageRect.width() - painter.fontMetrics().width(invoiceType)) / 2
        painter.drawText(self.x, self.y, invoiceType)
        self.y += painter.fontMetrics().height()
            
    def paintInvoice(self):
        painter = QPainter(self.printer)
        
        pageRect = self.printer.pageRect()
        
        lastPage = len(self.generateStatements().values()) - 1
        
        for page, statement in enumerate(self.generateStatements().values()):
            self.x = 0
            self.y = pageRect.y()
            
            self.paintLetterHead(painter, pageRect)
                
            self.paintVerticalSpace(40)
            
            self.paintInvoiceType(painter, pageRect)
            
            self.paintDetails(painter, pageRect, statement)
                
            self.paintVerticalSpace(painter.fontMetrics().height())
            
            self.paintPageLine(painter, pageRect)
            
            self.paintVerticalSpace(painter.fontMetrics().height() * 2)
                
            self.paintPayloads(painter, pageRect, statement)
            
            self.paintPageLine(painter, pageRect)
            
            self.paintVerticalSpace(painter.fontMetrics().height() * 3)
            
            self.paintTotals(painter, pageRect, statement)
            
            self.paintVerticalSpace(painter.fontMetrics().height() * 2)
            
            self.paintFooter(painter, pageRect)
            
            if page == lastPage:
                pass
            else:
                self.printer.newPage()
            
        painter.end()
                
    
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
        
        print(self.generateStatements())
            
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
    