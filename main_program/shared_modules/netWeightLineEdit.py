try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.validatingLineEdit import ValidatingLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class NetWeightLineEdit(ValidatingLineEdit):
    
    enableGrossWeight = pyqtSignal()
    disableGrossWeight = pyqtSignal()
    
    def __init__(self, parent=None):
        super(NetWeightLineEdit, self).__init__(parent)
    
    @pyqtSlot()
    def onTextEdited(self):
        if self.text() == "":
            self.enableGrossWeight.emit()
            super(NetWeightLineEdit, self).validate()
        else:
            self.disableGrossWeight.emit()
            super(NetWeightLineEdit, self).validate()
        
    @pyqtSlot()
    def clearNetWeight(self):
        self.clear()
        super(NetWeightLineEdit, self).validate()

    @pyqtSlot()
    def enableNetWeight(self):
        self.setReadOnly(False)
        super(NetWeightLineEdit, self).validate()
        
    @pyqtSlot()
    def disableNetWeight(self):
        self.setReadOnly(True)
        super(NetWeightLineEdit, self).validate()
        
    @pyqtSlot()
    def calculateNetWeight(self, gross, tare):
        net = str(Decimal(gross) - Decimal(tare))
        self.setText(net)
        super(NetWeightLineEdit, self).validate()