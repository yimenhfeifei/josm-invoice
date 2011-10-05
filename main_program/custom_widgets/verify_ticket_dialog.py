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
        
        self.databaseSettings = {'host': '127.0.0.1',
                                 'unix_socket': '/var/run/mysql/mysql.sock',
                                 'port': 3306,
                                 'user': 'john',
                                 'passwd': 'dragon',
                                 'db': 'business'}
        
        self.server = MysqlManager()
        self.server.connect(self.databaseSettings)

        self.connect(self.scanButton, SIGNAL("clicked()"),
                     self.scanQR)

        self.connect(self.submitButton, SIGNAL("clicked()"),
                     self.submit)

    def scanQR(self):
        qrCode = subprocess.check_output(["bin/zbarcam", "--raw", "/dev/video1"])

        self.hashIdLineEdit.setText(str(qrCode)[2:-3])
        self.submitButton.setFocus()

    def submit(self):
        ticketHash = self.hashIdLineEdit.text()
        if self.server.valueInDatabase("hash", ticketHash):
            if self.server.setPaidTrue("hash", ticketHash):
                QMessageBox.warning(self, "Attention",
                                "Ticket {} is valid. You may now pay the customer.".format(ticketHash))
            else:
                QMessageBox.warning(self, "Warning",
                                "Ticket {} has already been paid. Do not pay the customer.".format(ticketHash))
        else:
            QMessageBox.warning(self, "Attention",
                                "Ticket {} was not found.".format(ticketHash))
