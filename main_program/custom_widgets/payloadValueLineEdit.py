try:
    import sys
    import decimal
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from custom_widgets.validatingLineEdit import ValidatingLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class PayloadValueLineEdit(ValidatingLineEdit):
    
    def __init__(self, parent=None):
        super(PayloadValueLineEdit, self).__init__(parent)
    
    @pyqtSlot()
    def onTextEdited(self):
        super(PayloadValueLineEdit, self).validate()
        
    @pyqtSlot()
    def onClearPayloadValue(self):
        self.clear()
        super(PayloadValueLineEdit, self).validate()
        
    @pyqtSlot()
    def onCalculatePayloadValue(self, net, price):
        net = Decimal(net)
        self.setText(str(net * Decimal(price)))
        super(PayloadValueLineEdit, self).validate()