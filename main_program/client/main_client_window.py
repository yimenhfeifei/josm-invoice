try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import main_client_window_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class MainClientWindow(QMainWindow, main_client_window_generated.Ui_mainClientWindow):

    def __init__(self, parent=None):
        super(MainClientWindow, self).__init__(parent)
        self.setupUi(self)