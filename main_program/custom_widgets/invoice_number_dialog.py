try:
    import sys
    import re
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import invoice_number_dialog_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class InvoiceNumberDialog(QDialog,
                      invoice_number_dialog_generated.Ui_invoiceNumberDialog):

    def __init__(self, parent=None):
        super(InvoiceNumberDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.connect(self.invoiceNumberEdit, SIGNAL("textChanged(QString)"),
                     self.changed)
        
        self.connect(self.acceptButton, SIGNAL("clicked()"),
                     self.acceptNumber)
        
        self.connect(self.cancelButton, SIGNAL("clicked()"),
                     self.rejectNumber)
        
    def changed(self):
        self.invoiceNumberEdit.validate()
        
    def acceptNumber(self):
        if self.invoiceNumberEdit.isValid():
            self.accept()
            
    def rejectNumber(self):
        QMessageBox.warning(self, "Attention", "Invoice number must be set!")
