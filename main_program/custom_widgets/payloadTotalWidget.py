try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import payload_total_widget_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class PayloadTotalWidget(QWidget,
                         payload_total_widget_generated.Ui_payloadTotalWidget):
    
    addPayload = pyqtSignal()
    
    def __init__(self, parent=None):
        super(PayloadTotalWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.connect(self.addPayloadButton, SIGNAL("clicked()"),
                     self.addPayload.emit)
    
    @pyqtSlot("QString", "QString", "bool")
    def updatePayloadTotal(self, net, ppu, materialValid):
        total = Decimal(net) * Decimal(ppu)
        print(net, ppu)
        self.payloadTotalLabel.setText(str(total))
        self.updateAddPayloadButton(total, materialValid)
        
    def updateAddPayloadButton(self, value, materialValid):
        if value and materialValid:
            self.addPayloadButton.setEnabled(True)
        else:
            self.addPayloadButton.setEnabled(False)
            
    def getPayloadValue(self):
        return self.payloadTotalLabel.text()
