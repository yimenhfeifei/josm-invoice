try:
    import unittest
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtTest import *
    
    from custom_widgets.payloadTableWidget import PayloadTableWidget
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestPayloadTableWidget(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = QDialog()
        self.gui.testWidget = PayloadTableWidget()
        
    def testSetCurrentToEmptyRow(self):
        """Tablewidget should be able to find empty row."""
        self.gui.testWidget.setCurrentToEmptyRow()
        self.assertEqual(self.gui.testWidget.currentItem(), None)
        
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
        
if __name__ == "__main__":
    unittest.main()
