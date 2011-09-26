try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import vehicle_dialog_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class VehicleDialog(QDialog, vehicle_dialog_generated.Ui_vehicleDialog):
    
    def __init__(self, vehicle, parent=None):
        super(VehicleDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.vehicleWidgets = [self.makeEdit,
                               self.modelEdit,
                               self.vehicleRegistrationEdit,
                               self.vinEdit]
        
        self.makeEdit.setText(vehicle["make"])
        self.modelEdit.setText(vehicle["model"])
        self.colourCombobox.setCurrentIndex(vehicle["colour"])
        self.vehicleRegistrationEdit.setText(vehicle["reg"])
        self.vinEdit.setText(vehicle["vin"])
        self.idCombobox.setCurrentIndex(vehicle["id"])
        
        for widget in self.vehicleWidgets:
            self.connect(widget, SIGNAL("textChanged(QString)"),
                         self.changed)
            
        self.changed()
    
    def changed(self):
        for widget in self.vehicleWidgets:
            widget.validate()