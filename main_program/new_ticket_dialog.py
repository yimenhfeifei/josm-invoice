try:
    import sys
    from decimal import Decimal
    from datetime import datetime
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import new_ticket_dialog_generated
    from ticket_review_dialog import TicketReviewDialog
    from vehicle_dialog import VehicleDialog
    from shared_modules.ticket import Ticket
    from shared_modules.customer import Customer
    from shared_modules.payload import Payload
    from shared_modules.vehicle import Vehicle
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class NewTicketDialog(QDialog,
                      new_ticket_dialog_generated.Ui_newTicketDialog):
    
    calculateTotalValue = pyqtSignal()

    def __init__(self, parent=None):
        super(NewTicketDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("New Ticket Details")
        
        self.dialogWidgets = (self.firstNameLineEdit,
                              self.lastNameLineEdit,
                              self.houseNumberLineEdit,
                              self.streetLineEdit,
                              self.townLineEdit,
                              self.postcodeLineEdit,
                              self.vehicleRegistrationLineEdit,
                              self.payloadTableWidget)
        
        self.vehicleDialogResult = None
        
        self.vehicles = {}
        
        self.populateMaterialCombobox()
        
        self.payloadTableWidget.setHorizontalHeaderLabels(["Weight",
                                                           "Material",
                                                           "Value",
                                                           "Delete"])
        
        self.connect(self.addPayloadButton, SIGNAL("clicked()"),
                     self.addPayload)

        self.connect(self.reviewTicketButton, SIGNAL("clicked()"),
                     self.reviewTicket)
        
        self.connect(self.payloadTableWidget, SIGNAL("cellClicked(int, int)"),
                     self.onCellClicked)
        
        self.connect(self.materialCombobox, SIGNAL("currentIndexChanged(QString)"),
                     self.onMaterialComboboxChange)
        
        self.connect(self.payloadTableWidget, SIGNAL("cellDoubleClicked(int, int)"),
                     self.onPayloadTableDoubleClicked)
        
    def onCellClicked(self, row, column):
        if column == self.payloadTableWidget.getDeleteColumn():
            self.payloadTableWidget.selectRow(row)
            self.deletePayload()
        
    def onPayloadTableDoubleClicked(self, row, column):
        materialColumn = self.payloadTableWidget.getMaterialColumn()
        item = self.payloadTableWidget.item(row, materialColumn)
        if id(item) in self.vehicles:
            vehicleDialog = VehicleDialog(vehicle=self.vehicles[id(item)])
            if vehicleDialog.exec_():
                self.vehicles[id(item)] = vehicleDialog.getFields()
        
    def processVehicleDialog(self, vehicleDialog):
        if vehicleDialog.exec_():
            self.vehicleDialogResult = vehicleDialog.getFields()
            
            materialComboboxIndex = self.materialCombobox.findText("Vehicle")
            self.materialCombobox.setItemData(materialComboboxIndex,
                                              self.vehicleDialogResult["typeValue"])
        
            if self.vehicleDialogResult["catalyticCheckbox"]:
                self.payloadValueLineEdit.onAddCatalyticValue(
                    self.vehicleDialogResult["catalyticValue"])
        else:
            self.vehicleDialogResult = None

    def onMaterialComboboxChange(self, selection):
        if selection == "Vehicle":
            vehicleDialog = VehicleDialog()
            
            self.processVehicleDialog(vehicleDialog)
                
            self.materialCombobox.onIndexChange()
                
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
    
    def getActiveWidgets(self):
        return [widget for widget in self.dialogWidgets if widget.isEnabled()]
    
    def allWidgetsValid(self):
        for widget in self.getActiveWidgets():
            if not widget.getValidatedStatus():
                return False
        return True
    
    def updateReviewTicketButton(self):
        self.reviewTicketButton.setEnabled(self.allWidgetsValid())
        
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
        super(NewTicketDialog, self).update()