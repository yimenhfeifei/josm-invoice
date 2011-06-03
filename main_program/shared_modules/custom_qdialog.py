try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class CustomQDialog(QDialog):
    
    def __init__(self, parent=None):
        super(CustomQDialog, self).__init__(parent)
    
    def setDynamicProperties(self, widget, **dynamicProperties):
        for dynamicProperty, value in dynamicProperties.items():
            widget.setProperty(dynamicProperty, value)

    def setValidators(self, widgets):
        for widget in widgets:
            regex = regexObjects[widget.property("regexString")]
            widget.setValidator(QRegExpValidator(regex, self))