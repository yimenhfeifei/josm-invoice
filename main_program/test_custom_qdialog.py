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
        self.testValidated = False
        self.testWidget = QLineEdit(self.gui)
        self.testNameString = "John"
        self.testNameStringResult = "JOHN"
        
        self.gui.setDynamicProperties(self.testWidget,
                                      regexString=self.testRegexString,
                                      validated=self.testValidated)
        
        QTest.keyClicks(self.testWidget, self.testNameString)
        self.gui.validate(self.testWidget)
        self.gui.updateStyleSheet(self.testWidget)
    
    def testvalidate(self):
        assert self.testWidget.property("validated") == True
        
    def testUpdateStyleSheets(self):
        assert self.testWidget.styleSheet() == ""
        
    def testAllWidgetsPassedValidation(self):
        assert self.gui.allWidgetsPassedValidation((self.testWidget,)) == True
        
    def testSetDynamicProperties(self):
        print(self.testWidget.property("regexString"))
        assert self.testWidget.property("regexString") == self.testRegexString
        assert self.testWidget.property("validated") == True
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()

if __name__ == "__main__":
    unittest.main()