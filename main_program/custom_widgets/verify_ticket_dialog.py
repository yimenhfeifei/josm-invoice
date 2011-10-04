try:
    import sys
    import subprocess

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

    from gui_interface_designs import verify_ticket_dialog_generated
    from shared_modules.mysql_manager import MysqlManager
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class VerifyTicketDialog(QDialog,
                         verify_ticket_dialog_generated.Ui_verifyTicketDialog):

    def __init__(self, parent=None):
        super(VerifyTicketDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Verify Ticket")
        self.server = MysqlManager()

        self.connect(self.scanButton, SIGNAL("clicked()"),
                     self.scanQR)

        self.connect(self.submitButton, SIGNAL("clicked()"),
                     self.submit)

    def scanQR(self):
        qrCode = subprocess.check_output(["bin/zbarcam", "--raw", "-q"])

        self.hashIdLineEdit.setText(str(qrCode)[2:-3])
        self.submitButton.setFocus()

    def submit(self):
        ticketHash = self.hashIdLineEdit.text()
        if self.server.valueInDatabase("hashId", ticketHash):
            self.server.setPaidTrue("hashId", ticketHash)
        else:
            QMessageBox.warning(self, "Attention",
                                "Ticket {} was not found.".format(ticketHash))
