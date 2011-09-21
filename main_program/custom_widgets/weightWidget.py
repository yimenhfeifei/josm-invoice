try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import weight_widget_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class WeightWidget(QWidget, weight_widget_generated.Ui_weightWidget):

    def __init__(self, parent=None):
        super(WeightWidget, self).__init__(parent)
        self.setupUi(self)
