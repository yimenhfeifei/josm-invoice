try:
    import unittest
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtTest import *
    
    from shared_modules.custom_qdialog import CustomQDialog
    from shared_modules.regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestCustomQDialog(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomQDialog()
        self.testRegexString = "Name"
        self.testMinimumLength = 1
        self.testMandatory = True
        self.testValidated = False
        self.testWidget = QLineEdit(self.gui)
        self.testNameString = "1234John"
        self.testNameStringResult = "John"
    
    def testvalidate(self):
        self.gui.setDynamicProperties(self.testWidget,
                                      regexString=self.testRegexString,
                                      minimumLength=self.testMinimumLength,
                                      mandatory=self.testMandatory,
                                      validated=self.testValidated)
        self.gui.setValidators((self.testWidget,))
        
        QTest.keyClicks(self.testWidget, self.testNameString)
        self.gui.validate((self.testWidget,))
        assert self.testWidget.property("validated") == True
        
    def testUpdateStyleSheets(self):
        self.gui.setDynamicProperties(self.testWidget,
                                      regexString=self.testRegexString,
                                      minimumLength=self.testMinimumLength,
                                      mandatory=self.testMandatory,
                                      validated=self.testValidated)
        self.gui.setValidators((self.testWidget,))
        
        QTest.keyClicks(self.testWidget, self.testNameString)
        self.gui.validate((self.testWidget,))
        self.gui.updateStyleSheets((self.testWidget,))
        assert self.testWidget.styleSheet() == ""
        
    def testAllWidgetsPassedValidation(self):
        self.gui.setDynamicProperties(self.testWidget,
                                      regexString=self.testRegexString,
                                      minimumLength=self.testMinimumLength,
                                      mandatory=self.testMandatory,
                                      validated=self.testValidated)
        self.gui.setValidators((self.testWidget,))
        
        QTest.keyClicks(self.testWidget, self.testNameString)
        self.gui.validate((self.testWidget,))
        assert self.gui.allWidgetsPassedValidation((self.testWidget,)) == True
        
    def testSetDynamicProperties(self):
        self.gui.setDynamicProperties(self.testWidget,
                                      regexString=self.testRegexString,
                                      minimumLength=self.testMinimumLength,
                                      mandatory=self.testMandatory,
                                      validated=self.testValidated)
        
        assert self.testWidget.property("regexString") == self.testRegexString
        assert self.testWidget.property("minimumLength") == self.testMinimumLength
        assert self.testWidget.property("mandatory") == self.testMandatory
        assert self.testWidget.property("validated") == self.testValidated
    
    def testSetValidators(self):
        self.gui.setDynamicProperties(self.testWidget,
                                      regexString=self.testRegexString,
                                      minimumLength=self.testMinimumLength,
                                      mandatory=self.testMandatory,
                                      validated=self.testValidated)
        self.gui.setValidators((self.testWidget,))
        
        QTest.keyClicks(self.testWidget, self.testNameString)
        assert self.testWidget.text() == self.testNameStringResult
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()

if __name__ == "__main__":
    unittest.main()