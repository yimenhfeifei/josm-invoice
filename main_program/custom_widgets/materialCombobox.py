try:
    import sys
    from decimal import Decimal
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class MaterialCombobox(QComboBox):
    
    materialChanged = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(MaterialCombobox, self).__init__(parent)
        
        self.onIndexChange()
        
    @pyqtSlot()
    def onIndexChange(self):
        selectedIndex = self.currentIndex()
        self.materialChanged.emit(self.itemData(selectedIndex))
