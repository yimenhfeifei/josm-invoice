try:
    import sys
    
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
                                  minimumLength=4,
                                  mandatory=False,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.tareWeightLineEdit,
                                  regexString="Weight",
                                  minimumLength=4,
                                  mandatory=False,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.setDynamicProperties(self.netWeightLineEdit,
                                  regexString="Weight",
                                  minimumLength=4,
                                  mandatory=True,
                                  validated=False,
                                  onEditCallback=self.validateWidgets)
        
        self.connect(self.manualPriceCheckbox, SIGNAL("toggled(bool)"), 
                     self.payloadValueReadOnlyToggle)
        
        for widget in self.dialogWidgets:
            self.setValidator(widget)
            self.connect(widget, SIGNAL("textChanged(QString)"),
                     widget.property("onEditCallback"))
            
        self.validateWidgets()
    
    def payloadValueReadOnlyToggle(self, state):
        self.payloadValueLineEdit.setReadOnly(not state)
        
    def validateWidgets(self):
        self.toggleWeightWidgets()
        
        for widget in self.dialogWidgets:
            if widget.property("mandatory"):
                self.validate(widget)
            else:
                if widget.text() == "":
                    widget.setProperty("validated", True)
        
        self.updateInterface()
    
    def toggleWeightWidgets(self):
        if self.grossWeightLineEdit.text() == "":
            self.grossWeightLineEdit.setProperty("mandatory", False)
            self.tareWeightLineEdit.setProperty("mandatory", False)
            self.tareWeightLineEdit.setEnabled(False)
            self.netWeightLineEdit.setReadOnly(False)
        else:
            self.grossWeightLineEdit.setProperty("mandatory", True)
            self.tareWeightLineEdit.setProperty("mandatory", True)
            self.tareWeightLineEdit.setEnabled(True)
            self.netWeightLineEdit.setReadOnly(True)
    
    def updateInterface(self):
        for widget in self.dialogWidgets:
            self.updateStyleSheet(widget)
        
        if self.allWidgetsPassedValidation(self.dialogWidgets):
            self.reviewTicketButton.setEnabled(True)
        else:
            self.reviewTicketButton.setEnabled(False)