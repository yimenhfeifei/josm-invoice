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
        self.weightTestString = "179.00"
        self.tareWeightTestString = "169.00"
    
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
        
        QTest.keyClicks(testWidget, self.weightTestString)
        assert testWidget.text() == self.weightTestString
        
    def testTareWeightLineEditTextEntry(self):
        testWidget = self.gui.tareWeightLineEdit
        testWidget.clear()
        self.gui.grossWeightLineEdit.setText("12000.00")
        
        QTest.keyClicks(testWidget, self.tareWeightTestString)
        assert testWidget.text() == self.tareWeightTestString
        
    def testNetWeightLineEditTextEntry(self):
        self.gui.grossWeightLineEdit.clear()
        testWidget = self.gui.netWeightLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.weightTestString)
        assert testWidget.text() == self.weightTestString
    
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
        
        self.nameTestPairs = (("John", True),
                              ("John  ", False),
                              ("  John", False), 
                              ("  John  ", False),
                              ("Jo  hn", False),
                              ("28759John", False),
                              (",./John@~", False),
                              (" 87898 7John89845  ", False),
                              ("[]'John#89080", False),
                              ("8783  *(John)&%  78", False))
        
        self.houseNumberTestPairs = (("289", True),
                                     (" 289", False),
                                     (" 289 ", False),
                                     ("28 9", False),
                                     ("123456789", False),
                                     ("hello, 289!", False),
                                     (":2djeih_-8 9", False),
                                     ("u_289_hello ", False),
                                     ("^&289", False),
                                     ("~2,.89", False))
        
        self.streetTestPairs = (("United Road", True),
                                ("789U783nited Road", False),
                                ("  Unit89ed R90oad,", False),
                                (" Welcome Way ", False),
                                ("Summit", True),
                                (" Summit ", False),
                                ("678Summit87953", False),
                                ("^&*Summit *&(&", False),
                                (".Road", False),
                                ("78  United Road  89", False))
        
        self.townTestPairs = (("Truro", True),
                              (" Truro ", False),
                              ("68Truro", False),
                              ("98Redruth90", False),
                              (" 67St Ives 90 ", False),
                              (" St Ives ", False),
                              ("  St   Ives 90&*", False),
                              (" &^Tru ro767", False),
                              (" Tr8u9 ^&ro &^", False),
                              ("   ^&Truro   &*   ", False))
        
        self.postcodeTestPairs = (("TR165QY", True),
                                  ("Tr16 5QY", True),
                                  (" b17AW ", False),
                                  ("B109DS", True),
                                  (" PL258de", False),
                                  ("^& pl25 7DS *(", False),
                                  ("  BA1   6AW", False),
                                  ("TR16 5qy", True),
                                  ("TR16   5QY  ", False),
                                  ("N5 9Lp", True))
        
        self.vehicleRegistrationTestPairs = (("WK55SWL", True),
                                             (" WK55 SWL ", False),
                                             ("^&WK 55  swl", False),
                                             ("B567SWL", True),
                                             ("b567SWL", True),
                                             ("7896wK55SWL", False), 
                                             ("7WK55 SWL 190", False),
                                             ("&* wk55 &^SWL", False),
                                             ("90WK 55 SWL", False),
                                             ("7 WK55    SWL  ", False))
        
        self.grossWeightTestPairs = (("120.00", True),
                                             ("120.50", True),
                                             (" 120.00", False),
                                             ("  120.50  ", False),
                                             ("^&hj120.50", False),
                                             ("120", False), 
                                             ("1.50", True),
                                             ("23.00", True),
                                             ("12 34.50", False),
                                             ("10000.00", True))
        
        self.tareWeightTestPairs = (("110.00", True),
                                             ("110.50", True),
                                             (" 110.00", False),
                                             ("  110.50  ", False),
                                             ("^&hj110.50", False),
                                             ("110", False), 
                                             ("1.00", True),
                                             ("22.00", True),
                                             ("12 33.50", False),
                                             ("1000.00", True))
        
        self.netWeightTestPairs = (("120.00", True),
                                             ("120.50", True),
                                             (" 120.00", False),
                                             ("  120.50  ", False),
                                             ("^&hj120.50", False),
                                             ("120", False), 
                                             ("1.50", True),
                                             ("23.00", True),
                                             ("12 34.50", False),
                                             ("10000.00", True))
        
    def testNameLineEditsValidate(self):
        testWidgets = (self.gui.firstNameLineEdit,
                       self.gui.lastNameLineEdit)
        
        for testWidget in testWidgets:
            for pair in self.nameTestPairs:
                testWidget.clear()
                testString, validString = pair[0], pair[1]
                QTest.keyClicks(testWidget, testString)
                testWidget.validate()
            assert testWidget.getValidatedStatus() == validString
    
    def testHouseNumberLineEditValidate(self):
        testWidget = self.gui.houseNumberLineEdit
        
        for pair in self.houseNumberTestPairs:
            testWidget.clear()
            testString, validString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            testWidget.validate()
            assert testWidget.getValidatedStatus() == validString

    def testStreetLineEditValidate(self):
        testWidget = self.gui.streetLineEdit
        
        for pair in self.streetTestPairs:
            testWidget.clear()
            testString, validString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            testWidget.validate()
            assert testWidget.getValidatedStatus() == validString
    
    def testTownLineEditValidate(self):
        testWidget = self.gui.townLineEdit
        
        for pair in self.townTestPairs:
            testWidget.clear()
            testString, validString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            testWidget.validate()
            assert testWidget.getValidatedStatus() == validString
    
    def testPostcodeLineEditValidate(self):
        testWidget = self.gui.postcodeLineEdit
        
        for pair in self.postcodeTestPairs:
            testWidget.clear()
            testString, validString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            testWidget.validate()
            assert testWidget.getValidatedStatus() == validString
        
    def testVehicleRegistrationLineEditValidate(self):
        testWidget = self.gui.vehicleRegistrationLineEdit
        
        for pair in self.vehicleRegistrationTestPairs:
            testWidget.clear()
            testString, validString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            testWidget.validate()
            assert testWidget.getValidatedStatus() == validString
            
    def testGrossWeightLineEditValidate(self):
        testWidget = self.gui.grossWeightLineEdit
        
        for pair in self.grossWeightTestPairs:
            testWidget.clear()
            testString, validString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            testWidget.validate()
            assert testWidget.getValidatedStatus() == validString
    
    def testTareWeightLineEditValidate(self):
        testWidget = self.gui.tareWeightLineEdit
        self.gui.grossWeightLineEdit.setText("12000.00")
        
        for pair in self.tareWeightTestPairs:
            testWidget.clear()
            testString, validString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            testWidget.validate()
            assert testWidget.getValidatedStatus() == validString
    
    def testNetWeightLineEditValidate(self):
        testWidget = self.gui.netWeightLineEdit
        
        for pair in self.netWeightTestPairs:
            testWidget.clear()
            testString, validString = pair[0], pair[1]
            QTest.keyClicks(testWidget, testString)
            testWidget.validate()
            assert testWidget.getValidatedStatus() == validString
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()

class TestNewTicketDialogMethods(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketDialog()
    
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
    
if __name__ == "__main__":
    unittest.main()