try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

def validate(value, expression):
    regex = regexObjects[expression]

    regexMatch = regex.match(value)
        
    if regexMatch:
        return True
    else:
        return False
