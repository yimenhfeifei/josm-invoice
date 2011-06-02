try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    

except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class CustomQDialog(QDialog):
    
    def __init__(self, parent=None):
        super(CustomQDialog, self).__init__(parent)
        
    def setValidators(self, widget, Qregex):
        pass