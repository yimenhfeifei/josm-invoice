try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import vehicle_dialog_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class VehicleDialog(QDialog, vehicle_dialog_generated.Ui_vehicleDialog):

    def __init__(self, parent=None):
        super(VehicleDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.dialogWidgets = (self.makeLineEdit,
                              self.modelLineEdit,
                              self.vehicleRegistrationLineEdit,
                              self.vinLineEdit,
                              self.catalyticLineEdit)

    def getActiveWidgets(self):
        return [widget for widget in self.dialogWidgets if widget.isEnabled()]
    
    def allWidgetsValid(self):
        for widget in self.getActiveWidgets():
            if not widget.getValidatedStatus():
                return False
        return True
    
    def updateAcceptButton(self):
        self.acceptButton.setEnabled(self.allWidgetsValid())

    def update(self):
        self.updateAcceptButton()
        super(VehicleDialog, self).update()