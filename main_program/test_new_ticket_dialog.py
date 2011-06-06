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
        
        self.nameTestPairs = (("John", "JOHN"),
                              ("John  ", "JOHN"),
                              ("  John", "JOHN"), 
                              ("  John  ", "JOHN"),
                              ("Jo  hn", "JOHN"),
                              ("28759John", "JOHN"),
                              (",./John@~", "JOHN"),
                              (" 87898 7John89845  ", "JOHN"),
                              ("[]'John#89080", "JOHN"),
                              ("8783  *(John)&%  78", "JOHN"))
        
        self.houseNumberTestPairs = (("289", "289"),
                                     (" 289", "289"),
                                     (" 289 ", "289"),
                                     ("28 9", "289"),
                                     ("123456789", "12345"),
                                     ("hello, 289!", "289"),
                                     (":2djeih_-8 9", "289"),
                                     ("u_289_hello ", "289"),
                                     ("^&289", "289"),
                                     ("~2,.89", "289"))
        
        self.streetTestPairs = (("United Road", "UNITED ROAD"),
                                ("789U783nited Road", "UNITED ROAD"),
                                ("  Unit89ed R90oad,", "UNITED ROAD"),
                                (" Welcome Way ", "WELCOME WAY"),
                                ("Summit", "SUMMIT"),
                                (" Summit ", "SUMMIT "),
                                ("678Summit87953", "SUMMIT"),
                                ("^&*Summit *&(&", "SUMMIT "),
                                (".Road", "ROAD"),
                                ("78  United Road  89", "UNITED ROAD"))
        
        self.townTestPairs = (("Truro", "TRURO"),
                              (" Truro ", "TRURO "),
                              ("68Truro", "TRURO"),
                              ("98Redruth90", "REDRUTH"),
                              (" 67St Ives 90 ", "ST IVES"),
                              (" St Ives ", "ST IVES"),
                              ("  St   Ives 90&*", "ST IVES"),
                              (" &^Tru ro767", "TRU RO"),
                              (" Tr8u9 ^&ro &^", "TRU RO"),
                              ("   ^&Truro   &*   ", "TRURO "))
        
        self.postcodeTestPairs = (("TR165QY", "TR165QY"),
                                  (" Tr165QY ", "TR165QY"),
                                  (" b17AW ", "B17AW"),
                                  ("B109DS", "B109DS"),
                                  (" PL258de", "PL258DE"),
                                  ("^& pl25 7DS *(", "PL257DS"),
                                  ("  BA1   6AW", "BA16AW"),
                                  ("Tr16 5QY", "TR165QY"),
                                  ("TR16   5QY  ", "TR165QY"),
                                  ("N5 9Lp", "N59LP"))
        
        self.vehicleRegistrationTestPairs = (("WK55SWL", "WK55SWL"),
                                             (" WK55 SWL ", "WK55SWL"),
                                             ("^&WK 55  swl", "WK55SWL"),
                                             ("B567SWL", "B567SWL"),
                                             (" b567 SWL ", "B567SWL"),
                                             ("7896wK55SWL", "WK55SWL"), 
                                             ("7WK55 SWL 190", "WK55SWL1"),
                                             ("&* wk55 &^SWL", "WK55SWL"),
                                             ("90WK 55 SWL", "WK55SWL"),
                                             ("7 WK55    SWL  ", "WK55SWL"))
        
    def testNameLineEditsValidate(self):
        testWidgets = (self.gui.firstNameLineEdit,
                       self.gui.lastNameLineEdit)
        
        for testWidget in testWidgets:
            for pair in self.nameTestPairs:
                testWidget.clear()
                testString, resultString = pair[0], pair[1]
                QTest.keyClicks(testWidget, testString)
                assert testWidget.text() == resultString
    
    def testHouseNumberLineEditValidate(self):
        testWidget = self.gui.houseNumberLineEdit
        
        for pair in self.houseNumberTestPairs:
            testWidget.clear()
            testString, resultString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            assert testWidget.text() == resultString

    def testStreetLineEditValidate(self):
        testWidget = self.gui.streetLineEdit
        
        for pair in self.streetTestPairs:
            testWidget.clear()
            testString, resultString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            assert testWidget.text() == resultString
    
    def testTownLineEditValidate(self):
        testWidget = self.gui.townLineEdit
        
        for pair in self.townTestPairs:
            testWidget.clear()
            testString, resultString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            assert testWidget.text() == resultString
    
    def testPostcodeLineEditValidate(self):
        testWidget = self.gui.postcodeLineEdit
        
        for pair in self.postcodeTestPairs:
            testWidget.clear()
            testString, resultString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            assert testWidget.text() == resultString
        
    def testVehicleRegistrationLineEditValidate(self):
        testWidget = self.gui.vehicleRegistrationLineEdit
        
        for pair in self.vehicleRegistrationTestPairs:
            testWidget.clear()
            testString, resultString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            assert testWidget.text() == resultString
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
    
if __name__ == "__main__":
    unittest.main()