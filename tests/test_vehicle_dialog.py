try:
    import unittest
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtTest import *
    
    from custom_widgets.vehicleDialog import VehicleDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestVehicleDialogGui(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.vehicle = {"make": "Porsche",
                        "model": "911",
                        "colour": 4,
                        "reg": "WK11TSA",
                        "vin": "78298yr9843r",
                        "id": 1}
        self.widget = VehicleDialog(self.vehicle)
        self.testString = "I"
      
    def testMakeLineEditTextEntry(self):
        testWidget = self.widget.makeEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testModelLineEditTextEntry(self):
        testWidget = self.widget.modelEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
        
    def testRegistrationLineEditTextEntry(self):
        testWidget = self.widget.vehicleRegistrationEdit
        testWidget.clear()
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testVinLineEditTextEntry(self):
        testWidget = self.widget.vinEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
        
    def tearDown(self):
        self.widget.deleteLater()
        self.app.deleteLater()

suite1 = unittest.makeSuite(TestVehicleDialogGui, "test")
    
if __name__ == "__main__":
    unittest.main()