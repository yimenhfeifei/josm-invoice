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
        self.streetResult = "United Road"
        self.streetTestStrings = ("United Road",
                                 "789U783nited Road",
                                 "  Unit89ed R90oad,",
                                 " United Road ",
                                 "United 890Road ",
                                 " 5*United! Road",
                                 " 7United ;R.,oad ",
                                 "8)U*nited R432,.oad",
                                 "%^United789 Road   ",
                                 "78  United Road  89")
        self.townResult = "Truro"
        self.townTestStrings = ("Truro",
                                " Truro ",
                                "68Truro",
                                "98Truro90",
                                " 67Truro 90 ",
                                "^&Truro&^%",
                                "%$Truro 90&*",
                                " &^Tru ro767",
                                " Tr89 ^&ro &^",
                                "   ^&Truro   &*   ")
        self.postcodeResults = ("TR165QY",
                                "TR165QY",
                                "B17AW",
                                "B109DS",
                                "PL258DE",
                                "PL257DS",
                                "BA16AW",
                                "TR165QY",
                                "TR165QY",
                                "N59LP")
        self.postcodeTestStrings = ("TR165QY",
                                " TR165QY ",
                                " B17AW ",
                                "B109DS",
                                " PL258DE",
                                "^& PL25 7DS *(",
                                "  BA1   6AW",
                                "TR16 5QY",
                                "TR16   5QY  ",
                                "N5 9LP")
        self.vehicleRegistrationResults = ("WK55SWL",
                                "WK55SWL",
                                "WK55SWL",
                                "B567SWL",
                                "B567SWL",
                                "WK55SWL",
                                "WK55SWL1",
                                "WK55SWL",
                                "WK55SWL",
                                "WK55SWL")
        self.vehicleRegistrationTestStrings = ("WK55SWL",
                                " WK55 SWL ",
                                "^&WK 55  SWL",
                                "B567SWL",
                                " B567 SWL ",
                                "7896WK55SWL",
                                "7WK55 SWL 190",
                                "&* WK55 &^SWL",
                                "90WK 55 SWL",
                                "7 WK55    SWL  ")
        
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

    def testStreetLineEditValidate(self):
        testWidget = self.gui.streetLineEdit
        
        for string in self.streetTestStrings:
            testWidget.clear()
            QTest.keyClicks(testWidget, string)
        assert testWidget.text() == self.streetResult
    
    def testTownLineEditValidate(self):
        testWidget = self.gui.townLineEdit
        
        for string in self.townTestStrings:
            testWidget.clear()
            QTest.keyClicks(testWidget, string)
        assert testWidget.text() == self.townResult
    
    def testPostcodeLineEditValidate(self):
        testWidget = self.gui.postcodeLineEdit
        
        for pair in zip(self.postcodeTestStrings, self.postcodeResults):
            testWidget.clear()
            testString, resultString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            assert testWidget.text() == resultString
        
    def testVehicleRegistrationLineEditValidate(self):
        testWidget = self.gui.vehicleRegistrationLineEdit
        
        for pair in zip(self.vehicleRegistrationTestStrings, 
                        self.vehicleRegistrationResults):
            testWidget.clear()
            testString, resultString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            print(testWidget.text())
            assert testWidget.text() == resultString
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
    
if __name__ == "__main__":
    unittest.main()