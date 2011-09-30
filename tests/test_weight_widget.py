try:
    import unittest
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtTest import *
    
    from custom_widgets.weightWidget import WeightWidget
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestNetWeightValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = WeightWidget()
        self.testWidget = self.gui.netEdit
        
        self.validNumbers = ("120.00",
                          "156.5",
                          "10.00",
                          "98.50",
                          "4.0",
                          "5000.50")
        
        self.maximumLength = "99999.50"
        self.minimumLength = "1.0"
    
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

class TestNetWeightInvalidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = WeightWidget()
        self.testWidget = self.gui.netEdit
        
        self.invalidNumbers = ("",
                            "99999.89",
                            "99999.5000000",
                            "-78.90",
                            "T!is is not valid!",
                            "56.9",
                            "12.2",
                            "89_90",
                            "864,50")
        
        self.exceedsMaximumLength = "99999.000"
        self.exceedsMinimumLength = "2."
    
    def testInvalidNumbers(self):
        """Invalid numbers should appear invalid."""
        for number in self.invalidNumbers:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, number)
            self.testWidget.validate()
            self.assertFalse(self.testWidget.isValid())
            
    def testExceedsMaximumLength(self):
        """Numbers exceeding maximum length should appear invalid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMaximumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        
    def testExceedsMinimumLength(self):
        """Numbers exceeding minimum length should appear invalid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMinimumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestTareWeightInvalidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = WeightWidget()
        self.testWidget = self.gui.tareEdit
        self.gui.grossEdit.setText("99999.50")
        
        self.invalidNumbers = ("",
                            "99999.89",
                            "99999.5000000",
                            "-78.90",
                            "T!is is not valid!",
                            "56.9",
                            "12.2",
                            "89_90",
                            "864,50")
        
        self.exceedsMaximumLength = "99999.000"
        self.exceedsMinimumLength = "2."
    
    def testInvalidNumbers(self):
        """Invalid numbers should appear invalid."""
        for number in self.invalidNumbers:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, number)
            self.testWidget.validate()
            self.assertFalse(self.testWidget.isValid())
            
    def testExceedsMaximumLength(self):
        """Numbers exceeding maximum length should appear invalid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMaximumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        
    def testExceedsMinimumLength(self):
        """Numbers exceeding minimum length should appear invalid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMinimumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestTareWeightValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = WeightWidget()
        self.testWidget = self.gui.tareEdit
        self.gui.grossEdit.setText("99999.50")
        
        self.validNumbers = ("120.00",
                          "156.5",
                          "10.00",
                          "98.50",
                          "4.0",
                          "5000.50")
        
        self.maximumLength = "99999.00"
        self.minimumLength = "1.0"
    
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

class TestGrossWeightInvalidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = WeightWidget()
        self.testWidget = self.gui.grossEdit
        
        self.invalidNumbers = ("",
                            "99999.89",
                            "99999.5000000",
                            "-78.90",
                            "T!is is not valid!",
                            "56.9",
                            "12.2",
                            "89_90",
                            "864,50")
        
        self.exceedsMaximumLength = "99999.000"
        self.exceedsMinimumLength = "2."
    
    def testInvalidNumbers(self):
        """Invalid numbers should appear invalid."""
        for number in self.invalidNumbers:
            self.testWidget.clear()
            QTest.keyClicks(self.testWidget, number)
            self.testWidget.validate()
            self.assertFalse(self.testWidget.isValid())
            
    def testExceedsMaximumLength(self):
        """Numbers exceeding maximum length should appear invalid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMaximumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        
    def testExceedsMinimumLength(self):
        """Numbers exceeding minimum length should appear invalid."""
        self.testWidget.clear()
        QTest.keyClicks(self.testWidget, self.exceedsMinimumLength)
        self.testWidget.validate()
        self.assertFalse(self.testWidget.isValid())
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
class TestGrossWeightValidInput(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = WeightWidget()
        self.testWidget = self.gui.grossEdit
        
        self.validNumbers = ("120.00",
                          "156.5",
                          "10.00",
                          "98.50",
                          "4.0",
                          "5000.50")
        
        self.maximumLength = "99999.50"
        self.minimumLength = "1.0"
    
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

class TestWeightWidget(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = WeightWidget()
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
if __name__ == "__main__":
    unittest.main()
