#!/usr/bin/python3
try:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import unit_frame_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class UnitFrame(QFrame, unit_frame_generated.Ui_unitFrame):

    def __init__(self, parent=None):
        super(UnitFrame, self).__init__(parent)
        self.setupUi(self)
