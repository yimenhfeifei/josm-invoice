try:
    import unittest
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtTest import *
    
    from new_ticket_dialog import NewTicketDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestNewTicketDialogGui(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketDialog()
        self.testString = "It works!"
    
    def testNameLineEditTextEntry(self):
        testWidget = self.gui.nameLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testHouseNumberLineEditTextEntry(self):
        testWidget = self.gui.houseNumberLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
        
    def testStreetLineEditTextEntry(self):
        testWidget = self.gui.streetLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
        
    def testTownLineEditTextEntry(self):
        testWidget = self.gui.townLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
        
    def testPostcodeLineEditTextEntry(self):
        testWidget = self.gui.postcodeLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testVehicleRegistrationLineEditTextEntry(self):
        testWidget = self.gui.vehicleRegistrationLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testGrossWeightLineEditTextEntry(self):
        testWidget = self.gui.grossWeightLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
        
    def testTareWeightLineEditTextEntry(self):
        testWidget = self.gui.tareWeightLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
        
    def testNetWeightLineEditTextEntry(self):
        testWidget = self.gui.netWeightLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testMaterialCombobox(self):
        assert self.gui.materialCombobox.isEnabled() == True
    
    def testManualPriceCheckboxToggle(self):
        testWidget = self.gui.manualPriceCheckbox
        assert testWidget.isChecked() == False
        
        QTest.mouseClick(testWidget, Qt.LeftButton)
        assert testWidget.isChecked() == True
        
        QTest.mouseClick(testWidget, Qt.LeftButton)
        assert testWidget.isChecked() == False
        
    def testPayloadValueLineEditToggle(self):
        testWidget = self.gui.payloadValueLineEdit
        checkboxWidget = self.gui.manualPriceCheckbox
        assert testWidget.isReadOnly() == True
        assert checkboxWidget.isChecked() == False
        
        QTest.mouseClick(checkboxWidget, Qt.LeftButton)
        assert testWidget.isReadOnly() == False
        assert checkboxWidget.isChecked() == True
        
        QTest.mouseClick(checkboxWidget, Qt.LeftButton)
        assert testWidget.isReadOnly() == True
        assert checkboxWidget.isChecked() == False
    
    def testPayloadValueLineEditTextEntry(self):
        testWidget = self.gui.payloadValueLineEdit
        testWidget.clear()
        checkboxWidget = self.gui.manualPriceCheckbox
        assert testWidget.isReadOnly() == True
        assert checkboxWidget.isChecked() == False
        
        QTest.mouseClick(checkboxWidget, Qt.LeftButton)
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testTotalValueLineEditTextEntry(self):
        testWidget = self.gui.totalValueLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString

    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()

suite1 = unittest.makeSuite(TestNewTicketDialogGui, "test")
    
if __name__ == "__main__":
    unittest.main()