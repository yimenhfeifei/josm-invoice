try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import main_client_window_generated
    from custom_widgets.newTicketWidget import NewTicketWidget
    from custom_widgets.customerWidget import CustomerWidget
    from verify_ticket_dialog import VerifyTicketDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

__version__ = "0.0"

class TicketClientWindow(QMainWindow,
                       main_client_window_generated.Ui_mainClientWindow):

    def __init__(self, parent=None):
        super(MainClientWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Orchard Suite")
        self.setCentralWidget(self.homeWidget)
        
        self.currentProcess = None
        
        self.connect(self.homeWidget.newTicketButton, SIGNAL("clicked()"),
                     self.createNewTicketDialog)
        
        self.connect(self.homeWidget.verifyTicketButton, SIGNAL("clicked()"),
                     self.createVerifyTicketDialog)
    
    def createNewTicketDialog(self):
        self.setCentralWidget(CustomerWidget())
        self.layout()
        
    def createVerifyTicketDialog(self):
        VerifyTicketDialog().exec_()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = MainClientWindow()
    application.setOrganizationName("John Orchard & Company")
    application.setOrganizationDomain("orchard.com")
    application.setApplicationName("Orchard Suite")
    application.setApplicationVersion(__version__)
    mainWindow.show()
    application.exec_()
    