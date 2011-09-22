try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class ValidatingLineEdit(QLineEdit):
    
    styleSheets = {True: "",
                   False: "QLineEdit {background-color: red;}"}
    
    def __init__(self, parent=None):
        super(ValidatingLineEdit, self).__init__(parent)
        
        self.setProperty("regexString", "")
        self.setValidStatus(False)
        
    def validate(self):
        self.makeUppercase()
        
        self.applyRegex()
        
    def makeUppercase(self):
        self.setText(self.text().upper())

    def applyRegex(self):
        regex = regexObjects[self.property("regexString")]

        regexMatch = regex.match(self.text())
        
        if regexMatch:
            self.setValidStatus(True)
        else:
            self.setValidStatus(False)
            
    def setValidStatus(self, value):
        self.setStyleSheet(self.styleSheets[value])
        self.setProperty("valid", value)
        
    def isValid(self):
        return self.property("valid")
