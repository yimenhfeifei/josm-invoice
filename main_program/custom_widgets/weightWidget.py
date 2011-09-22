try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import weight_widget_generated
    from shared_modules.validate import validateLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class WeightWidget(QWidget, weight_widget_generated.Ui_weightWidget):

    widgetChanged = pyqtSignal()
    
    def __init__(self, parent=None):
        super(WeightWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.widgets = [self.grossEdit,
                        self.tareEdit,
                        self.netEdit]
        
        self.connect(self.useGrossBox, SIGNAL("toggled(bool)"),
                     self.grossBox, SLOT("setEnabled(bool)"))
        
        self.connect(self.useGrossBox, SIGNAL("toggled(bool)"),
                     self.tareBox, SLOT("setEnabled(bool)"))
        
        self.connect(self.useGrossBox, SIGNAL("toggled(bool)"),
                     self.toggleNetEdit)
        
        self.connect(self.useGrossBox, SIGNAL("toggled(bool)"),
                     self.clear)
        
        self.connect(self.grossEdit, SIGNAL("textEdited(QString)"),
                     self.changed)
        
        self.connect(self.tareEdit, SIGNAL("textEdited(QString)"),
                     self.changed)
        
        self.connect(self.netEdit, SIGNAL("textEdited(QString)"),
                     self.changed)
        
        self.connect(self.grossEdit, SIGNAL("textChanged(QString)"),
                     self.changed)
        
        self.connect(self.tareEdit, SIGNAL("textChanged(QString)"),
                     self.changed)
        
        self.connect(self.netEdit, SIGNAL("textChanged(QString)"),
                     self.changed)
        
    def changed(self):
        for widget in self.widgets:
            widget.validate()
        
        if self.grossEdit.property("valid") and self.tareEdit.property("valid"):
            self.calculateNetWeight()
        else:
            if self.useGrossBox.isChecked():
                self.netEdit.clear()
        
        if self.netEdit.property("valid") == True:
            if Decimal(self.netEdit.text()) == 0:
                self.netEdit.setValidStatus(False)
                
        self.widgetChanged.emit()
            
    def calculateNetWeight(self):
        grossWeight = Decimal(self.grossEdit.text())
        tareWeight = Decimal(self.tareEdit.text())
        netWeight = grossWeight - tareWeight
        
        if netWeight > 0 and netWeight < grossWeight:
            self.netEdit.setText(str(netWeight))
        else:
            self.netEdit.clear()
            self.tareEdit.setValidStatus(False)

    def toggleNetEdit(self, state):
        self.netEdit.setReadOnly(state)
        
    def clear(self):
        self.grossEdit.clear()
        self.tareEdit.clear()
        self.netEdit.clear()
        
    def getNetWeight(self):
        if self.isValid():
            return self.netEdit.text()
        else:
            return "0"
    
    def isValid(self):
        if self.netEdit.isValid():
            return True
        else:
            return False
