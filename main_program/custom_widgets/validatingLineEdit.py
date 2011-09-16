try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class ValidatingLineEdit(QLineEdit):
    
    styleSheets = {"Valid": "",
                   "Invalid": "QLineEdit {background-color: red;}"}
    
    def __init__(self, parent=None):
        super(ValidatingLineEdit, self).__init__(parent)
        
        self.setProperty("regexString", "")
        
    def validate(self):
        self.makeUppercase()
        
        self.applyRegex()
        
    def makeUppercase(self):
        self.setText(self.text().upper())

    def applyRegex(self):
        regex = regexObjects[self.property("regexString")]

        regexMatch = regex.match(self.text())
        
        if regexMatch:
            self.setStyleSheet(self.styleSheets["Valid"])
        else:
            self.setStyleSheet(self.styleSheets["Invalid"])
    
    def setReadOnlyInverted(self, state):
        self.setReadOnly(not state)
        
    def setEnabled(self, value):
        super(ValidatingLineEdit, self).setEnabled(value)
        if value == False:
            self.setStyleSheet(self.styleSheets["Valid"])
        else:
            self.validate()
        
    def getValidatedStatus(self):
        if self.styleSheet() == self.styleSheets["Valid"]:
            return True
        else:
            return False
