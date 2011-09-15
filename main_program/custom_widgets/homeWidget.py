try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import home_widget_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class HomeWidget(QWidget, home_widget_generated.Ui_Form):

    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)
        self.setupUi(self)
