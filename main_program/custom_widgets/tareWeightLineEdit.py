try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from custom_widgets.validatingLineEdit import ValidatingLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TareWeightLineEdit(ValidatingLineEdit):
    
    sendGrossWeightValue = pyqtSignal()
    calculateNetWeight = pyqtSignal(str, str)
    clearNetWeight = pyqtSignal()
    
    def __init__(self, parent=None):
        super(TareWeightLineEdit, self).__init__(parent)
        self.hide()
    
    @pyqtSlot()
    def onTextEdited(self):
        super(TareWeightLineEdit, self).validate()
    
    @pyqtSlot()
    def onValid(self):
        super(TareWeightLineEdit, self).onValid()
        self.sendGrossWeightValue.emit()
        
    @pyqtSlot()
    def onInvalid(self):
        super(TareWeightLineEdit, self).onInvalid()
        self.clearNetWeight.emit()
    
    @pyqtSlot()
    def onGrossWeightValue(self, grossValue):
        if Decimal(self.text()) >= Decimal(grossValue):
            self.invalid.emit()
        else:
            self.calculateNetWeight.emit(grossValue, self.text())
    
    @pyqtSlot()
    def onDisableTareWeight(self):
        self.setEnabled(False)
        self.hide()
        self.clear()
    
    @pyqtSlot()
    def onEnableTareWeight(self):
        self.setEnabled(True)
        self.show()
        super(TareWeightLineEdit, self).validate()