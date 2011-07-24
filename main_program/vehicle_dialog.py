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
            
            self.typeCombobox.setCurrentIndex(vehicle["TypeIndex"])
            self.typeCombobox.setItemData(self.typeCombobox.currentIndex(),
                                          Decimal(vehicle["TypeValue"]))
            self.makeLineEdit.setText(vehicle["Make"])
            self.modelLineEdit.setText(vehicle["Model"])
            self.colourCombobox.setCurrentIndex(vehicle["ColourIndex"])
            self.vehicleRegistrationLineEdit.setText(vehicle["Registration"])
            self.vinLineEdit.setText(vehicle["Vin"])
            self.catalyticCheckbox.setChecked(vehicle["CatalyticCheckbox"])
            self.catalyticLineEdit.setText(vehicle["CatalyticValue"])
            self.idCombobox.setCurrentIndex(vehicle["IdIndex"])
            
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
        
    def getDialogResult(self):
        return {"TypeText": self.typeCombobox.currentText(),
        "TypeValue": self.typeCombobox.itemData(self.typeCombobox.currentIndex()),
        "TypeIndex": self.typeCombobox.currentIndex(),
        "Make": self.makeLineEdit.text(),
        "Model": self.modelLineEdit.text(),
        "Colour": self.colourCombobox.currentText(),
        "ColourIndex": self.colourCombobox.currentIndex(),
        "Registration": self.vehicleRegistrationLineEdit.text(),
        "Vin": self.vinLineEdit.text(),
        "CatalyticCheckbox": self.catalyticCheckbox.isChecked(),
        "CatalyticValue": self.catalyticLineEdit.text(),
        "Id": self.idCombobox.currentText(),
        "IdIndex": self.idCombobox.currentIndex()}
        
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