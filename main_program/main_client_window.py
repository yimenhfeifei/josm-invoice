try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import new_main_generated
    from custom_widgets.newTicketWidget import NewTicketWidget
    from verify_ticket_dialog import VerifyTicketDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

__version__ = "0.0"

class MainClientWindow(QMainWindow,
                       new_main_generated.Ui_mainClientWindow):

    def __init__(self, parent=None):
        super(MainClientWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Orchard Suite")
        self.setCentralWidget(self.homeWidget)
        
        self.connect(self.homeWidget.newTicketButton, SIGNAL("clicked()"),
                     self.createNewTicketDialog)
        
        self.connect(self.homeWidget.verifyTicketButton, SIGNAL("clicked()"),
                     self.createVerifyTicketDialog)
    
    def createNewTicketDialog(self):
        #NewTicketDialog().exec_()
        self.setCentralWidget(NewTicketWidget())
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
    