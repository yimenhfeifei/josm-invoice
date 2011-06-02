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
        self.testDynamicValueList = ("Name",)
        self.testWidgetList = (QLineEdit(self.gui),)
        self.testDynamicProperty = "regexString"
        self.testNameString = "1234John"
        self.testNameStringResult = "John"
    
    def testSetDynamicProperties(self):
        self.gui.setDynamicProperties(self.testDynamicProperty,
                                      self.testWidgetList,
                                      self.testDynamicValueList)
        
        property = self.testWidgetList[0].property("regexString")
        assert property == self.testDynamicValueList[0]
    
    def testSetValidators(self):
        self.gui.setDynamicProperties(self.testDynamicProperty,
                                      self.testWidgetList,
                                      self.testDynamicValueList)
        self.gui.setValidators(self.testWidgetList)
        
        QTest.keyClicks(self.testWidgetList[0], self.testNameString)
        assert self.testWidgetList[0].text() == self.testNameStringResult
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()

if __name__ == "__main__":
    unittest.main()