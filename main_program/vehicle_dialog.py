try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import vehicle_dialog_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class VehicleDialog(QDialog, vehicle_dialog_generated.Ui_vehicleDialog):

    def __init__(self, parent=None, vehicle=None):
        super(VehicleDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.setWindowTitle("New Vehicle Details")
        
        self.dialogWidgets = (self.makeLineEdit,
                              self.modelLineEdit,
                              self.vehicleRegistrationLineEdit,
                              self.vinLineEdit,
                              self.catalyticLineEdit)
        
        self.populateTypeCombobox()
        
        if vehicle:
            self.setWindowTitle("Edit Vehicle Details")
            
            self.typeCombobox.setCurrentIndex(vehicle["typeIndex"])
            self.typeCombobox.setItemData(self.typeCombobox.currentIndex(),
                                          Decimal(vehicle["typeValue"]))
            self.makeLineEdit.setText(vehicle["make"])
            self.modelLineEdit.setText(vehicle["model"])
            self.colourCombobox.setCurrentIndex(vehicle["colourIndex"])
            self.vehicleRegistrationLineEdit.setText(vehicle["registration"])
            self.vinLineEdit.setText(vehicle["vin"])
            self.catalyticCheckbox.setChecked(vehicle["catalyticCheckbox"])
            self.catalyticLineEdit.setText(vehicle["catalyticValue"])
            self.idCombobox.setCurrentIndex(vehicle["idIndex"])
            
            self.typeCombobox.setEnabled(False)
            self.catalyticLineEdit.setReadOnly(True)
            
            for widget in self.dialogWidgets:
                widget.validate()
                
        self.update()

    def populateTypeCombobox(self):
        self.typeCombobox.addItem("Banger", "1.00")
        self.typeCombobox.addItem("Bike", "0.70")
        self.typeCombobox.addItem("Car", "1.70")
        self.typeCombobox.addItem("Shell", "0.50")
        self.typeCombobox.addItem("Van", "1.60")
        
    def getFields(self):
        return {"typeText": self.typeCombobox.currentText(),
        "typeValue": self.typeCombobox.itemData(self.typeCombobox.currentIndex()),
        "typeIndex": self.typeCombobox.currentIndex(),
        "make": self.makeLineEdit.text(),
        "model": self.modelLineEdit.text(),
        "colour": self.colourCombobox.currentText(),
        "colourIndex": self.colourCombobox.currentIndex(),
        "registration": self.vehicleRegistrationLineEdit.text(),
        "vin": self.vinLineEdit.text(),
        "catalyticCheckbox": self.catalyticCheckbox.isChecked(),
        "catalyticValue": self.catalyticLineEdit.text(),
        "id": self.idCombobox.currentText(),
        "idIndex": self.idCombobox.currentIndex()}
        
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