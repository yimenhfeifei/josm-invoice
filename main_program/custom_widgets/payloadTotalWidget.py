try:
    import sys
    import re
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import payload_total_widget_generated
    from shared_modules.regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class PayloadTotalWidget(QWidget,
                         payload_total_widget_generated.Ui_payloadTotalWidget):
    
    addPayload = pyqtSignal()
    payloadEdited = pyqtSignal()
    
    def __init__(self, parent=None):
        super(PayloadTotalWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.connect(self.addPayloadButton, SIGNAL("clicked()"),
                     self.addPayload.emit)
        
        self.connect(self.payloadTotalLabel, SIGNAL("linkActivated(QString)"),
                     self.payloadEdited.emit)
    
    @pyqtSlot("QString", "QString", "bool")
    def updatePayloadTotal(self, net, ppu, materialValid):
        total = Decimal(net) * Decimal(ppu)
        
        totalString = re.sub(regexObjects["spanTagContents"],
                             str(total),
                             self.payloadTotalLabel.text())
        
        self.payloadTotalLabel.setText(totalString)
        self.updateAddPayloadButton(total, materialValid)
        
    def updateAddPayloadButton(self, value, materialValid):
        if value and materialValid:
            self.addPayloadButton.setEnabled(True)
        else:
            self.addPayloadButton.setEnabled(False)
            
    def getPayloadValue(self):
        match = re.search(regexObjects["spanTagContents"],
                          self.payloadTotalLabel.text())
        
        return match.group(0)
