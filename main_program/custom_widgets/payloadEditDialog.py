try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import payload_edit_dialog_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class PayloadEditDialog(QDialog,
                      payload_edit_dialog_generated.Ui_payloadEditDialog):

    def __init__(self, parent=None):
        super(PayloadEditDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Enter payload value")
        
        self.connect(self.acceptButton, SIGNAL("clicked()"),
                     self.accept)
        
        self.connect(self.cancelButton, SIGNAL("clicked()"),
                     self.reject)
        
        self.connect(self.payloadValueEdit, SIGNAL("textChanged(QString)"),
                     self.changed)
        
    def changed(self):
        self.payloadValueEdit.validate()
        
        self.updateAcceptButton()
        
    def updateAcceptButton(self):
        self.acceptButton.setEnabled(self.isValid())
        
    def isValid(self):
        if self.payloadValueEdit.isValid():
            return True
        else:
            return False
