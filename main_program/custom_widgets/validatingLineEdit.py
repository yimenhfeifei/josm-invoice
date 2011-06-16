try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class ValidatingLineEdit(QLineEdit):
    
    valid = pyqtSignal()
    invalid = pyqtSignal()
    
    styleSheets = {"Valid": "",
                   "Invalid": "QLineEdit {background-color: red;}"}
    
    def __init__(self, parent=None):
        super(ValidatingLineEdit, self).__init__(parent)
        
        self.setProperty("regexString", "")
    
    @pyqtSlot()
    def onTextEdited(self):
        self.validate()
        
    @pyqtSlot()
    def validate(self):
        self.makeUppercase()
        
        self.applyRegex()
        
    def makeUppercase(self):
        self.setText(self.text().upper())

    def applyRegex(self):
        regex = regexObjects[self.property("regexString")]

        regexMatch = regex.match(self.text())
        
        if regexMatch:
            self.valid.emit()
        else:
            self.invalid.emit()
    
    @pyqtSlot(bool)
    def setReadOnlyInverted(self, state):
        self.setReadOnly(not state)
            
    @pyqtSlot()
    def onValid(self):
        self.setStyleSheet(self.styleSheets["Valid"])
    
    @pyqtSlot()
    def onInvalid(self):
        self.setStyleSheet(self.styleSheets["Invalid"])
        
    def getValidatedStatus(self):
        if self.styleSheet() == self.styleSheets["Valid"]:
            return True
        else:
            return False
