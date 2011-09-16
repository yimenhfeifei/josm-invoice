try:
    import sys
    from decimal import Decimal
    from datetime import datetime
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import new_ticket_widget_generated
    from ticket_review_dialog import TicketReviewDialog
    from vehicle_dialog import VehicleDialog
    from shared_modules.ticket import Ticket
    from shared_modules.customer import Customer
    from shared_modules.payload import Payload
    from shared_modules.vehicle import Vehicle
    from custom_widgets import grossWeightLineEdit
    from custom_widgets import tareWeightLineEdit
    from custom_widgets import netWeightLineEdit
    from custom_widgets import validatingLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class NewTicketWidget(QWidget,
                      new_ticket_widget_generated.Ui_newTicketWidget):
    
    calculateTotalValue = pyqtSignal()

    def __init__(self, parent=None):
        super(NewTicketWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.vehicles = {}
        
        self.classesToValidate = (grossWeightLineEdit.GrossWeightLineEdit,
                                  tareWeightLineEdit.TareWeightLineEdit,
                                  netWeightLineEdit.NetWeightLineEdit,
                                  validatingLineEdit.ValidatingLineEdit)
        
        self.validationCandidates = []
        for candidate in self.getValidationCandidates(self):
            self.validationCandidates.append(candidate)
        
        self.populateMaterialCombobox()
        
        self.populateTypeCombobox()
        
        self.payloadTableWidget.setHorizontalHeaderLabels(["Weight",
                                                           "Material",
                                                           "Value",
                                                           "Delete"])
        
        for lineEdit in self.validationCandidates:
            self.connect(lineEdit, SIGNAL("textEdited(QString)"),
                         lineEdit.validate)
            
        for lineEdit in self.validationCandidates:
            self.connect(lineEdit, SIGNAL("textChanged(QString)"),
                         self.update)
            
        self.connect(self.catalyticCheckbox, SIGNAL("toggled(bool)"),
                         self.catalyticLineEdit.setEnabled)
        
        self.connect(self.materialCombobox, SIGNAL("currentIndexChanged(int)"),
                         self.onMaterialComboboxChanged)
        
        self.connect(self.materialCombobox, SIGNAL("currentIndexChanged(int)"),
                         self.update)
        
        self.connect(self.typeCombobox, SIGNAL("currentIndexChanged(int)"),
                         self.update)
        
        self.connect(self.manualPriceCheckbox, SIGNAL("toggled(bool)"),
                         self.update)
        
        self.connect(self.manualPriceCheckbox, SIGNAL("toggled(bool)"),
                         self.payloadValueLineEdit.setReadOnlyInverted)
        
        self.connect(self.manualPriceCheckbox, SIGNAL("toggled(bool)"),
                         self.payloadValueLineEdit.clearPayloadValue)
        
        self.connect(self.catalyticCheckbox, SIGNAL("toggled(bool)"),
                         self.update)
        
        self.connect(self.grossWeightLineEdit, SIGNAL("textEdited(QString)"),
                         self.grossWeightLineEdit.onTextEdited)
        
    def getValidationCandidates(self, widget):
        for widget in widget.children():
            if isinstance(widget, QGroupBox):
                for result in self.getValidationCandidates(widget):
                    yield result
            else:
                if isinstance(widget, self.classesToValidate):
                    yield widget
        
    def getWidgetsToValidate(self, candidates):
        for candidate in candidates:
            if candidate.isEnabled():
                yield candidate
                
    def onMaterialComboboxChanged(self):
        index = self.materialCombobox.findText("Vehicle")
        if self.materialCombobox.currentIndex() == index:
            self.vehicleGroupBox.setEnabled(True)
        else:
            self.vehicleGroupBox.setEnabled(False)
        
    def loadVehicleDetails(self, vehicle):
        self.typeCombobox.setCurrentIndex(vehicle["typeIndex"])
        self.typeCombobox.setItemData(self.typeCombobox.currentIndex(),
                                      Decimal(vehicle["typeValue"]))
        self.makeLineEdit.setText(vehicle["make"])
        self.modelLineEdit.setText(vehicle["model"])
        self.colourCombobox.setCurrentIndex(vehicle["colourIndex"])
        self.vehicleRegistrationLineEdit.setText(vehicle["registration"])
        self.vinLineEdit.setText(vehicle["vin"])
        self.catalyticCheckbox.setChecked(vehicle["catalyticCheckbox"])
        self.catalyticLineEdit.setText(vehicle["catalyticValue"])
        self.idCombobox.setCurrentIndex(vehicle["idIndex"])
        
        self.typeCombobox.setEnabled(False)
        self.catalyticLineEdit.setReadOnly(True)
        
        for widget in self.dialogWidgets:
            widget.validate()
        
    def onCellClicked(self, row, column):
        if column == self.payloadTableWidget.getDeleteColumn():
            self.payloadTableWidget.selectRow(row)
            self.deletePayload()
        
    def onPayloadTableDoubleClicked(self, row, column):
        materialColumn = self.payloadTableWidget.getMaterialColumn()
        item = self.payloadTableWidget.item(row, materialColumn)
        if id(item) in self.vehicles:
            self.loadVehicleDetails(self.vehicles[id(item)])
            # code to update details if edited
                
    def collectPayload(self):
        return (self.netWeightLineEdit.text(),
                self.materialCombobox.currentText(),
                self.payloadValueLineEdit.text())
    
    def addDeleteButton(self, row):
        deleteItem = QTableWidgetItem("Delete")
        deleteItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        deleteItem.setTextColor(Qt.red)
        deleteItem.setFont(QFont("Monospace", weight=QFont.Bold))
        
        self.payloadTableWidget.setItem(row, 3, deleteItem)
        
    def formatString(self, column, string):
        weightColumn = self.payloadTableWidget.getWeightColumn()
        valueColumn = self.payloadTableWidget.getValueColumn()
        
        if column == valueColumn or column == weightColumn:
            return "{:.2f}".format(Decimal(string))
        else:
            return string
        
    def vehiclePresent(self, column):
        materialColumn = self.payloadTableWidget.getMaterialColumn()
        
        if column == materialColumn and self.vehicleDialogResult:
            return True
        else:
            return False
        
    def setVehicleItemFont(self, item):
        item.setText(self.vehicleDialogResult["typeText"])
        item.setTextColor(Qt.blue)
        item.setFont(QFont("Monospace", weight=QFont.Bold))

    def addPayload(self):
        self.payloadTableWidget.setCurrentToEmptyRow()
        
        for column, string in enumerate(self.collectPayload()):
            string = self.formatString(column, string)
                
            item = QTableWidgetItem(string)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            
            if self.vehiclePresent(column):
                self.setVehicleItemFont(item)
                self.vehicles[id(item)] = self.vehicleDialogResult.copy()
                self.vehicleDialogResult = None
            
            row = self.payloadTableWidget.currentRow()
            self.payloadTableWidget.setItem(row, column, item)
            
            self.addDeleteButton(row)
            
    def deletePayload(self):
        table = self.payloadTableWidget
        
        table.setItem(table.currentRow(),
                      self.payloadTableWidget.getValueColumn(),
                      QTableWidgetItem("00.00"))
        
        try:
            del self.vehicles[id(table.item(table.currentRow(),
                                            table.getMaterialColumn()))]
        except KeyError:
            pass
        
        table.removeRow(table.currentRow())
        self.update()
        
    def populateMaterialCombobox(self):
        self.materialCombobox.addItem("Copper", "5.00")
        self.materialCombobox.addItem("Iron", "0.70")
        self.materialCombobox.addItem("Lead", "3.00")
        self.materialCombobox.addItem("Gold", "4.50")
        self.materialCombobox.addItem("Vehicle", "00.00")
        
    def populateTypeCombobox(self):
        self.typeCombobox.addItem("Banger", "1.00")
        self.typeCombobox.addItem("Bike", "0.70")
        self.typeCombobox.addItem("Car", "1.70")
        self.typeCombobox.addItem("Shell", "0.50")
        self.typeCombobox.addItem("Van", "1.60")
    
    def allWidgetsValidated(self):
        for widget in self.getWidgetsToValidate(self.validationCandidates):
            if not widget.getValidatedStatus():
                return False
        return True
    
    def updateReviewTicketButton(self):
        self.reviewTicketButton.setEnabled(self.allWidgetsValidated())
        
    def updateAddPayloadButton(self):
        netWeight = self.netWeightLineEdit.getValidatedStatus()
        payloadValue = self.payloadValueLineEdit.getValidatedStatus()

        if netWeight and payloadValue:
            self.addPayloadButton.setEnabled(True)
        else:
            self.addPayloadButton.setEnabled(False)
            
    def getNewTicketNumber(self):
        return "12000"
    
    def getTicketFields(self):
        return {"number": self.getNewTicketNumber(),
                "date": datetime.now().strftime("%Y/%m/%d"),
                "time": datetime.now().strftime("%H:%M"),
                "totalValue": self.totalValueLineEdit.text()}
    
    def getCustomerFields(self):
        return {"firstName": self.firstNameLineEdit.text(),
                "lastName": self.lastNameLineEdit.text(),
                "houseNumber": self.houseNumberLineEdit.text(),
                "street": self.streetLineEdit.text(),
                "town": self.townLineEdit.text(),
                "postcode": self.postcodeLineEdit.text(),
                "registration": self.vehicleRegistrationLineEdit.text()}
    
    def getPayloadFields(self):
        payloads = {}
        table = self.payloadTableWidget
        
        for row in range(table.rowCount()):
            fields = []
            for column in range(table.columnCount()):
                fields.append(table.item(row, column).text())
                
            materialItem = table.item(row, table.getMaterialColumn())
            
            try:
                fields.append(self.vehicles[id(materialItem)])
            except KeyError:
                fields.append(None)
                
            payloads["payload {}".format(row)] = {"weight": fields[0],
                                                  "material": fields[1],
                                                  "value": fields[2],
                                                  "vehicle": fields[4]}
        return payloads
    
    def getVehicleFields(self):
        return {"typeText": self.typeCombobox.currentText(),
        "typeValue": self.typeCombobox.itemData(self.typeCombobox.currentIndex()),
        "typeIndex": self.typeCombobox.currentIndex(),
        "make": self.makeLineEdit.text(),
        "model": self.modelLineEdit.text(),
        "colour": self.colourCombobox.currentText(),
        "colourIndex": self.colourCombobox.currentIndex(),
        "registration": self.vehicleRegistrationLineEdit.text(),
        "vin": self.vinLineEdit.text(),
        "catalyticCheckbox": self.catalyticCheckbox.isChecked(),
        "catalyticValue": self.catalyticLineEdit.text(),
        "id": self.idCombobox.currentText(),
        "idIndex": self.idCombobox.currentIndex()}
    
    def makeTicket(self):
        ticket = self.getTicketFields()
        customer = self.getCustomerFields()
        payloads = self.getPayloadFields()
        
        customerObject = Customer(customer)
        
        payloadObjects = []
        for payload in payloads.values():
            if payload["vehicle"]:
                vehicle = Vehicle(payload["vehicle"])
            else:
                vehicle = None
            payloadObjects.append(Payload(payload, vehicle))
        
        return Ticket(ticket, customerObject, payloadObjects)
    
    def reviewTicket(self):
        ticket = self.makeTicket()
        TicketReviewDialog(ticket).exec_()
        
    def update(self):
        self.updateReviewTicketButton()
        self.updateAddPayloadButton()
        super(NewTicketWidget, self).update()
