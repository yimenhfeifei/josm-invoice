try:
    import sys
    from decimal import Decimal
    from decimal import InvalidOperation
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import new_ticket_dialog_generated
    from shared_modules.custom_qdialog import CustomQDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class NewTicketDialog(CustomQDialog,
                      new_ticket_dialog_generated.Ui_newTicketDialog):
    
    grossWeightEmpty = pyqtSignal(name='grossWeightEmpty')
    grossWeightNotEmpty = pyqtSignal(name='grossWeightNotEmpty')
    checkForEmptyTareWeight = pyqtSignal(name='checkForEmptyTareWeight')
    tareWeightEmpty = pyqtSignal(name='tareWeightEmpty')
    tareWeightNotEmpty = pyqtSignal(name='tareWeightNotEmpty')
    guiNeedsUpdate = pyqtSignal(name='guiNeedsUpdate')
    grossWeightValid = pyqtSignal(name='grossWeightValid')
    grossWeightInvalid= pyqtSignal(name='grossWeightInvalid')
    tareWeightValid = pyqtSignal(name='tareWeightValid')
    tareWeightInvalid= pyqtSignal(name='tareWeightInvalid')
    tareAndGrossValid = pyqtSignal(name='tareAndGrossValid')

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
                              self.grossWeightLineEdit,
                              self.tareWeightLineEdit,
                              self.netWeightLineEdit)
        
        self.setDynamicProperties(self.firstNameLineEdit,
                                  regexString="Name",
                                  validated=False,
                                  onEditCallback=self.updateDialog)
        
        self.setDynamicProperties(self.lastNameLineEdit,
                                  regexString="Name",
                                  validated=False,
                                  onEditCallback=self.updateDialog)
        
        self.setDynamicProperties(self.houseNumberLineEdit,
                                  regexString="HouseNumber",
                                  validated=False,
                                  onEditCallback=self.updateDialog)
        
        self.setDynamicProperties(self.streetLineEdit,
                                  regexString="Street",
                                  validated=False,
                                  onEditCallback=self.updateDialog)
        
        self.setDynamicProperties(self.townLineEdit,
                                  regexString="Town",
                                  validated=False,
                                  onEditCallback=self.updateDialog)
        
        self.setDynamicProperties(self.postcodeLineEdit,
                                  regexString="Postcode",
                                  validated=False,
                                  onEditCallback=self.updateDialog)
        
        self.setDynamicProperties(self.vehicleRegistrationLineEdit,
                                  regexString="VehicleRegistration",
                                  validated=False,
                                  onEditCallback=self.updateDialog)
        
        self.setDynamicProperties(self.grossWeightLineEdit,
                                  regexString="optionalWeight",
                                  validated=True,
                                  onEditCallback=self.updateGrossWeight)
        
        self.setDynamicProperties(self.tareWeightLineEdit,
                                  regexString="optionalWeight",
                                  validated=True,
                                  onEditCallback=self.updateTareWeight)
        
        self.setDynamicProperties(self.netWeightLineEdit,
                                  regexString="NetWeight",
                                  validated=False,
                                  onEditCallback=self.updateDialog)
        
        self.connect(self.manualPriceCheckbox, SIGNAL("toggled(bool)"), 
                     self.payloadValueReadOnlyToggle)
        
        self.guiNeedsUpdate.connect(self.updateInterface)
        
        self.grossWeightEmpty.connect(self.disableTareWeight)
        
        self.grossWeightEmpty.connect(self.enableNetWeight)
        
        self.grossWeightEmpty.connect(self.clearTareWeight)
        
        self.grossWeightEmpty.connect(self.validateTareWeight)
        
        self.grossWeightEmpty.connect(self.validateGrossWeight)
        
        self.grossWeightNotEmpty.connect(self.enableTareWeight)
        
        self.grossWeightNotEmpty.connect(self.disableNetWeight)
        
        self.grossWeightNotEmpty.connect(self.emitTareWeightEmptyStatus)
        
        self.grossWeightNotEmpty.connect(self.validateGrossWeight)
        
        self.tareWeightEmpty.connect(self.makeTareWeightInvalid)
        
        self.tareWeightNotEmpty.connect(self.validateTareWeight)
        
        self.tareWeightNotEmpty.connect(self.determineTareAndGrossStatus)
        
        self.tareAndGrossValid.connect(self.calculateNetWeight)
        
        self.grossWeightInvalid.connect(self.clearNetWeight)
        
        self.tareWeightInvalid.connect(self.clearNetWeight)
        
        self.tareWeightInvalid.connect(self.makeTareWeightInvalid)
        
        self.grossWeightValid.connect(self.determineTareAndGrossStatus)
        
        for widget in self.dialogWidgets:
            self.connect(widget, SIGNAL("textChanged(QString)"),
                     widget.property("onEditCallback"))
        
        self.updateInterface()
    
    def enableTareWeight(self):
        self.tareWeightLineEdit.setEnabled(True)
    
    def disableTareWeight(self):
        self.tareWeightLineEdit.setEnabled(False)
    
    def enableNetWeight(self):
        self.netWeightLineEdit.setReadOnly(False)
    
    def disableNetWeight(self):
        self.netWeightLineEdit.setReadOnly(True)
    
    def clearTareWeight(self):
        self.tareWeightLineEdit.clear()
        self.guiNeedsUpdate.emit()
        
    def clearNetWeight(self):
        self.netWeightLineEdit.clear()
        self.guiNeedsUpdate.emit()
    
    def emitTareWeightEmptyStatus(self):
        if self.tareWeightLineEdit.text() == "":
            self.tareWeightEmpty.emit()
        else:
            self.tareWeightNotEmpty.emit()
        
    def determineTareAndGrossStatus(self):
        if self.allWidgetsPassedValidation((self.grossWeightLineEdit,
                                            self.tareWeightLineEdit)) == False:
            return
        
        try:
            grossValue = Decimal(self.grossWeightLineEdit.text())
            tareValue = Decimal(self.tareWeightLineEdit.text())
        except InvalidOperation:
            return
        
        if tareValue >= grossValue:
            self.tareWeightInvalid.emit()
        else:
            self.tareAndGrossValid.emit()
        
    def makeTareWeightInvalid(self):
        self.tareWeightLineEdit.setProperty("validated", False)
        self.guiNeedsUpdate.emit()
    
    def updateGrossWeight(self):
        if self.grossWeightLineEdit.text() == "":
            self.grossWeightEmpty.emit()
        else:
            self.grossWeightNotEmpty.emit()
            
    def updateTareWeight(self):
        self.emitTareWeightEmptyStatus()
        
    def validateTareWeight(self):
        self.validate(self.tareWeightLineEdit)
        if self.tareWeightLineEdit.property("validated"):
            self.tareWeightValid.emit()
        else:
            self.tareWeightInvalid.emit()
        self.guiNeedsUpdate.emit()
    
    def validateGrossWeight(self):
        self.validate(self.grossWeightLineEdit)
        if self.grossWeightLineEdit.property("validated"):
            self.grossWeightValid.emit()
        else:
            self.grossWeightInvalid.emit()
        self.guiNeedsUpdate.emit()
    
    def payloadValueReadOnlyToggle(self, state):
        self.payloadValueLineEdit.setReadOnly(not state)
        
    def updateDialog(self):
        self.validate(self.sender())
        self.guiNeedsUpdate.emit()
    
    def calculateNetWeight(self):
        grossValue = Decimal(self.grossWeightLineEdit.text())
        tareValue = Decimal(self.tareWeightLineEdit.text())
    
        netValue = grossValue - tareValue
        self.netWeightLineEdit.setText(str(netValue))
    
    def updateInterface(self):
        for widget in self.dialogWidgets:
            self.updateStyleSheet(widget)
        
        if self.allWidgetsPassedValidation(self.dialogWidgets):
            self.reviewTicketButton.setEnabled(True)
        else:
            self.reviewTicketButton.setEnabled(False)