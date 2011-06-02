try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import vehicle_dialog_generated
    from shared_modules.custom_qdialog import CustomQDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class VehicleDialog(CustomQDialog, vehicle_dialog_generated.Ui_vehicleDialog):

    def __init__(self, parent=None):
        super(VehicleDialog, self).__init__(parent)
        self.setupUi(self)