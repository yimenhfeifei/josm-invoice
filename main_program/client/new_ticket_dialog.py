try:
    import sys
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import new_ticket_dialog_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class NewTicketDialog(QDialog, new_ticket_dialog_generated.Ui_newTicketDialog):

    def __init__(self, parent=None):
        super(NewTicketDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.connect(self.manualPriceCheckbox, SIGNAL("toggled(bool)"), 
                     self.payloadValueReadOnlyToggle)
    
    def payloadValueReadOnlyToggle(self, state):
        self.payloadValueLineEdit.setReadOnly(not state)