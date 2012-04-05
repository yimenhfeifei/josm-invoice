#!/usr/bin/python3
try:
    import traceback
    import sys

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)

class ExtendedComboBox(QComboBox):
    
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)
        
    def populate(self, items):
        for index, name in enumerate(items):
            self.insertItem(index, name)
