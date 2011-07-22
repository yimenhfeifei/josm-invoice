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
        
        self.populateTypeCombobox()

    def populateTypeCombobox(self):
        self.typeCombobox.addItem("Banger", "1.00")
        self.typeCombobox.addItem("Bike", "0.70")
        self.typeCombobox.addItem("Car", "1.70")
        self.typeCombobox.addItem("Shell", "0.50")
        self.typeCombobox.addItem("Van", "1.60")
        
    def getDialogResult(self):
        return {"TypeText": self.typeCombobox.currentText(),
        "TypeValue": self.typeCombobox.itemData(self.typeCombobox.currentIndex()),
        "Make": self.makeLineEdit.text(),
        "Model": self.modelLineEdit.text(),
        "Colour": self.colourCombobox.currentText(),
        "Registration": self.vehicleRegistrationLineEdit.text(),
        "Vin": self.vinLineEdit.text(),
        "CatalyticCheckbox": self.catalyticCheckbox.isChecked(),
        "CatalyticValue": self.catalyticLineEdit.text(),
        "Id": self.idCombobox.currentText()}
        
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