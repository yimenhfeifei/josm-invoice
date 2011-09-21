try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import ticket_client_window_generated
    from custom_widgets.customerWidget import CustomerWidget
    from custom_widgets.homeWidget import HomeWidget
    from shared_modules.new_ticket_process import NewTicketProcess
    from verify_ticket_dialog import VerifyTicketDialog
    from shared_modules.exceptions import ProcessFinished
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

__version__ = "0.0"

class TicketClientWindow(QMainWindow,
                       ticket_client_window_generated.Ui_ticketClientWindow):

    def __init__(self, parent=None):
        super(TicketClientWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ticket")
        self.goHome()
        
        self.process = None
        
    def goHome(self):
        self.setCentralWidget(HomeWidget())
        
        self.connect(self.centralWidget().newTicketButton, SIGNAL("clicked()"),
                     self.startNewTicket)
        
        self.connect(self.centralWidget().verifyTicketButton, SIGNAL("clicked()"),
                     self.createVerifyTicketDialog)
        
    def startNewTicket(self):
        self.process = NewTicketProcess(self)
        
    def createVerifyTicketDialog(self):
        VerifyTicketDialog().exec_()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = TicketClientWindow()
    application.setOrganizationName("John Orchard & Company")
    application.setOrganizationDomain("orchard.com")
    application.setApplicationName("Orchard Suite")
    application.setApplicationVersion(__version__)
    mainWindow.show()
    application.exec_()
    