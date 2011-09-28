try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import payload_widget_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class PayloadWidget(QWidget, payload_widget_generated.Ui_payloadWidget):

    newPayloadTotal = pyqtSignal("QString", "QString", "bool")
    
    def __init__(self, parent=None):
        super(PayloadWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.connect(self.weightWidget, SIGNAL("widgetChanged()"),
                     self.changed)
        
        self.connect(self.materialWidget, SIGNAL("widgetChanged()"),
                     self.changed)
        
    def changed(self):
        self.newPayloadTotal.emit(self.weightWidget.getNetWeight(),
                                  self.materialWidget.getPricePerUnit(),
                                  self.materialWidget.isValid())
        
    def getNetWeight(self):
        return self.weightWidget.getNetWeight()
    
    def getMaterial(self):
        return self.materialWidget.getMaterial()
    
    def vehicleSelected(self):
        return self.materialWidget.vehicleSelected()
    
    def getVehicleDetails(self):
        return self.materialWidget.getVehicleDetails()
    
    def reset(self):
        self.weightWidget.reset()
        self.materialWidget.reset()
        
    def isMaterialValid(self):
        return self.materialWidget.isValid()
    
    def isWeightValid(self):
        return self.weightWidget.isValid()
