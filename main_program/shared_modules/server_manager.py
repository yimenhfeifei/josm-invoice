try:
    import sys

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class ServerManagerBaseCall(Exception):
    pass

class ServerManager(object):
    def __init__(self):
        pass
    
    def valueInDatabase(self, field, value):
        raise ServerManagerBaseCall()
        
    def setPaidTrue(self, field, value):
        raise ServerManagerBaseCall()
        