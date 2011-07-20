try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from custom_widgets.validatingLineEdit import ValidatingLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class NetWeightLineEdit(ValidatingLineEdit):
    
    enableGrossWeight = pyqtSignal()
    disableGrossWeight = pyqtSignal()
    calculatePayloadValue = pyqtSignal(str, str)
    clearPayloadValue = pyqtSignal()
    
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
    def onClearNetWeight(self):
        self.clear()
        super(NetWeightLineEdit, self).validate()

    @pyqtSlot()
    def onEnableNetWeight(self):
        self.setReadOnly(False)
        super(NetWeightLineEdit, self).validate()
        
    @pyqtSlot()
    def onDisableNetWeight(self):
        self.setReadOnly(True)
        super(NetWeightLineEdit, self).validate()
        
    @pyqtSlot()
    def onCalculateNetWeight(self, gross, tare):
        net = str(Decimal(gross) - Decimal(tare))
        self.setText(net)
        super(NetWeightLineEdit, self).validate()
        
    @pyqtSlot()
    def onValid(self):
        self.calculatePayloadValue.emit(self.text(), self.materialValue)
        super(NetWeightLineEdit, self).onValid()
    
    @pyqtSlot()
    def onInvalid(self):
        self.clearPayloadValue.emit()
        super(NetWeightLineEdit, self).onInvalid()
    
    @pyqtSlot()
    def onMaterialComboboxChange(self):
        super(NetWeightLineEdit, self).validate()
        
    @pyqtSlot()
    def onMaterialChanged(self, value):
        self.materialValue = value
        super(NetWeightLineEdit, self).validate()