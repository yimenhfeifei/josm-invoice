try:
    import sys

    import pymysql
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class ServerManager(object):
    def __init__(self):
        pass
    
    def valueInDatabase(self, field, value):
        if value == "http://en.m.wikipedia.org":
            return True
        else:
            return False
        
    def setPaidTrue(self, field, value):
        pass
        