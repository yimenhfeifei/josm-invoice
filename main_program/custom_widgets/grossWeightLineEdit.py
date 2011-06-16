try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from custom_widgets.validatingLineEdit import ValidatingLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class GrossWeightLineEdit(ValidatingLineEdit):
    
    disableNetWeight = pyqtSignal()
    enableNetWeight = pyqtSignal()
    enableTareWeight = pyqtSignal()
    disableTareWeight = pyqtSignal()
    grossWeightValue = pyqtSignal(str)
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
    def onEnableGrossWeight(self):
        self.setEnabled(True)
        super(GrossWeightLineEdit, self).validate()
        self.show()
        
    @pyqtSlot()
    def onDisableGrossWeight(self):
        self.setEnabled(False)
        self.hide()
            
    @pyqtSlot()
    def onValid(self):
        super(GrossWeightLineEdit, self).onValid()
        self.enableTareWeight.emit()
    
    @pyqtSlot()
    def onInvalid(self):
        super(GrossWeightLineEdit, self).onInvalid()
        self.disableTareWeight.emit()
        self.clearNetWeight.emit()
        
    @pyqtSlot()
    def onSendGrossWeightValue(self):
        self.grossWeightValue.emit(self.text())