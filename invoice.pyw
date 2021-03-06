#!/usr/bin/env python3

try:
    import sys
    import platform
    import locale
    import re
    from configparser import ConfigParser
    from decimal import Decimal
    from decimal import InvalidOperation
    from datetime import datetime
    from random import choice

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

    from view.gui import Ui_invoiceWindow
    from regular_expressions import regexObjects
    from state import State
    from view.letterhead import LetterHead
    from database_mapper import Database
    from view.database_dialog import DatabaseDialog
    from view.print_preview_dialog import PrintPreviewDialogExtended
    from view.backdate_dialog import backdateDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

__VERSION__ = "0.997"
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

        self.setWindowIcon(QIcon("resources/images/penguin.png"))

        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setPaperSize(QPrinter.A4)
        self.printer.setResolution(300)
        self.printer.setPageMargins(5.0, 5.0, 5.0, 5.0,
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
                      "vatFont": QFont("Helvetica", 10)}

        self.invoiceLabels = ["Invoice number: ",
                              "Date: ",
                              "Name: ",
                              "Address: ",
                              "Vat Reg. Number: "]

        self.totalLabels = ["Total: ",
                            "VAT ({}%): ".format(self.getInvoiceVatRate()),
                            "Invoice total: "]

        self.sectionPercentages = [40, 20, 20, 20]

        self.screenRect = QDesktopWidget().geometry()

        self.move((self.screenRect.width() - self.width()) / 2,
                  (self.screenRect.height() - self.height()) / 2)

        self.typeCombobox.populate(["Purchase Invoice",
                                    "Sales Invoice"])

        self.database = Database("customers.csv")

        self.populateCustomerComboBox()

        self.changeInvoiceType(self.typeCombobox.currentText())

        self.setVatRate(self.getVatRateFromFile())

        self.validating = [self.descriptionEdit,
                           self.weightEdit,
                           self.pricePerUnitEdit,
                           self.valueEdit,
                           self.vatEdit,
                           self.numberEdit]

        self.valueText = self.invoiceTable.getHeaderName(3)

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

        self.connect(self.customerCombobox,
                     SIGNAL("currentIndexChanged(QString)"),
                     self.returnFocus)

        self.connect(self.invoiceTable, SIGNAL("cellClicked(int, int)"),
                     self.on_invoiceTable_clicked)

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
                     self.showAboutInvoice)

        self.connect(self.actionToggleAutoCalc, SIGNAL("triggered()"),
                     self.toggleAutoCalculation)

        self.changed()

        self.statusBar().setStyleSheet("background: #FFECB3")

        self.autoCalcLabel = QLabel("Auto Calc:")
        self.autoCalcStatus = QLabel("")
        self.statusBar().addPermanentWidget(self.autoCalcLabel)
        self.statusBar().addPermanentWidget(self.autoCalcStatus)

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

        self.connect(self.actionDatabaseDialog, SIGNAL("triggered()"),
                     self.showDatabaseDialog)

        self.connect(self.actionRevert, SIGNAL("triggered()"),
                     self.revert)

        self.connect(self.actionResetForm, SIGNAL("triggered()"),
                     self.onResetForm)

        self.connect(self.actionAboutQt, SIGNAL("triggered()"),
                     self.showAboutQt)

        self.connect(self.actionSaveVat, SIGNAL("triggered()"),
                     self.saveVat)

        self.connect(self.actionPopulateWithDummyData, SIGNAL("triggered()"),
                     self.populateWithDummyData)

        self.connect(self.actionBackdate, SIGNAL("triggered()"),
                     self.showBackdateDialog)

        self.connect(self.addButton, SIGNAL("clicked()"),
                     self.addPayload)

        self.connect(self.deleteButton, SIGNAL("clicked()"),
                     self.on_deleteButton_clicked)

        self.connect(self.updateButton, SIGNAL("clicked()"),
                     self.on_updateButton_clicked)

        self.updatePriceHeader()
        self.updateWeightHeader()

        self.lastPrintedInvoice = None

        self.settingsFile = "settings.cfg"

        self.date = None

        self.backdate = False

    def addPayload(self):
        if self.allValid():
            weight = self.formatNumber(self.weightEdit.text())

            pricePerUnit = self.formatNumber(self.pricePerUnitEdit.text())

            value = self.formatNumber(self.valueEdit.text())

            self.addRow(self.descriptionEdit.text(),
                        weight,
                        pricePerUnit,
                        value)

            self.clearInputWidgets()
            self.invoiceTable.resizeRowsToContents()
        else:
            QMessageBox.warning(self, "Attention", "All fields must be valid!")

    def addRow(self, *args):
        self.invoiceTable.appendRow()
        row = self.invoiceTable.rowCount() - 1
        self.invoiceTable.setCurrentCell(row, 0)

        for column, value in enumerate(args):
            item = QTableWidgetItem(value)

            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.invoiceTable.setItem(row, column, item)

    def allValid(self):
        for widget in self.validating:
            if not widget.validator().validate(widget.text(), 0)[0] == 2:
                return False
        return True

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

    def changed(self):
        weightStatus = self.weightEdit.validator().validate(self.weightEdit.text(), 0)
        ppuStatus = self.pricePerUnitEdit.validator().validate(self.pricePerUnitEdit.text(), 0)

        if weightStatus[0] == 2 and ppuStatus[0] == 2:
            if self.autoCalcStatus.text() == "On":
                self.calculatePayloadValue()
            else:
                pass
        else:
            pass

    def changeInvoiceType(self, name):
        self.setInvoiceNumber(self.getInvoiceNumberFromFile(name))

        self.returnFocus()

    def changeRichText(self, label, string):
        return re.sub(regexObjects["spanTagContents"],
                      string,
                      label.text())

    def clearInputWidgets(self):
        self.descriptionEdit.clear()
        self.weightEdit.clear()
        self.pricePerUnitEdit.clear()
        self.valueEdit.clear()

        self.returnFocus()

    def closeEvent(self, event):
        messageBox = self.createMessageBox("Quitting",
                                           "Do you really want to quit?")

        if messageBox.exec_() == QMessageBox.Ok:
            event.accept()
        else:
            event.ignore()

    def convertTonnesToKg(self, value, valueType):
        if valueType == "weight":
            return value * Decimal(1000)
        else:
            return value / Decimal(1000)

    def createMessageBox(self, title, text):
        messageBox = QMessageBox(self)
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setWindowTitle(title)
        messageBox.setText(text)
        messageBox.setStandardButtons(QMessageBox.Ok |
                                      QMessageBox.Cancel)
        return messageBox

    def formatNumber(self, value, grouping=True, symbol=False):
        try:
            decimalValue = Decimal(value)
            return locale.currency(decimalValue, grouping=grouping,
                                   symbol=symbol)
        except InvalidOperation:
            return value

    def gatherInvoice(self):
        return {"type": self.typeCombobox.currentText(),
                "customer": self.customerCombobox.currentText(),
                "vatRate": self.vatEdit.text(),
                "number": self.numberEdit.text(),
                "weightHeader": self.weightGroup.checkedButton(),
                "ppuHeader": self.priceGroup.checkedButton(),
                "payloads": self.invoiceTable.getRows(self.invoiceTable.columnCount()),
                "autoCalc": self.autoCalcStatus.text()}

    def getDate(self):
        if self.backdate:
            return self.date
        else:
            return datetime.now().strftime("%d/%m/%Y")

    def getGrandTotal(self):
        return self.getPayloadTotal() + self.getVatTotal(self.getPayloadTotal())

    def getInvoiceNumberFromFile(self, invoiceType):
        cp = ConfigParser()
        cp.read("settings.cfg")

        if invoiceType == "Purchase Invoice":
            return cp.get("invoice_numbers", "purchase")
        else:
            return cp.get("invoice_numbers", "sales")

    def getInvoiceVatRate(self):
        return self.vatEdit.text()

    def getPayloadTotal(self):
        values = []
        for row in range(self.invoiceTable.rowCount()):
            value = self.invoiceTable.item(row, self.invoiceTable.getHeaderIndex(self.valueText)).text().replace(",", "")
            values.append(Decimal(value))

        return sum(values)

    def getVatRateFromFile(self):
        cp = ConfigParser()
        cp.read("settings.cfg")

        return cp.get("vat", "rate")

    def getVatTotal(self, amount):
        return amount * (Decimal(self.getInvoiceVatRate()) / 100)

    def noop(self, value, valueType):
        return value

    def on_deleteButton_clicked(self):
        row = self.invoiceTable.currentRow()
        self.invoiceTable.removeRow(row)

    def on_invoiceTable_clicked(self, row, column):
        values = [self.stripCommas(self.invoiceTable.item(row, column).text())
                  for column in range(self.invoiceTable.columnCount())]

        self.descriptionEdit.setText(values[0])
        self.weightEdit.setText(values[1])
        self.pricePerUnitEdit.setText(values[2])
        self.valueEdit.setText(values[3])

    def on_updateButton_clicked(self):
        if self.allValid():
            row = self.invoiceTable.currentRow()

            for column, string in enumerate([self.descriptionEdit.text(),
                                              self.weightEdit.text(),
                                              self.pricePerUnitEdit.text(),
                                              self.valueEdit.text()]):

                item = QTableWidgetItem(self.formatNumber(string))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                self.invoiceTable.setItem(row, column, item)

            self.invoiceTable.resizeRowsToContents()

    def onResetForm(self):
        messageBox = self.createMessageBox("Resetting form",
                                           "Do you really want to reset the form?")

        if messageBox.exec_() == QMessageBox.Ok:
            self.resetForm()
        else:
            return

    def paintBottom(self, painter, pageRect):
        self.paintPageLine(painter, pageRect)

        self.paintVerticalSpace(painter.fontMetrics().height() * 3)

        self.paintTotals(painter, pageRect)

        self.paintVerticalSpace(painter.fontMetrics().height() * 2)

        if self.typeCombobox.currentText() == "Purchase Invoice":
            self.paintFooter(painter, pageRect)
        else:
            pass

    def paintDetails(self, painter, pageRect, invoiceNumber):
        invoiceDetails = [invoiceNumber,
                          self.getDate()]

        invoiceDetails = invoiceDetails[:2] + self.database.loadRecordByName(self.customerCombobox.currentText())

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

            self.paintVerticalSpace(painter.fontMetrics().height())

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

    def paintInvoice(self):
        painter = QPainter(self.printer)

        pageRect = self.printer.pageRect()

        self.paintLooper(painter, pageRect)

        painter.end()

    def paintInvoiceType(self, painter, pageRect):
        invoiceType = self.typeCombobox.currentText()

        painter.setFont(self.fonts["invoiceTypeFont"])

        self.x = (pageRect.width() - painter.fontMetrics().width(invoiceType)) / 2
        painter.drawText(self.x, self.y, invoiceType)

    def paintLooper(self, painter, pageRect):
        self.paintTop(painter, pageRect, self.numberEdit.text(), 1)

        payloadSpace = self.calculatePayloadSpace(painter, pageRect)

        payloadStart = self.y

        pageNumber = 1

        for num, payload in enumerate(self.gatherInvoice()["payloads"]):
            if self.y > (payloadStart + payloadSpace):
                pageNumber += 1
                self.paintPageLine(painter, pageRect)
                self.paintVerticalSpace(painter.fontMetrics().height() * 2)
                self.paintNewPageMessage(painter, pageRect, pageNumber)
                self.printer.newPage()
                self.paintTop(painter, pageRect, self.numberEdit.text(),
                              pageNumber)

            self.paintPayload(painter, pageRect, payload)
            self.paintVerticalSpace(painter.fontMetrics().height())

        self.paintBottom(painter, pageRect)

    def paintNewPageMessage(self, painter, pageRect, pageNum):
        message = "Continued on page {} -------->".format(pageNum)

        painter.setFont(self.fonts["invoiceDetailsFont"])
        mWidth = painter.fontMetrics().width(message)
        self.x = (pageRect.width() - mWidth) / 2
        painter.drawText(self.x, self.y, message)

    def paintPageLine(self, painter, pageRect):
        painter.drawLine(0, self.y, pageRect.width(), self.y)

    def paintPageNumber(self, painter, pageRect, pageNumber):
        painter.setFont(self.fonts["payloadFont"])
        pageString = "Page {}".format(pageNumber)
        width = painter.fontMetrics().width(pageString)
        painter.drawText(pageRect.width() - width, self.y, pageString)

    def paintPayload(self, painter, pageRect, payload):
        painter.setFont(self.fonts["payloadFont"])

        self.paintSection(painter, pageRect, payload,
                          self.sectionPercentages)

    def paintPayloadHeaders(self, painter, pageRect):
        painter.setFont(self.fonts["payloadHeadersFont"])

        weight = re.search(regexObjects["spanTagContents"],
                  self.weightLabel.text()).group(0)

        ppu = re.search(regexObjects["spanTagContents"],
                  self.pricePerUnitLabel.text()).group(0)

        payloadHeaders = ["Description",
                          weight,
                          ppu,
                          "Value (GBP)"]

        self.paintSection(painter, pageRect, payloadHeaders,
                          self.sectionPercentages)

    def paintSection(self, painter, pageRect, strings, sectionSizes):
        self.x = 0

        for string, sectionPercentage in zip(strings, sectionSizes):
            textLength = painter.fontMetrics().width(string)
            sectionLength = (sectionPercentage / 100) * pageRect.width()
            offset = (sectionLength - textLength) / 2
            if textLength > sectionLength:
                print("'{}' is too long for the section!".format(string))
            painter.drawText(self.x + offset, self.y, string)
            self.x += sectionLength

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

    def paintTotals(self, painter, pageRect):
        payloadTotal = locale.currency(self.getPayloadTotal(), grouping=True,
                                       symbol=True)

        vatTotal = locale.currency(self.getVatTotal(self.getPayloadTotal()),
                                   grouping=True,
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

            self.paintVerticalSpace(painter.fontMetrics().height())

    def paintVerticalSpace(self, size):
        self.y += size

    def populateCustomerComboBox(self):
        self.customerCombobox.clear()
        self.customerCombobox.populate([record[0]
                                        for record in self.database.loadRecords()])

    def populateWithDummyData(self):
        materials = ["Iron",
                     "Copper",
                     "Gold",
                     "Cars",
                     "Titanium"]

        for i in range(145):
            material = choice(materials)
            weight = choice(range(1, 3560))
            ppu = choice(range(200, 5000))
            value = choice(range(1, 6000))

            self.descriptionEdit.setText(material)
            self.weightEdit.setText(str(weight))
            self.pricePerUnitEdit.setText(str(ppu))
            self.valueEdit.setText(str(value))

            self.addPayload()

        self.invoiceTable.resizeRowsToContents()

    def printPreview(self):
        if not self.invoiceTable.isValid():
            QMessageBox.warning(self, "Attention", "No payloads to review!")
            return

        previewDialog = PrintPreviewDialogExtended(self.printer,
                                                   self.paintInvoice,
                                                   self)

        if previewDialog.exec_():

            self.lastPrintedInvoice = self.gatherInvoice()

            self.setInvoiceNumber("{:03d}".format(int(self.numberEdit.text()) + 1))

            if self.typeCombobox.currentText() == "Purchase Invoice":
                configOption = "purchase"
            else:
                configOption = "sales"

            cp = ConfigParser()
            cp.read(self.settingsFile)
            cp.set("invoice_numbers", configOption,
                   self.numberEdit.text())

            with open(self.settingsFile, "w") as file:
                cp.write(file)

            self.invoiceTable.removeAllRows()

        self.returnFocus()

    def resetForm(self):
        self.typeCombobox.setCurrentIndex(0)
        self.customerCombobox.setCurrentIndex(0)
        self.setVatRate(self.getVatRateFromFile())
        self.setInvoiceNumber(self.getInvoiceNumberFromFile("Purchase Invoice"))

        self.unitFrame.weightKgRadio.setChecked(True)
        self.unitFrame.priceTonnesRadio.setChecked(True)
        self.updateWeightHeader()
        self.updatePriceHeader()
        self.clearInputWidgets()

        self.invoiceTable.removeAllRows()

        self.autoCalcStateOff.enable()

        self.statusBar().showMessage("Successfully reset form.")

    def returnFocus(self):
        self.descriptionEdit.setFocus()

    def revert(self):
        messageBox = self.createMessageBox("Reverting to the last printed invoice",
                                           "Do you really want to revert?")

        if messageBox.exec_() == QMessageBox.Cancel:
            return

        if self.lastPrintedInvoice != None:
            self.resetForm()

            typeIndex = self.typeCombobox.findText(self.lastPrintedInvoice["type"])
            self.typeCombobox.setCurrentIndex(typeIndex)

            customerIndex = self.customerCombobox.findText(self.lastPrintedInvoice["customer"])
            self.customerCombobox.setCurrentIndex(customerIndex)

            self.vatEdit.setText(self.lastPrintedInvoice["vatRate"])
            self.numberEdit.setText(self.lastPrintedInvoice["number"])

            self.lastPrintedInvoice["weightHeader"].setChecked(True)
            self.lastPrintedInvoice["ppuHeader"].setChecked(True)
            self.updateWeightHeader()
            self.updatePriceHeader()

            for row in self.lastPrintedInvoice["payloads"]:
                self.addRow(*row)

            if self.lastPrintedInvoice["autoCalc"] == "On":
                self.autoCalcStateOn.enable()
            else:
                self.autoCalcStateOff.enable()

            self.statusBar().showMessage("Successfully reverted to last printed invoice.")
        else:
            QMessageBox.information(self, "Cannot revert at this time",
                                    "There is no previous invoice for this session.")

    def saveVat(self):
        cp = ConfigParser()
        cp.read(self.settingsFile)
        cp.set("vat", "rate",
               self.vatEdit.text())

        with open(self.settingsFile, "w") as file:
                cp.write(file)

        self.statusBar().showMessage("VAT rate successfully saved to file.")

    def setDate(self, date):
        self.date = date

    def setInvoiceNumber(self, value):
        self.numberEdit.setText(value)

    def setVatRate(self, value):
        self.vatEdit.setText(value)

    def showAboutInvoice(self):
        QMessageBox.about(self, "About Invoice", "Invoice version {}\n".format(__VERSION__)
                          + "Python {}\n".format(__PYTHON__)
                          + "QT {}\n".format(__QT__)
                          + "PYQT {}\n".format(__PYQT__)
                          + "Copyright \N{COPYRIGHT SIGN} John Orchard & Company 2011")

    def showAboutQt(self):
        QMessageBox.aboutQt(self, "About Qt")

    def showBackdateDialog(self):
        dialog = backdateDialog(self)
        if dialog.exec_():
            self.backdate = True
            date = dialog.dateWidget.date()
            self.date = "{:0>2}/{:0>2}/{}".format(date.day(),
                                                  date.month(),
                                                  date.year())
        else:
            pass

    def showDatabaseDialog(self):
        dialog = DatabaseDialog(self)
        dialog.exec_()
        self.populateCustomerComboBox()

    def stripCommas(self, string):
        return string.replace(",", "")

    def toggleAutoCalculation(self):
        if self.autoCalcStatus.text() == "On":
            self.autoCalcStateOff.enable()
        elif self.autoCalcStatus.text() == "Off":
            self.autoCalcStateOn.enable()

        self.changed()

    def updatePriceHeader(self):
        newPrice = "Price ({})".format(self.priceGroup.checkedButton().text())

        self.pricePerUnitLabel.setText(self.changeRichText(self.pricePerUnitLabel, newPrice))

    def updateWeightHeader(self):
        newWeight = "Weight ({})".format(self.weightGroup.checkedButton().text())

        self.weightLabel.setText(self.changeRichText(self.weightLabel, newWeight))

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = InvoiceWindow()
    application.setOrganizationName("John Orchard & Company")
    application.setOrganizationDomain("orchard.com")
    application.setApplicationName("Orchard Invoice")
    application.setApplicationVersion(__VERSION__)
    mainWindow.show()
    sys.exit(application.exec_())
