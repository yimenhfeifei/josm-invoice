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
        self.nameTestString = "I"
        self.houseNumberTestString = "289"
    
    def testFirstNameLineEditTextEntry(self):
        testWidget = self.gui.firstNameLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.nameTestString)
        assert testWidget.text() == self.nameTestString
    
    def testHouseNumberLineEditTextEntry(self):
        testWidget = self.gui.houseNumberLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.houseNumberTestString)
        assert testWidget.text() == self.houseNumberTestString
        
    def testStreetLineEditTextEntry(self):
        testWidget = self.gui.streetLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.nameTestString)
        assert testWidget.text() == self.nameTestString
        
    def testTownLineEditTextEntry(self):
        testWidget = self.gui.townLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.nameTestString)
        assert testWidget.text() == self.nameTestString
        
    def testPostcodeLineEditTextEntry(self):
        testWidget = self.gui.postcodeLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.nameTestString)
        assert testWidget.text() == self.nameTestString
    
    def testVehicleRegistrationLineEditTextEntry(self):
        testWidget = self.gui.vehicleRegistrationLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.nameTestString)
        assert testWidget.text() == self.nameTestString
    
    def testGrossWeightLineEditTextEntry(self):
        testWidget = self.gui.grossWeightLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.nameTestString)
        assert testWidget.text() == self.nameTestString
        
    def testTareWeightLineEditTextEntry(self):
        testWidget = self.gui.tareWeightLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.nameTestString)
        assert testWidget.text() == self.nameTestString
        
    def testNetWeightLineEditTextEntry(self):
        testWidget = self.gui.netWeightLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.nameTestString)
        assert testWidget.text() == self.nameTestString
    
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
        QTest.keyClicks(testWidget, self.nameTestString)
        assert testWidget.text() == self.nameTestString
    
    def testTotalValueLineEditTextEntry(self):
        testWidget = self.gui.totalValueLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.nameTestString)
        assert testWidget.text() == self.nameTestString

    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
    
class TestNewTicketDialogValidators(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketDialog()
        self.nameResult = "John"
        self.nameTestStrings = ("John",
                            "John  ",
                            "  John",
                            "  John  ",
                            "Jo  hn",
                            "28759John",
                            ",./John@~",
                            " 87898 7John89845  ",
                            "[]'John#89080",
                            "8783  *(John)&%  78")
        
        self.houseNumberResult = "289"
        self.houseNumberTestStrings = ("289",
                            " 289",
                            " 289 ",
                            "28 9",
                            "289  ",
                            "hello, 289!",
                            ":2djeih_-8 9",
                            "u_289_hello ",
                            "^&289",
                            "~2,.89")
        
    def testFirstNameLineEditValidate(self):
        testWidget = self.gui.firstNameLineEdit
        
        for string in self.nameTestStrings:
            testWidget.clear()
            QTest.keyClicks(testWidget, string)
        assert testWidget.text() == self.nameResult
        
    def testLastNameLineEditValidate(self):
        testWidget = self.gui.lastNameLineEdit
        
        for string in self.nameTestStrings:
            testWidget.clear()
            QTest.keyClicks(testWidget, string)
        assert testWidget.text() == self.nameResult
    
    def testHouseNumberLineEditValidate(self):
        testWidget = self.gui.houseNumberLineEdit
        
        for string in self.houseNumberTestStrings:
            testWidget.clear()
            QTest.keyClicks(testWidget, string)
        assert testWidget.text() == self.houseNumberResult
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
    
if __name__ == "__main__":
    unittest.main()