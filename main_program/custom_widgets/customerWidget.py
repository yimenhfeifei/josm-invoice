try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import customer_widget_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class CustomerWidget(QWidget, customer_widget_generated.Ui_customerWidget):

    widgetChanged = pyqtSignal()
    
    def __init__(self, parent=None):
        super(CustomerWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.widgets = [self.firstNameEdit,
                        self.lastNameEdit,
                        self.houseNumberEdit,
                        self.streetEdit,
                        self.townEdit,
                        self.postcodeEdit,
                        self.customerRegEdit]
        
        for widget in self.widgets:
            self.connect(widget, SIGNAL("textChanged(QString)"),
                         self.changed)

    def getFields(self):
        return {"firstName": self.firstNameEdit.text(),
                "lastName": self.lastNameEdit.text(),
                "houseNumber": self.houseNumberEdit.text(),
                "street": self.streetEdit.text(),
                "town": self.townEdit.text(),
                "postcode": self.postcodeEdit.text(),
                "customerReg": self.customerRegEdit.text()}
            
    def changed(self):
        for widget in self.widgets:
            widget.validate()
            
        self.widgetChanged.emit()
            
    def isValid(self):
        for widget in self.widgets:
            if not widget.isValid():
                return False
        return True
