try:
    import sys
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import car_widget_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class CarWidget(QDialog, car_widget_generated.Ui_carWidget):

    def __init__(self, parent=None):
        super(CarWidget, self).__init__(parent)
        self.setupUi(self)