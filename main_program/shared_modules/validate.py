try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

styles = {True: "",
          False: "QLineEdit {background-color: red;}"}

def validateLineEdit(widget, expression):
    regex = regexObjects[expression]

    regexMatch = regex.match(widget.text())
        
    if regexMatch:
        result = True
    else:
        result = False
        
    widget.setProperty("valid", result)
    widget.setStyleSheet(styles[result])
