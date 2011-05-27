try:
    import unittest
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtTest import *
    
    from vehicle_dialog import VehicleDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestVehicleDialogGui(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.widget = VehicleDialog()
        self.testString = "It works!"
      
    def testMakeLineEditTextEntry(self):
        testWidget = self.widget.makeLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testModelLineEditTextEntry(self):
        testWidget = self.widget.modelLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testColourLineEditTextEntry(self):
        testWidget = self.widget.colourLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
        
    def testRegistrationLineEditTextEntry(self):
        testWidget = self.widget.registrationLineEdit
        testWidget.clear()
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testVinLineEditTextEntry(self):
        testWidget = self.widget.vinLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testCatalyticLineEditTextEntry(self):
        testWidget = self.widget.catalyticLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testCatalyticCheckboxToggle(self):
        testWidget = self.widget.catalyticCheckbox
        assert testWidget.isChecked() == False
        
        QTest.mouseClick(testWidget, Qt.LeftButton)
        assert testWidget.isChecked() == True
        
        QTest.mouseClick(testWidget, Qt.LeftButton)
        assert testWidget.isChecked() == False
        
    def testCatalyticLineEditToggle(self):
        testWidget = self.widget.catalyticLineEdit
        assert testWidget.isEnabled() == False
        
        QTest.mouseClick(self.widget.catalyticCheckbox, Qt.LeftButton)
        
        assert testWidget.isEnabled() == True
        
        QTest.mouseClick(self.widget.catalyticCheckbox, Qt.LeftButton)
        
        assert testWidget.isEnabled() == False
        
    def tearDown(self):
        self.widget.deleteLater()
        self.app.deleteLater()

suite1 = unittest.makeSuite(TestVehicleDialogGui, "test")
    
if __name__ == "__main__":
    unittest.main()