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
                                  minimumLength=1,
                                  mandatory=True,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.lastNameLineEdit,
                                  regexString="Name",
                                  minimumLength=1,
                                  mandatory=True,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.houseNumberLineEdit,
                                  regexString="HouseNumber",
                                  minimumLength=1,
                                  mandatory=True,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.streetLineEdit,
                                  regexString="Street",
                                  minimumLength=2,
                                  mandatory=True,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.townLineEdit,
                                  regexString="Town",
                                  minimumLength=2,
                                  mandatory=True,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.postcodeLineEdit,
                                  regexString="Postcode",
                                  minimumLength=5,
                                  mandatory=True,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.vehicleRegistrationLineEdit,
                                  regexString="VehicleRegistration",
                                  minimumLength=5,
                                  mandatory=True,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.grossWeightLineEdit,
                                  regexString="Weight",
                                  minimumLength=1,
                                  mandatory=False,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.tareWeightLineEdit,
                                  regexString="Weight",
                                  minimumLength=1,
                                  mandatory=False,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.netWeightLineEdit,
                                  regexString="Weight",
                                  minimumLength=1,
                                  mandatory=True,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.connect(self.manualPriceCheckbox, SIGNAL("toggled(bool)"), 
                     self.payloadValueReadOnlyToggle)
        
        self.connect(self.grossWeightLineEdit, SIGNAL("textChanged(QString)"), 
                     self.calculateNetWeight)
        
        self.connect(self.tareWeightLineEdit, SIGNAL("textChanged(QString)"), 
                     self.calculateNetWeight)
        
        for widget in self.dialogWidgets:
            self.setValidator(widget)
            self.connect(widget, SIGNAL("textChanged(QString)"),
                     widget.property("onEditCallback"))
            
        self.validateWidgets()
    
    def payloadValueReadOnlyToggle(self, state):
        self.payloadValueLineEdit.setReadOnly(not state)
    
    def calculateNetWeight(self):
        try:
            grossValue = Decimal(self.grossWeightLineEdit.text())
            tareValue = Decimal(self.tareWeightLineEdit.text())
        except InvalidOperation:
            self.netWeightLineEdit.setText("00.00")
            return    
        
        if tareValue >= grossValue:
            self.tareWeightLineEdit.clear()
            self.netWeightLineEdit.setText("00.00")
            return
        
        netValue = Decimal(grossValue) - Decimal(tareValue)
        
        self.netWeightLineEdit.setText(str(netValue))
        
    def validateWidgets(self):
        if self.grossWeightLineEdit.text() == "":
            self.setGrossAndTareMandatory(False)
        else:
            self.setGrossAndTareMandatory(True)
        
        for widget in self.dialogWidgets:
            if widget.property("mandatory"):
                self.validate(widget)
            else:
                if widget.text() == "":
                    widget.setProperty("validated", True)
        
        self.updateInterface()
    
    def setGrossAndTareMandatory(self, manStatus):
        self.grossWeightLineEdit.setProperty("mandatory", manStatus)
        self.tareWeightLineEdit.setProperty("mandatory", manStatus)
    
    def updateInterface(self):
        for widget in self.dialogWidgets:
            self.updateStyleSheet(widget)
        
        weightFlag = self.grossWeightLineEdit.property("mandatory")
        self.tareWeightLineEdit.setEnabled(weightFlag)
        self.netWeightLineEdit.setReadOnly(weightFlag)
        
        if self.allWidgetsPassedValidation(self.dialogWidgets):
            self.reviewTicketButton.setEnabled(True)
        else:
            self.reviewTicketButton.setEnabled(False)