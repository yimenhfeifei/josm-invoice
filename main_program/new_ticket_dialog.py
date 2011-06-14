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

class NewTicketDialog(QDialog,
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
        
    def getActiveWidgets(self):
        return [widget for widget in self.dialogWidgets if widget.isEnabled()]
    
    def allWidgetsValid(self):
        for widget in self.getActiveWidgets():
            if not widget.getValidatedStatus():
                return False
        return True
    
    def updateReviewTicketButton(self):
        self.reviewTicketButton.setEnabled(self.allWidgetsValid())