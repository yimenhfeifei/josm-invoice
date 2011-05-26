try:
    import unittest
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtTest import *
    
    from settings_dialog import SettingsDialog
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestSettingsDialogGui(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = SettingsDialog()
        self.testString = "It works!"
      
    def testAddressLineEditsTextEntry(self):
        testWidgets = (self.gui.addressLineEditOctet1,
                   self.gui.addressLineEditOctet2,
                   self.gui.addressLineEditOctet3,
                   self.gui.addressLineEditOctet4)
        
        for widget in testWidgets:
            widget.clear()
            
            QTest.keyClicks(widget, self.testString)
            assert widget.text() == self.testString
    
    def testPortLineEditTextEntry(self):
        testWidget = self.gui.portLineEdit
        testWidget.clear()
        
        QTest.keyClicks(testWidget, self.testString)
        assert testWidget.text() == self.testString
    
    def testTimeoutSpinBoxArrowClicks(self):
        testWidget = self.gui.timeoutSpinbox
        minValue = testWidget.minimum()
        assert testWidget.value() == minValue
        upArrow = QPoint(30, 2)
        downArrow = QPoint(30, 15)
        
        QTest.mouseClick(testWidget, Qt.LeftButton, pos=upArrow)
        assert testWidget.value() == minValue + 1

        QTest.mouseClick(testWidget, Qt.LeftButton, pos=downArrow)
        assert testWidget.value() == minValue

    def testTimeoutSpinboxRange(self):
        testWidget = self.gui.timeoutSpinbox
        minValue = testWidget.minimum()
        maxValue = testWidget.maximum()
        assert testWidget.value() == minValue
        upArrow = QPoint(30, 2)
        downArrow = QPoint(30, 15)
        
        QTest.mouseClick(testWidget, Qt.LeftButton, pos=downArrow)
        assert testWidget.value() == minValue

        testWidget.setValue(maxValue)
        assert testWidget.value() == maxValue

        QTest.mouseClick(testWidget, Qt.LeftButton, pos=upArrow)
        testWidget.value() == maxValue

    def testTimeoutDialSpinboxConnection(self):
        testWidget = self.gui.timeoutDial
        minValue = testWidget.minimum()
        maxValue = testWidget.maximum()
        validNumbers = list(range(minValue, maxValue))
        middleIndex = len(validNumbers) // 2
        testValue = validNumbers[middleIndex]

        testWidget.setValue(testValue)
        assert testWidget.value() == testValue
        assert self.gui.timeoutSpinbox.value() == testValue
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()

suite1 = unittest.makeSuite(TestSettingsDialogGui, "test")
    
if __name__ == '__main__':
    unittest.main()