try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    

except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

regexObjects = {"Name": QRegExp(r"^[a-z]+\s+[a-z]+$", Qt.CaseInsensitive)}