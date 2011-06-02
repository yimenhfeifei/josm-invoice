try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    

except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class QDialogWithLineEditValidator(QDialog):
    
    def __init__(self, parent=None):
        super(QDialogWithLineEditValidator, self).__init__(parent)
        
    def validateLineEdits(self):
        pass