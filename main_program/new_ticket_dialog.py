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
                              self.vehicleRegistrationLineEdit)
        
        self.setDynamicProperties(self.firstNameLineEdit,
                                  regexString="Name",
                                  minimumLength=10,
                                  mandatory=True,
                                  validated=False)
        
        self.setDynamicProperties(self.lastNameLineEdit,
                                  regexString="Name",
                                  minimumLength=10,
                                  mandatory=True,
                                  validated=False)
        
        self.setDynamicProperties(self.houseNumberLineEdit,
                                  regexString="HouseNumber",
                                  minimumLength=5,
                                  mandatory=True,
                                  validated=False)
        
        self.setDynamicProperties(self.streetLineEdit,
                                  regexString="Street",
                                  minimumLength=10,
                                  mandatory=True,
                                  validated=False)
        
        self.setDynamicProperties(self.townLineEdit,
                                  regexString="Name",
                                  minimumLength=10,
                                  mandatory=True,
                                  validated=False)
        
        self.setDynamicProperties(self.postcodeLineEdit,
                                  regexString="Postcode",
                                  minimumLength=5,
                                  mandatory=True,
                                  validated=False)
        
        self.setDynamicProperties(self.vehicleRegistrationLineEdit,
                                  regexString="VehicleRegistration",
                                  minimumLength=5,
                                  mandatory=True,
                                  validated=False)
        
        self.setValidators(self.dialogWidgets)
        
        self.connect(self.manualPriceCheckbox, SIGNAL("toggled(bool)"), 
                     self.payloadValueReadOnlyToggle)
    
    def payloadValueReadOnlyToggle(self, state):
        self.payloadValueLineEdit.setReadOnly(not state)