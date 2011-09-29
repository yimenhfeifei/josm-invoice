try:
    import unittest
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtTest import *
    
    from custom_widgets.customerWidget import CustomerWidget
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)
        
class TestNamesValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidgets = (self.gui.firstNameEdit,
                            self.gui.lastNameEdit)
        
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
                self.assertTrue(testWidget.isValid())
                self.assertEqual(testWidget.text(), string.upper())
        
    def testMaximumLength(self):
        """Maximum length string should appear valid and uppercase."""
        for testWidget in self.testWidgets:
            testWidget.clear()
            QTest.keyClicks(testWidget, self.maximumLength)
            testWidget.validate()
            self.assertTrue(testWidget.isValid())
            self.assertEqual(testWidget.text(), self.maximumLength.upper())
            
    def testMinimumLength(self):
        """Minimum length string should appear valid and uppercase."""
        for testWidget in self.testWidgets:
            testWidget.clear()
            QTest.keyClicks(testWidget, self.minimumLength)
            testWidget.validate()
            self.assertTrue(testWidget.isValid())
            self.assertEqual(testWidget.text(), self.minimumLength.upper())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestNamesInvalidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidgets = (self.gui.firstNameEdit,
                            self.gui.lastNameEdit)
        
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
                self.assertFalse(testWidget.isValid())
                self.assertEqual(testWidget.text(), string.upper())
            
    def testInvalidNumbers(self):
        """Invalid numbers should appear invalid."""
        for testWidget in self.testWidgets:
            for string in self.invalidNumbers:
                testWidget.clear()
                QTest.keyClicks(testWidget, string)
                testWidget.validate()
                self.assertFalse(testWidget.isValid())
            
    def testInvalidPunctuation(self):
        """Invalid punctuation should appear invalid."""
        for testWidget in self.testWidgets:
            for string in self.invalidPunctuation:
                testWidget.clear()
                QTest.keyClicks(testWidget, string)
                testWidget.validate()
                self.assertFalse(testWidget.isValid())
                
    def testExceedsMaximumLength(self):
        """Text exceeding maximum length should appear invalid and uppercase."""
        for testWidget in self.testWidgets:
            testWidget.clear()
            QTest.keyClicks(testWidget, self.exceedsMaximumLength)
            testWidget.validate()
            self.assertFalse(testWidget.isValid())
            self.assertEqual(testWidget.text(),
                             self.exceedsMaximumLength.upper())
        
    def testExceedsMinimumLength(self):
        """Text exceeding minimum length should appear invalid and uppercase."""
        for testWidget in self.testWidgets:
            testWidget.clear()
            QTest.keyClicks(testWidget, self.exceedsMinimumLength)
            testWidget.validate()
            self.assertFalse(testWidget.isValid())
            self.assertEqual(testWidget.text(),
                             self.exceedsMinimumLength.upper())
            
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestHouseNumberValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidget = self.gui.houseNumberEdit
        
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
            self.assertTrue(self.testWidget.isValid())
            
    def testMaximumLength(self):
        """Maximum length numbers should appear valid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.maximumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.isValid())
        
    def testMinimumLength(self):
        """Minimum length numbers should appear valid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.minimumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.isValid())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestHouseNumberInvalidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidget = self.gui.houseNumberEdit
        
        self.invalidNumbers = ("12.90",
                             "202.78986896",
                             "-6",
                             "-9000",
                             " 78  ",
                             "7^**&89",
                             "()[]387&**3")
        
        self.exceedsMaximumLength = "8" * 6
        self.exceedsMinimumLength = ""
    
    def testInvalidNumbers(self):
        """Invalid numbers should appear invalid."""
        for number in self.invalidNumbers:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, number)
            self.testWidget.validate()
            self.assertFalse(self.testWidget.isValid())
            
    def testExceedsMaximumLength(self):
        """Number exceeding maximum length should appear invalid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMaximumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        
    def testExceedsMinimumLength(self):
        """Number exceeding minimum length should appear invalid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMinimumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestStreetValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidget = self.gui.streetEdit
        
        self.validText = ("The Way",
                          "Funny Crescent",
                          "Maple",
                          "Weird Drive",
                          "Dastardly",
                          "Kensington Place")
        
        self.maximumLength = ("J" * 20) + (" ") + ("J" * 20)
        self.minimumLength = "J"
    
    def testValidText(self):
        """Valid text should appear valid and uppercase."""
        for string in self.validText:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, string)
            self.testWidget.validate()
            self.assertTrue(self.testWidget.isValid())
            self.assertEqual(self.testWidget.text(), string.upper())
            
    def testMaximumLength(self):
        """Maximum length strings should appear valid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.maximumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(), self.maximumLength.upper())
        
    def testMinimumLength(self):
        """Minimum length strings should appear valid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.minimumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(), self.minimumLength.upper())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestStreetInvalidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidget = self.gui.streetEdit
        
        self.invalidText = ("54678",
                            "434.000",
                            " Hell Way ",
                            "Strange Pl aCE",
                            "T!is is not valid!",
                            "$HOME",
                            "M4ary14nD")
        
        self.exceedsMaximumLength = ("J" * 20) + (" ") + ("J" * 21)
        self.exceedsMinimumLength = ""
    
    def testInvalidText(self):
        """Invalid text should appear invalid and uppercase."""
        for string in self.invalidText:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, string)
            self.testWidget.validate()
            self.assertFalse(self.testWidget.isValid())
            self.assertEqual(self.testWidget.text(), string.upper())
            
    def testExceedsMaximumLength(self):
        """Text exceeding maximum length should appear invalid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMaximumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(),
                         self.exceedsMaximumLength.upper())
        
    def testExceedsMinimumLength(self):
        """Text exceeding minimum length should appear invalid and uppercase"""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMinimumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(),
                         self.exceedsMinimumLength.upper())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestTownValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidget = self.gui.townEdit
        
        self.validText = ("The Way",
                          "Funny Crescent",
                          "Maple",
                          "Weird Drive",
                          "Dastardly",
                          "Kensington Place")
        
        self.maximumLength = ("J" * 20) + (" ") + ("J" * 20)
        self.minimumLength = "J"
    
    def testValidText(self):
        """Valid text should appear valid and uppercase."""
        for string in self.validText:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, string)
            self.testWidget.validate()
            self.assertTrue(self.testWidget.isValid())
            self.assertEqual(self.testWidget.text(), string.upper())
            
    def testMaximumLength(self):
        """Maximum length strings should appear valid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.maximumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(), self.maximumLength.upper())
        
    def testMinimumLength(self):
        """Minimum length strings should appear valid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.minimumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(), self.minimumLength.upper())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestTownInvalidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidget = self.gui.townEdit
        
        self.invalidText = ("54678",
                            "434.000",
                            " Hell Way ",
                            "Strange Pl aCE",
                            "T!is is not valid!",
                            "$HOME",
                            "M4ary14nD")
        
        self.exceedsMaximumLength = ("J" * 20) + (" ") + ("J" * 21)
        self.exceedsMinimumLength = ""
    
    def testInvalidText(self):
        """Invalid text should appear invalid and uppercase."""
        for string in self.invalidText:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, string)
            self.testWidget.validate()
            self.assertFalse(self.testWidget.isValid())
            self.assertEqual(self.testWidget.text(), string.upper())
            
    def testExceedsMaximumLength(self):
        """Text exceeding maximum length should appear invalid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMaximumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(),
                         self.exceedsMaximumLength.upper())
        
    def testExceedsMinimumLength(self):
        """Text exceeding minimum length should appear invalid and uppercase"""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMinimumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(),
                         self.exceedsMinimumLength.upper())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()

class TestPostcodeValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidget = self.gui.postcodeEdit
        
        self.validText = ("TR165QY",
                          "TR16 5qy",
                          "TR16 5QY",
                          "tr165qy",
                          "tr165qy",
                          "BA16AW",
                          "ba1 6aw")
        
        self.maximumLength = "TR16 5QY"
        self.minimumLength = "T6 8NP"
    
    def testValidText(self):
        """Valid text should appear valid and uppercase."""
        for string in self.validText:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, string)
            self.testWidget.validate()
            self.assertTrue(self.testWidget.isValid())
            self.assertEqual(self.testWidget.text(), string.upper())
            
    def testMaximumLength(self):
        """Maximum length strings should appear valid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.maximumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(), self.maximumLength.upper())
        
    def testMinimumLength(self):
        """Minimum length strings should appear valid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.minimumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(), self.minimumLength.upper())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestPostcodeInvalidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidget = self.gui.postcodeEdit
        
        self.invalidText = ("TR165 5QY",
                            "tr1665qy",
                            " tr165qy",
                            "$tr165qy",
                            "T!is is not valid!",
                            "ba1  6aw",
                            "*(&BA16AW",
                            "TR16_5QY")
        
        self.exceedsMaximumLength = "TR16 5QY0"
        self.exceedsMinimumLength = "T1 7A"
    
    def testInvalidText(self):
        """Invalid text should appear invalid and uppercase."""
        for string in self.invalidText:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, string)
            self.testWidget.validate()
            self.assertFalse(self.testWidget.isValid())
            self.assertEqual(self.testWidget.text(), string.upper())
            
    def testExceedsMaximumLength(self):
        """Text exceeding maximum length should appear invalid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMaximumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(),
                         self.exceedsMaximumLength.upper())
        
    def testExceedsMinimumLength(self):
        """Text exceeding minimum length should appear invalid and uppercase"""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMinimumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(),
                         self.exceedsMinimumLength.upper())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestVehicleRegistrationValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidget = self.gui.customerRegEdit
        
        self.validText = ("TT54YUT",
                          "TU89JKO",
                          "PP60TER",
                          "UO78JKL",
                          "EW65KKL")
        
        self.maximumLength = "WK00KLP"
        self.minimumLength = "GT66TWA"
    
    def testValidText(self):
        """Valid text should appear valid and uppercase."""
        for string in self.validText:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, string)
            self.testWidget.validate()
            self.assertTrue(self.testWidget.isValid())
            self.assertEqual(self.testWidget.text(), string.upper())
            
    def testMaximumLength(self):
        """Maximum length strings should appear valid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.maximumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(), self.maximumLength.upper())
        
    def testMinimumLength(self):
        """Minimum length strings should appear valid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.minimumLength)
        self.testWidget.validate()
        self.assertTrue(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(), self.minimumLength.upper())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestVehicleRegistrationInvalidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = CustomerWidget()
        self.testWidget = self.gui.customerRegEdit
        
        self.invalidText = ("",
                            "T67 890",
                            " T678UI",
                            "!TY7890K",
                            "T!is is not valid!",
                            "T67 89097hJKI",
                            "6YH89KI",
                            "67HYwe45_90KO",
                            "HU89_K98")
        
        self.exceedsMaximumLength = "WK78T8990"
        self.exceedsMinimumLength = "T8"
    
    def testInvalidText(self):
        """Invalid text should appear invalid and uppercase."""
        for string in self.invalidText:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, string)
            self.testWidget.validate()
            self.assertFalse(self.testWidget.isValid())
            self.assertEqual(self.testWidget.text(), string.upper())
            
    def testExceedsMaximumLength(self):
        """Text exceeding maximum length should appear invalid and uppercase."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMaximumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(),
                         self.exceedsMaximumLength.upper())
        
    def testExceedsMinimumLength(self):
        """Text exceeding minimum length should appear invalid and uppercase"""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMinimumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        self.assertEqual(self.testWidget.text(),
                         self.exceedsMinimumLength.upper())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
if __name__ == "__main__":
    unittest.main()
