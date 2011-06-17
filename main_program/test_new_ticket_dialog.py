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

class TestManualPriceCheckbox(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketDialog()
        self.testWidget = self.gui.manualPriceCheckbox
    
    def testToggleFalseToTrue(self):
        """Unchecked checkbox should be checked when clicked."""
        self.assertFalse(self.testWidget.isChecked())
        
        QTest.mouseClick(self.testWidget, Qt.LeftButton)
        self.assertTrue(self.testWidget.isChecked())
        
    def testToggleTrueToFalse(self):
        """Checked checkbox should be unchecked when clicked."""
        self.testWidget.setChecked(True)
        self.assertTrue(self.testWidget.isChecked())
        
        QTest.mouseClick(self.testWidget, Qt.LeftButton)
        self.assertFalse(self.testWidget.isChecked())

    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestManualPriceAndPayloadValue(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketDialog()
        self.manualPrice = self.gui.manualPriceCheckbox
        self.payloadValue = self.gui.payloadValueLineEdit
        
    def testPayloadValueActivate(self):
        """Payload value should be editable when checkbox is checked."""
        self.assertFalse(self.manualPrice.isChecked())
        self.assertTrue(self.payloadValue.isReadOnly())
        
        QTest.mouseClick(self.manualPrice, Qt.LeftButton)
        
        self.assertTrue(self.manualPrice.isChecked())
        self.assertFalse(self.payloadValue.isReadOnly())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestNamesValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketDialog()
        self.testWidgets = (self.gui.firstNameLineEdit,
                            self.gui.lastNameLineEdit)
        
        self.validText = ("JOHN",
                          "MARK",
                          "BOB",
                          "John",
                          "Mary",
                          "Jessica",
                          "juLIE",
                          "tori",
                          "LunA")
        
        self.maximumLength = "J" * 20
        self.minimumLength = "J"

    def testValidText(self):
        """Valid text should appear valid and uppercase."""
        for testWidget in self.testWidgets:
            for string in self.validText:
                testWidget.clear()
                QTest.keyClicks(testWidget, string)
                testWidget.validate()
                self.assertTrue(testWidget.getValidatedStatus())
                self.assertEqual(testWidget.text(), string.upper())
        
    def testMaximumLength(self):
        """Maximum length string should appear valid and uppercase."""
        for testWidget in self.testWidgets:
            testWidget.clear()
            QTest.keyClicks(testWidget, self.maximumLength)
            testWidget.validate()
            self.assertTrue(testWidget.getValidatedStatus())
            self.assertEqual(testWidget.text(), self.maximumLength.upper())
            
    def testMinimumLength(self):
        """Minimum length string should appear valid and uppercase."""
        for testWidget in self.testWidgets:
            testWidget.clear()
            QTest.keyClicks(testWidget, self.minimumLength)
            testWidget.validate()
            self.assertTrue(testWidget.getValidatedStatus())
            self.assertEqual(testWidget.text(), self.minimumLength.upper())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestNamesInvalidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketDialog()
        self.testWidgets = (self.gui.firstNameLineEdit,
                            self.gui.lastNameLineEdit)
        
        self.invalidText = ("John  ",
                            " john ",
                            "jo hn",
                            "    ",
                            "John Orchard")
        
        self.invalidNumbers = ("234.00",
                               "342545",
                               "6478",
                               "89024",
                               "67  89")
        
        self.invalidPunctuation = ("!john",
                                   "John!",
                                   "John's text",
                                   "JohN_OrcHARD",
                                   "J(ohn){orchard}",
                                   "john.orchard",
                                   "john,orchard",
                                   "j. orchard")
        
        self.exceedsMaximumLength = "J" * 21
        self.exceedsMinimumLength = ""
    
    def testInvalidText(self):
        """Invalid text should appear invalid and uppercase."""
        for testWidget in self.testWidgets:
            for string in self.invalidText:
                testWidget.clear()
                QTest.keyClicks(testWidget, string)
                testWidget.validate()
                self.assertFalse(testWidget.getValidatedStatus())
                self.assertEqual(testWidget.text(), string.upper())
            
    def testInvalidNumbers(self):
        """Invalid numbers should appear invalid."""
        for testWidget in self.testWidgets:
            for string in self.invalidNumbers:
                testWidget.clear()
                QTest.keyClicks(testWidget, string)
                testWidget.validate()
                self.assertFalse(testWidget.getValidatedStatus())
            
    def testInvalidPunctuation(self):
        """Invalid punctuation should appear invalid."""
        for testWidget in self.testWidgets:
            for string in self.invalidPunctuation:
                testWidget.clear()
                QTest.keyClicks(testWidget, string)
                testWidget.validate()
                self.assertFalse(testWidget.getValidatedStatus())
                
    def testExceedsMaximumLength(self):
        """Text exceeding maximum length should appear invalid and uppercase."""
        for testWidget in self.testWidgets:
            testWidget.clear()
            QTest.keyClicks(testWidget, self.exceedsMaximumLength)
            testWidget.validate()
            self.assertFalse(testWidget.getValidatedStatus())
            self.assertEqual(testWidget.text(),
                             self.exceedsMaximumLength.upper())
        
    def testExceedsMinimumLength(self):
        """Text exceeding minimum length should appear invalid and uppercase."""
        for testWidget in self.testWidgets:
            testWidget.clear()
            QTest.keyClicks(testWidget, self.exceedsMinimumLength)
            testWidget.validate()
            self.assertFalse(testWidget.getValidatedStatus())
            self.assertEqual(testWidget.text(),
                             self.exceedsMinimumLength.upper())
            
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestHouseNumberValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketDialog()
        self.testWidget = self.gui.houseNumberLineEdit
        
        self.validNumbers = ("12345",
                             "20",
                             "6",
                             "09",
                             "66",
                             "320")
        
        self.maximumLength = "8" * 5
        self.minimumLength = "8"
    
    def testValidNumbers(self):
        """Valid numbers should appear valid."""
        for number in self.validNumbers:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, number)
            self.testWidget.validate()
            self.assertTrue(self.testWidget.getValidatedStatus())
            
    def testMaximumLength(self):
        """Maximum length numbers should appear valid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.maximumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.getValidatedStatus())
        
    def testMinimumLength(self):
        """Minimum length numbers should appear valid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.minimumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.getValidatedStatus())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()

class TestNewTicketDialogValidators(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketDialog()
        self.weightTestString = "12000.00"
        
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
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()

class TestNewTicketDialogUsage(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketDialog()
        
    def testUsage(self):
        QTest.keyClicks(self.gui.firstNameLineEdit, "John")
        QTest.keyClicks(self.gui.lastNameLineEdit, "Orchard")
        QTest.keyClicks(self.gui.houseNumberLineEdit, "8")
        QTest.keyClicks(self.gui.streetLineEdit, "Kensington Place")
        QTest.keyClicks(self.gui.townLineEdit, "Bath")
        QTest.keyClicks(self.gui.postcodeLineEdit, "BA1 6AW")
        QTest.keyClicks(self.gui.vehicleRegistrationLineEdit, "G678H9")
        
        QTest.keyClicks(self.gui.grossWeightLineEdit, "2500.00")
        QTest.keyClicks(self.gui.tareWeightLineEdit, "1554.00")
        
        assert self.gui.netWeightLineEdit.text() == "946.00"
        assert self.gui.reviewTicketButton.isEnabled() == True
        
        QTest.keyClicks(self.gui.tareWeightLineEdit, "1")
        
        assert self.gui.reviewTicketButton.isEnabled() == False
    
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
    
if __name__ == "__main__":
    unittest.main()
