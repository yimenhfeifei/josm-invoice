try:
    import sys
    import subprocess
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import verify_ticket_dialog_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class VerifyTicketDialog(QDialog,
                      verify_ticket_dialog_generated.Ui_verifyTicketDialog):

    def __init__(self, parent=None):
        super(VerifyTicketDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Verify Ticket")
        
        self.connect(self.scanButton, SIGNAL("clicked()"),
                     self.scanQR)
    
    def scanQR(self):
        qrCode = subprocess.check_output(["zbarcam", "--raw", "-q"])
        
        self.hashIdLineEdit.setText(str(qrCode)[2:-3])
        self.submitButton.setFocus()