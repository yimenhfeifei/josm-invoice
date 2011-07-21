try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from custom_widgets.validatingLineEdit import ValidatingLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TotalValueLineEdit(ValidatingLineEdit):
    
    def __init__(self, parent=None):
        super(TotalValueLineEdit, self).__init__(parent)
        
    @pyqtSlot()
    def onCalculateTotalValue(self, values):
        total = sum([Decimal(value) for value in values])
        total = Decimal(total).to_integral()
        self.setText("{:.2f}".format(total))
