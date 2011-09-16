try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from custom_widgets.customerWidget import CustomerWidget
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class Process(object):
    def __init__(self):
        self.name = "Base"
        self.pages = []