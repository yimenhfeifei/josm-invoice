try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.validatingLineEdit import ValidatingLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class GrossWeightLineEdit(ValidatingLineEdit):
    
    disableNetWeight = pyqtSignal()
    enableNetWeight = pyqtSignal()
    valid = pyqtSignal()
    invalid = pyqtSignal()
    enableTare = pyqtSignal()
    disableTare = pyqtSignal()
    sendGrossValue = pyqtSignal(str)
    clearNetWeight = pyqtSignal()
    
    def __init__(self, parent=None):
        super(GrossWeightLineEdit, self).__init__(parent)
    
    @pyqtSlot()
    def onTextEdited(self):
        if self.text() == "":
            self.enableNetWeight.emit()
            super(GrossWeightLineEdit, self).validate()
        else:
            self.disableNetWeight.emit()
            super(GrossWeightLineEdit, self).validate()
    
    @pyqtSlot()
    def enableGrossWeight(self):
        self.setEnabled(True)
        super(GrossWeightLineEdit, self).validate()
        
    @pyqtSlot()
    def disableGrossWeight(self):
        self.setEnabled(False)
            
    @pyqtSlot()
    def validReceived(self):
        self.enableTare.emit()
    
    @pyqtSlot()
    def invalidReceived(self):
        self.disableTare.emit()
        self.clearNetWeight.emit()
        
    @pyqtSlot()
    def requestGrossValueReceived(self):
        self.sendGrossValue.emit(self.text())