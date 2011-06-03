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
        
        self.widgetRegexStrings = ("Name", "Name", "HouseNumber", "Street",
                                   "Name", "Postcode", "VehicleRegistration")
        
        self.widgetMinimumLengths = (10, 10, 5, 10, 10, 10, 10)
        
        self.widgetMandatoryStatus = (True, True, True, True, True,
                                      True, True)
        
        self.setDynamicProperties("regexString", self.dialogWidgets,
                           self.widgetRegexStrings)
        
        self.setDynamicProperties("minimumLength", self.dialogWidgets,
                           self.widgetMinimumLengths)
        
        self.setDynamicProperties("mandatory", self.dialogWidgets,
                           self.widgetMandatoryStatus)
        
        self.setValidators(self.dialogWidgets)
        
        self.connect(self.manualPriceCheckbox, SIGNAL("toggled(bool)"), 
                     self.payloadValueReadOnlyToggle)
    
    def payloadValueReadOnlyToggle(self, state):
        self.payloadValueLineEdit.setReadOnly(not state)