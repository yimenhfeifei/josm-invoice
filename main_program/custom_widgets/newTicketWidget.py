try:
    import sys
    from decimal import Decimal
    from datetime import datetime
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import new_ticket_widget_generated
    from ticket_review_dialog import TicketReviewDialog
    from custom_widgets.vehicleDialog import VehicleDialog
    from shared_modules.ticket import Ticket
    from shared_modules.customer import Customer
    from shared_modules.payload import Payload
    from shared_modules.vehicle import Vehicle
    from custom_widgets.customerWidget import CustomerWidget
    from custom_widgets.weightWidget import WeightWidget
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
        
        self.classesToValidate = (CustomerWidget,
                                  WeightWidget)
        
        self.payloadTableWidget.setHorizontalHeaderLabels(["Weight",
                                                           "Material",
                                                           "Value",
                                                           "Delete"])
        
        self.connect(self.customerWidget, SIGNAL("widgetChanged()"),
                     self.update)
        
        self.connect(self.payloadWidget, SIGNAL("newPayloadTotal(QString, QString, bool)"),
                     self.payloadTotalWidget, SLOT("updatePayloadTotal(QString, QString, bool)"))
        
        self.connect(self.payloadTableWidget, SIGNAL("updateTicketTotal()"),
                     self.updateTicketTotal)
        
        self.connect(self.payloadTotalWidget, SIGNAL("addPayload()"),
                     self.addPayload)
        
        self.connect(self.deletePayloadButton, SIGNAL("clicked()"),
                     self.deletePayload)
        
        self.connect(self.editPayloadButton, SIGNAL("clicked()"),
                     self.deletePayload)
        
        self.connect(self.payloadTableWidget, SIGNAL("cellDoubleClicked(int, int)"),
                     self.onPayloadTableDoubleClicked)
        
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
        if column == materialColumn and id(item) in self.vehicles:
            d = VehicleDialog(self.vehicles[id(item)])
            if d.exec_():
                self.vehicles[id(item)] = d.getFields()
                
    def collectPayload(self):
        return (self.payloadWidget.getNetWeight(),
                self.payloadWidget.getMaterial(),
                self.payloadTotalWidget.getPayloadValue())
    
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
        
    def vehicleSelected(self):
        return self.payloadWidget.vehicleSelected()
        
    def setVehicleItemFont(self, item):
        item.setTextColor(Qt.blue)
        item.setFont(QFont("Monospace", weight=QFont.Bold))

    def addPayload(self):
        self.payloadTableWidget.setCurrentToEmptyRow()
        
        for column, string in enumerate(self.collectPayload()):
            string = self.formatString(column, string)
                
            item = QTableWidgetItem(string)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            
            if self.vehicleSelected() and column == self.payloadTableWidget.materialColumn:
                self.setVehicleItemFont(item)
                self.vehicles[id(item)] = self.payloadWidget.getVehicleDetails()
            
            row = self.payloadTableWidget.currentRow()
            self.payloadTableWidget.setItem(row, column, item)
            
            #self.addDeleteButton(row)
            
        self.payloadWidget.reset()
            
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
    
    def updateReviewTicketButton(self):
        if self.payloadTableWidget.isValid() and self.customerWidget.isValid():
            self.reviewTicketButton.setEnabled(True)
        else:
            self.reviewTicketButton.setEnabled(False)
            
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
    
    def updateTicketTotal(self):
        self.ticketTotalLabel.setText(str(self.payloadTableWidget.getTotal()))
    
    def reviewTicket(self):
        ticket = self.makeTicket()
        TicketReviewDialog(ticket).exec_()
        
    def update(self):
        self.updateReviewTicketButton()
        super(NewTicketWidget, self).update()
