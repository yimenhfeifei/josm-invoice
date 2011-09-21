try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class BaseProcess(object):
    def __init__(self, name="Base"):
        self.name = name
        self.stages = []
        self.currentStage = None
        