try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import weight_widget_generated
    from shared_modules.validate import validate
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class WeightWidget(QWidget, weight_widget_generated.Ui_weightWidget):

    def __init__(self, parent=None):
        super(WeightWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.styles = {True: "",
                       False: "QLineEdit {background-color: red;}"}
        
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
                     self.edited)
        
        self.connect(self.tareEdit, SIGNAL("textEdited(QString)"),
                     self.edited)
        
        self.connect(self.netEdit, SIGNAL("textEdited(QString)"),
                     self.edited)
        
        self.connect(self.grossEdit, SIGNAL("textChanged(QString)"),
                     self.edited)
        
        self.connect(self.tareEdit, SIGNAL("textChanged(QString)"),
                     self.edited)
        
        self.connect(self.netEdit, SIGNAL("textChanged(QString)"),
                     self.edited)
        
    def edited(self):
        for widget in self.widgets:
            status = validate(widget.text(), "weight")
            widget.setProperty("valid", status)
            widget.setStyleSheet(self.styles[status])
        
        if self.grossEdit.property("valid") and self.tareEdit.property("valid"):
            self.calculateNetWeight()
        else:
            if self.useGrossBox.isChecked():
                self.netEdit.clear()
        
        if self.netEdit.property("valid") == True:
            if Decimal(self.netEdit.text()) == 0:
                self.netEdit.setProperty("valid", False)
                self.netEdit.setStyleSheet(self.styles[False])
            
    def calculateNetWeight(self):
        grossWeight = Decimal(self.grossEdit.text())
        tareWeight = Decimal(self.tareEdit.text())
        netWeight = grossWeight - tareWeight
        
        if netWeight > 0 and netWeight < grossWeight:
            self.netEdit.setText(str(netWeight))
        else:
            self.netEdit.clear()
            self.tareEdit.setProperty("valid", False)
            self.tareEdit.setStyleSheet(self.styles[False])

    def toggleNetEdit(self, state):
        self.netEdit.setReadOnly(state)
        
    def clear(self):
        self.grossEdit.clear()
        self.tareEdit.clear()
        self.netEdit.clear()