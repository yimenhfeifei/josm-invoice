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
        
        self.validatedStyleSheet = ""
        self.invalidatedStyleSheet = "QLineEdit {background-color: red;}"
    
    def setDynamicProperties(self, widget, **dynamicProperties):
        for dynamicProperty, value in dynamicProperties.items():
            widget.setProperty(dynamicProperty, value)
    
    def setValidator(self, widget):
        regex = regexObjects[widget.property("regexString")]
        widget.setValidator(QRegExpValidator(regex, self))
    
    def validate(self, widget):
        widgetText = widget.text()
        if len(widgetText) >= widget.property("minimumLength"):
            widget.setProperty("validated", True)
        else:
            widget.setProperty("validated", False)
        widget.setText(widgetText.upper())

    def updateStyleSheet(self, widget):
        if widget.property("validated") == True:
            widget.setStyleSheet(self.validatedStyleSheet)
        else:
            widget.setStyleSheet(self.invalidatedStyleSheet)
    
    def allWidgetsPassedValidation(self, widgets):
        for widget in widgets:
            if widget.property("validated") == False:
                return False
        return True