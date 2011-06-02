try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class CustomQDialog(QDialog):
    
    def __init__(self, parent=None):
        super(CustomQDialog, self).__init__(parent)
    
    def setDynamicProperties(self, dynamicProperty, widgets, values):
        for pair in zip(widgets, values):
            widget, value = pair[0], pair[1]
            widget.setProperty(dynamicProperty, value)

    def setValidators(self, widgets):
        for widget in widgets:
            regex = regexObjects[widget.property("regexString")]
            widget.setValidator(QRegExpValidator(regex, self))