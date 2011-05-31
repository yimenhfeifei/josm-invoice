try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import main_client_window_generated
    from new_ticket_dialog import NewTicketDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class MainClientWindow(QMainWindow,
                       main_client_window_generated.Ui_mainClientWindow):

    def __init__(self, parent=None):
        super(MainClientWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.connect(self.newTicketButton, SIGNAL("clicked()"),
                     self.createNewTicketDialog)
    
    def createNewTicketDialog(self):
        NewTicketDialog().exec_()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = MainClientWindow()
    mainWindow.show()
    application.exec_()