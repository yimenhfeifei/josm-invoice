#!/usr/bin/python3
try:
    import sys
    import platform
    import locale
    import re
    from configparser import ConfigParser
    from decimal import Decimal
    from datetime import datetime

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

    from view.gui import Ui_invoiceWindow
    from business_customers import customers
    from shared_modules.regular_expressions import regexObjects
    from shared_modules.state import State
    from shared_modules.letterhead import LetterHead
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

__VERSION__ = "0.94"
__QT__ = QT_VERSION_STR
__SIP__ = "4.12.4"
__PYQT__ = PYQT_VERSION_STR
__PYTHON__ = platform.python_version()


class InvoiceWindow(Ui_invoiceWindow):

    def __init__(self, parent=None):
        super(InvoiceWindow, self).__init__(parent)
        self.setWindowTitle("Invoice")
        self.unitFrame.setVisible(False)

        locale.setlocale(locale.LC_ALL, "")

        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setPaperSize(QPrinter.A4)
        self.printer.setResolution(300)
        self.printer.setPageMargins(10.0, 10.0, 10.0, 10.0,
                                    QPrinter.Millimeter)

        self.fonts = {"payloadFont": QFont("Helvetica", 10),
                      "totalsLabelFont": QFont("Helvetic", 12,
                                               QFont.Bold),
                      "totalsDetailFont": QFont("Helvetic", 12,
                                                QFont.Bold),
                      "payloadHeadersFont": QFont("Helvetica", 10,
                                                  weight=QFont.Bold),
                      "footerFont": QFont("Helvetica", 12,
                                          QFont.Bold),
                      "invoiceLabelsFont": QFont("Helvetica", 10),
                      "invoiceDetailsFont": QFont("Helvetica", 10,
                                                  QFont.Bold),
                      "invoiceTypeFont": QFont("Helvetica", 12,
                                               QFont.Bold),
                      "companyFont": QFont("Helvetica", 16,
                                           weight=QFont.Bold),
                      "merchantFont": QFont("Helvetica", 10,
                                            weight=QFont.Bold),
                      "addressFont": QFont("Helvetica", 12,
                                           weight=QFont.Bold),
                      "numberLineFont": QFont("Helvetica", 10,
                                              weight=QFont.Bold),
                      "vatFont": QFont("Helvetica", 10)}

        merchant = "Chosen View, United Road, St Day, Redruth, TR16 5HT"
        numbers = "WML: 20659 TEL.: (01209)820313 FAX: (01209)822512 WCL: CB/JM3986P2"

        self.letterHead = [("John Orchard and Company",
                            self.fonts["companyFont"]),
                           ("Scrap Metal Merchants",
                            self.fonts["merchantFont"]),
                           (merchant,
                            self.fonts["addressFont"]),
                           (numbers,
                            self.fonts["numberLineFont"]),
                           ("VAT Registration number: 1319249 76",
                            self.fonts["vatFont"])]

        self.invoiceLabels = ["Invoice number: ",
                              "Date: ",
                              "Name: ",
                              "Address: ",
                              "Vat Reg. Number: "]

        self.payloadHeaders = [("Description", 500),
                               ("Weight (Kg)", 50),
                               ("Price Per Tonne", 50),
                               ("Value (GBP)", 50)]

        self.totalLabels = ["Total: ",
                            "VAT ({}%): ".format(self.getInvoiceVatRate()),
                            "Invoice total: "]

        self.screenRect = QDesktopWidget().geometry()

        self.move((self.screenRect.width() - self.width()) / 2,
                  (self.screenRect.height() - self.height()) / 2)

        self.customers = customers["Purchase Invoice"]

        self.populateCustomerBox(self.customers)

        self.populateTypeBox("Purchase Invoice", "Sales Invoice")

        self.setInvoiceNumber(self.getInvoiceNumberFromFile("Purchase Invoice"))
        
        self.vatEdit.setText(self.getVatRateFromFile())

        self.validating = [self.descriptionEdit,
                           self.weightEdit,
                           self.pricePerUnitEdit,
                           self.valueEdit,
                           self.vatEdit,
                           self.numberEdit]

        self.descriptionText = "Description"
        self.weightText = "Weight"
        self.ppuText = "Price Per Unit"
        self.valueText = "Value"
        self.deleteText = "Delete"

        self.invoiceTable.setHorizontalHeaderLabels([self.descriptionText,
                                                     self.weightText,
                                                     self.ppuText,
                                                     self.valueText,
                                                     self.deleteText])

        self.weightGroup = QButtonGroup()
        self.weightGroup.addButton(self.unitFrame.weightKgRadio)
        self.weightGroup.addButton(self.unitFrame.weightTonnesRadio)
        self.unitFrame.weightKgRadio.setChecked(True)

        self.priceGroup = QButtonGroup()
        self.priceGroup.addButton(self.unitFrame.priceKgRadio)
        self.priceGroup.addButton(self.unitFrame.priceTonnesRadio)
        self.unitFrame.priceTonnesRadio.setChecked(True)

        self.kgString = self.unitFrame.weightKgRadio.text()
        self.tonneString = self.unitFrame.weightTonnesRadio.text()

        self.unitConverter = {self.kgString: self.noop,
                              self.tonneString: self.convertTonnesToKg}

        self.connect(self.weightGroup, SIGNAL("buttonClicked(int)"),
                     self.updateWeightHeader)

        self.connect(self.priceGroup, SIGNAL("buttonClicked(int)"),
                     self.updatePriceHeader)

        for widget in self.validating:
            widget.setValidator(regexObjects["qValue"])

        self.descriptionEdit.setValidator(regexObjects["qMaterial"])

        for widget in self.validating:
            self.connect(widget, SIGNAL("textChanged(QString)"),
                         self.changed)

        self.connect(self.typeCombobox, SIGNAL("currentIndexChanged(QString)"),
                     self.changeInvoiceType)

        self.connect(self.customerCombobox, SIGNAL("currentIndexChanged(QString)"),
                     self.returnFocus)

        self.connect(self.addButton, SIGNAL("clicked()"),
                     self.addPayload)

        self.connect(self.invoiceTable, SIGNAL("cellClicked(int, int)"),
                     self.payloadTableClicked)

        self.connect(self.reviewButton, SIGNAL("clicked()"),
                     self.printPreview)

        self.connect(self.pricePerUnitEdit, SIGNAL("returnPressed()"),
                     self.addPayload)

        self.connect(self.valueEdit, SIGNAL("returnPressed()"),
                     self.addPayload)

        self.connect(self.actionQuit, SIGNAL("triggered()"),
                     self.close)

        self.connect(self.actionPrintPreview, SIGNAL("triggered()"),
                     self.printPreview)

        self.connect(self.actionAboutInvoice, SIGNAL("triggered()"),
                     self.showAbout)

        self.connect(self.actionToggleAutoCalc, SIGNAL("triggered()"),
                     self.toggleAutoCalculation)

        self.changed()

        self.descriptionEdit.setFocus()

        self.statusBar().setStyleSheet("background: #FFECB3")

        self.autoCalcLabel = QLabel("Auto Calc:")
        self.autoCalcStatus = QLabel("")
        self.statusBar().addWidget(self.autoCalcLabel)
        self.statusBar().addWidget(self.autoCalcStatus)

        self.autoCalcStateOn = State()
        self.autoCalcStateOn.addVariable(self.autoCalcStatus.setText, "On")
        self.autoCalcStateOn.addVariable(self.valueEdit.setReadOnly, True)
        self.autoCalcStateOn.addVariable(self.pricePerUnitEdit.setValidator,
                                         regexObjects["qValue"])

        self.autoCalcStateOff = State()
        self.autoCalcStateOff.addVariable(self.autoCalcStatus.setText, "Off")
        self.autoCalcStateOff.addVariable(self.valueEdit.setReadOnly, False)
        self.autoCalcStateOff.addVariable(self.pricePerUnitEdit.setValidator,
                                         regexObjects["qMaterial"])

        self.autoCalcStateOff.enable()

        self.changeInvoiceType("Purchase Invoice")

        self.updatePriceHeader()
        self.updateWeightHeader()

    def toggleAutoCalculation(self):
        if self.autoCalcStatus.text() == "On":
            self.autoCalcStateOff.enable()
        elif self.autoCalcStatus.text() == "Off":
            self.autoCalcStateOn.enable()

        self.changed()

    def changeInvoiceType(self, name):
        self.customerCombobox.clear()

        self.customers = customers[name]

        self.populateCustomerBox(self.customers)

        self.setInvoiceNumber(self.getInvoiceNumberFromFile(name))

        self.returnFocus()

    def setInvoiceNumber(self, value):
        self.numberEdit.setText(value)

    def returnFocus(self):
        self.descriptionEdit.setFocus()

    def showAbout(self):
        QMessageBox.about(self, "About Invoice", "Invoice version {}\n".format(__VERSION__)
                          + "Python {}\n".format(__PYTHON__)
                          + "QT {}\n".format(__QT__)
                          + "PYQT {}\n".format(__PYQT__)
                          + "Copyright John Orchard & Company 2011")

    def getInvoiceNumberFromFile(self, invoiceType):
        cp = ConfigParser()
        cp.read("settings.cfg")

        if invoiceType == "Purchase Invoice":
            return cp.get("invoice_numbers", "purchase")
        else:
            return cp.get("invoice_numbers", "sales")
        
    def getVatRateFromFile(self):
        cp = ConfigParser()
        cp.read("settings.cfg")

        return cp.get("vat", "rate")

    def getInvoiceVatRate(self):
        return self.vatEdit.text()

    def populateTypeBox(self, *types):
        for index, name in enumerate(types):
            self.typeCombobox.insertItem(index, name)

    def populateCustomerBox(self, customers):
        for index, name in enumerate(customers.keys()):
            self.customerCombobox.insertItem(index, name)

    def payloadTableClicked(self, row, column):
        if column == self.invoiceTable.getHeaderIndex(self.deleteText):
            self.invoiceTable.selectRow(row)
            self.invoiceTable.removeRow(row)

    def changeRichText(self, label, string):
        return re.sub(regexObjects["spanTagContents"],
                      string,
                      label.text())

    def updatePriceHeader(self):
        newPrice = "Price ({})".format(self.priceGroup.checkedButton().text())

        self.payloadHeaders[2] = (newPrice, self.payloadHeaders[2][1])

        self.pricePerUnitLabel.setText(self.changeRichText(self.pricePerUnitLabel, newPrice))

    def updateWeightHeader(self):
        newWeight = "Weight ({})".format(self.weightGroup.checkedButton().text())

        self.payloadHeaders[1] = (newWeight, self.payloadHeaders[1][1])

        self.weightLabel.setText(self.changeRichText(self.weightLabel, newWeight))

    def changed(self):
        weightStatus = self.weightEdit.validator().validate(self.weightEdit.text(), 0)
        ppuStatus = self.pricePerUnitEdit.validator().validate(self.pricePerUnitEdit.text(), 0)

        if weightStatus[0] == 2 and ppuStatus[0] == 2:
            if self.autoCalcStatus.text() == "On":
                self.calculatePayloadValue()
            else:
                pass
        else:
            self.valueEdit.clear()

    def calculatePayloadValue(self):
        weight = Decimal(self.weightEdit.text())
        pricePerUnit = Decimal(self.pricePerUnitEdit.text())

        weightUnit = self.weightGroup.checkedButton().text()
        priceUnit = self.priceGroup.checkedButton().text()

        if weightUnit == self.kgString and priceUnit == self.kgString:
            pass
        else:
            weight = self.unitConverter[weightUnit](weight, "weight")
            pricePerUnit = self.unitConverter[priceUnit](pricePerUnit, "price")

        self.valueEdit.setText("{:.2f}".format(weight * pricePerUnit))

    def convertTonnesToKg(self, value, valueType):
        if valueType == "weight":
            return value * Decimal(1000)
        else:
            return value / Decimal(1000)

    def noop(self, value, valueType):
        return value

    def allValid(self):
        for widget in self.validating:
            if not widget.validator().validate(widget.text(), 0)[0] == 2:
                return False
        return True

    def addPayload(self):
        if self.allValid():
            if self.autoCalcStatus.text() == "On":
                pricePerUnit = "{:.2f}".format(Decimal(self.pricePerUnitEdit.text()))
            else:
                pricePerUnit = self.pricePerUnitEdit.text()

            value = locale.currency(Decimal(self.valueEdit.text()), grouping=True,
                                    symbol=False)

            self.addRow(self.descriptionEdit.text(),
                        "{:.2f}".format(Decimal(self.weightEdit.text())),
                        pricePerUnit,
                        value)

            self.resetForm()
        else:
            QMessageBox.warning(self, "Attention", "All fields must be valid!")

    def addRow(self, *args):
        self.invoiceTable.appendRow()
        row = self.invoiceTable.rowCount() - 1

        for column, value in enumerate(args):
            item = QTableWidgetItem(value)

            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.invoiceTable.setItem(row, column, item)

        self.invoiceTable.addDeleteCell(row,
                                        self.invoiceTable.getHeaderIndex(self.deleteText),
                                        text=self.deleteText)

    def getPayloadTotal(self):
        values = []
        for row in range(self.invoiceTable.rowCount()):
            value = self.invoiceTable.item(row, self.invoiceTable.getHeaderIndex(self.valueText)).text().replace(",", "")
            values.append(Decimal(value))

        return sum(values)

    def getVatTotal(self, amount):
        return amount * (Decimal(self.getInvoiceVatRate()) / 100)

    def getGrandTotal(self):
        return self.getPayloadTotal() + self.getVatTotal(self.getPayloadTotal())

    def getPayloads(self):
        payloads = self.invoiceTable.getContents()
        for group in payloads.values():
            del group[self.deleteText]

        return payloads

    def printPreview(self):
        if not self.invoiceTable.isValid():
            QMessageBox.warning(self, "Attention", "No payloads to review!")
            return

        previewDialog = QPrintPreviewDialog(self.printer, self)

        self.connect(previewDialog, SIGNAL("paintRequested(QPrinter*)"),
                     self.paintInvoice)

        if previewDialog.exec_():

            self.setInvoiceNumber("{:03d}".format(int(self.numberEdit.text()) + 1))

            if self.typeCombobox.currentText() == "Purchase Invoice":
                configOption = "purchase"
            else:
                configOption = "sales"

            cp = ConfigParser()
            cp.read("settings.cfg")
            cp.set("invoice_numbers", configOption,
                   self.numberEdit.text())

            with open("settings.cfg", "w") as file:
                cp.write(file)

            self.invoiceTable.removeAllRows()

        self.returnFocus()

    def paintLetterHead(self, painter, pageRect):
        for num, (line, font) in enumerate(self.letterHead):
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

    def paintPayloadHeaders(self, painter, pageRect):
        length = 0
        painter.setFont(self.fonts["payloadHeadersFont"])
        for item, space in self.payloadHeaders:
            length += painter.fontMetrics().width(item) + space

        self.x = (pageRect.width() - length) / 2

        self.headerPos = []
        for item, space in self.payloadHeaders:
            headerLength = (painter.fontMetrics().width(item) + space)
            offset = (headerLength - painter.fontMetrics().width(item)) / 2
            self.headerPos.append((self.x + offset, painter.fontMetrics().width(item)))
            painter.drawText(self.x + offset, self.y, item)
            self.x += headerLength

    def paintPayload(self, painter, pageRect, payload):
        painter.setFont(self.fonts["payloadFont"])
        values = [payload[self.descriptionText], payload[self.weightText],
                  payload[self.ppuText], payload[self.valueText]]

        for num, item in enumerate(values):
            pair = self.headerPos[num]
            self.x = pair[0]
            self.x += ((pair[1] - painter.fontMetrics().width(item)) / 2)

            painter.drawText(self.x, self.y, item)

    def paintTotals(self, painter, pageRect):
        payloadTotal = locale.currency(self.getPayloadTotal(), grouping=True,
                                       symbol=True)

        vatTotal = locale.currency(self.getVatTotal(self.getPayloadTotal()), grouping=True,
                                   symbol=True)

        grandTotal = locale.currency(self.getGrandTotal(), grouping=True,
                                     symbol=True)

        totalDetails = [payloadTotal,
                        vatTotal,
                        grandTotal]

        self.totalLabels[1] = "VAT ({}%): ".format(self.getInvoiceVatRate())

        labelLengths = []
        lineLengths = []
        for label, detail in zip(self.totalLabels, totalDetails):
            painter.setFont(self.fonts["totalsLabelFont"])
            labelLength = painter.fontMetrics().width(label)

            labelLengths.append(labelLength)

            painter.setFont(self.fonts["totalsDetailFont"])
            detailLength = painter.fontMetrics().width(detail)

            lineLengths.append(labelLength + detailLength)

        longestLabel = max(labelLengths)
        longestLine = max(lineLengths)

        self.x = 0
        self.x += (pageRect.width() - longestLine) / 2
        for label, detail in zip(self.totalLabels, totalDetails):
            painter.setFont(self.fonts["totalsLabelFont"])
            painter.drawText(self.x, self.y, label)

            painter.setFont(self.fonts["totalsDetailFont"])
            painter.drawText(self.x + longestLabel, self.y, detail)

            self.y += painter.fontMetrics().height()

    def paintFooter(self, painter, pageRect):
        footer = "N.B.: The VAT shown on this document is your output tax, and must be accounted for accordingly."
        painter.setFont(self.fonts["footerFont"])
        footerWidth = painter.fontMetrics().width(footer)

        if footerWidth > pageRect.width():
            splitNumber = footerWidth // pageRect.width()

            strings = footer.split(",", splitNumber)
        else:
            strings = [footer]

        self.x = 0
        offset = 0
        self.x += (pageRect.width() - painter.fontMetrics().width(strings[0])) / 2
        for num, string in enumerate(strings):
            if num > 0:
                offset = painter.fontMetrics().width(strings[0][:6])
            painter.drawText(self.x + offset, self.y, string)
            self.paintVerticalSpace(painter.fontMetrics().height())

    def paintDetails(self, painter, pageRect, invoiceNumber):
        invoiceDetails = [invoiceNumber,
                          datetime.now().strftime("%d/%m/%Y"),
                          self.customerCombobox.currentText(),
                          self.customers[self.customerCombobox.currentText()]["address"],
                          self.customers[self.customerCombobox.currentText()]["vatReg"]]

        lengths = []
        labels = []
        for pair in zip(self.invoiceLabels, invoiceDetails):
            painter.setFont(self.fonts["invoiceLabelsFont"])
            labelWidth = painter.fontMetrics().width(pair[0])

            painter.setFont(self.fonts["invoiceDetailsFont"])
            valueWidth = painter.fontMetrics().width(pair[1])

            lengths.append(labelWidth + valueWidth)
            labels.append(painter.fontMetrics().width(pair[0]))

        longestLine = max(lengths)
        longestLabel = max(labels)

        self.x = 0
        self.x += (pageRect.width() - longestLine) / 2
        for pair in zip(self.invoiceLabels, invoiceDetails):
            painter.setFont(self.fonts["invoiceLabelsFont"])
            painter.drawText(self.x, self.y, pair[0])

            painter.setFont(self.fonts["invoiceDetailsFont"])
            painter.drawText(self.x + longestLabel, self.y, pair[1])

            self.y += painter.fontMetrics().height()

    def paintVerticalSpace(self, size):
        self.y += size

    def paintPageLine(self, painter, pageRect):
        painter.drawLine(0, self.y, pageRect.width(), self.y)

    def paintInvoiceType(self, painter, pageRect):
        invoiceType = self.typeCombobox.currentText()

        painter.setFont(self.fonts["invoiceTypeFont"])

        self.x = (pageRect.width() - painter.fontMetrics().width(invoiceType)) / 2
        painter.drawText(self.x, self.y, invoiceType)

    def paintPageNumber(self, painter, pageRect, pageNumber):
        painter.setFont(self.fonts["payloadFont"])
        pageString = "Page {}".format(pageNumber)
        width = painter.fontMetrics().width(pageString)
        painter.drawText(pageRect.width() - width, self.y, pageString)

    def paintTop(self, painter, pageRect, invoiceNumber, pageNumber):
        self.x = 0
        self.y = pageRect.y()

        self.paintPageNumber(painter, pageRect, pageNumber)

        letterHead = LetterHead(painter, pageRect)
        self.x, self.y = letterHead.paint(self.x, self.y)

        self.paintVerticalSpace(40)

        self.paintInvoiceType(painter, pageRect)

        self.paintVerticalSpace(painter.fontMetrics().height())

        self.paintDetails(painter, pageRect, invoiceNumber)

        self.paintVerticalSpace(painter.fontMetrics().height())

        self.paintPageLine(painter, pageRect)

        self.paintVerticalSpace(painter.fontMetrics().height() * 2)

        self.paintPayloadHeaders(painter, pageRect)

        self.paintVerticalSpace(painter.fontMetrics().height())

    def paintNewPageMessage(self, painter, pageRect, pageNum):
        message = "Continued on page {} -------->".format(pageNum)

        painter.setFont(self.fonts["merchantFont"])
        mWidth = painter.fontMetrics().width(message)
        self.x = (pageRect.width() - mWidth) / 2
        painter.drawText(self.x, self.y, message)

    def calculatePayloadSpace(self, painter, pageRect):
        painter.setFont(self.fonts["totalsLabelFont"])
        totalsHeight = painter.fontMetrics().height() * len(self.totalLabels)

        painter.setFont(self.fonts["footerFont"])
        footerHeight = painter.fontMetrics().height() * 2

        painter.setFont(self.fonts["payloadFont"])
        spaceHeight = painter.fontMetrics().height() * 5

        bottomHeight = totalsHeight + footerHeight + spaceHeight

        usedSpace = self.y + bottomHeight

        return pageRect.height() - usedSpace

    def paintLooper(self, painter, pageRect):
        self.paintTop(painter, pageRect, self.numberEdit.text(), 1)

        payloadSpace = self.calculatePayloadSpace(painter, pageRect)

        payloadStart = self.y

        pageNumber = 1

        for num, payload in enumerate(self.getPayloads().values()):
            if self.y > (payloadStart + payloadSpace):
                pageNumber += 1
                self.paintPageLine(painter, pageRect)
                self.paintVerticalSpace(painter.fontMetrics().height() * 2)
                self.paintNewPageMessage(painter, pageRect, pageNumber)
                self.printer.newPage()
                self.paintTop(painter, pageRect, self.numberEdit.text(), pageNumber)

            self.paintPayload(painter, pageRect, payload)
            self.paintVerticalSpace(painter.fontMetrics().height())

        self.paintBottom(painter, pageRect)

    def paintBottom(self, painter, pageRect):
        self.paintPageLine(painter, pageRect)

        self.paintVerticalSpace(painter.fontMetrics().height() * 3)

        self.paintTotals(painter, pageRect)

        self.paintVerticalSpace(painter.fontMetrics().height() * 2)

        if self.typeCombobox.currentText() == "Purchase Invoice":
            self.paintFooter(painter, pageRect)
        else:
            pass

    def paintInvoice(self):
        painter = QPainter(self.printer)

        pageRect = self.printer.pageRect()

        self.paintLooper(painter, pageRect)

        painter.end()

    def resetForm(self):
        vat = self.vatEdit.text()
        number = self.numberEdit.text()
        for widget in self.validating:
            widget.clear()
        self.vatEdit.setText(vat)
        self.numberEdit.setText(number)
        self.returnFocus()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = InvoiceWindow()
    application.setOrganizationName("John Orchard & Company")
    application.setOrganizationDomain("orchard.com")
    application.setApplicationName("Orchard Invoice")
    application.setApplicationVersion(__VERSION__)
    mainWindow.show()
    sys.exit(application.exec_())
