try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import new_ticket_dialog_generated
    from vehicle_dialog import VehicleDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class NewTicketDialog(QDialog,
                      new_ticket_dialog_generated.Ui_newTicketDialog):
    
    calculateTotalValue = pyqtSignal()

    def __init__(self, parent=None):
        super(NewTicketDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.dialogWidgets = (self.firstNameLineEdit,
                              self.lastNameLineEdit,
                              self.houseNumberLineEdit,
                              self.streetLineEdit,
                              self.townLineEdit,
                              self.postcodeLineEdit,
                              self.vehicleRegistrationLineEdit,
                              self.payloadTableWidget)
        
        self.populateMaterialCombobox()
        
        self.payloadTableWidget.setHorizontalHeaderLabels(["Weight",
                                                           "Material",
                                                           "Value"])
        
        self.connect(self.addPayloadButton, SIGNAL("clicked()"),
                     self.addPayload)
        
        self.connect(self.deletePayloadButton, SIGNAL("clicked()"),
                     self.deletePayload)
        
        self.connect(self.materialCombobox, SIGNAL("currentIndexChanged(QString)"),
                     self.onMaterialComboboxChange)
        
    def onMaterialComboboxChange(self, selection):
        if selection == "Vehicle":
            vehicleDialog = VehicleDialog()
            if vehicleDialog.exec_():
                typeComboboxIndex = vehicleDialog.typeCombobox.currentIndex()
                typePrice = vehicleDialog.typeCombobox.itemData(typeComboboxIndex)
                
                if vehicleDialog.catalyticCheckbox.isChecked():
                    self.payloadValueLineEdit.onAddCatalyticValue(
                        vehicleDialog.catalyticLineEdit.text())
                
                materialComboboxIndex = self.materialCombobox.findText("Vehicle")
                self.materialCombobox.setItemData(materialComboboxIndex, typePrice)
                self.materialCombobox.onIndexChange()
                
    def collectPayload(self):
        return (self.netWeightLineEdit.text(),
                self.materialCombobox.currentText(),
                self.payloadValueLineEdit.text())

    def addPayload(self):
        self.payloadTableWidget.setCurrentToEmptyRow()
        
        for column, string in enumerate(self.collectPayload()):
            if column == self.payloadTableWidget.columnCount() - 1 or column == 0:
                string = "{:.2f}".format(Decimal(string))
            item = QTableWidgetItem(string)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            row = self.payloadTableWidget.currentRow()
            self.payloadTableWidget.setItem(row, column, item)
            
    def deletePayload(self):
        table = self.payloadTableWidget
        
        table.setItem(table.currentRow(),
                      self.payloadTableWidget.columnCount() - 1,
                      QTableWidgetItem("00.00"))
        
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
        
    def update(self):
        self.updateReviewTicketButton()
        self.updateAddPayloadButton()
        super(NewTicketDialog, self).update()