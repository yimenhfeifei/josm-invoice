try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.validatingLineEdit import ValidatingLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TareWeightLineEdit(ValidatingLineEdit):
    
    valid = pyqtSignal()
    invalid = pyqtSignal()
    requestGrossValue = pyqtSignal()
    calculateNetWeight = pyqtSignal(str, str)
    clearNetWeight = pyqtSignal()
    
    def __init__(self, parent=None):
        super(TareWeightLineEdit, self).__init__(parent)
    
    @pyqtSlot()
    def onTextEdited(self):
        super(TareWeightLineEdit, self).validate()
    
    @pyqtSlot()
    def validReceieved(self):
        self.requestGrossValue.emit()
        
    @pyqtSlot()
    def invalidReceieved(self):
        self.clearNetWeight.emit()
    
    @pyqtSlot()
    def grossValueReceived(self, grossValue):
        if Decimal(self.text()) >= Decimal(grossValue):
            self.invalid.emit()
        else:
            self.calculateNetWeight.emit(grossValue, self.text())
    
    @pyqtSlot()
    def disableTare(self):
        self.setEnabled(False)
        self.clear()
    
    @pyqtSlot()
    def enableTare(self):
        self.setEnabled(True)
        super(TareWeightLineEdit, self).validate()